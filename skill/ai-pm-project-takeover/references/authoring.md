# Evidence-backed dossier authoring

Write for decision-makers while preserving technical truth.

## Voice

- Lead with outcome, decision, or risk—not implementation chronology.
- Explain technical mechanisms in product language, then give exact technical evidence.
- Separate shipped fact, supported conclusion, inference, plan, and unknown.
- Preserve identifiers, metric definitions, commands, model routing, thresholds, and contracts exactly.
- Avoid hype such as “intelligent,” “powerful,” or “accurate” without evidence.

## Confidence badges

Use:

```html
<span class="evidence e3">E3 · Verified</span>
<span class="evidence e2">E2 · Supported</span>
<span class="evidence e1">E1 · Inferred</span>
<span class="evidence e0">E0 · Unknown</span>
```

Attach badges to material claims or section summaries. Never decorate every sentence.

## Decision block

```html
<section class="decision-block">
  <h3>Activation definition is not stable</h3>
  <p><strong>Evidence.</strong> Two dashboards use different events.</p>
  <p><strong>Impact.</strong> Onboarding experiments cannot be compared.</p>
  <p><strong>Action.</strong> Align event contract with Product and Data.</p>
  <span class="evidence e2">E2 · Supported</span>
</section>
```

## AI capability card

```html
<article class="capability-card">
  <h3>Knowledge-grounded answer</h3>
  <dl class="definitions">
    <div><dt>User outcome</dt><dd>Resolve a policy question with evidence.</dd></div>
    <div><dt>AI mechanism</dt><dd>Retrieve, rerank, generate, cite.</dd></div>
    <div><dt>Human control</dt><dd>Open source, edit answer, report issue.</dd></div>
    <div><dt>Release gate</dt><dd>Groundedness and citation validity.</dd></div>
  </dl>
</article>
```

## Risk table

Include risk, scenario, affected user/outcome, impact, likelihood, detectability, confidence, mitigation, owner, and next checkpoint. Do not create scores without explaining scale.

## Fragment rules

- Write `content/<slug>.html` fragments without `html`, `head`, `body`, scripts, or page-level `h1`.
- Use `h2`/`h3` for page navigation and `h4` inside cards.
- Link pages with `href="page:<slug>"` and assets with `src="asset:<path>"`.
- Use standard semantic HTML and descriptive alternative text.
- Do not use remote assets, event-handler attributes, iframes, or untrusted HTML.
- Use tables for exact comparisons, flows for sequence, and cards for repeated capability dimensions.

## Public case study rules

- Replace company/project names with neutral descriptors when required.
- Remove customer data, screenshots, prompts, metrics, internal architecture, paths, endpoints, and vendors if confidential.
- Present your process, decisions, trade-offs, tooling, verification, and lessons.
- Never imply business impact that was not measured.
