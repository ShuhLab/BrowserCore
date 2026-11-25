# Unreleased P0 dropdown safety — 25 November 2026

Browser Core connects user-approved Chrome tabs to ChatGPT or Claude to perform website actions. For example, when preparing an order, share its tab through the extension and ask the assistant to select a supplier by exact option value. If that value matches several options, or the option is disabled or hidden, the assistant must stop rather than guess. Multi-select controls require manual resolution. Choosing an option is not submitting the order; website scripts may autosave.

## Verification
Local staging branch `p0-select-guard-0734`, commit `4c1766a`, based on `93089e8`. The baseline failed 11 of 13 synthetic Chromium checks; the corrected code passed all 13. It rejects duplicate option values and disabled optgroups, refuses ambiguous controls, avoids redundant input/change events when already selected, and checks the actual option identity after events. Changes, replacement or delayed reversion are reported as uncertain, not success. Also passed: 69 Python cases, 60 JavaScript cases and 10 previous isolated Chromium edit cases.

## Limits
No new permissions, no real user profile or submission tested. Bounded 450 ms observation cannot establish server acceptance or prevent website-side autosave. Native installed-extension acceptance and release packaging remain pending. Public attended preview remains 0.7.28 and signed update feed remains 0.7.27. No new public feature or separate charge.

## Demand
[agent-browser #1928](https://github.com/vercel-labs/agent-browser/issues/1928), 18 September 2026: ambiguous dropdown options. [Playwright #4921](https://github.com/microsoft/playwright/issues/4921), 6 January 2021: historical dynamic-select failure. Alternatives include Playwright locator.selectOption and official portal APIs where available. The competitor's current release notes also describe ambiguity guards; this is essential safety parity, not evidence of unique demand or willingness to pay.
