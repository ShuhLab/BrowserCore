## Unreleased — P0 dropdown safety (25 November 2026)

- Reject ambiguous, hidden and disabled choices; verify selected option identity after events; report uncertain results instead of false success. [Tests and limits](docs/p0-select-guard-staging.md). Staging only.

## Unreleased — P0 DOM edit guard (25 November 2026)

- Reject protected or changed inputs, maxlength overflow and native value rejection before live writes. [Tests and limitations](docs/p0-dom-edit-staging.md). Staging only.

## Unreleased — P0 Portal Bridge replay scope (25 November 2026)

- Require active consent and ancestor lineage on both tabs for cached apply and status; recheck document identity and stop on uncertainty after final fill. [Tests and limitations](docs/p0-portal-replay-staging.md). Staging only.

## Unreleased — P0 receipt scope (25 November 2026)

- Cached replay and receipt lookup respect current consent, pause, credential handoff and parent lineage. Corrupt or failed results cannot claim verified success. [Tests and limitations](docs/p0-receipt-scope-staging.md). Staging only.

## Unreleased — P1 Portal Bridge context binding (25 November 2026)

- Prevent stale draft writes after a changed document or URL, including query/fragment changes. Recheck grants and connection after asynchronous reads, block concurrent cancellation and expired queued applies. [Tests and limitations](docs/p1-portal-context-staging.md). Staging only; not included in 0.7.28.

## Unreleased — P0 delegated-tab isolation (25 November 2026)

- Preserve manually paused children across root resume and restart; reject operations with invalid ancestors and cascade native revocation. Wait for authoritative extension state before resuming. Staging tests passed; not included in released packages. [Verification and limitations](docs/p0-delegated-tab-isolation-staging.md).

## 0.7.28-beta (attended preview) — 25 November 2026

- **P0:** Metadata-only local action/event journal and operation receipt lookup. Unknown outcomes are never automatically retried. Native child-tab pause state is synchronized with parent takeover; reconnect and disconnect counters are available on an already shared tab.
- **P1 Portal Bridge phase 1:** Two independently user-shared HTTPS tabs can exchange up to 12 explicitly mapped visible text fields. Preview returns a short-lived plan with field lengths, no field contents. Apply rechecks the source fingerprint and uses existing idempotent, verified field filling. Submission is never performed.
- **P1 files (inspection only):** Read-only file picker status returns count, total selected bytes and broad image/video/other categories; no filenames, file contents or uploads.
- **Safety and limitations:** Does not copy binary photo/video, select files, publish forms, bypass CAPTCHA or switch sites without consent. Real Mac two-portal acceptance is still outstanding.
- [Public preview packages and documentation](docs/p0-p1-portal-bridge-preview.md). The signed auto-update channel remains at 0.7.27-beta.

## 0.7.26-beta (attended preview) — 20 November 2026

- Same-origin child tabs opened by an agent action inherit the parent's explicitly approved site scope, including a new child handle for subsequent MCP work.
- Agent-triggered link popups are scoped by opener tab and a brief command window; site-generated/unrelated popups never inherit access.
- Root pause/revoke/site-permission removal propagates to children; cross-origin navigation does not inherit rights.
- Optional HTTPS host permission is requested for the **current exact origin**, not enabled for all websites. Audio is always separately consented.
- Direct child opens now retain URL query/fragment for navigation while persisting only sanitized origin/path.
- Signed feed is still 0.7.23; this is a verified attended preview, not an automatic user deployment.

## Browser Core 0.7.22-beta — 19 November 2026

- Published full Mac installer and Chrome unpacked extension 0.7.22, plus an extension-only ZIP and checksums at both download mirrors.
- Fixed Chrome tab-audio stream-ID creation by moving capture earlier in the popup flow and adding a scoped fallback; added diagnostic details to the popup.
- On the owner's Mac, agent and extension 0.7.22 connected, an Instagram tab was granted, tab audio became enabled, and the user confirmed a completed 20-second capture. Server-side transcription via this connected MCP client is not yet verified.
- Mac package includes local SSL certificate store fix and the complete inventory for future updates. Linux remains 0.7.21-beta and Windows remains 0.8.5-beta.
- Signed automatic-update feed v2 still advertises 0.7.21-beta. Mac 0.7.22 uses an attended installer and future-version unattended updating remains unverified.
- No changes to billing; paid checkout is still disabled.

## Browser Core 0.7.19-beta — 18 November 2026

- Added a registered-destination, popup-confirmed, encrypted API-key handoff channel, isolated from ordinary MCP snapshots and action arguments. Private UNIX-socket receiver authenticated by owner/worker identity and signed local approval. Only synthetic secrets were used in tests; first real Mac/provider transfer remains pending.
- Added per-tab FIFO-style serial execution and atomic operation-ID admission. Different approved tabs remain independently runnable; paused and revoked tabs cannot execute waiting actions; duplicate submissions are not dispatched twice.
- Kept exactly the 0.7.18 signed-updater package file set to preserve unattended compatibility. Mac and extension 0.7.19 and Linux 0.7.19 published, Windows standalone 0.8.5 requires a new CI acceptance run.
- Improved commerce preview ledger handling: partial refunds now require review rather than automatically canceling all access; early renewals require fiscal policy review. Checkout remains disabled.
- Private receiver and payment-preview services are running; browser runtime was not restarted and no user credentials were read or copied.

## 0.7.19-beta signed updater bootstrap — 18 Nov 2026

- Added pinned Ed25519 manifest verification, exact SHA-256/size checks, allowlisted files and atomic user-scoped Mac/Linux release switching; update source and signature are public.
- Added an hourly-cadence-independent two-hour Mac launchd and Linux user-systemd timer. Owner Stop, disabled updates, active sessions/tabs and in-flight jobs defer automatic restart.
- Added local Chrome extension update watcher that reloads unpacked extension after the signed local updater has installed new files; old versions need one bootstrap.
- Added Mac menu controls for checking and disabling updates, and update-state diagnostics without page contents.
- Fixed same-second fractional heartbeat timestamp validation; added regression coverage.
- Published Mac/Linux 0.7.19-beta, Chrome extension 0.7.19 and Windows standalone 0.8.5-beta artifacts. Windows updater remains unfinished.
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
