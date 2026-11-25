# Signed Browser Core beta updates

**Verified 25 November 2026:** the legacy signed **v2** update feed remains **0.7.23-beta**; the newer signed **v3** feed offers **0.7.27-beta**. Both Ed25519 signatures were verified against the pinned public key. The default download manifest still lists 0.7.23 for Mac/Linux/Chrome. The separately installed 0.7.28 technical preview is not in the signed feed. [Unreleased P0 correction](p0-delegated-tab-isolation-staging.md) is staging-only; it is not part of 0.7.28. Historical descriptions below refer to the dates of those previews, not the current channel state.



**Published client packages:** Mac 0.7.23-beta (signed update + attended installer), extension 0.7.23, Linux 0.7.23-beta, Windows standalone 0.8.5-beta.

The current signed v2 feed **now offers 0.7.23-beta**:

- Manifest: https://browser.m2g.pro/downloads/browsercore-beta-updates-v2.json
- Signature: https://browser.m2g.pro/downloads/browsercore-beta-updates-v2.sig
- Ed25519 public key: `ad1f40ce4961e1c512793a6a101bea4f7a3a1201d6e3983de65bc11adadc0b70`

Signature, SHA-256 digest, package length, inventory and safe file paths are checked before installation. Mac uses a user-owned launchd periodic checker; Linux uses a user-owned systemd timer. Updates are deferred during active sessions, explicitly shared tabs, in-flight commands, disabled updates or owner Stop. Pairing and saved profiles are outside release directories.

**0.7.23 is published as a signed automatic upgrade, but active tabs and sessions block installation until safe idle.** The attended Mac installer includes the native sound capture files, certificate-chain trust-store fix, managed unpacked Chrome extension and release inventory for future upgrades. An `up_to_date` message merely indicates the installed version is not older than the current signed feed.

Chrome cannot download a new unpacked extension from a server itself. Its local watcher only reloads files installed in the same managed directory. An old extension loaded from Downloads remains at its old version until the user loads the managed folder. Its grants may be cleared during reload.

Windows has no unattended updater. Mac installers are not Apple signed or notarized. Never disable TLS certificate verification to make updates work; the Mac installer uses the certifi CA store. Paid checkout remains disabled.

**Recovery limitations:** Version 0.7.23 keeps explicit tab grants across extension worker restarts using local storage. Restoring a tab after a full browser restart with a changed tab ID may require a separate host-permission opt-in, not included in 0.7.23. Never restore manually revoked or paused access automatically.

## 0.7.24 server-signalled update / tab restoration preview

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
