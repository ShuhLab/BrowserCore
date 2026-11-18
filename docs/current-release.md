# Current coordinated release

| Component | Published version |
|---|---|
| Hosted MCP | 0.8.4-beta |
| Mac and Linux worker | 0.7.18-beta |
| Chrome extension | 0.7.18 |
| Windows standalone | 0.8.4-beta |

[Machine-readable release JSON](../RELEASE.json) · [Hashes](../RELEASE_SHA256.txt) · [Signed auto-update design](auto-updates.md)

The full Mac installer bundles the **identical extension files** from the extension-only ZIP. All versioned archives are published at both https://browser.m2g.pro/downloads/ and https://m2g.pro/browser-core/downloads/; the old archives are preserved for rollback. Production server remains 0.8.4-beta.

**Signed updater:** one Mac/Linux bootstrap adds user-scoped checks, cryptographic verification, a background timer, status and safe deferral during active sessions. Windows still needs manual updates. More details in [auto-updates.md](auto-updates.md).

**Tests:** 18 isolated update tests, real signed HTTPS download and atomic install in a temporary Linux home, Mac/Linux extracted-package Chromium smoke tests, Windows package import checks, 8 real Chromium MV3 panel checks, 5 local extension-watcher tests, source launchd/menu and native messaging regressions. These are not proof of the update process running unattended on the owner's Mac.

The current release does not include the experimental credential handoff, billing, paid access, signed Mac installer or existing-tab support on Windows. Do not enable or claim those features based solely on version numbers.
