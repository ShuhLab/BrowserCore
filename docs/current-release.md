# Current coordinated release

| Component | Published version |
|---|---|
| Hosted MCP | 0.8.4-beta |
| Mac and Linux worker | 0.7.19-beta |
| Chrome extension | 0.7.19 |
| Windows standalone | 0.8.4-beta |

[Machine-readable release JSON](../RELEASE.json) · [Hashes](../RELEASE_SHA256.txt) · [Signed auto-update design](auto-updates.md)

The full Mac installer bundles the **identical extension files** from the extension-only ZIP. All versioned archives are published at both https://browser.m2g.pro/downloads/ and https://m2g.pro/browser-core/downloads/; the old archives are preserved for rollback. Production server remains 0.8.4-beta.

**Signed updater:** one Mac/Linux bootstrap adds user-scoped checks, cryptographic verification, a background timer, status and safe deferral during active sessions. Windows still needs manual updates. More details in [auto-updates.md](auto-updates.md).

**Tests:** 18 isolated update tests, real signed HTTPS download and atomic install in a temporary Linux home, Mac/Linux extracted-package Chromium smoke tests, Windows package import checks, 8 real Chromium MV3 panel checks, 5 local extension-watcher tests, source launchd/menu and native messaging regressions. These are not proof of the update process running unattended on the owner's Mac.

The 0.7.19 beta includes a registered-destination encrypted secret handoff UI and a live private receiver. Its final real Mac acceptance and first provider installation remain outstanding, so this is not yet an end-to-end production credential service. Billing and paid access remain off; desktop packages are unsigned; Windows has no existing-tab support. Do not enable or claim those features based solely on version numbers.

## New: concurrent tab safety

A per-tab serial queue prevents DOM clicks, snapshots and form actions from interleaving on the same tab; different tabs can run simultaneously. Concurrent operation IDs are deduplicated before dispatch. Revoked or paused tabs cancel waiting actions. No unrelated browser tab is closed.
