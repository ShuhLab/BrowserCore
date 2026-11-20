# Signed Browser Core beta updates

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
