# Get started with Browser Core

Website: https://browser.m2g.pro/ — current versions and checksums in [RELEASE.json](../RELEASE.json).

Connect `https://m2g.pro/browser-core/mcp` via OAuth in **ChatGPT or Claude**. The same verified Telegram login grants access to the same Browser Core account and paired devices. For a new worker, use a separate one-time pairing code; do not recreate an existing worker.

## Mac

1. Download [Mac 0.7.18-beta](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.18-beta.zip). Extract and run `Install Browser Core.app`. This is unsigned beta software; do not disable macOS security globally.
2. It preserves pairing/profiles and installs a user-level signed-update check. Approve a restart only when ready to interrupt a live browser.
3. Chrome → chrome://extensions → Load unpacked. Choose `~/Library/Application Support/BrowserCore/Extension` or the extension-only extracted folder containing `manifest.json`.
4. Permit only the desired tabs in the popup. The extension shows only connected tabs.
5. From now on signed updates run at a two-hour cadence unless disabled in the Mac menu, and restart is deferred while tabs/sessions are in use.

An older Mac 0.7.12-beta agent still works with extension 0.7.14; there is no requirement to re-pair. Auto-updates require the one-time newer installer.

## Linux

Review https://browser.m2g.pro/downloads/install-linux.sh and execute it as an unprivileged user. It installs worker 0.7.18-beta, pins the package SHA-256, and creates a `systemd --user` updater timer. Existing desktop Chrome tabs are not attached by this package.

## Windows

Download [Windows standalone 0.8.4-beta](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.4-beta.zip). It starts separate Playwright Chromium and requires Python 3.10–3.13. It does not attach to current Chrome/Edge tabs and has no unattended updater or signed EXE.

## Modes and consent

Always check `execution_status` and `execution_options`, reuse a suitable live session/approved tab and avoid opening duplicates. Local and BYO use the user's resources; Cloud is limited and ephemeral. A task may include multiple ordinary sends without a new confirmation for every message. Draft-only, stop and no-send instructions remain binding. Never retry an uncertain send automatically.

Users enter passwords, OAuth, 2FA and CAPTCHA in their own browser during handoff, not in chat. Browser-to-server secret transfer is not shipped. Card and Stars checkout are not yet open.
