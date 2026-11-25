# Unreleased P0 — tab queue lifecycle (25 November 2026)

Browser Core connects user-approved Chrome tabs to ChatGPT or Claude to perform website tasks. For example, share a supplier's tab using the extension, prepare a draft, and revoke access when finished. Idle command locks should not accumulate as tabs come and go. This change neither closes tabs nor grants permissions, submits forms or restarts Chrome.

**Staging only:** local branch `p0-tab-lock-lifecycle-0735`, commit `4227867`. Public attended preview remains 0.7.28; signed updates remain 0.7.27.

## Reproduction and correction
The baseline retained 1,000 idle asyncio locks after 1,000 simulated grant/command/revoke cycles. Remove the lock when the last queued or active command exits, only if the lock identity matches, without an intervening await. The corrected test retained zero locks. All four new tests passed (churn, same-tab serialization and independent tabs, regrant while busy, cancelled waiter). The regression command returned success: 73 Python unittest cases including the four new tests, 27 isolated Chromium cases, and seven JavaScript suites (60 cases previously enumerated). No real user profile was used. No measured RAM saving or claim to fix Chromium's own memory growth. Installed Mac endurance and packaging pending.

## Evidence and alternatives
- [agent-browser #2736, 24 November 2026](https://github.com/vercel-labs/agent-browser/issues/2736) — long-lived macOS session memory growth, issue listing.
- [Playwright MCP #1636, 27 May 2026](https://github.com/microsoft/playwright-mcp/issues/1636) — long-running memory pressure; closed as not planned.
- [agent-browser #1536, 12 July 2026](https://github.com/vercel-labs/agent-browser/issues/1536) — cleanup after interrupted integrations; different mechanism.
These are independent technical reports, not evidence of identical root causes or market size. Developers and long-running business operators benefit from reliability. Alternatives: explicit session cleanup, approved portal API where available, Playwright or agent-browser. P0, small correction, included in base access; no willingness-to-pay data. Respect existing user grants; never close the owner's tabs to reclaim locks.

## Next verification
[Playwright #41837, 17 July 2026](https://github.com/microsoft/playwright/issues/41837) (closed): manually dismissed dialogs could leave phantom modal state. [Playwright documentation](https://playwright.dev/docs/dialogs) explains modal blocking. Browser Core currently marks native timeouts uncertain; its queue can advance after a timeout while the extension may still be executing. This requires isolated late-result testing, not automatic confirmation or retries. Not yet fixed or reproduced end-to-end.
