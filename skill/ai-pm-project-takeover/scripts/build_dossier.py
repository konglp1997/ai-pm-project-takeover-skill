#!/usr/bin/env python3
"""Build a searchable offline AI PM takeover dossier."""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from dossier_common import (
    ASSET_REF_RE,
    MERMAID_RE,
    PAGE_REF_RE,
    extract_text,
    flatten_pages,
    load_config,
    relative_url,
)


HEADING_RE = re.compile(r"<(h[23])(?P<attrs>\s[^>]*)?>(?P<body>[\s\S]*?)</\1>", re.I)


def process_headings(fragment: str) -> tuple[str, list[dict[str, Any]]]:
    toc: list[dict[str, Any]] = []
    used: set[str] = set()

    def replace(match: re.Match[str]) -> str:
        tag = match.group(1).lower()
        attrs = match.group("attrs") or ""
        body = match.group("body")
        text = extract_text(body)
        found = re.search(r'\bid=(["\'])([^"\']+)\1', attrs, re.I)
        if found:
            anchor = found.group(2)
        else:
            normalized = unicodedata.normalize("NFKD", text).lower()
            anchor = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", normalized).strip("-")
            anchor = anchor or f"section-{len(toc) + 1}"
        base = anchor
        suffix = 2
        while anchor in used:
            anchor = f"{base}-{suffix}"
            suffix += 1
        used.add(anchor)
        if found:
            attrs = attrs[: found.start()] + f'id="{html.escape(anchor, quote=True)}"' + attrs[found.end() :]
        else:
            attrs += f' id="{html.escape(anchor, quote=True)}"'
        toc.append({"level": int(tag[1]), "id": anchor, "text": text})
        label = html.escape(f"链接到{text}", quote=True)
        return f'<{tag}{attrs}><a class="heading-anchor" href="#{html.escape(anchor, quote=True)}" aria-label="{label}">#</a>{body}</{tag}>'

    return HEADING_RE.sub(replace, fragment), toc


def rewrite_links(fragment: str, page: dict[str, Any], by_slug: dict[str, dict[str, Any]]) -> str:
    def page_link(match: re.Match[str]) -> str:
        quote, slug, anchor = match.group(1), match.group(2), match.group(3) or ""
        if slug not in by_slug:
            return match.group(0)
        href = relative_url(page["url"], by_slug[slug]["url"]) + anchor
        return f"href={quote}{href}{quote}"

    def asset_link(match: re.Match[str]) -> str:
        attr, quote, name = match.group(1), match.group(2), match.group(3)
        normalized = posixpath.normpath(name).lstrip("/")
        if normalized.startswith("../") or "\\" in normalized:
            return match.group(0)
        href = relative_url(page["url"], f"assets/{normalized}")
        return f"{attr}={quote}{href}{quote}"

    return ASSET_REF_RE.sub(asset_link, PAGE_REF_RE.sub(page_link, fragment))


def sidebar(config: dict[str, Any], current: dict[str, Any], by_slug: dict[str, dict[str, Any]]) -> str:
    groups: list[str] = []
    for section in config["sections"]:
        links: list[str] = []
        for raw in section["pages"]:
            target = by_slug[raw["slug"]]
            active = " current" if target["slug"] == current["slug"] else ""
            aria = ' aria-current="page"' if active else ""
            links.append(
                f'<a class="nav-link{active}" href="{html.escape(relative_url(current["url"], target["url"]), quote=True)}"{aria}>'
                f'<span class="nav-number">{target["number"]:02d}</span><span>{html.escape(target["title"])}</span></a>'
            )
        groups.append(f'<section class="nav-section"><h2>{html.escape(section["title"])}</h2>{"".join(links)}</section>')
    home = next(page for page in by_slug.values() if page["home"])
    return (
        f'<div class="brand"><a href="{html.escape(relative_url(current["url"], home["url"]), quote=True)}">'
        f'<strong>{html.escape(config["title"])}</strong><span>{html.escape(config["subtitle"])}</span></a></div>'
        f'<nav aria-label="档案章节">{"".join(groups)}</nav>'
    )


def toc_html(toc: list[dict[str, Any]]) -> str:
    if len(toc) < 2:
        return ""
    items = "".join(
        f'<li class="level-{x["level"]}"><a href="#{html.escape(x["id"], quote=True)}">{html.escape(x["text"])}</a></li>'
        for x in toc
    )
    return f'<aside class="page-toc" aria-label="本页目录"><h2>本页目录</h2><ol>{items}</ol></aside>'


def sources_html(page: dict[str, Any]) -> str:
    if page.get("sources"):
        chips = "".join(f"<code>{html.escape(x)}</code>" for x in page["sources"])
        return f'<div class="page-sources"><span>证据来源</span>{chips}</div>'
    if page.get("rationale"):
        return f'<div class="page-sources"><span>页面依据</span><p>{html.escape(str(page["rationale"]))}</p></div>'
    return ""


def status_html(page: dict[str, Any]) -> str:
    status = page.get("status")
    labels = {
        "verified": ("e3", "E3 · 已验证"),
        "supported": ("e2", "E2 · 有依据"),
        "inferred": ("e1", "E1 · 推断"),
        "unknown": ("e0", "E0 · 未知"),
    }
    if status not in labels:
        return ""
    css, label = labels[status]
    return f'<p class="status-line"><span class="evidence {css}">{label}</span></p>'


