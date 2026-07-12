# Metrics and evaluation system

Connect user value to model behavior and operational reality.

## Five-layer scorecard

| Layer | Example questions | Example metrics |
|---|---|---|
| Business | Does the product create economic value? | Revenue, conversion, cost avoided, expansion, margin |
| Product | Do users reach and repeat value? | Activation, task completion, retention, depth, time-to-value |
| AI quality | Does the AI complete the task well? | Accuracy, groundedness, task success, preference, edit distance |
| Safety/trust | Can users rely on and control it? | Harm rate, override, escalation, citation coverage, incident rate |
| System | Is the experience fast, reliable, and affordable? | P50/P95 latency, availability, fallback, token/call cost, failure rate |

Never use model quality as a substitute for product outcome.

## Metric contract

For every important metric record:

- Name and decision it informs.
- Exact numerator, denominator, exclusions, window, and unit.
- Population and segmentation.
- Event/source and data owner.
- Baseline, target, guardrail, and confidence.
- Cadence, dashboard, reviewer, and response threshold.

Mark metrics without stable definitions as product debt.

## Evaluation architecture

Separate:

1. **Component evals:** retrieval, classification, extraction, tool selection, schema adherence.
2. **End-to-end task evals:** representative user tasks and workflows.
3. **Safety evals:** adversarial, privacy, prompt injection, harmful action, policy.
4. **Human evaluation:** domain rubric, calibration, disagreement handling.
5. **Online evaluation:** experiments, implicit feedback, complaint and override signals.

For each evaluation capture dataset provenance, representativeness, rubric, judge, baseline, sample size, reproducibility, release gate, and owner.

Tests that only execute code do not count as AI quality evaluation.

## Evaluation gaps

Common gaps:

- Only curated happy-path examples.
- No production distribution or hard cases.
- LLM judge without calibration or human agreement.
- Aggregate score hides user/locale/task segments.
- Retrieval and generation errors are not separated.
- No regression suite for prompt/model changes.
- No cost/latency/safety guardrails in release decisions.

## Feedback loop

Map signal collection → labeling → analysis → backlog/evaluation update → release decision → monitoring. Distinguish explicit user feedback, implicit behavior, support reports, human edits, and model-generated labels.

Prevent feedback contamination, privacy leakage, silent label drift, and optimizing for easily measured proxy signals.

## Unit economics

Estimate per meaningful task, not per model call:

- Model calls, tokens, retrieval, tools, storage, review labor, and support.
- Cache/fallback rate and retry amplification.
- Cost distribution by segment and heavy users.
- Gross value or willingness-to-pay proxy.
- Marginal cost trend as usage grows.

State assumptions and confidence. Do not fabricate absent cost data.
