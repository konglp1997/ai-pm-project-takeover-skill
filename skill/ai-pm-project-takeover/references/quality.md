# Quality and delivery gates

The dossier is complete only when it is factually credible, decision-useful, safe, and reproducible.

## 1. Coverage gate

Confirm the dossier addresses product, users, journeys, capabilities, AI system, data, evaluation, metrics, economics, architecture, operations, roadmap, product debt, risks, unknowns, stakeholders, and 30/60/90 plan.

Missing evidence becomes an explicit E0 item; it does not justify omitting the decision area.

## 2. Factual spot check

Check at least one page from every major part against source evidence. Always verify:

- Rollout state and product scope.
- Metric definition and segmentation.
- Model/provider/config routing.
- Prompt/context/retrieval/tool sequence.
- Evaluation dataset, rubric, baseline, and release gate.
- Data source, ownership, privacy, and retention.
- Cost, latency, failure, fallback, and human review.

Correct source fragments and rebuild; never patch generated HTML.

## 3. Decision-readiness gate

For each major conclusion ask:

- What decision does this support?
- What evidence and confidence support it?
- What could make it wrong?
- Who owns validation or action?
- What is the consequence of waiting?

Reject generic recommendations without owner, measure, dependency, and exit criterion.

## 4. Automated gate

```bash
python3 scripts/build_dossier.py /absolute/path/to/ai-pm-dossier
python3 scripts/verify_dossier.py /absolute/path/to/ai-pm-dossier
```

Require zero errors. Resolve or explain warnings. Automation does not prove product truth or AI quality.

## 5. Browser and accessibility gate

Open `index.html` locally and inspect cover, executive brief, AI system, metrics/evaluation, risk, and takeover plan pages. Check desktop/narrow layouts, search, navigation, anchors, code copy, light/dark theme, keyboard focus, print, and console errors.

If Mermaid is used, confirm each block becomes SVG. Report honestly when browser rendering was not performed.

## 6. Confidentiality gate

Inspect content, config, generated pages, search index, diagrams, and screenshots for credentials, customer data, private prompts, proprietary datasets, internal hosts, personal paths, signed URLs, and unapproved metrics.

Internal dossier and public portfolio case study must be separate when confidentiality applies.

## 7. Interview gate

Be able to explain:

1. The incoming AI PM problem.
2. Why repository summarization alone is insufficient.
3. The evidence and confidence model.
4. Product and AI-system audit architecture.
5. How metrics connect business value to model/system behavior.
6. Why deterministic scripts handle build/verification.
7. Safety, privacy, offline design, and limitations.
8. Test evidence and next roadmap.
