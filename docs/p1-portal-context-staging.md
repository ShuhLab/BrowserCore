# Unreleased P1 correction — Portal Bridge document/route binding

25 November 2026. Staging candidate `portal-context-0730` based on the most recent `p0-lineage-0729` working tree. **Not part of the public 0.7.28 downloads; not in production.** Signed update v3 remains 0.7.27.

## Problem and proof
The previous Portal Bridge compared URL paths after removing query and fragment information. A same-path account/record switch could therefore leave a stale preview usable. Synthetic regression reproduced two writes after a simulated account route change. A separate test reproduced a KeyError when a tab grant disappeared during asynchronous preview. Public reports [agent-browser #1922, 18 September 2026](https://github.com/vercel-labs/agent-browser/issues/1922) and [#1677, 10 August 2026](https://github.com/vercel-labs/agent-browser/issues/1677) illustrate related navigation hazards; they do not prove the same underlying implementation defect.

## Correction
- An opaque random context ID binds the plan to each document and the exact current URL (including query/fragment), held only in the extension's isolated-world memory. The full URL is not included in the context response or journal.
- Check both grants after asynchronous reads, bind the plan to the original native connection, and validate the destination context before focusing/writing and during readback. If context changes, stop rather than replay. Concurrent cancellation and expired queued applies fail closed.
- Internal context operation only; no new public MCP capability or permissions. No file upload, transfer, submission or payment.

## How to use once released
The existing `portal_preview` / `portal_apply` flow and field mappings remain unchanged. If `PORTAL_CONTEXT_CHANGED_REPREVIEW_REQUIRED` or a related context/grant error occurs, inspect both user-authorized pages and prepare a fresh preview. If any write may have occurred, inspect the destination first; do not blindly retry. Same-document account switches that keep the identical URL still require independent account/record checks. The correction does not guarantee a page cannot autosave a field.

## Verification and remaining work
54 Python tests and 60 JavaScript suite cases passed, including six added bridge regressions and five context checks. Tests use synthetic fixtures/mocks, not live customer data. Live Chrome end-to-end acceptance, packaging and signed release are pending. No commercial activation. No new public feature: this is a correction to the existing preview.