def pager(current: dict[str, Any], pages: list[dict[str, Any]]) -> str:
    index = current["number"] - 1
    previous = pages[index - 1] if index else None
    following = pages[index + 1] if index + 1 < len(pages) else None

    def link(page: dict[str, Any] | None, label: str, css: str) -> str:
        if page is None:
            return f'<span class="pager-item {css} disabled"></span>'
        return (
            f'<a class="pager-item {css}" href="{html.escape(relative_url(current["url"], page["url"]), quote=True)}">'
            f'<span>{label}</span><strong>{html.escape(page["title"])}</strong></a>'
        )

    return f'<nav class="pager" aria-label="Page navigation">{link(previous, "上一篇", "previous")}{link(following, "下一篇", "next")}</nav>'


def shell(
    config: dict[str, Any],
    page: dict[str, Any],
    pages: list[dict[str, Any]],
    by_slug: dict[str, dict[str, Any]],
    body: str,
    toc: list[dict[str, Any]],
    mermaid_asset: bool,
) -> str:
    base = "" if page["home"] else "../"
    mermaid = f'<script src="{base}assets/mermaid.min.js"></script>' if mermaid_asset and MERMAID_RE.search(body) else ""
    return f"""<!doctype html>
<html lang="{html.escape(str(config['language']), quote=True)}" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(page['summary'], quote=True)}">
  <title>{html.escape(page['title'])} · {html.escape(config['title'])}</title>
  <link rel="stylesheet" href="{base}assets/style.css">
  <script>window.__DOSSIER_BASE__={json.dumps(base)};</script>
</head>
<body>
  <a class="skip-link" href="#main-content">跳到正文</a>
  <div class="scrim" data-menu-close></div>
  <div class="layout">
    <aside class="sidebar" id="sidebar">{sidebar(config, page, by_slug)}</aside>
    <main class="main" id="main-content">
      <header class="topbar">
        <button class="icon-button menu-button" type="button" data-menu-toggle aria-controls="sidebar" aria-expanded="false">目录</button>
        <p class="breadcrumbs">{html.escape(page['section_title'])} / {html.escape(page['title'])}</p>
        <button class="search-button" type="button" data-search-open>搜索 <kbd>⌘K</kbd></button>
        <button class="icon-button" type="button" data-theme-toggle>明暗</button>
        <span class="progress" aria-hidden="true"><span data-progress></span></span>
      </header>
      <div class="content-layout">
        <article class="article">
          <header class="page-header">
            <p class="eyebrow">{html.escape(page['section_title'])}</p>
            {status_html(page)}
            <h1>{html.escape(page['title'])}</h1>
            <p class="page-summary">{html.escape(page['summary'])}</p>
            <p class="page-meta">约 {page['minutes']} 分钟 · 第 {page['number']} / {len(pages)} 页</p>
            {sources_html(page)}
          </header>
          {body}
          {pager(page, pages)}
        </article>
        {toc_html(toc)}
      </div>
    </main>
  </div>
  <div class="search-dialog" role="dialog" aria-modal="true" aria-label="搜索手册" hidden>
    <div class="search-panel">
      <label for="search-input">搜索手册</label>
      <input id="search-input" type="search" autocomplete="off" placeholder="输入页面、概念或命令">
      <div class="search-results" aria-live="polite"></div>
      <button type="button" class="search-close" data-search-close>关闭</button>
    </div>
  </div>
  <script src="{base}assets/search-index.js"></script>
  {mermaid}
  <script src="{base}assets/app.js"></script>
</body>
</html>
"""


def build(root: Path) -> tuple[int, list[str]]:
    root = root.expanduser().resolve()
    config = load_config(root)
    pages = flatten_pages(config)
    by_slug = {page["slug"]: page for page in pages}
    assets = root / "assets"
    for name in ("style.css", "app.js"):
        if not (assets / name).is_file():
            raise ValueError(f"Missing required asset: assets/{name}")
    output_pages = root / "pages"
    output_pages.mkdir(parents=True, exist_ok=True)
    for stale in output_pages.glob("*.html"):
        stale.unlink()

    warnings: list[str] = []
    search: list[dict[str, str]] = []
    has_mermaid = (assets / "mermaid.min.js").is_file()
    for page in pages:
        source = root / "content" / f'{page["slug"]}.html'
        if not source.is_file():
            raise ValueError(f"Missing content fragment: {source}")
        fragment = source.read_text(encoding="utf-8")
        if MERMAID_RE.search(fragment) and not has_mermaid:
            warnings.append(f'{page["slug"]}: Mermaid source present but assets/mermaid.min.js is missing')
        rewritten = rewrite_links(fragment, page, by_slug)
        processed, toc = process_headings(rewritten)
        target = root / page["url"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(shell(config, page, pages, by_slug, processed, toc, has_mermaid), encoding="utf-8")
        search.append(
            {
                "url": page["url"],
                "title": page["title"],
                "section": page["section_title"],
                "summary": page["summary"],
                "text": extract_text(fragment)[:5000],
            }
        )
    (assets / "search-index.js").write_text(
        "window.__DOSSIER_SEARCH__=" + json.dumps(search, ensure_ascii=True, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )
    return len(pages), warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an offline AI PM project takeover dossier.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    try:
        count, warnings = build(args.root)
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Built AI PM dossier with {count} page(s) in {args.root.expanduser().resolve()}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
