# Release notes

## v0.7.8-beta — November 2026
- Mac extension animated button states: pressed, busy, success and failure
- Explicit per-tab authorization for existing Chrome, native messaging bridge
- Outbound WebSocket worker and reconnect
- Separate Local and personal BYO execution
- Manual remote intervention for password, CAPTCHA, 2FA
- Persistent encrypted worker profiles

Known: unsigned/notarized Mac app, Python prerequisite, manual extension installation, invite-only access, zero hosted commercial Cloud slots.

## Public Local/BYO onboarding — 2026-11-15
- Verified Telegram self-service OAuth without operator invitations
- 10-language website with sourced competitor comparisons
- Anonymous website view and CTA counters, IndexNow submission
- Hosted Cloud and merchant checkout remain disabled pending verification

## Public Linux worker and mobile QA — 2026-11-15
- User-level Linux Local/BYO installer with pinned SHA-256 archive, Playwright browser smoke test and systemd --user service
- Ten translated landing pages checked at 390px and 1280px widths (20 browser viewport cases); comparison table and RTL overflow fixed
- Hosted Cloud and payment checkout remain unavailable pending isolation and merchant approval

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
- 10-language site now shows live aggregate queue size and public limitations
- Multi-node autoscaling and paid checkout remain unavailable
