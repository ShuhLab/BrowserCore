# Current release — 25 November 2026

**Unreleased Mac 0.7.29 RC2 release identity (26 November 2026):** Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude for website actions. The private staging installer rejects same-version directories with different or missing source/assets, unexpected files or symlinks before activation; it does not overwrite the previous code. 124 Python tests and seven JavaScript suites passed in Linux fixtures. No new archive, no real Mac acceptance; full post-activation rollback and installer/updater coordination remain pending. Not released. [Details and limits](mac-0729-rc2-preflight-staging.md).

**Unreleased Mac 0.7.29 RC2 follow-up (26 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude. The private staging installer now asks before switching an existing installation; Later or a failed dialog defers activation, and an unverified post-restart connection no longer reports success. 120 Python tests and seven JS suites passed in isolated fixtures; no new archive, full rollback or real Mac acceptance. [Details and limits](mac-0729-rc2-preflight-staging.md).

**Unreleased P0 confirmed pause:** [Staging correction and limits](p0-pause-reannounce-staging.md). Three simulation cases pass; not in the attended or signed releases. Installed Chrome/Mac unverified.


**Latest attended preview:** Mac/Chrome/Linux **0.7.28-beta**, with P0 operation receipts and P1 Portal Bridge draft-only text transfer. [Mac](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.28-beta.zip) · [Chrome](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.28.zip) · [Linux](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.28-beta.tar.gz). See [preview usage and limitations](p0-p1-portal-bridge-preview.md). Full live owner-Mac acceptance is pending.

**Verified 25 November 2026:** the legacy signed **v2** update feed remains **0.7.23-beta**; the newer signed **v3** feed offers **0.7.27-beta**. Both Ed25519 signatures were verified against the pinned public key. The default download manifest still lists 0.7.23 for Mac/Linux/Chrome. The separately installed 0.7.28 technical preview is not in the signed feed. [Unreleased P0 correction](p0-delegated-tab-isolation-staging.md) is staging-only; it is not part of 0.7.28. Historical descriptions below refer to the dates of those previews, not the current channel state.

**Unreleased P0 native grant scope:** [Queued-command binding](p0-native-grant-scope-staging.md), simulation only; not in 0.7.28. Three historical updater tests remain failing and installed-extension verification is pending.

**Unreleased P0 follow-up:** [Immediate tab access withdrawal](p0-revoke-atomic-staging.md); staging tests only, not in 0.7.28. Installed-extension verification pending.

**Unreleased P1 follow-up:** [Portal Bridge context correction](p1-portal-context-staging.md) is staging-only and not part of 0.7.28. Live Chrome acceptance remains pending.

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

## Owner-Mac acceptance checklist — 0.7.26

On 22 November 2026, a live `existing_tabs_list` check on the owner's connected Mac Intel worker reported agent **0.7.26-beta** and explicitly shared Chrome tabs with extension **0.7.26**. This verifies the reported versions, **not** completion of the full owner-Mac acceptance checklist (child-tab delegation, pause/revoke, reconnect and rollback). The signed v2 updater still targets **0.7.23** and cannot deliver the 0.7.26 preview automatically.

1. Before the attended upgrade, finish or pause active browser tasks. Do not close the actual Chrome social-network tabs or sign out of the sites.
2. Download the [0.7.26 Mac OneClick installer](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.26-beta.zip). This ZIP is unsigned/notarized by Apple; do not disable Gatekeeper or other system security. Verify the [.sha256](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.26-beta.zip.sha256) if needed.
3. Launch **Install Browser Core.app** in the extracted archive and follow the on-screen prompts. The existing worker identity and saved encrypted profiles must remain intact. A restart is deferred while a task cannot safely be interrupted.
4. In `chrome://extensions`, confirm the Browser Core unpacked extension points to `~/Library/Application Support/BrowserCore/Extension` and displays **0.7.26**. Do not load the older copy from Downloads.
5. Grant each original Instagram/TikTok/YouTube tab if Chrome discarded its old extension grant; enable **automatic child-tab access and recovery** on each site only by clicking its dedicated popup option. This grants exact-site scope, not access to the entire browser.
6. Verify `existing_tabs_list` returns Mac agent **0.7.26-beta**, extension **0.7.26** and the expected tab handles. Exercise a harmless child-tab open, snapshot, pause/resume, then a simulated recovery and explicit revocation. Confirm that unrelated tabs never appear.

**Production acceptance:** do not claim unattended server-push updates until the v3 signed manifest is published by the authorized signing workflow and a real Mac upgrade/reconnect/rollback cycle passes. The 0.7.26 preview does not replace the signed 0.7.23 default.


**Private RC2 staging correction (27 November 2026):** [Unicode-safe page summary](snapshot-unicode-staging.md) prevents malformed UTF-16 in descriptive snapshot output and flags repaired text. 140 Python tests and seven Node test files passed in isolation. Exact draft values unchanged; included in a later private unsigned RC2 candidate, not the earlier archive, public downloads or production. Mac end-to-end validation pending.

**Private RC2 staging correction (28 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude for website actions. [Bounded snapshot coverage](snapshot-coverage-staging.md) reports text/action-reference/shadow-root limits and labels the rendered DOM scope; a false truncation flag never proves complete records. 141 Python tests and seven Node suites passed. Private unsigned candidate only, not a public release or attended preview; Mac installation and rollback unverified. Exact Portal Bridge transfer is unchanged.

**Private RC2 staging safety correction (28 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude for website actions. [Safer target resolution](target-resolution-staging.md) stops an incomplete search before acting instead of guessing the target. 142 Python tests and seven Node suites passed; Mac installation and rollback unverified. Private unsigned candidate only, not a public release or attended-preview update. Public capabilities and signed channel unchanged.
