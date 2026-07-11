---
name: build-project-handbook
description: Turn a software repository's scattered, stale, or missing documentation into a structured, searchable, offline HTML handbook grounded in source-code evidence. Use when Codex is asked to reorganize project docs, create a documentation website or project book, prepare an onboarding guide, explain an unfamiliar codebase, reconcile docs with implementation, or derive documentation from a repository with little reliable documentation. Supports docs-first, hybrid, and code-first workflows and produces reading routes, source attribution, a drift register, a static site, and a verification report.
---

# Build Project Handbook

Create a readable project handbook from repository evidence. Treat executable code and runtime configuration as the current-state baseline; treat documents, comments, and history as evidence that may be incomplete or stale.

## Choose the route

Inventory the repository before drafting:

| Route | Signals | Primary evidence |
|---|---|---|
| Docs-first | Architecture, setup, data, and operations are documented and agree with code | Documents with targeted code checks |
| Hybrid | Documents cover only part of the system or conflict with implementation | Documents plus systematic code survey |
| Code-first | No useful docs beyond a short README or comments | Entrypoints, configuration, schemas, tests, and history |

Read [references/source-audit.md](references/source-audit.md) before a hybrid or code-first survey. Use its evidence-ranking and secret-handling rules for every route.

## Workflow

### 1. Establish scope and safety

- Confirm the repository root and output location.
- Preserve user files and unrelated worktree changes.
- Exclude credentials, private data, generated dependencies, and binary output.
- Record uncertainty instead of inventing missing facts.
- Do not run applications, migrations, deployments, or networked tests unless requested and safe.

### 2. Build an evidence ledger

Create temporary working notes outside the published site:

- `inventory.md`: documents, entrypoints, modules, schemas, configuration, deployment, tests, and history.
- `source-map.md`: planned claims or pages mapped to source paths and confidence.
- `drift-register.md`: document-versus-code conflicts and unresolved gaps.

Use exact file paths and symbols. Keep copied excerpts short. Follow [references/source-audit.md](references/source-audit.md).

### 3. Design the reading architecture

Organize by reader questions, not the repository's directory tree. Start with this progression and omit empty sections:

1. Start here: purpose, audience, reading routes.
2. System overview: responsibilities, boundaries, architecture.
3. Evolution and decisions.
4. Domain concepts, rules, and terminology.
5. Runtime capabilities and end-to-end flows.
6. Data, APIs, events, and external integrations.
7. Setup, configuration, deployment, observability, and recovery.
8. Commands, conventions, glossary, and drift register.

Read [references/information-architecture.md](references/information-architecture.md) before finalizing the page list.

### 4. Scaffold the site

Run:

```bash
python3 scripts/scaffold_handbook.py /absolute/path/to/handbook
```

The command creates missing starter files without overwriting existing ones. Edit `handbook.json` first; it is the single source of truth for page order, navigation, metadata, and attribution.

### 5. Author evidence-backed pages

- Write HTML fragments in `content/<slug>.html`; omit `html`, `head`, `body`, scripts, and page-level `h1`.
- Preserve exact commands, identifiers, ports, table names, defaults, and numeric thresholds.
- Distinguish current behavior, history, plans, environment-specific behavior, and inference.
- Add `sources` or a clear `rationale` to every page in `handbook.json`.
- Include a reading guide and drift register, even if the latter states no conflicts were found.
- Use `href="page:<slug>"` for pages and `src="asset:<path>"` for local assets.

Read [references/authoring.md](references/authoring.md) for components, tone, accessibility, diagrams, and fact preservation.

### 6. Build and verify

```bash
python3 scripts/build_handbook.py /absolute/path/to/handbook
python3 scripts/verify_handbook.py /absolute/path/to/handbook
```

The builder generates `index.html`, `pages/*.html`, and `assets/search-index.js`. The verifier checks configuration, content, output completeness, links, anchors, forbidden HTML, source attribution, remote assets, path traversal, and common secret patterns.

Then perform [references/quality.md](references/quality.md): factual spot checks, browser rendering, responsive layout, keyboard navigation, dark theme, offline behavior, and final drift review. Never claim browser or Mermaid rendering was verified unless it was actually rendered.

### 7. Deliver transparently

Report:

- Output location and how to open `index.html`.
- Selected route: docs-first, hybrid, or code-first.
- Pages and evidence sources covered.
- Drift items and unresolved uncertainty.
- Commands run and their results.
- Checks not performed and why.

Keep working notes out of the published site unless requested.

## Resource map

| Need | Resource |
|---|---|
| Survey, evidence confidence, drift, secret handling | [references/source-audit.md](references/source-audit.md) |
| Chapters, page sizing, reading routes, diagrams | [references/information-architecture.md](references/information-architecture.md) |
| HTML fragments, components, tone, accessibility | [references/authoring.md](references/authoring.md) |
| Static checks, browser QA, delivery criteria | [references/quality.md](references/quality.md) |
| Create a safe starter site | `scripts/scaffold_handbook.py` |
| Build the offline site | `scripts/build_handbook.py` |
| Verify source and output | `scripts/verify_handbook.py` |

## Hard rules

- Do not present inference as implemented fact.
- Do not copy secrets into notes, pages, screenshots, examples, or search indexes.
- Do not silently resolve document-code conflicts; record them.
- Do not edit generated `index.html`, `pages/`, or `assets/search-index.js`; edit sources and rebuild.
- Do not claim offline Mermaid support unless a local runtime is present or diagrams are pre-rendered.
- Do not overwrite an existing handbook during scaffolding.
