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
54 Python tests and 60 JavaScript suite cases passed, including six added bridge regressions and five context checks. Four additional cases passed using a real isolated headless Chromium DOM fixture (successful fill, changed query, navigation during beforeinput, and reload). This evaluates the DOM functions in the page, not the installed native extension or real customer data. Native Chrome end-to-end acceptance, packaging and signed release are pending. No commercial activation. No new public feature: this is a correction to the existing preview.


## 26 November 2026 — explicit record label guard (private RC2 prototype, not released)

Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude for website actions. An operator preparing a status draft must not fill order B after reviewing order A. The unchanged URL/document context is insufficient: on RC2 a real isolated Chromium fixture switched visible label ORD-001 to ORD-002 and a draft fill still succeeded. No submission occurred. This was not a production incident.

Local staging branch `consolidated-0729-rc2-record-guard`, commit `0126d2ede30294d9f40496ed789d99047467ea7b`, based on `a8157dc`. The prototype accepts an optional `target_record` object in the existing preview JSON, e.g. `"target_record":{"selector":"#order","value":"ORD-001"}` (synthetic example). The user must explicitly confirm the non-secret identifier and the destination tab before use. Only a unique, visible static leaf text label is accepted; editable, hidden, ambiguous or protected labels fail closed. New internal check/fill operations prevent an older extension silently ignoring the guard. Preview, apply, focus, beforeinput, readback and replay are checked; no automatic retry of uncertain results. Existing unguarded plans do NOT verify business record identity. This is not proof of true account identity or protection from site autosave; avoid live status forms until manually verified. No new browser permissions, submission, file handling or payments. No production use of this argument.

133 unittest cases, 37 isolated Chromium fixture scenarios (10 new), seven JS suites passed before the final scope recheck; a focused 36-test rerun passed after it. Full rerun/native extension path and Mac acceptance still to be verified on the final commit; packaging, full installer rollback and signed release remain blocked. No public feature or download.
