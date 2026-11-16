# Browser Core 0.7.12 — P0 DOM actions candidate

Status: **fix published; live macOS Telegram acceptance is still pending**. This is an unsigned beta, not a completed P0 sign-off. No real Telegram message was sent during diagnostics.

## Components

- Mac agent / installer: `0.7.12-beta`
- Shared Chromium extension: `0.7.12`, DOM protocol `2`
- Browser Core server: `0.8.2-beta`; existing-tab action schema adds optional `confirm_submission: boolean = false`
- Native messaging framing and extension ID are unchanged. No debugger, cookies or broad host permissions were added to the distributed extension.

Mac download: https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.12-beta.zip

Mac SHA-256: `d36549051f2efce079ddc4a0cc377ef1d3b7c49c0f2e67133e8de9c0474774dd`

Extension-only download: https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.12.zip

Extension SHA-256: `5d2df190279ec6706ae0102aa9598d295b7ba7c7973da8e6130a52a789ff4dd6`

Both public downloads were fetched and their hashes matched. Older packages were not replaced. The general website download was not switched to this candidate before live Mac acceptance.

## Root cause reproduced

The older action implementation used the native HTMLInputElement value setter for a contenteditable DIV. An actual MV3 chrome.scripting.executeScript test reproduced the resulting missing/null injection result, which the old wrapper reported as NO_DOM_RESULT. The old implementation also returned completed after dispatching input/click/key events without reading back the effect.

The Mac's snapshot response matched the older limited DOM shape (60 controls, no semantic-role metadata), even though its agent had previously been updated. The exact installed extension version was not reported by that old version; do not infer it from the agent version. A stale separately loaded extension directory is an additional deployment concern, not an excuse to bypass permission checks.

## Generic implementation, not a Telegram workaround

- Prioritize editable controls before long SPA lists; discover contenteditable, plaintext-only, nested editing hosts and open shadow-root editors.
- Use document-scoped stable node references; stale references fail closed after node replacement or navigation.
- Resolve visible targets and reject ambiguous visible matches rather than selecting the first CSS match.
- Use browser editing commands with a bounded DOM-range fallback for rich editors, and the proper native setter for input/textarea controls. Honor canceled beforeinput and dispatch structured InputEvent events.
- Read the resulting value repeatedly after event processing; asynchronously reverted or replaced editors do not produce a successful result.
- Differentiate focus verification, value readback and observed DOM effects. A no-op click or uncertain submission is not reported as completed.
- Capture sanitized exception class and stage inside the injected function. No raw exception message or stack is returned. Empty injection frames, rejected injection, stale documents, permission loss, disabled targets and value rejection have separate reasons.
- Enter/submit/send-like actions require explicit `confirm_submission=true`. Clients must obtain separate user approval first. Heuristic recognition of every possible custom submission control is not guaranteed; client-side user-consent rules still apply.
- A submission is marked as a visible-message result only when new visible matching text and a cleared editor are both observed. This is not proof of network delivery or recipient acknowledgement.
- Preserve operation-ID deduplication and keep uncertain outcomes pending. Bind responses to the expected tab handle and transport. Do not persist draft text in the action-intent ledger.
- Preserve the existing Google Cloud project verification guard and sensitive-field restrictions.

## Tests completed

18 checks passed using a real Chromium extension service worker and actual chrome.scripting.executeScript in the isolated world, against synthetic local fixtures:

1. Legacy DIV setter produces the missing result.
2. Contenteditable fill and stable readback without sending.
3. Contenteditable append and InputEvent.
4. Hidden duplicates excluded; search UI state updated.
5. Controlled input native setter.
6. Asynchronous value reversal rejected.
7. Sensitive and readonly fields rejected without returning their values.
8. No-op click uncertain; actual toggle verified.
9. Enter and send controls blocked without explicit confirmation.
10. Confirmed submission verified exactly once in the **synthetic fixture only**.
11. Nested child resolves to its editing host.
12. Open-shadow editor and stable reference.
13. Rerendered node produces uncertainty.
14. Editor priority and stale-reference rejection.
15. Invalid-selector diagnostics.
16. Existing protected-project guard in the real isolated world.
17. Canceled beforeinput does not mutate the editor.
18. Injection exception returns stage/type without private exception text.

Native transport/agent regressions also passed: origin/grant boundaries, Unix socket isolation, actual native-host subprocess framing, reconnect/regrant, large responses up to 850,000 synthetic characters, action deduplication, explicit human takeover, file-picker restrictions, wrong-tab response rejection and no draft content in the action ledger. Fixture-only localhost host permissions were added to a throwaway test manifest, never to the released manifest.

These Linux Chromium tests do **not** constitute a live Mac Telegram test. The existing Mac was contacted for attachment, a redacted control snapshot, focus and a Search fill request; the legacy completed response was not treated as verified text entry. Chat history and real credentials were not printed or saved in the diagnostic reports.

## Required Mac update

1. Install the new Mac package over the existing agent; allow the requested agent restart only when current work is safe to interrupt.
2. In chrome://extensions, load the installed folder `~/Library/Application Support/BrowserCore/Extension`. Do not keep an older unpacked extension from Downloads.
3. Confirm that the extension popup reports `0.7.12`. The agent and extension versions are independent.
4. Grant the Telegram tab again if Chrome cleared its activeTab permission on reload. Do not close the tab, delete the profile or re-pair the device.

## Pending acceptance

On the real Mac Intel, find the BotFather conversation, confirm its identity, inspect an empty editor, fill `/newbot`, verify the exact draft and present the result without sending. Only after separate user approval may the send action run once, followed by a fresh check that the message appeared. No P0 completion claim is made before this test.

Websites requiring trusted native hardware input or unsupported closed-shadow/cross-origin frame access may still reject an action; such a rejection must be diagnosed, not hidden or bypassed. No promise of leak-proof or universally successful browser automation is made.