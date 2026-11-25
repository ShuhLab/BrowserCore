# Unreleased P0 — Native connection isolation (25 November 2026)

Browser Core connects only Chrome tabs that the user explicitly shares with ChatGPT or Claude for website actions. For example, if the connection drops while an assistant is filling an order form, reconnecting must not make an old answer look like the result of the new connection. Reconnect through the extension and inspect the form yourself before deciding whether a new action is necessary. Filling a draft is not proof of submission.

## Reproduction and correction

Staging branch `p0-native-port-isolation-0737` (base `2f5659c`, implementation `28852d4`, fixture adjustments `92b0536`). A delayed mocked Chrome injection completed after native-port replacement and sent its result to the new port. The baseline regression failed with "old result crossed native connection". The fix binds incoming messages, asynchronous grant announcements and result delivery to their original port; ignores stale disconnect callbacks; and checks connection identity after permission verification, before dispatch. The physical-tab single-flight guard remains intact. A command already dispatched may still finish: no automatic replay, cancellation guarantee or new authorization is implied. No files, credentials, publication or payments were exercised.

## Verification

64 JavaScript fixture cases, 73 Python unit tests, and 27 isolated Chromium DOM cases (4 context, 10 edit and 13 select) passed. Two new worker tests cover delayed result, stale request, stale disconnect, and disconnect during permission verification. These are mocked native connections and isolated DOM tests, not an installed extension restart or real user account. Production, signed auto-update channel (0.7.27) and the attended 0.7.28 package were not changed. Installed extension/native-host restart, durable in-flight handling across service-worker replacement, and end-to-end recovery remain unverified. File collection remains planned, not released.

## External signal

[Playwright issue #43005](https://github.com/microsoft/playwright/issues/43005) describes asynchronous debugger attachment surviving connection teardown; related lifecycle risk, not proof of identical defects. [Playwright #41874](https://github.com/microsoft/playwright/issues/41874), 20 July 2026, describes extension reconnection failure, closed upstream. Developers and operators using long-running authorized tabs benefit from safe recovery. Existing alternatives include restarting a relay or using an official site API where available. Reliability is a baseline capability, not a separate paid feature; willingness to pay is not established. No expansion of browser permissions or bypass of site rules.
