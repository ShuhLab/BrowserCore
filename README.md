# Browser Core — browser automation with human control

**Connect AI agents to a browser you own. Choose your local Chrome or a personal Linux server.**

Browser Core is an MCP-connected browser automation service by Shuh Lab. It opens pages, reads accessible controls, clicks, fills forms, extracts information, takes screenshots and saves encrypted browser profiles. When a login requires a password, CAPTCHA, 2FA or OAuth approval, the agent pauses for a user to briefly take control of that same session, then resumes.

**Status: free public Local/BYO beta. Automated Telegram verification; Hosted Cloud is not public yet.**

- Product website: https://browser.m2g.pro/
- GitHub documentation: https://github.com/ShuhLab/BrowserCore
- MCP endpoint: https://m2g.pro/browser-core/mcp (OAuth; invitation required)
- Official MCP Registry: io.github.ShuhLab/browser-core — version 0.7.8
- Mac 0.7.8 beta: https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.8-beta.zip
- Linux / VPS 0.7.8 beta: https://browser.m2g.pro/docs#linux (self-service installer and worker package)
- Linux worker package: https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.8-beta.tar.gz
- Linux installer: https://browser.m2g.pro/downloads/install-linux.sh

- Support: https://t.me/OpsTetherBot?start=browsercore

## Current capabilities

| Feature | Local Mac | Personal Linux BYO | Hosted commercial cloud |
|---|---|---|---|
| MCP browser automation | Tested | Tested | Not available |
| Encrypted, reusable browser profile | Yes | Yes | Not available |
| Manual login / CAPTCHA / 2FA | Native Chrome or controlled window | Short, temporary remote live view | Not available |
| Connect to existing, individually approved Chrome tabs | Yes | No | Not available |
| Infrastructure provided by the user | Local computer | Your own server | Not available |

**Manual remote viewing is ONLY for short authentication or verification steps.** It is not intended for normal browsing; use your own computer when you need comfortable interactive work.

## Getting started

1. Open https://t.me/OpsTetherBot?start=browsercore or send /browser to the bot. It issues a one-time OAuth code automatically; no manual operator invitation.
2. Add the OAuth-enabled MCP endpoint https://m2g.pro/browser-core/mcp in ChatGPT.
3. Enter your Telegram-issued code on the official Browser Core OAuth page. This code expires after 15 minutes and is single-use.
4. Choose Local or BYO, pair the worker using a separate pairing code, and explicitly grant the Chrome tab to operate.
5. Enter sensitive login details only in the real browser, never in chat.

The current Mac installer is **unsigned, not notarized, and requires Python 3.10–3.13**. On Linux, the separately documented self-service script runs under an ordinary account and validates the downloaded versioned worker package checksum. Chrome extension installation may require Developer Mode. Windows, Apple Silicon and large-scale commercial hosted Cloud are not yet release-certified.

## Why consider Browser Core?

- Work in your existing, explicitly approved Chrome tab instead of copying a profile into an agent cloud.
- Choose a local computer or your own Linux host; no mandatory commercial browser-minute subscription for these two modes during the beta.
- Human and agent can cooperate in the same remote context during an authentication challenge.
- Persistent sessions and encrypted browser profiles, with explicit permission boundaries.

These are our current product design choices, **not claims of industry-first features**. Manual takeover exists in Browserbase and other platforms. TinyFish offers a mature managed Chromium, CDP and proxy service that this beta does NOT replace at scale.

See detailed, sourced product positioning in docs/alternatives.md.

## Documentation

- docs/getting-started.md
- docs/architecture.md
- docs/alternatives.md
- docs/roadmap.md
- SECURITY.md
- CHANGELOG.md
- https://browser.m2g.pro/privacy
- https://browser.m2g.pro/terms

## Distribution, access, and payment

Free public beta access needs no manual invitation. Merchant checkout and shared Hosted Cloud are disabled pending security and provider approval. This repo contains **documentation and release metadata only**; the service backend is proprietary, not open source.
