"""Shared configuration and HTML helpers for handbook scripts."""

from __future__ import annotations

import json
import posixpath
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PAGE_REF_RE = re.compile(r'href=(["\'])page:([a-z0-9-]+)(#[^"\']*)?\1', re.I)
ASSET_REF_RE = re.compile(r'(href|src)=(["\'])asset:([^"\']+)\2', re.I)
MERMAID_RE = re.compile(r'\bclass=(["\'])[^"\']*\bmermaid\b[^"\']*\1', re.I)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style"}:
            self.hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)

    def value(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def extract_text(markup: str) -> str:
    parser = TextExtractor()
    parser.feed(markup)
    return parser.value()


def load_config(root: Path) -> dict[str, Any]:
    path = root / "handbook.json"
    if not path.is_file():
        raise ValueError(f"Missing {path}")
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid handbook.json: {exc}") from exc
    if not isinstance(config, dict):
        raise ValueError("handbook.json must contain an object")
    for field in ("language", "title", "subtitle", "description", "version", "sections"):
        if field not in config:
            raise ValueError(f"handbook.json missing field: {field}")
    if not isinstance(config["sections"], list) or not config["sections"]:
        raise ValueError("sections must be a non-empty array")
    return config


def flatten_pages(config: dict[str, Any]) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    slugs: set[str] = set()
    homes = 0
    for section_index, section in enumerate(config["sections"]):
        if not isinstance(section, dict) or not isinstance(section.get("title"), str):
            raise ValueError(f"Section {section_index + 1} requires a title")
        raw_pages = section.get("pages")
        if not isinstance(raw_pages, list) or not raw_pages:
            raise ValueError(f"Section {section['title']!r} requires pages")
        for raw in raw_pages:
            if not isinstance(raw, dict):
                raise ValueError(f"Page in {section['title']!r} must be an object")
            for field in ("slug", "title", "summary", "minutes", "sources"):
                if field not in raw:
                    raise ValueError(f"Page in {section['title']!r} missing field: {field}")
            slug = raw["slug"]
            if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
                raise ValueError(f"Invalid slug: {slug!r}")
            if slug in slugs:
                raise ValueError(f"Duplicate slug: {slug}")
            slugs.add(slug)
            if not isinstance(raw["title"], str) or not raw["title"].strip():
                raise ValueError(f"Page {slug} requires a title")
            if not isinstance(raw["summary"], str):
                raise ValueError(f"Page {slug} summary must be a string")
            if not isinstance(raw["minutes"], int) or raw["minutes"] < 1:
                raise ValueError(f"Page {slug} minutes must be a positive integer")
            if not isinstance(raw["sources"], list) or not all(isinstance(x, str) for x in raw["sources"]):
                raise ValueError(f"Page {slug} sources must be an array of strings")
            page = dict(raw)
            page.update(
                section_title=section["title"],
                section_index=section_index,
                number=len(pages) + 1,
                home=bool(raw.get("home", False)),
            )
            page["url"] = "index.html" if page["home"] else f"pages/{slug}.html"
            homes += int(page["home"])
            pages.append(page)
    if homes != 1:
        raise ValueError(f"Exactly one page must set home=true; found {homes}")
    return pages


def relative_url(from_url: str, to_url: str) -> str:
    return posixpath.relpath(to_url, posixpath.dirname(from_url) or ".")
