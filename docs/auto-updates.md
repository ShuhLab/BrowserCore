# Signed Browser Core beta updates

**Published client packages:** Mac 0.7.22-beta (attended full installer), extension 0.7.22, Linux 0.7.21-beta, Windows standalone 0.8.5-beta.

The current signed v2 feed **still offers 0.7.21-beta**:

- Manifest: https://browser.m2g.pro/downloads/browsercore-beta-updates-v2.json
- Signature: https://browser.m2g.pro/downloads/browsercore-beta-updates-v2.sig
- Ed25519 public key: `ad1f40ce4961e1c512793a6a101bea4f7a3a1201d6e3983de65bc11adadc0b70`

Signature, SHA-256 digest, package length, inventory and safe file paths are checked before installation. Mac uses a user-owned launchd periodic checker; Linux uses a user-owned systemd timer. Updates are deferred during active sessions, explicitly shared tabs, in-flight commands, disabled updates or owner Stop. Pairing and saved profiles are outside release directories.

**0.7.22 is not yet published as a signed automatic upgrade.** The attended Mac installer includes the native sound capture files, certificate-chain trust-store fix, managed unpacked Chrome extension and release inventory for future upgrades. An `up_to_date` message merely indicates the installed version is not older than the current signed feed.

Chrome cannot download a new unpacked extension from a server itself. Its local watcher only reloads files installed in the same managed directory. An old extension loaded from Downloads remains at its old version until the user loads the managed folder. Its grants may be cleared during reload.

Windows has no unattended updater. Mac installers are not Apple signed or notarized. Never disable TLS certificate verification to make updates work; the Mac installer uses the certifi CA store. Paid checkout remains disabled.
