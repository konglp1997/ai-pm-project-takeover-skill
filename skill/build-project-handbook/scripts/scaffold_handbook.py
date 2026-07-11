#!/usr/bin/env python3
"""Create a non-destructive starter directory for an offline handbook."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


CONFIG = {
    "language": "zh-CN",
    "title": "项目手册",
    "subtitle": "从文档与代码还原的项目全景",
    "description": "面向项目接手者的离线、可搜索手册。",
    "version": "0.1.0",
    "repository": "",
    "sections": [
        {
            "title": "从这里开始",
            "pages": [
                {
                    "slug": "index",
                    "title": "项目手册",
                    "summary": "先认识项目，再选择阅读路线。",
                    "minutes": 5,
                    "home": True,
                    "sources": ["README.md"],
                },
                {
                    "slug": "reading-guide",
                    "title": "阅读指南",
                    "summary": "完整通读、快速浏览与按角色切入。",
                    "minutes": 5,
                    "sources": [],
                    "rationale": "导航页基于本手册章节结构编写。",
                },
            ],
        },
        {
            "title": "参考",
            "pages": [
                {
                    "slug": "drift-register",
                    "title": "文档漂移清单",
                    "summary": "记录文档、配置与实现的差异。",
                    "minutes": 5,
                    "sources": [],
                    "rationale": "汇总审计过程中发现的差异。",
                }
            ],
        },
    ],
}


CONTENT = {
    "index.html": """<section class="hero">
  <p class="eyebrow">PROJECT HANDBOOK</p>
  <h2>把项目事实组织成可阅读的路径</h2>
  <p class="hero-lead">替换这段文字，说明项目解决的问题、服务对象与职责边界。</p>
  <div class="hero-actions">
    <a class="button primary" href="page:reading-guide">选择阅读路线</a>
    <a class="button" href="page:drift-register">查看漂移清单</a>
  </div>
</section>

<h2>项目定位</h2>
<p>用证据充分的文字说明项目当前承担的职责，并明确它不负责什么。</p>

<div class="cards">
  <article class="card"><h4>输入</h4><p>系统接收什么。</p></article>
  <article class="card"><h4>处理</h4><p>系统执行什么核心工作。</p></article>
  <article class="card"><h4>输出</h4><p>系统交付什么结果。</p></article>
</div>
""",
    "reading-guide.html": """<h2>完整通读</h2>
<p>按侧边栏顺序阅读，适合首次接手项目的维护者。</p>

<h2>快速浏览</h2>
<ol class="steps">
  <li><strong>项目定位。</strong>从封面确认职责边界。</li>
  <li><strong>系统结构。</strong>补充架构页后链接到该页。</li>
  <li><strong>运行方式。</strong>补充运维页后链接到该页。</li>
  <li><strong>漂移清单。</strong><a href="page:drift-register">查看已知差异</a>。</li>
</ol>

<h2>按角色切入</h2>
<p>根据真实章节补充开发、运维、产品或数据角色的最短路线。</p>
""",
    "drift-register.html": """<h2>使用方式</h2>
<p>每条差异都应包含文档说法、实现证据、采用结论与来源路径。</p>

<aside class="callout note">
  <h4>当前状态</h4>
  <p>尚未发现已确认的漂移项。完成资料审计后更新本页。</p>
</aside>
""",
}


README = """# Handbook maintenance

1. Edit page metadata and order in `handbook.json`.
2. Edit source fragments in `content/<slug>.html`.
3. Rebuild with `python3 /path/to/build_handbook.py .`.
4. Verify with `python3 /path/to/verify_handbook.py .`.

Do not edit `index.html`, `pages/`, or `assets/search-index.js` directly.
"""


def write_missing(path: Path, text: str, created: list[Path], kept: list[Path]) -> None:
    if path.exists():
        kept.append(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    created.append(path)


def copy_missing(source: Path, target: Path, created: list[Path], kept: list[Path]) -> None:
    if target.exists():
        kept.append(target)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    created.append(target)


def scaffold(output: Path) -> tuple[list[Path], list[Path]]:
    output = output.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    asset_root = Path(__file__).resolve().parent.parent / "assets" / "site"
    created: list[Path] = []
    kept: list[Path] = []
    for name in ("style.css", "app.js"):
        if not (asset_root / name).is_file():
            raise FileNotFoundError(f"Skill asset missing: {name}")
    write_missing(output / "handbook.json", json.dumps(CONFIG, ensure_ascii=False, indent=2) + "\n", created, kept)
    write_missing(output / "README.md", README, created, kept)
    for name, body in CONTENT.items():
        write_missing(output / "content" / name, body, created, kept)
    for name in ("style.css", "app.js"):
        copy_missing(asset_root / name, output / "assets" / name, created, kept)
    return created, kept


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a handbook starter without overwriting files.")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        created, kept = scaffold(args.output)
    except OSError as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"Handbook scaffold ready: {args.output.expanduser().resolve()}")
    print(f"Created {len(created)} file(s); preserved {len(kept)} existing file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
