---
name: ai-pm-project-takeover
description: Take over an unfamiliar AI product as an AI product manager by auditing its product documents, repository, prompts, models, agents, RAG pipelines, data, evaluations, metrics, architecture, operations, roadmap, risks, and stakeholder gaps. Use when Codex needs to help an AI PM 接手新项目、梳理完整项目、做产品与技术尽调、准备交接材料、建立 AI 能力地图、识别产品债和未知问题、制定 30/60/90 天计划，or create an evidence-backed project dossier for onboarding and stakeholder alignment. Produces structured takeover notes and a searchable offline AI PM dossier without presenting inference as fact.
---

# AI PM Project Takeover

Take over an unfamiliar AI product from evidence to action. Build an AI product manager's operating model of the project—not merely a technical summary or a reformatted documentation site.

## Define success

Produce two coordinated deliverables:

1. `takeover-notes/`: working evidence, gaps, decisions, and stakeholder questions.
2. `ai-pm-dossier/`: a polished offline handbook for daily work, onboarding, decision-making, and stakeholder alignment.

The dossier must explain:

- Why the product exists, who uses it, and what outcome it creates.
- What is live, partial, planned, deprecated, or unknown.
- How AI creates value and where models, prompts, retrieval, agents, tools, data, and humans participate.
- How quality, safety, cost, latency, reliability, adoption, and business value are measured.
- Which assumptions, risks, dependencies, product debts, and open questions matter.
- What the incoming AI PM should do in the first 30, 60, and 90 days.

## Choose an evidence route

| Route | Signals | Operating approach |
|---|---|---|
| Product-led | Current PRDs, roadmaps, metrics, research, architecture, and operations exist | Synthesize product narrative; verify critical claims in code and config |
| Hybrid audit | Documents are partial, stale, or inconsistent | Use documents as hypotheses; inspect code, data contracts, tests, and runtime wiring |
| Evidence recovery | Product knowledge is mostly tribal or code-only | Reconstruct current product behavior from implementation; create a stakeholder validation agenda |

Record the selected route and why. Read [references/source-audit.md](references/source-audit.md) before collecting evidence.

## Use the confidence model

Label material claims in working notes:

- **E3 · Verified**: supported by current implementation plus tests, runtime wiring, production metrics, or multiple independent sources.
- **E2 · Supported**: supported by one strong current source.
- **E1 · Inferred**: plausible from indirect evidence; needs confirmation.
- **E0 · Unknown**: missing or contradictory evidence.

Do not hide E0/E1 items. Convert them into stakeholder questions, experiments, instrumentation tasks, or roadmap risks.

## Workflow

### 1. Frame the takeover

Capture role, project scope, deadline, audience, confidentiality, known stakeholders, and expected decisions. Write `takeover-notes/00-brief.md`.

If the user provides no product context, continue with repository evidence and explicitly mark business context as unknown. Do not block progress on questions that can be answered later.

### 2. Build the evidence ledger

Inventory product docs, research, designs, analytics, code, prompts, model configs, agent graphs, retrieval pipelines, data schemas, evaluations, tests, deployments, incidents, support material, roadmaps, and history.

Write:

- `01-inventory.md`: what exists, freshness, owner, and likely authority.
- `02-evidence-ledger.md`: important claims mapped to sources and E0–E3 confidence.
- `03-drift-register.md`: contradictions between product narrative, docs, code, configuration, and runtime evidence.
- `04-unknowns.md`: unanswered questions grouped by decision impact.

Follow [references/source-audit.md](references/source-audit.md). Preserve privacy and never copy real secrets.

### 3. Reconstruct the product

Identify product objective, target users, jobs-to-be-done, use cases, entry points, end-to-end journeys, capability map, scope boundaries, activation, retention loop, operational workflows, and current lifecycle stage.

Distinguish:

- User problem from feature implementation.
- Product outcome from model output.
- Current scope from aspiration.
- Primary user from buyer, admin, operator, reviewer, and downstream consumer.

Read [references/product-discovery.md](references/product-discovery.md).

### 4. Audit the AI system

Trace every material AI experience from user intent to final outcome. Map models, prompts, context assembly, retrieval, memory, agent planning, tool calls, structured outputs, guardrails, human review, fallbacks, and observability.

For each AI capability, document:

- User value and triggering scenario.
- Inputs, context, model/provider, orchestration, and tools.
- Output contract and downstream action.
- Failure modes, fallback, and human control.
- Evaluation coverage and production feedback.
- Cost, latency, privacy, security, and vendor dependency.

Read [references/ai-system-audit.md](references/ai-system-audit.md).

