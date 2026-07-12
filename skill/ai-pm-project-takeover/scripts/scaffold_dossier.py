#!/usr/bin/env python3
"""Create a non-destructive AI PM project takeover dossier."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


SECTIONS = [
    ("Start", [
        ("index", "AI Product Takeover", "Project identity, current confidence, and takeover entry point."),
        ("executive-brief", "Executive Brief", "The product, AI value, current state, critical risks, and immediate decisions."),
        ("reading-guide", "Reading Guide", "Executive, AI PM, engineering, leadership, and portfolio reading routes."),
    ]),
    ("Product", [
        ("product-context", "Product Context and Users", "Problem, users, buyer, operators, value proposition, and lifecycle."),
        ("user-journeys", "User Journeys", "Happy paths, failure recovery, human handoffs, and time-to-value."),
        ("capability-map", "Capability Map", "User outcomes, capabilities, AI contribution, scope, and rollout state."),
    ]),
    ("AI System", [
        ("ai-system", "AI System Map", "Models, prompts, retrieval, agents, tools, controls, and fallbacks."),
        ("data-knowledge", "Data and Knowledge", "Sources, lineage, freshness, privacy, retrieval, memory, and feedback."),
        ("evaluation-guardrails", "Evaluation and Guardrails", "Quality evidence, release gates, safety, trust, and human oversight."),
    ]),
    ("Measurement", [
        ("metrics-scorecard", "Metrics Scorecard", "Business, product, AI quality, safety, and system metrics."),
        ("economics-performance", "Economics and Performance", "Cost per task, latency, reliability, capacity, and value assumptions."),
    ]),
    ("Delivery", [
        ("architecture-integrations", "Architecture and Integrations", "Runtime boundaries, dependencies, contracts, and ownership."),
        ("operations-dependencies", "Operations and Dependencies", "Deployment, observability, incidents, vendors, and hidden manual work."),
    ]),
    ("Direction", [
        ("current-state-roadmap", "Current State and Roadmap", "What is live, limited, partial, planned, deprecated, or unknown."),
        ("product-debt", "Product Debt", "Evidence, instrumentation, workflow, evaluation, and decision debt."),
    ]),
    ("Takeover", [
        ("risks-unknowns", "Risks and Unknowns", "Prioritized product, AI, data, delivery, and governance risks."),
        ("stakeholder-agenda", "Stakeholder Agenda", "Questions, owners, evidence requests, and decision meetings."),
        ("takeover-plan", "30 / 60 / 90 Day Plan", "Outcomes, actions, dependencies, owners, and exit criteria."),
    ]),
    ("Reference", [
        ("drift-register", "Drift Register", "Contradictions across narrative, docs, code, configuration, and runtime evidence."),
        ("glossary-sources", "Glossary and Source Map", "Canonical terms, definitions, sources, owners, freshness, and confidence."),
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
                "rationale": "Populate from the project evidence ledger during takeover.",
                "status": "unknown",
            }
            if slug == "index":
                page["home"] = True
                page["minutes"] = 4
            rendered.append(page)
        sections.append({"title": section, "pages": rendered})
    return {
        "language": "zh-CN",
        "title": "AI Product Takeover Dossier",
        "subtitle": "Evidence-backed AI PM operating model",
        "description": "A searchable offline dossier for taking over an unfamiliar AI product.",
        "version": "0.1.0",
        "repository": "",
        "sections": sections,
    }


SPECIAL_CONTENT = {
    "index": """<section class="hero">
  <p class="eyebrow">AI PRODUCT MANAGEMENT · PROJECT TAKEOVER</p>
  <h2>From repository evidence to product decisions</h2>
  <p class="hero-lead">Replace this introduction with the product objective, target users, AI value mechanism, current lifecycle stage, and most important takeover decision.</p>
  <div class="hero-actions">
    <a class="button primary" href="page:executive-brief">Read executive brief</a>
    <a class="button" href="page:takeover-plan">Open takeover plan</a>
  </div>
</section>

