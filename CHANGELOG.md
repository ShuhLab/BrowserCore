## 0.7.18-beta signed updater bootstrap — 18 Nov 2026

- Added pinned Ed25519 manifest verification, exact SHA-256/size checks, allowlisted files and atomic user-scoped Mac/Linux release switching; update source and signature are public.
- Added an hourly-cadence-independent two-hour Mac launchd and Linux user-systemd timer. Owner Stop, disabled updates, active sessions/tabs and in-flight jobs defer automatic restart.
- Added local Chrome extension update watcher that reloads unpacked extension after the signed local updater has installed new files; old versions need one bootstrap.
- Added Mac menu controls for checking and disabling updates, and update-state diagnostics without page contents.
- Fixed same-second fractional heartbeat timestamp validation; added regression coverage.
- Published Mac/Linux 0.7.18-beta, Chrome extension 0.7.18 and Windows standalone 0.8.4-beta artifacts. Windows updater remains unfinished.
- Checkout and secure credential handoff remain disabled. Real Mac unattended update and new Windows CI result still require acceptance.

# Release notes

## Coordinated distribution: server 0.8.4-beta / agents 0.7.14 / Windows 0.8.1

- Synchronized the ten-language website, documentation, extension-only ZIP and full Mac installer.
- Mac 0.7.14 contains the exact extension 0.7.14 bytes; Linux 0.7.14 and Windows standalone 0.8.1 use current reviewed agent modules.
- Extension panel shows connected tabs only, including paused tabs. Removed unconnected placeholders, internal window IDs, empty usage cards and broad optional tabs permission.
- Retained verified DOM editing and per-operation deduplication; ordinary sends within an authorized task do not require a physical click per message. Explicit draft-only requests remain binding.
- Documented the confirmed owner Claude connection and shared account/device identity.
- Added RELEASE.json, all current SHA-256 digests and a public-distribution consistency workflow covering both mirrors, all ten landing pages and Mac/extension byte equality.
- Repointed Windows CI to the exact new archive and digest. Package imports and Chromium smoke checks passed on Linux; native Windows result must be verified independently.
- Public downloads verified over HTTPS. Existing user devices, sessions, profiles and other projects were not restarted or migrated by publication.
- Checkout and secret handoff remain disabled. Unsigned installer and Windows existing-tab limitations remain.

Historical notes below describe their release dates, not current availability. See docs/current-release.md and RELEASE.json for installation choices.

## macOS Local v0.7.9-beta — 2026-11-16
- LaunchAgent watchdog runs every 90 seconds, recovering absent or stale agents while the gateway is reachable; restart cooldown prevents loops
- Grace period extends for active browser sessions to avoid unnecessary loss of live state
- Explicit Stop persists across macOS login and reinstall until the owner chooses Start or Repair
- Existing device pairing, encrypted local profiles and browser extension permissions remain preserved during upgrade
- SHA-256 verified hosted download and simulated watchdog/launchd unit tests passed; live macOS E2E verification is still required
- The unsigned, non-notarized beta cannot remain connected while macOS is asleep or powered off

## v0.7.8-beta — November 2026
- Mac extension animated button states: pressed, busy, success and failure
- Explicit per-tab authorization for existing Chrome, native messaging bridge
- Outbound WebSocket worker and reconnect
- Separate Local and personal BYO execution
- Manual remote intervention for password, CAPTCHA, 2FA
- Persistent encrypted worker profiles

Known at that release: unsigned/notarized Mac app, Python prerequisite, manual extension installation, invite-only access, zero hosted commercial Cloud slots.

## Public Local/BYO onboarding — 2026-11-15
- Verified Telegram self-service OAuth without operator invitations
- 10-language website with sourced competitor comparisons
- Anonymous website view and CTA counters, IndexNow submission
- Hosted Cloud and merchant checkout remained disabled pending verification

## Public Linux worker and mobile QA — 2026-11-15
- User-level Linux Local/BYO installer with pinned SHA-256 archive, Playwright browser smoke test and systemd --user service
- Ten translated landing pages checked at 390px and 1280px widths (20 browser viewport cases); comparison table and RTL overflow fixed
- Hosted Cloud and payment checkout remained unavailable pending isolation and merchant approval

## Windows standalone preview — 15 November 2026
- Experimental Windows standalone Chromium agent ZIP published with verified SHA-256
- Microsoft Windows runner successfully completed real Chromium automation smoke test
- No Windows native existing-Chrome-tab attachment, code signing, bundled Python or public auto-update yet
- Cloud beta, Linux, Mac and MCP continue to work independently

## v0.8.1-beta — 15 November 2026
- Owner-scoped persistent FIFO queue for free Hosted Cloud, maximum 200 entries
- MCP tools cloud_queue_join, cloud_queue_status, cloud_queue_cancel
- Ten-minute no-poll expiry and two-minute ready-to-claim window
- Two live isolated Chromium workers passed fairness and cleanup verification
- 10-language site showed live aggregate queue size and public limitations
- Multi-node autoscaling and paid checkout remained unavailable
