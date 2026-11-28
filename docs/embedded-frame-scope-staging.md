# Embedded forms — private RC2 staging preview (28 November 2026)

Browser Core connects the Chrome tabs you explicitly authorize to ChatGPT or Claude for website actions. If a form is embedded in a page, a read of the surrounding page must not be mistaken for a read of that form.

The private RC2 candidate adds two read-only fields to `existing_tab_snapshot`: `frame_scope: top_document_only` and `embedded_frames: detected` or `not_observed`. Only the main document and bounded open shadow roots are inspected. No embedded document contents, frame URL, credentials or form values are accessed; no browser permissions are added. `not_observed` is not proof of absence. If the task is inside an embedded form, inspect it manually or use the site's authorized integration. Do not select a different control in the outer page as a substitute. This is not iframe automation.

Synthetic Chromium verification: seven subcases (plain page, same-origin frame, other-origin frame, hidden frame, open shadow, closed shadow and traversal bound); no child content or URLs returned. 149 Python tests, 21 recovery QA cases and seven Node suites passed on Linux; the private package was checked. Actual installed Chrome/Mac transport and complete rollback remain unverified. Not available in the attended preview or signed feed. No distribution or production change.
