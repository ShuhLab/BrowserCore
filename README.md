# Browser Core — your browser, under your control

Use your permitted Chrome tabs, a personal Linux VPS, or limited Hosted Cloud through **ChatGPT and Claude**. Step in for passwords, CAPTCHA and 2FA, then return control to the agent.

**Status: technical beta.** Current access has no charges; this is not a promise of permanently free or unlimited Local/BYO service. Checkout and browser-to-server credential transfer remain disabled.

## Current releases

| Component | Version | Download / status |
|---|---|---|
| Hosted MCP server | 0.8.4-beta | https://m2g.pro/browser-core/mcp |
| Mac installer and agent | 0.7.14-beta | https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.14-beta.zip |
| Chrome extension | 0.7.14 | https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.14.zip |
| Linux/BYO worker | 0.7.14-beta | https://browser.m2g.pro/docs#linux |
| Windows standalone package | 0.8.1-beta | https://browser.m2g.pro/docs#windows |

The Mac package contains **the same extension bytes** as the extension-only ZIP. Existing Mac agents 0.7.12-beta remain compatible with extension 0.7.14; a working installation does not need to be replaced just to match version numbers.

[Machine-readable release manifest](RELEASE.json) · [SHA-256 checksums](RELEASE_SHA256.txt) · [Current release notes and verification scope](docs/current-release.md)

## What changed

- The extension panel lists **only connected tabs**, including paused tabs. Unconnected, unnamed tabs, internal window numbers and empty usage cards are hidden. No broad `tabs` permission is requested.
- Per-tab counters measure Browser Core calls and text volume. The approximate text-token equivalent is **not** ChatGPT/Claude token billing or monetary cost.
- DOM actions support contenteditable editors and verify their effects. Missing results, stale elements and rejected values have diagnostic reason codes rather than a false success.
- Ordinary sends within an authorized task do not require a physical click or a fresh conversational confirmation for each message. Explicit draft-only instructions remain binding. Operation IDs prevent accidental duplicate execution, not multiple authorized messages.
- ChatGPT and Claude use the same verified Browser Core account and its devices. The owner confirmed Claude connection and device access. This is not an Anthropic directory listing or certification.

## Get started

1. Connect `https://m2g.pro/browser-core/mcp` through OAuth in your MCP client. Account sign-in is provided through https://t.me/OpsTetherBot?start=browsercore (`/browser`); enter any code only on the official authorization screen.
2. Reuse an existing paired worker where available. A new computer requires a **separate worker pairing code**, not the account sign-in code.
3. On Mac, install the ZIP and load `~/Library/Application Support/BrowserCore/Extension` through Chrome's **Load unpacked**. Select the directory containing `manifest.json`, not the Mac installer directory.
4. Permit the intended existing tab through the extension. Reading the local list does not give an AI access to other tabs.
5. Before a task, check execution status and use the selected Local/BYO/Cloud mode. Reuse suitable live sessions rather than repeatedly opening the same site.

[Detailed setup](docs/getting-started.md) · [Claude](docs/claude.md) · [Windows limitations](docs/windows-beta.md)

## Execution modes

| Capability | Mac + permitted Chrome | Linux BYO | Hosted Cloud beta |
|---|---|---|---|
| Browser location | Your computer | Your server | Isolated hosted worker |
| Existing logged-in Chrome tabs | Individually permitted | Not configured by the BYO package | No |
| Profile storage | Locally persistent | Persistent on your VPS | Ephemeral |
| Manual login / CAPTCHA / 2FA | Your existing browser | Brief handoff | Brief handoff |
| Capacity | Device and configured worker limits | Your VPS and worker limits | Two shared slots; one per account |

Hosted Cloud currently allows 30 minutes per session and 120 minutes per account daily. Its FIFO queue has at most 200 waiting entries, a ten-minute inactive-entry expiry and a two-minute ready-to-claim window. It does not auto-start a browser, guarantee a wait time or purchase infrastructure. Close the browser and release the Cloud worker when done. Never silently switch a Local task to Cloud.

## Verification and limits

Published archives were downloaded over HTTPS and checked against SHA-256. Extracted Mac, Linux and Windows worker code passed import and Chromium smoke tests **on Linux**. Extension panel regressions ran in a real Chromium MV3 environment. Current Windows CI is a separate check; do not substitute the older 0.8.0 result for the new package's result.

The owner previously verified real Telegram draft input on Mac with the 0.7.12 DOM engine, retained in 0.7.14. This release synchronization does not claim a newly completed Telegram send, a new Mac installer acceptance test or universal website compatibility.

Desktop packages are unsigned; Mac is not notarized. Python 3.10–3.13 is required. Windows runs a separate Chromium and **does not attach to existing Chrome/Edge tabs**. Hosted Cloud is not persistent, unlimited, independently audited or covered by a commercial SLA. Browser Core is not claimed faster or more reliable than competitors without comparable benchmarks.

## Privacy and commercial status

Only the authenticated account's workers and permitted tabs are routed to it. Do not publish cookies, passwords, bot tokens or private messages in diagnostics. No independent no-leak guarantee, SOC 2 or ISO certification is claimed.

YooKassa merchant approval and key verification are complete, but checkout, receipts and delivery acceptance are not complete; **sales remain off**. Telegram Stars sales for Browser Core and secure credential handoff are also not enabled. Do not buy beta access codes from third parties.

Website: https://browser.m2g.pro/ · Support: https://browser.m2g.pro/support · Privacy: https://browser.m2g.pro/privacy · Terms: https://browser.m2g.pro/terms

Official MCP Registry identity: `io.github.ShuhLab/browser-core`. This repository contains public documentation, metadata and QA workflows; the backend remains proprietary.
