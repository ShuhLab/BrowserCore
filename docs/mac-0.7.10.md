# macOS Local 0.7.10-beta — 16 November 2026

This unsigned, non-notarized beta supersedes macOS 0.7.9. Apple Developer ID enrollment and paid signing have not been initiated.

Download: https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.10-beta.zip

SHA-256: `6cfcde861fb0b4ed3ab2f3ae8707a455a5ba34709fbc997bebbf943b1f74e483`

## Changes

- All four bundled launchd helpers are now byte-identical and support the watchdog label and module. Previously the installer and Repair contained an older helper that rejected the watchdog.
- Existing Repair and Control apps are refreshed during installation rather than silently retaining older copies.
- Failed launchctl commands now retain their bounded error text in the local repair log, with the home path abbreviated. Full launchctl environment output is not logged.
- Repair verifies a new server acknowledgement received after the repair request. Registering a service alone is no longer reported as confirmed recovery.
- A failed or absent watchdog causes an incomplete-recovery result rather than an unconditional success message.

## Verification and limitations

Python and shell syntax checks, launchd mock lifecycle tests, supervisor locking tests, consent/status tests, HTTP/WebSocket health tests, watchdog tests and package consistency checks passed. Both public download routes returned HTTP 200 and the expected SHA-256.

The exact cause of an existing Mac's `KICKSTART_FAILED rc=1` is not yet determined. No live macOS install/reboot test is claimed. This release does not install itself remotely and does not guarantee that an unknown permission or operating-system error is resolved.

Install the new package over the old one and approve the agent restart to use the new code. Existing pairing and persistent profiles are retained; live browser sessions may close on restart. Do not disable Gatekeeper or other macOS security controls. The Python prerequisite and manual extension onboarding remain unchanged.

The hosted MCP/server release remains 0.8.1. Linux and Windows packages are unchanged. Payments remain disabled; this update does not alter tariffs, legal terms or merchant settings.
