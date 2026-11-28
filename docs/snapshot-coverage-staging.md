# Browser Core — snapshot coverage (internal staging only, 28 November 2026)

Browser Core connects the Chrome tabs you explicitly authorize to ChatGPT or Claude for actions on websites. It is not a replacement browser.

## Why this matters
When checking a long list or a form, a short page summary is not a complete export. Previously, newline separators and the 80-action-reference limit could omit material without setting the truncation flag.

## Verified isolated prototype
Local staging commit `e3bcc5652319cba5cd9ba1a3928ef8146b1aa1d3` (not a public source commit) marks the rendered DOM scope with `coverage: "rendered_dom_only"` and reports the text, action-reference and open-shadow-root limits via `truncated`. In a synthetic grid with 200 declared rows and 20 rendered rows, the summary still contains only those 20. A false truncation flag does **not** establish completeness. For full records prefer an authorized native export/API, or explicitly verify the count and filters. No automatic scrolling, hidden-data extraction, changes to exact Portal Bridge fields, form submission, or expansion of permissions.

141 Python tests and seven Node suites passed, including synthetic Chromium coverage cases. Private unsigned Mac candidate SHA-256 `6c2c7eed9d2ff0ca11b4ddaa8f2e21fa12180a5aae9fd9f136b99983466d5266`. No Mac installation or rollback verified; not signed or notarized. This is not a download, production capability, or an attended-preview update. The existing public releases are unchanged.

## Research
- [Capterra Octoparse reviews](https://www.capterra.com/p/150508/Octoparse/reviews/) — 5 August 2026: independent solo consultant reports setup and troubleshooting burden on dynamic pages, pagination and inconsistent formatting.
- [G2 Thunderbit reviews](https://www.g2.com/products/thunderbit/reviews) — 6 May 2026: small-business operator reports difficulties with infinite scrolling on large datasets.
- [Independent operator request](https://www.reddit.com/r/learnjavascript/comments/1g6kbo3/) — 18 October 2024: internal table exposes only about 20 of 200 rows at once.
- [Web Scraper documentation](https://webscraper.io/documentation/guides/pagination-load-more-infinite-scroll) describes native tool alternatives; no generic bulk scraper is being added. No paid demand for Browser Core established.
