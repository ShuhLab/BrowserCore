# Signed Browser Core beta updates

Current release: Mac/Linux agent **0.7.19-beta**, Chrome extension **0.7.19**, Windows standalone **0.8.4-beta**.

## Protocol and verification

The user-scoped updater checks the fixed HTTPS origin:
- Manifest: https://browser.m2g.pro/downloads/browsercore-beta-updates-v1.json
- Detached signature: https://browser.m2g.pro/downloads/browsercore-beta-updates-v1.sig
- Ed25519 public key: `ad1f40ce4961e1c512793a6a101bea4f7a3a1201d6e3983de65bc11adadc0b70` (pinned inside the installed updater)

The manifest is verified as raw bytes against Ed25519 before parsing. It has a finite validity period. Each artifact has a strictly scoped filename, SHA-256 digest and exact size. The updater refuses redirects, unsafe package members, changed browser permissions, downgrades and unexpected Python dependency changes.

The update is staged in a private new release directory; the current symlink is changed atomically and rollback restores the previous version on a detected apply/restart failure. Account/device pairing, saved browser profiles, logs and secrets are outside the update directory.

## Unattended behavior

- Mac: user-owned launchd updater, every two hours, with an opt-out switch and manual check in the Browser Core menu.
- Linux: user-owned systemd timer, every two hours.
- Mac extension: checks **its own local update-version.json**, never fetching remote executable code. When signed files have been installed by the native agent, it calls `chrome.runtime.reload()` for the unpacked extension.
- Existing active sessions, shared tabs, in-flight actions, an explicit owner Stop or disabled auto-update prevent a background restart.
- The update may remain deferred indefinitely if tabs stay shared. The user can finish/close the session and let the timer apply it; the updater will not silently close tabs.

## Bootstrap and platform boundaries

Install [Mac 0.7.19-beta](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.19-beta.zip) once to add the updater to an existing Mac. The already-installed 0.7.12 agent and 0.7.14 extension do not gain unattended updates remotely. Once bootstrapped, new versions use the signed channel.

Linux installer: https://browser.m2g.pro/downloads/install-linux.sh, including an exact SHA-256 pin.

Windows 0.8.5-beta is a manual-update standalone beta. A signed Windows updater and existing-Chrome-tab bridge require separate implementation/testing. Apple signing/notarization is also unfinished.

## Verified scope

The 0.7.18 signed updater was verified against the *0.7.19 package's unchanged file allowlist* and can accept this release unattended when the worker becomes idle. The updater passed isolated tests for invalid signatures, tampered manifests, unsafe archives, unexpected permissions, rollback, no profile access and delayed restart. A live HTTPS signed-package test installed the release atomically in a **temporary test home on Linux**. The Chrome panel and update watcher have synthetic/Chromium regression tests. A real user Mac background timer and future-version update cycle have not yet been acceptance-tested.

No payment keys, browser sessions or other projects were modified by the release publication. Checkout and secure credential transfer remain disabled.

The 0.7.19 package has no new on-disk module filenames compared with 0.7.18; additional security code is bundled into reviewed existing modules. This deliberately preserves upgrade compatibility without another bootstrap installation.
