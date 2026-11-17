# Roadmap and unfinished gates

See [current release](current-release.md) for what is shipped.

## Remaining before commercial availability

- Complete receipt handling, account-bound paid delivery, renewal and refund acceptance for YooKassa and Telegram Stars. Merchant approval/key verification alone does not enable sales.
- Finish and audit a separate credential-provisioning channel with a trusted local destination approval UI; it is not shipped or enabled in the current release.
- Complete reproducible real Mac end-to-end installation, recovery and authorized-send acceptance, not just draft input or Linux fixtures.
- Implement and verify Windows native existing-tab attachment; current Windows is standalone Chromium only.
- Add signed/notarized desktop installers, a bundled Python runtime and verified update handling.
- Improve duplicate-tab reuse and concurrency controls. The current duplicate-site badge is informational, not a deployed hard cap.
- Report actual provider API token usage only where the provider supplies it; do not charge for a bytes/4 estimate of MCP text.

Hosted Cloud remains limited and ephemeral. Multi-node commercial autoscaling, permanent cloud sessions, independently audited tenant isolation and guaranteed service levels are not claimed.
