# Browser Core — safer target resolution (private staging, 28 November 2026)

Browser Core connects the Chrome tabs you explicitly authorize to ChatGPT or Claude for actions on websites. It is not a replacement browser.

When filling a form or choosing a record, a partial element search must not be treated as proof that the intended control is unique. The private RC2 candidate now stops an incomplete search before acting and reports that it cannot safely resolve the target. Refresh the authorized tab's summary and verify the intended control, or complete the action manually. A fresh reference does not authorize submission, additional tabs, or sensitive actions.

Verified in isolated Chromium: 12 new synthetic cases; 142 Python unittest cases and seven Node suites passed. No live user data or form submissions were used. Private staging commit `ae8185a9add8645e2ddec33684cead29d870b82b` is not a public source commit. The unsigned, non-notarized Mac candidate has not passed isolated Mac installation or rollback. The current public attended preview and signed update channel are unchanged. This note is not a download or a statement of public availability.