<h2>Takeover status</h2>
<div class="cards">
  <article class="card"><h4>Evidence route</h4><p>Product-led, hybrid audit, or evidence recovery.</p></article>
  <article class="card"><h4>Current confidence</h4><p>Summarize E3/E2/E1/E0 distribution and critical gaps.</p></article>
  <article class="card"><h4>Next decision</h4><p>Name the highest-impact decision this dossier must unlock.</p></article>
</div>

<aside class="callout warning"><h4>Evidence required</h4><p>This starter contains no project conclusions. Replace placeholders only with verified evidence, labeled inference, or explicit unknowns.</p></aside>
""",
    "executive-brief": """<h2>Product in one page</h2>
<p>State the user, problem, product promise, AI mechanism, current stage, and business context.</p>

<h2>Decision snapshot</h2>
<div class="cards">
  <article class="card"><h4>What is working</h4><p>Verified strengths and evidence.</p></article>
  <article class="card"><h4>What is at risk</h4><p>Highest-impact risks and uncertainty.</p></article>
  <article class="card"><h4>What happens next</h4><p>Immediate decisions and 30-day priorities.</p></article>
</div>

<h2>Confidence summary</h2>
<p><span class="evidence e0">E0 · Unknown</span> Replace with the real confidence distribution after the audit.</p>
""",
    "reading-guide": """<h2>Executive 15-minute route</h2>
<ol class="steps">
  <li><a href="page:executive-brief">Executive brief</a></li>
  <li><a href="page:product-context">Product context and users</a></li>
  <li><a href="page:ai-system">AI system map</a></li>
  <li><a href="page:metrics-scorecard">Metrics scorecard</a></li>
  <li><a href="page:risks-unknowns">Risks and unknowns</a></li>
  <li><a href="page:takeover-plan">30 / 60 / 90 day plan</a></li>
</ol>

<h2>AI PM complete route</h2>
<p>Follow the sidebar from product context through the takeover plan and reference sections.</p>

<h2>Evidence convention</h2>
<p><span class="evidence e3">E3 · Verified</span> <span class="evidence e2">E2 · Supported</span> <span class="evidence e1">E1 · Inferred</span> <span class="evidence e0">E0 · Unknown</span></p>
""",
    "takeover-plan": """<h2>First 30 days · Establish truth and control</h2>
<div class="table-scroll"><table><thead><tr><th>Outcome</th><th>Actions</th><th>Owner</th><th>Exit criteria</th></tr></thead><tbody><tr><td>Replace with evidence-backed outcome</td><td>Define concrete actions</td><td>Assign owner</td><td>Use observable criteria</td></tr></tbody></table></div>

<h2>Days 31–60 · Validate and improve</h2>
<p>Resolve critical unknowns, establish evaluations, and ship bounded improvements.</p>

<h2>Days 61–90 · Establish operating system</h2>
<p>Create the product/AI scorecard, review cadence, roadmap logic, and ownership model.</p>
""",
}


def generic_content(title: str, summary: str) -> str:
    return f"""<p><span class="evidence e0">E0 · Unknown</span></p>
<h2>Current understanding</h2>
<p>{summary} Replace this placeholder with evidence-backed findings.</p>

<h2>What we know</h2>
<p>List verified or supported facts with sources and confidence.</p>

<h2>What remains uncertain</h2>
<p>List contradictions, missing evidence, affected decisions, and owners.</p>

<h2>Why it matters</h2>
<p>Explain the user, business, AI quality, safety, cost, or delivery impact.</p>

<h2>Next validation or decision</h2>
<p>Specify the question, method, owner, evidence required, and target date.</p>
"""


README = """# AI PM dossier maintenance

1. Edit navigation, metadata, sources, and confidence in `dossier.json`.
2. Edit source fragments in `content/<slug>.html`.
3. Rebuild with `python3 /path/to/build_dossier.py .`.
4. Verify with `python3 /path/to/verify_dossier.py .`.

Do not edit generated `index.html`, `pages/`, or `assets/search-index.js` directly.
Keep confidential internal dossiers separate from sanitized portfolio case studies.
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
