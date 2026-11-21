# Current release — 21 November 2026

**Latest attended preview:** Mac/Chrome/Linux **0.7.26-beta**, with child-tab delegation after per-site consent. [Mac](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.26-beta.zip) · [Chrome](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.26.zip) · [Linux](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.26-beta.tar.gz). These downloads are validated but are **not** distributed through the signed automatic update feed. Real owner-Mac acceptance is pending.

**Current signed update channel:** 0.7.23-beta for Mac/Linux (Chrome extension 0.7.23). The table below describes the signed default downloads, not the newer attended preview.

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
