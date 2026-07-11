# Quality assurance

Complete all applicable layers and report skipped layers.

## 1. Factual spot checks

Select at least one page from each evidence-heavy section and compare it with the ledger. Check:

- Commands and flags.
- Ports, URLs, config names, and defaults.
- Schema, table, field, queue, event, and workflow names.
- Limits, timeouts, retries, and statuses.
- Responsibility boundaries and external dependencies.

Correct source fragments and rebuild. Never patch generated pages.

## 2. Automated checks

```bash
python3 scripts/build_handbook.py /absolute/path/to/handbook
python3 scripts/verify_handbook.py /absolute/path/to/handbook
```

Require zero errors. Explain or resolve warnings. The verifier does not prove prose is factual or diagrams render.

## 3. Browser checks

Open `index.html` locally and inspect:

- Cover and reading guide.
- Longest or most complex page.
- A page with tables, code, and diagrams when present.
- Drift register.

Check desktop and narrow layouts, sidebar, search, previous/next, anchors, copy buttons, light/dark theme, and console errors. For Mermaid, confirm each block becomes SVG. If no browser is available, report it as not render-verified.

## 4. Accessibility and offline checks

- Navigate controls with the keyboard and confirm visible focus.
- Confirm image alternative text.
- Confirm no remote fonts, scripts, styles, images, media, or APIs are required.
- Confirm `file://` direct opening works.

## 5. Security review

Search source and output for private keys, tokens, real environment values, authenticated URLs, internal hosts, personal paths, inline scripts, and remote resources. Treat automation as a prompt for manual review, not proof of safety.

## Delivery criteria

- The docs-first, hybrid, or code-first route is recorded.
- Every page exists and has attribution or rationale.
- Reading routes work.
- Drift register exists and unresolved items are visible.
- Builder and verifier pass.
- Browser, responsive, theme, Mermaid, and offline checks are reported accurately.
- Maintenance instructions explain how to update and rebuild.
