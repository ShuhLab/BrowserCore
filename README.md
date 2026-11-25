# Browser Core — your browser, under your control

**ChatGPT and Claude** can automate individually authorized Chrome tabs, a personal Linux VPS or limited Hosted Cloud via [Browser Core MCP](https://m2g.pro/browser-core/mcp). Users may intervene for logins, CAPTCHA and 2FA.

**Current status: technical beta.** Paid checkout and browser-to-server credential provisioning are not yet enabled. Free beta access is not a promise of unlimited or permanently free Local/BYO usage.

## Latest attended preview: 0.7.28 — P0 reliability + P1 Portal Bridge

**Unreleased P0 confirmed pause (25 November 2026, staging only):** [Pause acknowledgement after grant refresh](docs/p0-pause-reannounce-staging.md) blocks subsequent queued fills in the simulated native bridge. Not in 0.7.28; installed Chrome/Mac unverified. Three historical updater tests still fail.


**Unreleased P0 native grant scope (25 November 2026, staging only):** [Queued-command binding](docs/p0-native-grant-scope-staging.md) prevents queued actions crossing a changed grant and treats late results as uncertain. Three pre-existing historical updater tests still fail; real Chrome acceptance pending. Not in 0.7.28.

**Unreleased P0 tab access withdrawal (25 November 2026, staging only):** [Immediate withdrawal guard](docs/p0-revoke-atomic-staging.md) prevents new commands during access cleanup and stale grant announcements; already dispatched actions may still finish. Not in 0.7.28; installed-extension verification pending.

**Unreleased P0 native connection isolation (25 November 2026, staging only):** [Connection-bound commands and results](docs/p0-native-port-isolation-staging.md) reject stale messages after reconnect. Mocked tests passed; installed-extension restart and uncertain-outcome reconciliation remain pending. Not in 0.7.28.

**Unreleased P0 browser command overlap guard (25 November 2026, staging only):** [Same-tab command isolation](docs/p0-native-single-flight-staging.md) rejects overlapping remote commands while a previous handler is active. Installed-extension timeout/restart verification pending; not in 0.7.28.

**Unreleased P0 tab queue lifecycle (25 November 2026, staging only):** [Idle lock cleanup](docs/p0-tab-lock-lifecycle-staging.md) eliminates retained queue locks in isolated churn tests. Not in 0.7.28; Mac endurance test pending.

**Unreleased P0 dropdown safety (25 November 2026, staging only):** [Safe dropdown selection](docs/p0-select-guard-staging.md) stops on ambiguous or disabled options and checks that the requested option remains selected. Not in public 0.7.28; installed-extension acceptance pending.

**Unreleased P0 — staging only:** [DOM edit guard](docs/p0-dom-edit-staging.md) refuses unsafe writes after editability/focus changes or native value rejection. Isolated Chromium tests passed; live acceptance pending, not included in 0.7.28.

**Unreleased P0 Portal Bridge replay safety (25 November 2026):** [Replay scope and verification](docs/p0-portal-replay-staging.md) — current grants and document context checked before cached apply; status is historical. Staging only, not in 0.7.28.

**Unreleased P0 receipt safety correction (25 November 2026):** [Receipt scope and verification](docs/p0-receipt-scope-staging.md) — current grant and lineage required for cached replay; failed records cannot claim verified success. Staging only, not in 0.7.28.

**Unreleased P1 safety correction — staging only (25 November 2026):** [Portal Bridge context binding](docs/p1-portal-context-staging.md) rejects stale previews after document/URL changes and handles revoked grants during preview. Synthetic tests passed; not included in 0.7.28. Live acceptance pending.

**Next P0 correction — staging only (25 November 2026):** [Delegated-tab pause/revoke isolation](docs/p0-delegated-tab-isolation-staging.md) preserves a manual child pause during a parent resume and rejects missing ancestor grants. Mocked tests passed; live Chrome acceptance and packaging are pending. This is not included in the 0.7.28 download.


**New attended preview 0.7.28 (25 November 2026):** [Mac](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.28-beta.zip) · [Chrome extension](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.28.zip) · [Linux](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.28-beta.tar.gz).

The P0 stage adds local, redacted operation receipts and reconnect diagnostics; the P1 Portal Bridge stage can preview and fill selected text fields between **two independently user-authorized tabs** with fingerprint validation and verified draft readback. No automated submit, file transfer, media upload, or payment. [Implementation, limitations, and exact tool usage](docs/p0-p1-portal-bridge-preview.md).

The latest **signed automatic-update feed is 0.7.27**. This newer 0.7.28 build is an unsigned/notarized-by-Apple **attended technical preview**, not yet installed on the owner's Mac or tested end-to-end on two live business portals. Existing browser tabs and production services are unaffected.

## Historical attended preview: 0.7.26

**0.7.26** introduces delegated same-origin child-tab access, available as a separately installed beta for [Mac](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.26-beta.zip), [Chrome](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.26.zip), and [Linux](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.26-beta.tar.gz). This release requires explicit, per-site browser permission. The owner Mac has not completed real acceptance. **At the time of that preview, the legacy v2 feed offered 0.7.23.**

## Current signed beta releases

| Component | Version | Package |
|---|---|---|
| Hosted MCP server | 0.8.4-beta | [Endpoint](https://m2g.pro/browser-core/mcp) |
| Mac agent and OneClick installer | 0.7.23-beta | [Mac ZIP](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.23-beta.zip) |
| Chrome extension | 0.7.23 | [Extension ZIP](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.23.zip) |
| Linux BYO worker | 0.7.23-beta | [Linux TAR.GZ](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.23-beta.tar.gz) |
| Windows standalone | 0.8.5-beta | [Windows ZIP](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.5-beta.zip) |

[Current release manifest](RELEASE.json) · [SHA-256 checksums](RELEASE_SHA256.txt) · [Release verification](docs/current-release.md)

## Signed automatic updates (new)

**Mac and Linux:** a compatible installation enables a user-level updater. The signed v2 feed currently offers 0.7.23; v3 offers 0.7.27. Both signatures were verified on 25 November 2026. The attended 0.7.28 preview and unreleased P0 isolation correction are not distributed through those feeds. It checks the fixed Browser Core HTTPS origin every two hours, verifies a pinned **Ed25519 signature**, checks exact ZIP/TAR SHA-256 and size, validates source paths/permissions and stages the next immutable version. It applies only when the worker reports no active sessions, no shared tabs and no in-flight jobs; otherwise the update is deferred. Mac shows auto-update on/off and a manual check in its menu bar. Linux uses a `systemd --user` timer.

The unpacked Chrome extension includes a local version-file watcher. After the updater installs a signed release, it reloads its own files. **Older extensions cannot install this watcher themselves**: the one-time bootstrap is required. An older installed extension may remain loaded from Downloads instead of the managed folder. Do not interrupt a live task just to align version numbers.

**Windows** still has manual updates. It is an unsigned separate-Chromium beta without native existing-Chrome-tab attachment, a bundled runtime, or Windows unattended updater. Do not promise background updates on Windows yet.

Signing public key (Ed25519, hex): `ad1f40ce4961e1c512793a6a101bea4f7a3a1201d6e3983de65bc11adadc0b70`. No private signing key is included in an installer. [Update protocol](docs/auto-updates.md).

> **Grant recovery (0.7.23):** The extension now persists explicitly granted tab state across extension worker restarts; manual Pause and Revoke remain authoritative. Restoration across a full browser restart when tab IDs change is not yet automatic, and will require separately approved site permissions. The managed Chrome extension must be loaded from the Mac installation folder.

## Existing Chrome tab experience

Only tabs explicitly connected in Browser Core are visible to the agent. The extension panel lists only those connected tabs, including paused ones; it hides empty usage cards, unrelated tabs and window IDs. No broad `tabs` permission is requested. A duplicate-site indicator does not close tabs or limit how many a user may open.

The browser checks that DOM actions actually change a field or page state before reporting success. A successfully entered draft is **not** proof of sending. Ordinary sends within an authorized task do not require repeated per-message confirmation; explicit draft-only/no-send instructions remain binding. Operation IDs prevent accidental duplicate submission after uncertain results.

Per-tab counters show measured calls and text volume; bytes/4 is an approximation, **not** actual ChatGPT/Claude token usage or a charge.

## Installation

1. Add `https://m2g.pro/browser-core/mcp` as an OAuth MCP connector to ChatGPT or Claude.
2. Sign in through [@OpsTetherBot](https://t.me/OpsTetherBot?start=browsercore). Account OAuth codes and one-time worker pairing codes are separate.
3. Install the Mac/Linux worker or select limited Cloud. For existing Chrome tabs, use **Load unpacked** on the Chrome extension folder containing `manifest.json`; then grant the tab.
4. Reuse suitable live sessions and the same verified account across both AI clients. Avoid duplicate workers and hidden switches to Cloud.

[Detailed setup](docs/getting-started.md) · [Claude](docs/claude.md) · [Windows](docs/windows-beta.md)

## Security and limits

Browser Core is not independently security-audited or certified to SOC 2/ISO. Passwords, tokens, cookies and chat content must not be logged or pasted into AI messages. The new beta updater signs packages and refuses unexpected permissions, paths and files; it does not make downloaded binaries notarized or guarantee a malicious operating system cannot read secrets.

Hosted Cloud is a separate ephemeral two-slot beta, with 30 minutes per session and 120 minutes per account daily; no commercial autoscaling. Desktop workers require the user's hardware. The Mac build is unsigned/unnotarized and needs Python 3.10–3.13. No universal browser-website guarantee or commercial SLA is claimed.

Merchant credentials for YooKassa are configured, but live Browser Core purchases, receipts, paid-entitlement delivery and Stars settlement are **off** pending acceptance tests. The private credential receiver and consented Chrome beta channel are deployed, but real-owner Mac acceptance and installing a provider key remain outstanding. Only registered destinations are supported; the current pilot target is a dedicated Community Pilot Telegram bot. [Roadmap](docs/roadmap.md).

Website: [browser.m2g.pro](https://browser.m2g.pro) · [Support](https://browser.m2g.pro/support) · [Privacy](https://browser.m2g.pro/privacy) · [Terms](https://browser.m2g.pro/terms)

The public repository contains release metadata, docs and CI; the backend remains proprietary.

## Protected credential handoff (new beta)

Browser Core 0.7.19 introduced a popup-only **Connect API credential** flow for a registered server destination. The user must choose a destination and select the secret directly in an authorized browser tab; it is encrypted before transport and is not returned to the model. The private server receiver verifies the destination identity and stores the credential under private file permissions. For now only the Community Pilot Telegram destination is registered. The feature has passed synthetic Chromium and native IPC tests, but **real Mac approval and provider setup remain to be verified**. Do not paste keys in ChatGPT/Claude; do not confuse a saved credential with activation of billing or the target service.

Commands to the *same* authorized tab now execute sequentially; commands to different tabs may run concurrently. A bounded per-tab queue protects resources, not a website-wide tab limit. Pause and revoke block queued work; operation IDs remain idempotent.

## Mac 0.7.22 audio beta acceptance

The owner confirmed agent and Chrome extension **0.7.22** on the same Mac, including an explicitly granted Instagram tab, connected tab audio, and a 20-second audio fragment at the ready state. Server-side speech transcription through this MCP client is **not yet verified**. The user's video must be unmuted in the webpage; the Mac output volume can be zero. No microphone or passive recording is used. 

Automatic updating remains separate from the latest attended preview: **v2 advertises 0.7.23 and v3 advertises 0.7.27**. See [current release](docs/current-release.md).

## Pricing and free beta roadmap — 19 November 2026

**Not yet an active billing offer.** The planned free tier is **100 one-time starter browser automation steps per verified account**, with free rate-limited page search and reading. User-approved tab audio is planned free for **one tab at a time**, up to **20 minutes of actual recorded audio per UTC day**; idle time does not count. Failed operations do not consume steps.

Based on TinyFish's published 19 November 2026 rates ([pricing](https://www.tinyfish.ai/pricing)), Browser Core targets **$0.008 per comparable automation step** versus TinyAgent $0.016, and **$0.001 per hosted-browser minute** versus TinyBrowser $0.002, *subject to verified unit economics*. These are targets, not currently purchasable prices or guarantees of feature parity: TinyAgent bundles model inference, residential proxies and anti-bot infrastructure, while our Local/BYO package does not.

The prior 149/399 RUB Local/BYO package amounts remain a separate unactivated preview and should not be interpreted as equivalent to per-step USD rates. Checkout is currently disabled; active free quotas are not yet enforced through the public MCP endpoint. The staged starter/audio ledger passed bounded quota checks, but full end-to-end payment and audio enforcement are incomplete.

[Pricing](https://browser.m2g.pro/pricing) · [Offer](https://browser.m2g.pro/offer)

## 0.7.24 attended recovery preview (20 November 2026)

An **attended 0.7.24 preview**, with optional persistent per-site Chrome permissions, is available: [Mac](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.24-beta.zip), [Chrome extension](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.24.zip), [Linux BYO](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.24-beta.tar.gz). SHA-256 checksum files accompany each package.

The new implementation accepts only an authenticated server release hint, checks a fixed-origin Ed25519-signed update manifest and applies the package after actions drain. Existing Chrome tab grants are restored from trusted local extension storage only when **each origin was individually opted in** (Instagram, TikTok, YouTube, or YouTube Studio). Revoked permissions, ambiguous tab matches, active managed browser sessions, manual takeover, queued writes and audio capture prevent an automatic restart. A changed Chrome optional-permission allowlist means **0.7.24 requires an attended bootstrap** from older clients.

**Not live as a signed push update:** the new v3 signed feed is pending authorized release signing, and the owner's Mac was last verified at agent/extension 0.7.22. The existing signed v2 channel remains at 0.7.23. The preview passed source, packaging, isolated update/rollback and grant-recovery tests; real Mac unattended update/recovery acceptance is still pending. This documentation does **not** assert that the server-signalled rollout is enabled.

## 0.7.25 historical attended preview — superseded by 0.7.26

An **attended beta preview** introduces same-origin inherited access for tabs created by Browser Core itself, with per-site owner consent:

- [Mac 0.7.25](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.25-beta.zip)
- [Chrome extension 0.7.25](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.25.zip)
- [Linux BYO 0.7.25](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.25-beta.tar.gz)

An owner first shares a parent tab and explicitly enables **child-tab access and recovery** for that particular HTTPS origin in the extension popup. Chrome requests an optional host permission for that one site; the extension never requests all-site access in a single approval. The agent can then call the existing `existing_tab_action` MCP tool with `action="open_tab"`, `tab_handle` set to the parent, `value` set to a same-origin URL and a unique `operation_id`. The result includes `child_tab_handle`, usable with the same existing-tab tools. Same-origin popups caused by an agent's explicitly requested click can also inherit access when Chrome supplies the parent tab ID. The parent/child relationship is preserved for reconnection.

Unrelated browser popups, manually opened tabs, cross-origin links, and unexpected redirects never inherit authorization. A parent pause propagates to children, and parent revocation/disabled delegation removes all child grants without closing browser tabs. User-granted audio capture remains **per tab** and is never automatically enabled on a child.

**Availability:** source, archive integrity, recovery and synthetic/native bridge checks passed. Real owner-Mac acceptance is pending. The **signed unattended update feed remains at 0.7.23**; 0.7.25 is an attended installer and not yet a server-pushed signed update. Existing 0.7.22 clients do not gain this capability by reading the docs alone.

## 0.7.26 attended preview — delegated child-tab access (20 November 2026)

This preview supersedes the 0.7.25 attended preview. Downloads (each has a .sha256 companion):
[Mac 0.7.26](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.26-beta.zip) ·
[Chrome extension 0.7.26](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.26.zip) ·
[Linux BYO 0.7.26](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.26-beta.tar.gz).

**Agent-created child tabs.** After the owner explicitly shares a parent Chrome tab and enables **child-tab access / auto-recovery** in the extension popup, Chrome asks for host permission for **that exact HTTPS origin only**. The extension requests no blanket host access during installation and no other origin inherits the grant.

For Mac existing-tab automation, use the unchanged `existing_tab_action` MCP tool with `action="open_tab"`, `tab_handle` referring to the parent, `value` set to the target URL on the same origin, and a unique `operation_id`. The response contains a `child_tab_handle`; subsequent snapshots, clicks and form actions use that child handle without another popup grant. Agent-clicked links that open a new tab may also be associated with the parent when Chrome supplies `openerTabId` within the short click window. Links opened with `noopener` or without that relationship are not auto-attached; the agent can use explicit `open_tab` instead.

The original navigation URL, including query parameters, is used for loading the child. Persistent permissions and the model-visible child handle store only the URL origin/path, not the query or fragment. A child is never attached across origins, and arbitrary browser popups cannot inherit permission. Parent pause propagates to children; parent revocation or disabling site delegation revokes all child handles without closing their browser tabs. Audio capture permission and recording require separate consent per tab.

**Status:** isolated tests for same-origin/cross-origin navigation, browser popups, per-site permissions, password/session restrictions, native writer isolation, exactly-once operations, restoration, and signed-updater rollback passed. Both public download mirrors and SHA-256 checksums verified. Real owner-Mac acceptance is still outstanding. The current signed unattended feed remains at **0.7.23**; 0.7.26 is an attended preview and server-triggered signed installation is **not yet active**. Older installed agents/extensions will not gain this capability without upgrading.
