# Browser Core — your browser, under your control

**ChatGPT and Claude** can automate individually authorized Chrome tabs, a personal Linux VPS or limited Hosted Cloud via [Browser Core MCP](https://m2g.pro/browser-core/mcp). Users may intervene for logins, CAPTCHA and 2FA.

**Current status: technical beta.** Paid checkout and browser-to-server credential provisioning are not yet enabled. Free beta access is not a promise of unlimited or permanently free Local/BYO usage.

## Latest verified releases

| Component | Version | Package |
|---|---|---|
| Hosted MCP server | 0.8.4-beta | [Endpoint](https://m2g.pro/browser-core/mcp) |
| Mac agent and OneClick installer | 0.7.18-beta | [Mac ZIP](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.18-beta.zip) |
| Chrome extension | 0.7.18 | [Extension ZIP](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.18.zip) |
| Linux BYO worker | 0.7.18-beta | [Linux TAR.GZ](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.18-beta.tar.gz) |
| Windows standalone | 0.8.4-beta | [Windows ZIP](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.4-beta.zip) |

[Current release manifest](RELEASE.json) · [SHA-256 checksums](RELEASE_SHA256.txt) · [Release verification](docs/current-release.md)

## Signed automatic updates (new)

**Mac and Linux:** one bootstrap installation of **0.7.18-beta** enables a user-level updater. It checks the fixed Browser Core HTTPS origin every two hours, verifies a pinned **Ed25519 signature**, checks exact ZIP/TAR SHA-256 and size, validates source paths/permissions and stages the next immutable version. It applies only when the worker reports no active sessions, no shared tabs and no in-flight jobs; otherwise the update is deferred. Mac shows auto-update on/off and a manual check in its menu bar. Linux uses a `systemd --user` timer.

The unpacked Chrome extension includes a local version-file watcher. After the updater installs a signed release, it reloads its own files. **Older extensions cannot install this watcher themselves**: the one-time bootstrap is required. A current working 0.7.14 extension remains compatible with an older 0.7.12 Mac agent; do not interrupt a task to align version numbers.

**Windows** still has manual updates. It is an unsigned separate-Chromium beta without native existing-Chrome-tab attachment, a bundled runtime, or Windows unattended updater. Do not promise background updates on Windows yet.

Signing public key (Ed25519, hex): `ad1f40ce4961e1c512793a6a101bea4f7a3a1201d6e3983de65bc11adadc0b70`. No private signing key is included in an installer. [Update protocol](docs/auto-updates.md).

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

Merchant credentials for YooKassa are configured, but live Browser Core purchases, receipts, paid-entitlement delivery and Stars settlement are **off** pending acceptance tests. The experimental secure credential-transfer service is **not yet shipped**. [Roadmap](docs/roadmap.md).

Website: [browser.m2g.pro](https://browser.m2g.pro) · [Support](https://browser.m2g.pro/support) · [Privacy](https://browser.m2g.pro/privacy) · [Terms](https://browser.m2g.pro/terms)

The public repository contains release metadata, docs and CI; the backend remains proprietary.
