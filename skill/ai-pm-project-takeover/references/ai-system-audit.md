# AI system audit

Describe AI as a product system, not a model name.

## Trace an AI experience

For each material AI capability, trace:

```text
User intent
  → input validation and policy
  → context assembly
  → retrieval / memory
  → prompt and orchestration
  → model call(s)
  → tools / agents / external actions
  → output validation and guardrails
  → human review or automated action
  → feedback, logging, and evaluation
```

Document the real runtime path; do not infer it from a marketing diagram.

## AI capability card

| Field | What to record |
|---|---|
| Product value | User outcome and job-to-be-done |
| Trigger | User action, event, schedule, or agent decision |
| Inputs | User data, retrieved data, memory, tools, configuration |
| Model layer | Provider, model class, routing, parameters, fallback |
| Orchestration | Prompt chain, agent loop, state machine, workflow |
| Output contract | Format, schema, confidence, citations, downstream action |
| Human control | Review, approval, edit, undo, escalation |
| Failure modes | Quality, safety, timeout, tool, retrieval, context, cost |
| Evaluation | Dataset, rubric, judge, baseline, release gate, monitoring |
| Economics | Tokens, calls, caching, cost per task, latency budget |
| Governance | Privacy, retention, access, policy, auditability |
| Confidence | E0–E3 and missing evidence |

## Prompt and context audit

- Locate system/developer/user templates and runtime assembly.
- Identify versioning, ownership, experiments, localization, and environment differences.
- Check injection boundaries, secret exposure, data minimization, and tool permissions.
- Separate durable policy from task instructions and retrieved content.
- Record truncation, context ordering, memory, and citation behavior.

Do not copy confidential prompt text into public materials. Describe structure and decision rationale.

## RAG and knowledge audit

Inspect ingestion, parsing, chunking, metadata, embeddings, indexing, retrieval, reranking, filters, citations, freshness, deletion, tenancy, and feedback. Ask:

- Which source is authoritative?
- How quickly do updates appear?
- Can one tenant retrieve another tenant's data?
- How is retrieval quality measured separately from answer quality?
- What happens when evidence is absent or contradictory?

## Agent and tool audit

- Map planner/controller, state, tools, permissions, termination, retries, and idempotency.
- Identify actions with irreversible, external, financial, privacy, or permission effects.
- Verify confirmation, least privilege, sandboxing, rate limits, and audit logs.
- Look for loop, compounding-error, and tool-selection failure modes.
- Distinguish “agentic UI” from genuinely autonomous execution.

## Guardrails and human oversight

Map prevention, detection, response, and recovery:

- Input policy and access control.
- Output schema and groundedness validation.
- Content/safety policy.
- Human approval and escalation.
- Fallback, retry, circuit breaker, and graceful degradation.
- Incident logging, replay, rollback, and user remediation.

## Vendor and model risk

Record provider dependency, data terms, residency, model deprecation, rate limits, quota, fallback compatibility, reproducibility, and switching cost. Avoid roadmap commitments that assume unverified model capability.
