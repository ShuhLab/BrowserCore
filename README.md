# Browser Core — a browser for AI agents, under your control

**Automate your own Chrome or Linux VPS through ChatGPT/MCP. Or choose limited Hosted Cloud without installing a worker. Step in for passwords, CAPTCHA and 2FA, then let the agent continue.**

**Status: free public beta, version 0.8.0.** No payment or manual invitation required. Hosted Cloud has **two** concurrent slots and ephemeral **30-minute** sessions (maximum 120 minutes per account daily).

- Website: https://browser.m2g.pro/
- OAuth-enabled MCP remote endpoint: https://m2g.pro/browser-core/mcp
- Official MCP Registry: io.github.ShuhLab/browser-core
- Mac beta 0.7.8: https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.8-beta.zip
- Linux/VPS beta 0.7.8: https://browser.m2g.pro/docs#linux
- Free verification and support: https://t.me/OpsTetherBot?start=browsercore

## Choose where your browser runs

| Feature | Local Chrome | Your Linux VPS (BYO) | Hosted Cloud (limited beta) |
|---|---|---|---|
| Browser location | Your computer | Your server | Our isolated server worker (fallback) |
| Installation needed | Mac agent + extension | Linux worker | **No** |
| MCP navigation, forms, extraction, screenshots | Yes | Yes | Yes |
| Existing Chrome tab with individual permission | Yes | No | No |
| Profile storage | Persistent locally | Persistent on your VPS | **Ephemeral, erased on release** |
| Manual login / CAPTCHA / 2FA | Native browser | Short handoff link | Short handoff link |
| Concurrent capacity | Your device | Your VPS | Two global slots; one per account |
| Price in free beta | Own hardware | Own VPS | Free: 30 min / session, 120 min / day |

**Use Local Chrome when the work depends on your existing browser login.** Your own VPS is an independent remote option; Hosted Cloud is an installation-free **third execution mode**, with only two simultaneous free beta slots and ephemeral login state. Remote live view is for brief human login or correction, not comfortable full-time browsing.

## Start in ChatGPT

1. Open the Telegram bot https://t.me/OpsTetherBot?start=browsercore and send /browser. It automatically issues a one-use OAuth code to your verified chat.
2. Add https://m2g.pro/browser-core/mcp as an OAuth-enabled MCP app in ChatGPT.
3. Enter the single-use code on Browser Core's actual OAuth consent page (15-minute validity).
4. Choose Cloud, Local or BYO in execution_options. Cloud needs no local installation; Local/BYO need separate worker pairing.
5. Ask the agent to browse. If a login needs you, intervene directly in the browser, never paste passwords into ChatGPT.
6. When finished in Cloud, close the browser and use cloud_release to free the slot and erase temporary profile data.

**Cloud is limited:** Only two slots exist. If busy, retry later or choose Local/BYO. Cloud cookies and login state are erased after the session; this is not permanent browser storage. There are no paid plans or automatic charges.

The Mac beta is unsigned and not notarized; it requires Python 3.10–3.13. Linux has a user-scoped installer with SHA-256 integrity verification. No broad Windows, Apple Silicon or commercial SLA certification is claimed.

## Actual competitive advantage

Browser Core combines **individually authorized existing Chrome tabs**, **your own personal Linux worker**, and **limited Hosted Cloud** in one MCP workflow. You decide where browser execution happens.

Human takeover is **not unique** to Browser Core: Browserbase and others already offer it. TinyFish and Browserbase have more mature hosted browser infrastructure, proxy offerings and scale. Browser Core's free two-slot Cloud beta does not replace their full commercial managed platforms. **We have not run comparable Browser Core-versus-TinyFish speed or task-completion benchmarks, so we do not claim our remote mode is faster or more reliable.**

Compare alternatives: docs/alternatives.md

## Privacy, security and current limitations

- OAuth account subjects are bound to verified Telegram IDs; no public browser session is shared with another account.
- Browser workers run under distinct restricted Linux users with CPU/RAM/process limits and independent encrypted storage.
- Private network ranges are denied; browser egress blocks unsafe destinations. A local-only bridge connects workers to MCP.
- The free Cloud broker enforces one slot per account, a 30-minute lease and 120 minutes daily; data is erased on release.
- Local Chrome extension permissions are granted tab by tab, not over the whole Chrome profile.
- There is **no** independently audited multi-tenant environment, SOC 2 / ISO claim, paid checkout or guaranteed 24/7 availability.
- This repository contains **public documentation and release metadata only**; the backend remains proprietary.

## Links

- [Getting started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Comparison](docs/alternatives.md)
- [Roadmap](docs/roadmap.md)
- [Release notes](CHANGELOG.md)
- [Security](SECURITY.md)
- [Privacy](https://browser.m2g.pro/privacy)
- [Terms](https://browser.m2g.pro/terms)

**Payments remain disabled.** YooKassa product approval is pending and Digiseller seller setup is incomplete. Never purchase Browser Core beta codes from third parties.

- Cloud scalability: [capacity and queue design](docs/cloud-scaling.md)
