# Current release — 19 November 2026

| Component | Version | Package |
|---|---|---|
| Hosted MCP server | 0.8.4-beta | [Endpoint](https://m2g.pro/browser-core/mcp) |
| Mac installer and agent | 0.7.22-beta | [Mac ZIP](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.22-installer-beta.zip) |
| Chrome extension | 0.7.22 | [Extension ZIP](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.22.zip) |
| Linux BYO worker | 0.7.21-beta | [Linux TAR.GZ](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.21-beta.tar.gz) |
| Windows standalone | 0.8.5-beta | [Windows ZIP](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.5-beta.zip) |

[Machine-readable manifest](../RELEASE.json) · [SHA-256 checksums](../RELEASE_SHA256.txt) · [Automatic-update protocol](auto-updates.md)

The Mac 0.7.22 full installer bundles extension 0.7.22. Versioned packages remain available at https://browser.m2g.pro/downloads/ and mirrored at https://m2g.pro/browser-core/downloads/. Older packages remain for rollback.

**Automatic-update limitation:** the signed v2 channel still advertises **0.7.21-beta**. Mac **0.7.22-beta** is distributed as an attended installer, not yet through unattended signed auto-update. A future unattended upgrade has not been acceptance-tested.

The owner's Mac successfully connected Browser Core agent and extension 0.7.22, with approved Instagram tab audio and one 20-second recording prepared. Speech transcription via the connected MCP client remains unverified. This is not evidence of audio transcription or universal browser compatibility.

Windows is a manual-update standalone Chromium beta, with no native existing-Chrome-tab bridge. All Mac desktop packages are unsigned and unnotarized; Python 3.10–3.13 is required. Paid checkout is disabled.
