# Current release — coordinated distribution

This page supersedes historical installation recommendations. Historical release files are retained; they are not the default downloads.

## Component versions

Server **0.8.4-beta**; Mac/Linux agent **0.7.14-beta**; extension **0.7.14**; Windows standalone bundle **0.8.1-beta**, containing agent 0.7.14-beta.

See [RELEASE.json](../RELEASE.json) for immutable filenames, SHA-256 digests and sizes. The public copy is https://browser.m2g.pro/downloads/browser-core-release.json . The two representations must agree.

## Extension 0.7.14

Only explicitly connected tabs are shown, including paused tabs. Unconnected placeholders, empty statistics and internal window IDs were removed. No broad tabs permission is requested. Duplicate-site badges count connected tabs only; they do not close tabs or impose a new quota.

Measured counters include calls, completed/blocked/failed results and text bytes. The rough UTF-8 bytes/4 figure is not provider token usage, model reasoning tokens, image usage or a bill. Metrics do not persist page contents or drafts.

The DOM action engine is unchanged from the verified 0.7.12 implementation. It verifies stable field values, rejects stale or ambiguous controls and preserves operation-ID replay protection. Server 0.8.3 and later default confirm_submission to true for ordinary authorized task actions; explicit draft-only requests remain binding. A send is not claimed successful merely because a click returned completed.

## Downloads and installation

- Mac: https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.14-beta.zip
- Extension only: https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.14.zip
- Linux: https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.14-beta.tar.gz
- Windows standalone: https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.1-beta.zip

The Mac installer bundles the exact extension-only release. Existing Mac 0.7.12-beta + extension 0.7.14 installations remain compatible. Do not force a reinstall or re-pair a working device solely to make displayed numbers equal.

No browser or paired worker was restarted by the distribution update. Installing a new local agent can require a user-approved restart. Existing browser profiles and account pairing must not be deleted.

## Evidence and limits

- Artifact import/copy audit and executable shell syntax checks passed for the Mac package.
- Extracted Mac/Linux/Windows Python modules imported from their package directories, not from the source checkout.
- All three extracted worker packages passed a real local Chromium smoke test on Linux.
- Eight connected-tabs popup scenarios passed in real Linux Chromium MV3; unit checks covered revoked/closed/private tabs, deduplication, numeric-only metrics and no broad enumeration.
- Agent/native-message tests passed for origin checks, regrant/reconnect, human takeover, duplicate protection, wrong-handle rejection and task-authorized submission.
- Every public archive was downloaded from browser.m2g.pro and the legacy m2g.pro/browser-core mirror; hashes matched.
- The current Windows workflow downloads the exact 0.8.1 archive by pinned digest. Read its actual run result; a Linux pass or the historical 0.8.0 Windows pass is not evidence that this Windows run succeeded.

The user's Mac previously verified real Telegram draft input using the retained DOM engine. Real Telegram send completion and a new Mac 0.7.14 installer acceptance are not asserted by these package checks.

Checkout and credential handoff remain disabled. No private API keys, environment files or device state are included. Experimental unpublished artifacts are not automatically promoted solely because they have a higher version number.
