#!/usr/bin/env python3
"""Create a non-destructive AI PM project takeover dossier."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


SECTIONS = [
    ("开始", [
        ("index", "AI 产品项目接手总览", "项目身份、当前置信度与接手入口。"),
        ("executive-brief", "管理摘要", "产品、AI 价值、当前状态、关键风险和近期决策。"),
        ("reading-guide", "阅读指南", "管理层、AI 产品经理和工程算法团队的阅读路线。"),
    ]),
    ("产品", [
        ("product-context", "产品背景与用户", "问题、用户、购买者、运营角色、价值主张和生命周期。"),
        ("user-journeys", "用户旅程", "主流程、失败恢复、人工交接和价值实现时间。"),
        ("capability-map", "能力地图", "用户结果、产品能力、AI 贡献、范围和发布状态。"),
    ]),
    ("AI 系统", [
        ("ai-system", "AI 系统地图", "模型、提示词、检索、智能体、工具、控制与降级。"),
        ("data-knowledge", "数据与知识", "来源、血缘、新鲜度、隐私、检索、记忆与反馈。"),
        ("evaluation-guardrails", "评估与安全护栏", "质量证据、发布门禁、安全、信任与人工监督。"),
    ]),
    ("度量", [
        ("metrics-scorecard", "指标记分卡", "业务、产品、AI 质量、安全和系统指标。"),
        ("economics-performance", "经济性与性能", "单任务成本、延迟、可靠性、容量与价值假设。"),
    ]),
    ("交付", [
        ("architecture-integrations", "架构与集成", "运行边界、依赖、接口契约和责任归属。"),
        ("operations-dependencies", "运维与依赖", "部署、可观测性、事故、供应商和隐藏人工工作。"),
    ]),
    ("方向", [
        ("current-state-roadmap", "当前状态与路线图", "已上线、有限开放、部分完成、规划中、已废弃或未知的内容。"),
        ("product-debt", "产品债务", "证据、埋点、工作流、评估和决策债务。"),
    ]),
    ("接手", [
        ("risks-unknowns", "风险与未知问题", "按优先级整理产品、AI、数据、交付和治理风险。"),
        ("stakeholder-agenda", "利益相关方议程", "问题、负责人、证据请求和决策会议。"),
        ("takeover-plan", "30 / 60 / 90 天计划", "结果、行动、依赖、负责人和退出标准。"),
    ]),
    ("参考", [
        ("drift-register", "漂移登记表", "产品叙事、文档、代码、配置和运行证据之间的矛盾。"),
        ("glossary-sources", "术语与来源地图", "统一术语、定义、来源、负责人、新鲜度和置信度。"),
    ]),
]


def make_config() -> dict:
    sections = []
    for section, pages in SECTIONS:
        rendered = []
        for slug, title, summary in pages:
            page = {
                "slug": slug,
                "title": title,
                "summary": summary,
                "minutes": 7,
                "sources": [],
                "rationale": "根据项目接手证据台账补充。",
                "status": "unknown",
            }
            if slug == "index":
                page["home"] = True
                page["minutes"] = 4
            rendered.append(page)
        sections.append({"title": section, "pages": rendered})
    return {
        "language": "zh-CN",
        "title": "AI 产品项目接手档案",
        "subtitle": "证据驱动的 AI 产品管理工作模型",
        "description": "用于接手陌生 AI 产品的可搜索离线档案。",
        "version": "0.1.0",
        "repository": "",
        "sections": sections,
    }


SPECIAL_CONTENT = {
    "index": """<section class="hero">
  <p class="eyebrow">AI 产品管理 · 项目接手</p>
  <h2>从项目证据走向产品决策</h2>
  <p class="hero-lead">在这里补充产品目标、目标用户、AI 价值机制、当前生命周期阶段和最重要的接手决策。</p>
  <div class="hero-actions">
    <a class="button primary" href="page:executive-brief">阅读管理摘要</a>
    <a class="button" href="page:takeover-plan">打开接手计划</a>
  </div>
</section>

<h2>接手状态</h2>
<div class="cards">
  <article class="card"><h4>证据路线</h4><p>产品资料驱动、混合审计或证据恢复。</p></article>
  <article class="card"><h4>当前置信度</h4><p>汇总 E3/E2/E1/E0 分布和关键缺口。</p></article>
  <article class="card"><h4>下一项决策</h4><p>说明这份档案需要支持的最高影响决策。</p></article>
</div>

