# Information architecture

Design around reader decisions instead of source-file locations.

## Default progression

| Section | Reader question | Typical pages |
|---|---|---|
| Start here | What is this and how should I read it? | Cover, reading guide |
| Overview | What does it own and how is it shaped? | Purpose, boundaries, architecture |
| Evolution | Why does the current design exist? | Timeline, decisions, migrations |
| Domain | Which concepts and rules matter? | Model, glossary, invariants |
| Runtime | What happens when it receives work? | Capabilities, flows, modules |
| Data and integrations | Where does state live and who exchanges it? | Data map, APIs, events, external systems |
| Operations | How do I run and support it safely? | Setup, deployment, observability, recovery |
| Reference | What must I look up precisely? | Commands, conventions, API index, drift |

Omit sections with no evidence. Do not create filler.

## Page boundaries

- Give each page one answerable question.
- Split pages with independent audiences or multiple major flows.
- Merge documents describing the same concept.
- Keep exact reference data in tables or dedicated pages.
- Separate historical context from current instructions.
- Use stable lowercase slugs containing letters, digits, and hyphens.

## Reading routes

Provide three routes:

1. **Complete**: configured page order.
2. **Quick**: purpose, architecture, one representative flow, operations quick start, and drift register.
3. **Role routes**: at most five roles, each pointing to required pages.

Ensure every route uses real links and matches `handbook.json`.

## Page specification

Define each page with:

- `slug`: stable identifier.
- `title`: reader-facing title.
- `summary`: one-sentence promise.
- `minutes`: realistic reading time.
- `sources`: repository-relative evidence paths.
- `rationale`: required when no source file directly supports the page.
- `home`: true only for the root cover page.

## Diagram selection

Use a diagram only when it clarifies relationships prose cannot:

- Boundary/dependency map for three or more components.
- Sequence for a multi-stage runtime path.
- State diagram for lifecycle transitions.
- Data flow for producers, stores, and consumers.

Label inferred edges. Avoid decorative diagrams.
