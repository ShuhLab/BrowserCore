# Immediate tab access withdrawal — unreleased staging correction, 25 November 2026

Browser Core connects Chrome tabs that you explicitly authorize to ChatGPT or Claude so they can carry out tasks on websites. For example, while an assistant is preparing a draft order, you can withdraw access through the extension popup. This staging correction prevents new commands on that tab (and its delegated descendants) from starting during asynchronous cleanup, and prevents a revoked grant from being announced again after an overlapping verification.

**Not released:** local staging branch `p0-revoke-atomic-0738`, base `aa6d84d`, code commit `24ef076`. Neither attended 0.7.28 nor signed 0.7.27 includes this correction. It cannot undo an action already dispatched or guarantee cancellation of an in-flight website operation. No new permission, file transfer, form submission, or automatic retry.

Verification: baseline isolated worker test reproduced the fault; both new worker cases passed after correction. 73 Python unit tests, 66 JavaScript cases (including 14 worker cases), 27 isolated Chromium DOM cases passed. Installed Chrome/native-host acceptance, durable storage failure scenarios and full media teardown race testing remain pending. No production runtime, package or signed feed was modified.

Related public report: [Playwright MCP #1442](https://github.com/microsoft/playwright-mcp/issues/1442), 5 March 2026, closed after correction: stale pending relay connections across tabs. Different mechanism; no claim of equivalent competitor vulnerability or willingness to pay. Baseline safety, no additional charge.
