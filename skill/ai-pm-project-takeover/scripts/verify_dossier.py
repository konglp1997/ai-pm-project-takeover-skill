#!/usr/bin/env python3
"""Verify AI PM dossier sources and generated offline output."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from dossier_common import ASSET_REF_RE, PAGE_REF_RE, REQUIRED_SLUGS, flatten_pages, load_config


FORBIDDEN = {"html", "head", "body", "script", "iframe", "object", "embed"}
REMOTE_ASSET_TAGS = {"img", "source", "video", "audio", "link", "script"}
SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("OpenAI-style token", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "credential assignment",
        re.compile(r"(?i)\b(?:password|passwd|api[_-]?key|client[_-]?secret|access[_-]?token)\s*[:=]\s*[\"'][^\s<\"']{8,}[\"']"),
    ),
    ("credential-bearing URL", re.compile(r"https?://[^/\s:@]+:[^/\s@]+@")),
)


def remote(value: str) -> bool:
    return value.strip().lower().startswith(("http://", "https://", "//"))


class Inspector(HTMLParser):
    def __init__(self, fragment: bool) -> None:
        super().__init__(convert_charrefs=True)
        self.fragment = fragment
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.remote_assets: list[tuple[str, str]] = []
        self.external_links: list[str] = []
        self.problems: list[str] = []
        self.mermaid = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check(tag, attrs)

    def _check(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = {name.lower(): value or "" for name, value in attrs}
        if self.fragment and tag in FORBIDDEN:
            self.problems.append(f"forbidden <{tag}> tag")
        if self.fragment and tag == "h1":
            self.problems.append("fragment contains <h1>; the shell supplies the title")
        for name in values:
            if name.startswith("on"):
                self.problems.append(f"inline event handler {name} is not allowed")
        if "id" in values:
            self.ids.append(values["id"])
        for attr in ("href", "src"):
            value = values.get(attr, "")
            if value.strip().lower().startswith(("javascript:", "vbscript:", "data:")):
                self.problems.append(f"unsafe {attr} scheme on <{tag}>")
        if "href" in values:
            self.hrefs.append(values["href"])
            if tag == "a" and remote(values["href"]):
                self.external_links.append(values["href"])
        resource = values.get("src") or (values.get("href") if tag == "link" else "")
        if tag in REMOTE_ASSET_TAGS and resource and remote(resource):
            self.remote_assets.append((tag, resource))
        if tag == "img" and "alt" not in values:
            self.problems.append("image is missing an alt attribute")
        if "mermaid" in set(values.get("class", "").split()):
            self.mermaid += 1


def duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    result: set[str] = set()
    for value in values:
        if value in seen:
            result.add(value)
        seen.add(value)
    return result


def scan_secrets(label: str, text: str, errors: list[str]) -> None:
    for name, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f"{label}: possible {name}")


def resolve_link(source: Path, root: Path, href: str) -> Path | None:
    if not href or href.startswith("#"):
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:")):
        return None
    if not parsed.path:
        return None
    target = (source.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return Path("/__outside_dossier__")
    return target


def verify(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    counts = {"pages": 0, "links": 0, "mermaid": 0, "external": 0}
    try:
        config = load_config(root)
        pages = flatten_pages(config)
    except (OSError, ValueError, UnicodeError) as exc:
        return [str(exc)], warnings, counts
    counts["pages"] = len(pages)
    slugs = {page["slug"] for page in pages}
    for slug in sorted(REQUIRED_SLUGS - slugs):
        errors.append(f"dossier.json: required AI PM chapter missing: {slug}")
    expected = {page["url"] for page in pages}
    assets = root / "assets"
    mermaid_source_count = 0

    for page in pages:
        label = f'content/{page["slug"]}.html'
        path = root / label
        if not path.is_file():
            errors.append(f"{label}: missing")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{label}: cannot read as UTF-8: {exc}")
            continue
        if not page.get("sources") and not str(page.get("rationale", "")).strip():
            errors.append(f"dossier.json page {page['slug']}: add sources or a rationale")
        inspector = Inspector(fragment=True)
        inspector.feed(text)
        for problem in inspector.problems:
            errors.append(f"{label}: {problem}")
        for value in sorted(duplicates(inspector.ids)):
            errors.append(f"{label}: duplicate id {value!r}")
        for tag, url in inspector.remote_assets:
            errors.append(f"{label}: remote <{tag}> asset breaks offline use: {url}")
        for url in inspector.external_links:
            warnings.append(f"{label}: external link requires network: {url}")
        for target in sorted({m.group(2) for m in PAGE_REF_RE.finditer(text)} - slugs):
            errors.append(f"{label}: page:{target} is not configured")
        for match in ASSET_REF_RE.finditer(text):
            name = match.group(3)
            parts = Path(name).parts
            if "\\" in name or Path(name).is_absolute() or ".." in parts:
                errors.append(f"{label}: unsafe asset path asset:{name}")
            elif not (assets / name).is_file():
                errors.append(f"{label}: missing asset asset:{name}")
        scan_secrets(label, text, errors)
        mermaid_source_count += inspector.mermaid

    for name in ("style.css", "app.js", "search-index.js"):
        if not (assets / name).is_file():
            errors.append(f"assets/{name}: missing; run scaffold/build")
    style = assets / "style.css"
    if style.is_file():
        css = style.read_text(encoding="utf-8")
        if re.search(r"@import\s+", css, re.I):
            errors.append("assets/style.css: @import is not allowed offline")
        if re.search(r"url\(\s*['\"]?(?:https?:)?//", css, re.I):
            errors.append("assets/style.css: remote url() breaks offline use")
        scan_secrets("assets/style.css", css, errors)
    if mermaid_source_count and not (assets / "mermaid.min.js").is_file():
        errors.append(f"assets/mermaid.min.js: missing for {mermaid_source_count} Mermaid block(s)")

    generated: list[Path] = []
    for relative in sorted(expected):
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: generated page missing; run build")
        else:
            generated.append(path)
    actual_pages = {f"pages/{x.name}" for x in (root / "pages").glob("*.html")} if (root / "pages").is_dir() else set()
    for stale in sorted(actual_pages - {x for x in expected if x.startswith("pages/")}):
        warnings.append(f"{stale}: stale generated page")

    for path in generated:
        label = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        inspector = Inspector(fragment=False)
        inspector.feed(text)
        for problem in inspector.problems:
            errors.append(f"{label}: {problem}")
        for value in sorted(duplicates(inspector.ids)):
            errors.append(f"{label}: duplicate id {value!r}")
        for tag, url in inspector.remote_assets:
            errors.append(f"{label}: remote <{tag}> asset breaks offline use: {url}")
        for href in inspector.hrefs:
            counts["links"] += 1
            target = resolve_link(path, root, href)
            if target is None:
                continue
            if target.as_posix() == "/__outside_dossier__":
                errors.append(f"{label}: link escapes dossier root: {href}")
            elif not target.exists():
                errors.append(f"{label}: broken link: {href}")
        counts["external"] += len(inspector.external_links)
        counts["mermaid"] += inspector.mermaid
        scan_secrets(label, text, errors)
    scan_secrets("dossier.json", (root / "dossier.json").read_text(encoding="utf-8"), errors)
    return errors, warnings, counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify an offline AI PM project takeover dossier.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    errors, warnings, counts = verify(args.root)
    print(f"Checked {counts['pages']} page(s), {counts['links']} link(s), {counts['mermaid']} Mermaid block(s), and {counts['external']} external link(s).")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Verification failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Verification passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