### 5. Build the measurement system

Separate five layers:

1. Business outcomes.
2. Product adoption and behavior.
3. AI task quality.
4. Safety and trust.
5. System efficiency and reliability.

Map each metric to definition, owner, event/source, segment, cadence, baseline, target, and decision. Identify proxy metrics and missing instrumentation. Read [references/metrics-evaluation.md](references/metrics-evaluation.md).

### 6. Surface risks, debt, and stakeholder gaps

Create:

- Product risks: unclear value, weak adoption, workflow mismatch, scope ambiguity.
- AI risks: hallucination, retrieval gaps, non-determinism, prompt drift, agent loops, unsafe actions.
- Data risks: provenance, consent, freshness, leakage, bias, feedback contamination.
- Delivery risks: cost, latency, reliability, vendor lock-in, operational burden.
- Product debt: missing metrics, manual workarounds, stale decisions, undocumented behavior, evaluation gaps.
- Stakeholder agenda: questions for product, engineering, ML, design, data, legal/security, operations, sales, and support.

Rank with impact, likelihood, urgency, evidence confidence, owner, and next action.

### 7. Set priorities and takeover plan

Translate findings into:

- Immediate safeguards and must-clarify items.
- Quick wins with evidence and expected outcome.
- Experiments and instrumentation needed before roadmap commitments.
- Product debt backlog.
- 30/60/90-day plan with outcomes, actions, dependencies, deliverables, and exit criteria.

Read [references/takeover-plan.md](references/takeover-plan.md).

### 8. Build the AI PM dossier

Run:

```bash
python3 scripts/scaffold_dossier.py /absolute/path/to/ai-pm-dossier
```

Edit `dossier.json` and `content/<slug>.html`. Required chapters:

1. Executive brief and reading guide.
2. Product context, users, and value proposition.
3. User journeys and capability map.
4. AI system and data/knowledge architecture.
5. Evaluation, guardrails, and human oversight.
6. Metrics, unit economics, cost, and latency.
7. Technical architecture, operations, and dependencies.
8. Current state, roadmap, and product debt.
9. Risks, unknowns, drift, and stakeholder questions.
10. 30/60/90-day takeover plan.

Use E0–E3 badges in evidence-sensitive sections. Follow [references/information-architecture.md](references/information-architecture.md) and [references/authoring.md](references/authoring.md).

### 9. Build and verify

```bash
python3 scripts/build_dossier.py /absolute/path/to/ai-pm-dossier
python3 scripts/verify_dossier.py /absolute/path/to/ai-pm-dossier
```

Then perform factual spot checks, browser rendering, responsive and keyboard checks, offline verification, privacy review, and a final decision-readiness review. Follow [references/quality.md](references/quality.md).

### 10. Deliver and present

Report:

- Selected route and coverage.
- Most important verified insights.
- Highest-impact unknowns and contradictions.
- Top risks, quick wins, and 30-day priorities.
- Files created and validation results.
- Checks not performed and why.

Prepare an executive explanation that separates product thinking, AI-system thinking, and implementation design. Do not expose confidential project content in externally shared material.

## Resource map

| Need | Read or run |
|---|---|
| Evidence, confidence, drift, privacy | [references/source-audit.md](references/source-audit.md) |
| Users, value, journeys, scope, capability map | [references/product-discovery.md](references/product-discovery.md) |
| Models, prompts, RAG, agents, tools, guardrails | [references/ai-system-audit.md](references/ai-system-audit.md) |
| Metrics, evaluations, experiments, economics | [references/metrics-evaluation.md](references/metrics-evaluation.md) |
| Prioritization and 30/60/90 plan | [references/takeover-plan.md](references/takeover-plan.md) |
| Dossier chapters and navigation | [references/information-architecture.md](references/information-architecture.md) |
| Evidence-backed HTML authoring | [references/authoring.md](references/authoring.md) |
| QA and delivery gates | [references/quality.md](references/quality.md) |
| Scaffold, build, verify | `scripts/scaffold_dossier.py`, `scripts/build_dossier.py`, `scripts/verify_dossier.py` |

## Hard rules

- Do not equate repository behavior with validated user value.
- Do not present inference, roadmap intent, or comments as shipped fact.
- Do not expose credentials, private data, internal endpoints, or confidential screenshots.
- Do not recommend roadmap priority without evidence, decision impact, and uncertainty.
- Do not claim an AI capability is evaluated because tests merely execute it.
- Do not edit generated HTML; edit `dossier.json` or `content/` and rebuild.
- Do not share a real company's dossier externally without authorization and redaction.
