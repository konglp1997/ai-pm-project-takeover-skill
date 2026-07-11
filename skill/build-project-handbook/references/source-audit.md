# Source audit

Establish a defensible factual baseline before outlining or writing.

## Evidence priority

Rank evidence in this order unless the repository proves otherwise:

1. Executable implementation and runtime wiring.
2. Tests that assert current behavior.
3. Schemas, migrations, API specifications, and deployment configuration.
4. Maintained top-level guidance such as `AGENTS.md`, `README.md`, or decisions.
5. Module documentation and comments.
6. Issues, planning documents, old examples, and commit messages.

Higher-ranked evidence is not automatically correct. Generated files can be stale and tests can be skipped. Record conflicts instead of forcing certainty.

## Survey passes

### Repository shape

- Identify languages, package managers, build systems, workspaces, and generated directories.
- Find repository guidance and nested instructions.
- Locate documents, examples, tests, schemas, migrations, infrastructure, and CI.

### Entry and startup

- Find application, worker, CLI, and scheduled-job entrypoints.
- Trace configuration loading, dependency registration, and startup order.
- Record processes started and conditions that enable them.

### Boundaries and dependencies

- Identify modules and their responsibilities.
- Trace dependency direction and integration adapters.
- State what the system does and what it delegates elsewhere.

### Data and state

- Trace representative input-to-output flows.
- Locate state machines, queues, caches, schemas, and idempotency keys.
- Mark the authoritative store for each important entity.

### Operations

- Inspect example environment files without copying real values.
- Record ports, services, health checks, deployment, observability, backup, and recovery.
- Mark destructive scripts, migrations, and production-only flags as hazards.

### Evolution

- Use releases, decisions, migrations, deprecations, and focused history searches.
- Do not turn chronology into a causal narrative without evidence.

## Evidence ledger

| Claim or topic | Evidence | Confidence | Notes |
|---|---|---|---|
| Server starts after configuration validation | `src/main.py`, `tests/test_startup.py` | High | Test covers missing config |
| Cache is optional | `config.example.env`, `src/cache.py` | Medium | Production not inspected |

Confidence:

- **High**: directly established by implementation plus tests or wiring.
- **Medium**: supported by one strong source or several indirect sources.
- **Low**: inferred, historical, environment-specific, or contradicted.

## Drift register

| Document says | Current evidence says | Authority and action | Sources |
|---|---|---|---|
| Service listens on 8080 | Default is 8081 | Use code default; update docs | `docs/setup.md`, `src/config.py` |

If unresolved, write "Unresolved" and state which evidence is missing.

## Secret handling

- Never copy `.env` values, tokens, cookies, private keys, credential-bearing URLs, customer data, or internal hostnames without explicit publication approval.
- Document variable names with placeholders such as `DATABASE_URL=<required>`.
- Redact as `***REDACTED***`; never preserve parts of real credentials.
- Inspect screenshots for terminals, usernames, paths, notifications, and sessions.

## Completion test

Answer before drafting final prose:

- What problem does the system solve and for whom?
- Where are its responsibility boundaries?
- How does it start and receive work?
- What are the major runtime paths?
- Where does state live?
- Which external systems are required?
- How is it configured, deployed, observed, and recovered?
- Which documentation is stale or uncertain?
