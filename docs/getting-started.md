# Get started with Browser Core

**Unreleased Mac 0.7.29 RC2 release identity (26 November 2026):** Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude for website actions. The private staging installer rejects same-version directories with different or missing source/assets, unexpected files or symlinks before activation; it does not overwrite the previous code. 124 Python tests and seven JavaScript suites passed in Linux fixtures. No new archive, no real Mac acceptance; full post-activation rollback and installer/updater coordination remain pending. Not released. [Details and limits](mac-0729-rc2-preflight-staging.md).

Website: https://browser.m2g.pro/ — use [current release notes](current-release.md) to distinguish the default manifest, signed updates and attended preview. **Verified 25 November 2026:** the legacy signed **v2** update feed remains **0.7.23-beta**; the newer signed **v3** feed offers **0.7.27-beta**. Both Ed25519 signatures were verified against the pinned public key. The default download manifest still lists 0.7.23 for Mac/Linux/Chrome. The separately installed 0.7.28 technical preview is not in the signed feed. [Unreleased P0 correction](p0-delegated-tab-isolation-staging.md) is staging-only; it is not part of 0.7.28. Historical descriptions below refer to the dates of those previews, not the current channel state.

Connect `https://m2g.pro/browser-core/mcp` via OAuth in **ChatGPT or Claude**. The same verified Telegram login grants access to the same Browser Core account and paired devices. For a new worker, use a separate one-time pairing code; do not recreate an existing worker.

## Mac

**Unreleased Mac 0.7.29 RC2 follow-up (26 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude. The private staging installer now asks before switching an existing installation; Later or a failed dialog defers activation, and an unverified post-restart connection no longer reports success. 120 Python tests and seven JS suites passed in isolated fixtures; no new archive, full rollback or real Mac acceptance. [Details and limits](mac-0729-rc2-preflight-staging.md).

1. Download [default Mac 0.7.23-beta](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.23-beta.zip). Extract and run `Install Browser Core.app`. This is unsigned beta software; do not disable macOS security globally.
2. It preserves pairing/profiles and installs a user-level signed-update check. Approve a restart only when ready to interrupt a live browser.
3. Chrome → chrome://extensions → Load unpacked. Choose `~/Library/Application Support/BrowserCore/Extension` or the extension-only extracted folder containing `manifest.json`.
4. Permit only the desired tabs in the popup. The extension shows only connected tabs.
5. From now on signed updates run at a two-hour cadence unless disabled in the Mac menu, and restart is deferred while tabs/sessions are in use.

An older Mac 0.7.12-beta agent still works with extension 0.7.14; there is no requirement to re-pair. Auto-updates require the one-time newer installer.

## Linux

Review https://browser.m2g.pro/downloads/install-linux.sh and execute it as an unprivileged user. It installs worker 0.7.23-beta, pins the package SHA-256, and creates a `systemd --user` updater timer. Existing desktop Chrome tabs are not attached by this package.

## Windows

Download [Windows standalone 0.8.5-beta](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.5-beta.zip). It starts separate Playwright Chromium and requires Python 3.10–3.13. It does not attach to current Chrome/Edge tabs and has no unattended updater or signed EXE.

## Modes and consent

Browser Core connects only the Chrome tabs you authorize to ChatGPT or Claude for website actions. If a shared tab reconnects during preparation of an order or other draft, inspect its actual contents before retrying any uncertain action. The [unreleased grant-scope safeguard](p0-native-grant-scope-staging.md) is staging-only; it is not available in 0.7.28.

Always check `execution_status` and `execution_options`, reuse a suitable live session/approved tab and avoid opening duplicates. Local and BYO use the user's resources; Cloud is limited and ephemeral. A task may include multiple ordinary sends without a new confirmation for every message. Draft-only, stop and no-send instructions remain binding. Never retry an uncertain send automatically.

Users enter passwords, OAuth, 2FA and CAPTCHA in their own browser during handoff, not in chat. Browser-to-server secret transfer is not shipped. Card and Stars checkout are not yet open.

## Connecting a registered provider API key (beta)

Open the provider's authorized browser tab, grant it to Browser Core and select only the credential text. In the extension popup choose the **registered destination** and confirm. The credential is encrypted in the tab and sent through the paired native worker to the private server receiver. The model sees only status. Do not paste the key in the chat or ordinary form-action arguments. The tab stays paused until you remove any secret from the screen and manually resume. Only the separate Community Pilot Telegram destination is currently registered; first real Mac/provider acceptance is pending. The target service and payments are not switched on simply by saving a credential.

## Tab audio for short videos (Mac/Chrome 0.7.22)

Open a short video in an explicitly authorized Chrome tab. In Browser Core's popup, enable optional audio capture permissions and click **Connect audio**. Once connected, click **Record 20 seconds** while the video's own audio is unmuted. A ready clip is not a text transcript; a separate MCP transcription tool call is required. Chrome may show an offscreen audio document in extension diagnostics; the microphone is not used.

If Chrome still shows 0.7.19, inspect the unpacked-extension source directory. Loading it from an old Downloads folder does not receive the managed update. Use `~/Library/Application Support/BrowserCore/Extension`, with a fresh tab grant if Chrome resets the previous permission.

Historical 0.7.22 audio instructions above do not represent current package versions. Signed v2 advertises 0.7.23 and v3 advertises 0.7.27; Windows remains a separate standalone beta.

**Private RC2 staging correction (28 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude for website actions. [Bounded snapshot coverage](snapshot-coverage-staging.md) reports text/action-reference/shadow-root limits and labels the rendered DOM scope; a false truncation flag never proves complete records. 141 Python tests and seven Node suites passed. Private unsigned candidate only, not a public release or attended preview; Mac installation and rollback unverified. Exact Portal Bridge transfer is unchanged.
