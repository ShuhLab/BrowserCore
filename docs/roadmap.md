# Browser Core remaining release gates

Current public release 0.7.19-beta. Confirmed active: Local Chrome per-tab consent, BYO, limited ephemeral Cloud, manual handoff, real DOM checks, task-authorized browser submissions, signed **Mac/Linux** background update bootstrap.

Not yet finished:
1. **YooKassa and Telegram Stars**: public checkout, fiscal receipt handling for future-period renewals, account-bound entitlement activation, refunds and one real opt-in purchase/rollback test. Merchant approval alone does not open sales.
2. **Protected API key connection**: complete local UI, device attestation, encrypted handoff and live target validation; currently prototype/staging only.
3. **Windows native Chrome and auto-updates**: current 0.8.4-beta is standalone and manually updated.
4. Apple Developer ID signing/notarization, bundled runtime, cross-platform update acceptance and tested rollback on actual OS devices.
5. Server-side duplicate-tab/session reuse and user-configurable task concurrency; a local duplicate badge alone does not enforce execution limits.
6. Exact provider token charges where available. Bytes/4 extension estimates are **not** billable model tokens.
7. Independent security and reliability audit, commercial scaling and meaningful SLAs.

Existing user devices and sessions are not force-updated merely by publishing a signed beta.

- **Parallel-tab command scheduling**: implemented in Mac beta 0.7.19 with a per-tab serial queue; owner-configurable multi-worker concurrency and resource metering remain future work.
