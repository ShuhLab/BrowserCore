# P0 delegated-tab isolation — staging candidate (25 November 2026)

**28 November 2026 — safety guidance:** Browser Core connects Chrome tabs you authorize to ChatGPT or Claude for website actions. In existing attended previews, leave automatic child-tab access/recovery disabled and authorize each intended tab separately until a verified update is available. Private RC2 testing requires separate authorization for browser-created tabs; the opt-in explicit same-site creation path remains under test. This is not a public release or a change to the signed update channel. [Details and limits](mac-0729-rc2-preflight-staging.md#28-november-2026--private-rc2-independent-tab-authorization).

**Not released.** The current attended preview is 0.7.28; the signed v3 feed is 0.7.27-beta. The staging-only follow-up is based on 0.7.28 and does not change the MCP tool schema, permissions, or file transfer.

## Why

[agent-browser #2407 (4 November 2026)](https://github.com/vercel-labs/agent-browser/issues/2407) describes unrelated tab state being affected by background tab closure. [agent-browser issues](https://github.com/vercel-labs/agent-browser/issues) lists #2620 (15 November 2026), a report of a pinned tab falling back to another tab after closure. These are independent demand signals, not proof of the same bug in Browser Core. Current agent-browser source already implements an explicit tab_gone guard.

Browser Core code review found a separate problem: resuming a root tab could clear a grandchild's inherited pause even if the intervening child had been paused manually. Native state also guessed descendant resume rather than waiting for the extension. Recovery could replace an explicit child pause with an inherited one.

## Candidate fix

- Preserve manual child pauses across parent resume and restart.
- Check the entire ancestor chain before delegated operations; missing or incompatible grants block the operation.
- Revoking a root invalidates its delegated descendants in the native bridge without changing independent grants.
- Wait for authoritative extension grant announcements before resuming; do not silently switch targets.
- No new access, permissions or automatic file transfers. Already-dispatched operations cannot be undone.

## Example and troubleshooting

For a tree A → B → C, pause A, manually pause B, resume A. B and C must remain paused. Explicitly resume B to resume its inherited descendants, provided all grants are still valid. If the ancestor is absent or revoked, reconnect or explicitly grant the intended tab; never operate on another tab as a substitute.

## Verification and limitations

48 Python tests and 55 JavaScript mocked tests passed (103 cases); five further signed-update tests exercised the unchanged 0.7.28 package. This is not live Chrome acceptance. Real three-level Chrome validation and a reviewed package/signature remain outstanding. Existing production, the signed update channel, and installed clients were not switched.

Potential customer: teams running multi-tab work in authorized browser profiles. Value hypothesis: fewer failed or wrongly resumed tasks; include this safety correction in the base product, not a paid add-on. No evidence of willingness to pay a separate price.