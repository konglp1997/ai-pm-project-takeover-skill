# Authoring guide

Write compact, evidence-backed fragments in `content/<slug>.html`.

## Voice and truthfulness

- Use calm declarative prose.
- State current behavior in present tense only when evidence supports it.
- Label history, plans, assumptions, and environment-specific behavior.
- Preserve exact identifiers, commands, fields, ports, defaults, and limits.
- Avoid marketing adjectives, unexplained acronyms, emoji, and filler.
- Prefer "Unknown from the inspected repository" to invented completeness.

## Fragment rules

- Start with page content, not `h1`; the builder supplies the title.
- Use `h2` and `h3` for the on-page table of contents.
- Use `h4` inside cards and callouts.
- Use `href="page:architecture"` and `src="asset:diagrams/overview.svg"`.
- Do not use inline scripts, event handlers, iframes, or remote assets.
- Give informative images meaningful `alt`; use empty `alt=""` only for decorative images.

## Components

```html
<aside class="callout warning">
  <h4>Operational risk</h4>
  <p>This command applies migrations. Back up the database first.</p>
</aside>
```

Variants: `note`, `tip`, `warning`, `danger`, `drift`.

```html
<div class="cards">
  <article class="card"><h4>API</h4><p>Accepts requests.</p></article>
  <article class="card"><h4>Worker</h4><p>Consumes jobs.</p></article>
</div>
```

```html
<dl class="definitions">
  <div><dt>Source of truth</dt><dd><code>orders</code> table</dd></div>
  <div><dt>Delivery</dt><dd>At least once</dd></div>
</dl>
```

```html
<ol class="steps">
  <li><strong>Validate.</strong> Stop if required config is absent.</li>
  <li><strong>Start.</strong> Wait for health checks.</li>
  <li><strong>Verify.</strong> Confirm readiness.</li>
</ol>
```

## Code and diagrams

- Escape `&`, `<`, and `>` inside code.
- Put shell commands in `<pre><code class="language-shell">`.
- Distinguish safe inspection from mutating commands.
- Use `<pre class="mermaid">` only with a local Mermaid runtime.
- Prefer pre-rendered SVG when a runtime cannot be bundled legally and offline.

## Accessibility

- Maintain logical heading order.
- Use descriptive link text.
- Do not communicate status by color alone.
- Wrap wide tables in `<div class="table-scroll">`.
- Keep custom controls keyboard reachable.

## Page checklist

- Every fact has sources or is labeled inference.
- Exact values match the evidence ledger.
- Current behavior is separated from history and plans.
- Risks and destructive operations are prominent.
- Internal links point to configured slugs.
- No secrets, private endpoints, or personal data appear.
