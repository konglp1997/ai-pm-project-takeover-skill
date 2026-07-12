# Evidence and source audit

Build a decision-grade evidence base before writing a polished narrative.

## Evidence layers

Do not use one universal source hierarchy. Rank sources by the claim being made:

| Claim | Strong evidence | Common weak evidence |
|---|---|---|
| User problem | Research recordings, support themes, observed workflows, validated discovery | Feature list, founder opinion |
| Adoption | Event data with definitions and segments | Screenshot of a dashboard, total accounts |
| Business value | Revenue, cost, conversion, retention, task outcome | Model benchmark alone |
| Shipped behavior | Runtime wiring, current configuration, tests, production observation | Roadmap, old PRD, comments |
| AI quality | Representative evaluation set, human rubric, production feedback | One demo, generic benchmark |
| Safety | Threat model, red-team evidence, incident history, enforcement path | Policy prose without enforcement |
| Roadmap intent | Approved roadmap, decision log, named owner | TODO, stale issue, commented code |

## Inventory dimensions

Inventory each source with path/link, owner, date, scope, freshness, confidentiality, and claim types it can support.

Search for:

- Strategy, PRD, roadmap, research, design, pricing, sales, support, analytics, and decision logs.
- Frontend routes, API entrypoints, service boundaries, schemas, tests, feature flags, and deployments.
- System/developer prompts, templates, model/provider configs, tool schemas, agent graphs, retrieval, memory, and guardrails.
- Offline evaluations, golden datasets, human review rubrics, experiment logs, production quality feedback, and incidents.
- Data sources, consent, lineage, retention, access, feedback loops, and deletion paths.
- Cost, latency, reliability, fallbacks, quotas, observability, and operational playbooks.

## Confidence model

| Level | Meaning | Allowed wording |
|---|---|---|
| E3 Verified | Multiple current sources or direct runtime/metric evidence | “The product does…” |
| E2 Supported | One strong current source | “Current evidence indicates…” |
| E1 Inferred | Indirect or incomplete evidence | “Likely…; confirm with…” |
| E0 Unknown | Missing or contradictory evidence | “Unknown; decision blocked until…” |

Assign confidence to important claims, not every sentence. Lower confidence when sources disagree, evidence is old, definitions are unclear, or only happy-path demos exist.

## Evidence ledger

| ID | Claim | Type | Evidence | Confidence | Decision impact | Next validation |
|---|---|---|---|---|---|---|
| C-01 | New users reach first value through document upload | User journey | `src/routes/upload`, onboarding design | E2 | High | Check activation events and user research |
| C-02 | Responses meet expert quality threshold | AI quality | No evaluation set found | E0 | Critical | Define rubric and sample production tasks |

## Drift register

Capture contradictions without silently choosing a convenient story:

| Narrative says | Evidence says | Impact | Provisional authority | Owner / action |
|---|---|---|---|---|
| Feature is generally available | Flag defaults off | Customer expectations | Runtime config | Confirm rollout owner |

Common drift:

- PRD “done” versus disabled or partial implementation.
- Claimed AI automation versus mandatory human operations.
- Metric name reused with different definitions.
- Prompt/model in docs differs from runtime config.
- Evaluation claims lack dataset, rubric, baseline, or reproducibility.
- Roadmap item exists in code but has no product decision.

## Privacy and confidentiality

- Never copy real secrets, customer records, private prompts, proprietary datasets, internal hosts, credentials, or signed URLs.
- Record environment variable names with placeholders.
- Aggregate or synthesize user examples for externally shared material.
- Keep the internal company dossier and externally shared material as separate artifacts.
- Treat screenshots and generated search indexes as potential data exports.

## Completion gate

Before synthesis, be able to answer or explicitly mark unknown:

- Product objective, lifecycle stage, target users, buyer, and operator.
- Core journey, time-to-value, repeated-use loop, and failure recovery.
- AI value mechanism, output contract, and human control.
- Data provenance, model/provider, orchestration, evaluation, and feedback.
- Business, product, AI, safety, and system metrics.
- Current scope, rollout state, dependencies, product debt, and critical unknowns.
