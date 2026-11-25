# Unreleased P0 — overlapping browser commands (25 November 2026)

Browser Core connects Chrome tabs explicitly shared by the user to ChatGPT or Claude for website tasks. For example, after preparing a supplier order in a shared tab, a command may time out while Chrome is still processing it. Sending another command immediately can duplicate or interfere with the first action. Share a tab through the extension only when needed; if the outcome is unclear, inspect it manually before deciding what to do next. This correction does not submit orders, auto-confirm dialogs, cancel a previously dispatched action, or add permissions.

## Staging proof
Candidate `p0-native-single-flight-0736`, local code commit `2f5659c`, derived from `4227867`. The previous extension handler could dispatch a second operation before the first asynchronous injection settled. An isolated service-worker harness reproduced it; the baseline failed because the second request did not return the expected busy response.

The handler now reserves the physical tab ID before awaiting permission verification, rejects subsequent remote commands on the same tab with TAB_PREVIOUS_COMMAND_RUNNING, limits the number of unresolved handlers to 32, rechecks grant identity after verification and releases the reservation only when the original handler settles. Different tabs remain independent below the cap. A rejected injection also releases the reservation. It never accepts dialogs or retries a command on the user's behalf.

Two added mock-Chrome worker tests passed, with the full 62 JavaScript checks and 73 Python unittest cases. The latter include three Chromium fixture groups reporting 27 DOM cases. This is not an end-to-end timeout/reconnect test of the installed extension. A service-worker restart may discard the in-memory guard; already-dispatched browser actions may still finish, and an uncertain result must not be retried automatically. Browser-side cancellation, persistent restart-safe recovery and installed Mac/Windows tests remain outstanding. Not part of public attended preview 0.7.28 or signed 0.7.27. No new public capability or charge.

## Demand and alternatives
- [Playwright #31309, 13 June 2024](https://github.com/microsoft/playwright/issues/31309): the reporter observed a click taking effect after a timeout.
- [Playwright #42817, 20 September 2026](https://github.com/microsoft/playwright/issues/42817): a navigation with a blocking dialog waited until timeout; issue closed with linked fix.
- [agent-browser #1713, 23 August 2026](https://github.com/vercel-labs/agent-browser/issues/1713): a stalled session could survive a client timeout.
These are technical reports, not proof of identical root causes or willingness to pay. Target clients: developers, operators and small businesses using shared authenticated tabs. Prefer official portal APIs with idempotency where available; alternatives include manual verification, Playwright dialog handling or agent-browser. P0 included in baseline reliability. No automatic payment, submission, CAPTCHA bypass or permission expansion.

## Next
[Playwright #42831, 16 September 2026](https://github.com/microsoft/playwright/issues/42831) reports persistent-profile download crashes despite successful file downloads; closed with linked fix. Independently verify download receipts without reading unrelated downloads or exposing files. P1, no implementation in this candidate.
