# Unreleased P0 — Portal Bridge replay scope (25 November 2026)

Candidate: `p0-portal-replay-0732`, separate local staging branch based on `p0-receipt-scope-0731`. Not in public 0.7.28 or signed 0.7.27.

## Reproduced defect
A prior Portal Bridge plan could return its cached draft result after revocation, pause, a changed document, or disconnected writer. A final fill could report success after the source grant disappeared. Six of seven focused synthetic regression tests failed before the correction.

## Correction
Both source and destination must have current grants, valid ancestor lineage, a connected writer, and no takeover or credential handoff. Status and cancellation check live grant and URL scope; status is explicitly historical, not current form verification. Cached apply rechecks both document context identifiers and grant scope before returning a stored result. The final write path rechecks grant scope and both contexts; uncertainty requires human review and is not retried automatically. No form submission or file transfer added.

## Verification and limitations
69 selected Python tests passed (including seven targeted tests and four isolated headless Chromium fixture cases); 60 JavaScript cases passed. No live user accounts, files, installed extension or production deployment tested. Native Mac/Chrome end-to-end acceptance and signed packaging remain pending. Context checks do not certify that a previously filled form still contains the same values; inspect it before any submission. No new public capability or video release.