# Current release — 20 November 2026

| Component | Version | Package |
|---|---|---|
| Hosted MCP server | 0.8.4-beta | [Endpoint](https://m2g.pro/browser-core/mcp) |
| Mac installer and agent | 0.7.23-beta | [Mac ZIP](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.23-beta.zip) |
| Chrome extension | 0.7.23 | [Extension ZIP](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.23.zip) |
| Linux BYO worker | 0.7.23-beta | [Linux TAR.GZ](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.23-beta.tar.gz) |
| Windows standalone | 0.8.5-beta | [Windows ZIP](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.5-beta.zip) |

[Machine-readable manifest](../RELEASE.json) · [SHA-256 checksums](../RELEASE_SHA256.txt) · [Automatic-update protocol](auto-updates.md)

The Mac 0.7.23 full installer and extension have been published and verified on both download mirrors. The signed v2 channel now offers 0.7.23; installed Mac 0.7.22 agents defer updates until there are no active sessions/shared tabs/in-flight commands. Live Mac installation of 0.7.23 remains unverified.

The extension persists user-granted tab intentions in local storage after worker reload; explicit Revoke and Pause remain binding. A full Chrome restart with changed tab IDs still needs separately approved site permission in a future release. No automatic renewal may bypass an explicit Revoke.

The owner's Mac successfully connected Browser Core agent and extension 0.7.22, with approved Instagram tab audio and one 20-second recording prepared. Speech transcription via the connected MCP client remains unverified. This is not evidence of audio transcription or universal browser compatibility.

Windows is a manual-update standalone Chromium beta, with no native existing-Chrome-tab bridge. All Mac desktop packages are unsigned and unnotarized; Python 3.10–3.13 is required. Paid checkout is disabled.
