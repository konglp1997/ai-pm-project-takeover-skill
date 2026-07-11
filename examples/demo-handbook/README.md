# Handbook maintenance

1. Edit page metadata and order in `handbook.json`.
2. Edit source fragments in `content/<slug>.html`.
3. Rebuild with `python3 /path/to/build_handbook.py .`.
4. Verify with `python3 /path/to/verify_handbook.py .`.

Do not edit `index.html`, `pages/`, or `assets/search-index.js` directly.
