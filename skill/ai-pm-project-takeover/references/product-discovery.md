# Product discovery reconstruction

Reconstruct the product model before describing features.

## Product thesis

Write a one-page product thesis:

- **Context:** What changed in the market, workflow, or technology?
- **User:** Who experiences the problem, buys, configures, operates, reviews, and consumes output?
- **Problem:** What job is difficult today and what is its current workaround?
- **Promise:** What measurable outcome should improve?
- **Mechanism:** Why is AI necessary or materially better here?
- **Boundary:** What is intentionally outside the product?
- **Proof:** Which adoption, quality, or business evidence supports the thesis?
- **Uncertainty:** Which assumptions remain unvalidated?

Do not derive the problem statement from feature names alone.

## Stakeholder and user model

Distinguish roles:

| Role | Questions |
|---|---|
| End user | What job do they complete and what do they trust? |
| Buyer | Which outcome, risk, or budget drives purchase? |
| Admin | What must be configured, governed, or integrated? |
| Operator | What manual work keeps the product functioning? |
| Reviewer | Who validates AI output and bears accountability? |
| Downstream consumer | Which system or person acts on the output? |

For each role capture context, goal, frequency, alternatives, constraints, success signal, failure cost, and evidence confidence.

## Journey reconstruction

Map at least one happy path and one failure/recovery path:

```text
Trigger → Entry → Setup/context → AI work → Review/control → Action/export → Feedback → Repeat use
```

For every step document:

- User intent and action.
- System behavior and AI behavior.
- Required data/context.
- Decision, wait, handoff, or friction.
- Observable event and success criterion.
- Failure mode and recovery owner.

## Capability map

Organize capabilities by user outcome rather than code modules:

| Outcome | Capability | User/role | AI contribution | Rollout | Evidence | Gap |
|---|---|---|---|---|---|---|

Use rollout states: `live`, `limited`, `internal`, `partial`, `planned`, `deprecated`, `unknown`.

## Scope and lifecycle

Determine whether the product is discovery, prototype, pilot, early scale, growth, mature, or sunset. Use evidence such as active users, rollout controls, support burden, metrics discipline, operational playbooks, and roadmap horizon.

Separate:

- Product strategy from current backlog.
- Platform capability from user-facing product.
- Custom delivery work from repeatable product behavior.
- AI novelty from durable user value.

## Product debt

Capture debt that blocks product decisions:

- Missing persona or job definition.
- No canonical journey or scope boundary.
- Feature flags without rollout rationale.
- Manual operations hidden from product metrics.
- No activation/retention definition.
- AI outputs without review or recovery design.
- Roadmap items without evidence or decision owner.

Turn each debt item into an owner, decision, validation method, and target date.
