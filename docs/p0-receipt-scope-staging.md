# Unreleased P0 — receipt authorization and verification (25 November 2026)

Isolated staging candidate `p0-receipt-scope-0731`, based on `portal-context-0730`. Not included in public 0.7.28; signed feed and production unchanged.

## Problem and evidence
Five of six initial regression tests reproduced failures: a cached action could report prior success after the tab grant was revoked or paused; lookup could return a receipt during credential handoff or after a parent grant disappeared; a failed historical record could claim verification. No fresh browser action was executed by these replay tests. These are our synthetic findings, not reports about Browser Core from customers.

## Correction
Cached replay and receipt lookup now require an active grant, live writer, valid parent lineage and no manual pause or credential handoff. A failed record cannot claim verified success; corrupted cached records block re-dispatch and require review. The original operation ID remains the idempotency key. Receipts are historical metadata, not evidence that a downloaded file exists or a remote transaction succeeded.

## Verification
Eight targeted tests, 62 selected Python tests in total, 60 JS regression checks and four isolated headless Chromium fixture cases passed. No actual user file/account access. Live native Mac acceptance, packaging and signing remain pending. No new public feature, expanded browser permissions, file transfer, or paid activation.

## Demand and next step
Independent reports [Browser Use #5132, 3 July 2026](https://github.com/browser-use/browser-use/issues/5132) and [agent-browser #989, 24 March 2026](https://github.com/vercel-labs/agent-browser/issues/989) describe completed downloads reported as failures and repeated downloads of an invoice respectively. The latter issue is closed. These support investigating download receipts for operators and bookkeepers, not demand for our specific fix or willingness to pay. Browser-native downloads APIs and official document exports are alternatives; browser-wide download history must not be exposed. Actual download verification remains a separate P1 design/test task requiring explicit file consent and reliable correlation with the approved action.