<aside class="callout warning"><h4>需要证据</h4><p>初始模板不包含项目结论，只能使用已验证证据、明确标注的推断或显式未知项替换占位内容。</p></aside>
""",
    "executive-brief": """<h2>一页产品概览</h2>
<p>说明用户、问题、产品承诺、AI 机制、当前阶段和业务背景。</p>

<h2>决策快照</h2>
<div class="cards">
  <article class="card"><h4>当前有效</h4><p>已经验证的优势和证据。</p></article>
  <article class="card"><h4>当前风险</h4><p>影响最大的风险和不确定性。</p></article>
  <article class="card"><h4>后续行动</h4><p>近期决策和未来 30 天优先事项。</p></article>
</div>

<h2>置信度汇总</h2>
<p><span class="evidence e0">E0 · 未知</span> 审计后替换为实际置信度分布。</p>
""",
    "reading-guide": """<h2>管理层 15 分钟路线</h2>
<ol class="steps">
  <li><a href="page:executive-brief">管理摘要</a></li>
  <li><a href="page:product-context">产品背景与用户</a></li>
  <li><a href="page:ai-system">AI 系统地图</a></li>
  <li><a href="page:metrics-scorecard">指标记分卡</a></li>
  <li><a href="page:risks-unknowns">风险与未知问题</a></li>
  <li><a href="page:takeover-plan">30 / 60 / 90 天计划</a></li>
</ol>

<h2>AI 产品经理完整路线</h2>
<p>按照侧边栏顺序，从产品背景阅读到接手计划和参考章节。</p>

<h2>证据约定</h2>
<p><span class="evidence e3">E3 · 已验证</span> <span class="evidence e2">E2 · 有依据</span> <span class="evidence e1">E1 · 推断</span> <span class="evidence e0">E0 · 未知</span></p>
""",
    "takeover-plan": """<h2>前 30 天 · 建立事实与控制</h2>
<div class="table-scroll"><table><thead><tr><th>结果</th><th>行动</th><th>负责人</th><th>退出标准</th></tr></thead><tbody><tr><td>补充有证据支持的结果</td><td>定义具体行动</td><td>指定负责人</td><td>使用可观察标准</td></tr></tbody></table></div>

<h2>第 31–60 天 · 验证并改进</h2>
<p>解决关键未知问题、建立评估，并交付边界明确的改进。</p>

<h2>第 61–90 天 · 建立运行机制</h2>
<p>建立产品与 AI 记分卡、评审节奏、路线图逻辑和责任模型。</p>
""",
}


def generic_content(title: str, summary: str) -> str:
    return f"""<p><span class="evidence e0">E0 · 未知</span></p>
<h2>当前理解</h2>
<p>{summary} 请替换为有证据支持的发现。</p>

<h2>已知事实</h2>
<p>列出已验证或有依据的事实、来源和置信度。</p>

<h2>仍不确定的内容</h2>
<p>列出矛盾、缺失证据、受影响决策和负责人。</p>

<h2>重要性</h2>
<p>说明对用户、业务、AI 质量、安全、成本或交付的影响。</p>

<h2>下一项验证或决策</h2>
<p>指定问题、方法、负责人、所需证据和目标日期。</p>
"""


README = """# AI 产品项目接手档案维护说明

1. 在 `dossier.json` 中编辑导航、元数据、来源和置信度。
2. 在 `content/<slug>.html` 中编辑正文片段。
3. 使用 `python3 /path/to/build_dossier.py .` 重新构建。
4. 使用 `python3 /path/to/verify_dossier.py .` 执行验证。

不要直接编辑生成的 `index.html`、`pages/` 或 `assets/search-index.js`。
包含机密信息的内部档案必须与可公开材料分开保存并独立审查。
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
    write_missing(output / "dossier.json", json.dumps(make_config(), ensure_ascii=False, indent=2) + "\n", created, kept)
    write_missing(output / "README.md", README, created, kept)
    for _, pages in SECTIONS:
        for slug, title, summary in pages:
            body = SPECIAL_CONTENT.get(slug, generic_content(title, summary))
            write_missing(output / "content" / f"{slug}.html", body, created, kept)
    for name in ("style.css", "app.js"):
        copy_missing(asset_root / name, output / "assets" / name, created, kept)
    return created, kept


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an AI PM takeover dossier without overwriting files.")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        created, kept = scaffold(args.output)
    except OSError as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"AI PM dossier scaffold ready: {args.output.expanduser().resolve()}")
    print(f"Created {len(created)} file(s); preserved {len(kept)} existing file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
