# AI PM dossier information architecture

Organize the dossier around decisions an incoming AI PM must make.

## Required sequence

| Part | Decision question | Required pages |
|---|---|---|
| Start | What is this product and how should I use this dossier? | Executive brief, reading guide |
| Product | Who has which problem and how does the product create value? | Context/users, journeys, capability map |
| AI system | How does AI produce the outcome and where can it fail? | AI system map, data/knowledge, guardrails |
| Measurement | How do we know it works and is sustainable? | Metrics/evaluation, economics/performance |
| Delivery | What actually runs and who keeps it operating? | Architecture/integrations, operations/dependencies |
| Direction | What is live, planned, blocked, or debt? | Current state/roadmap, product debt |
| Takeover | What is risky, unknown, and next? | Risks/unknowns, stakeholder agenda, 30/60/90 plan |
| Reference | What must be looked up precisely? | Drift register, glossary/source map |

Omit no required decision area. If evidence is absent, keep the page and state the unknown, impact, owner, and validation action.

## Reading routes

Create:

- **Executive 15-minute route:** executive brief → product thesis → AI system → scorecard → top risks → 30-day priorities.
- **AI PM complete route:** configured order from product to takeover plan.
- **Engineering/ML route:** AI system → data → evaluation → architecture → operations → risks.
- **Leadership route:** executive brief → value → scorecard → roadmap/debt → 30/60/90 plan.
- **Cross-functional review route:** problem → design decisions → system → quality/safety → results/lessons.

## Page contract

Each page in `dossier.json` defines:

- `slug`, `title`, `summary`, `minutes`, `sources`.
- `rationale` when no direct source exists.
- `home: true` for exactly one cover page.
- Optional `status`: `verified`, `supported`, `inferred`, or `unknown`.

Each evidence-heavy page should end with:

- **What we know.**
- **What remains uncertain.**
- **Why it matters.**
- **Next validation or decision.**

## Diagrams

Use only decision-useful diagrams:

- Product ecosystem and role map.
- End-to-end user journey with AI/human handoffs.
- AI runtime sequence.
- Data/knowledge flow and trust boundaries.
- Metric tree from business outcome to system indicators.
- Dependency and ownership map.

Label inferred edges and confidence. Avoid decorative architecture.

## External sharing boundary

The internal dossier may contain confidential paths and operational detail. Any externally shared version must be separately sanitized and should explain problem framing, method, design decisions, architecture, trade-offs, verification, and lessons without exposing company information.
