# Getting started (free public beta)

## Request access
Open https://t.me/OpsTetherBot?start=browsercore and send /browser. The verified Telegram bot issues an expiring, one-use Browser Core OAuth code automatically. No manual invitation, payment, or operator approval is necessary for Local/BYO.

Do not share the code: it authenticates your Browser Core account and is separate from a worker-pairing code.

## Connect to ChatGPT
Add the MCP endpoint https://m2g.pro/browser-core/mcp with OAuth in ChatGPT. Enter the one-time code issued by Telegram on the Browser Core consent page. Successful authorization creates a per-account identity isolated from other users.

## Local Mac
1. Download BrowserCore-Mac-OneClick-0.7.9-beta.zip from the website.
2. Requires macOS and Python 3.10–3.13. The beta is not signed or notarized.
3. Install and pair the local agent with your own code.
4. Open Chrome extensions and allow Browser Core for the specific tab.
5. Keep your own Chrome window open when login, password, 2FA or CAPTCHA is needed.
6. After installing 0.7.9, approve restarting the agent for the update to take effect. A launchd watchdog checks for stale service status every 90 seconds. Use the Browser Core menu's **Stop** to disable automatic restarts until **Start** is explicitly selected again; this choice persists after logout/login.
7. macOS sleep, a closed laptop lid, shutdown, or an offline network still interrupts Local mode. Use your own always-on Linux worker or free limited Hosted Cloud for tasks that must continue when the Mac is asleep.

## Linux / own VPS (BYO)

**Public self-service beta.** For supported Ubuntu and Debian versions with Python 3.10–3.13, get the script and review it locally before execution.

Download: https://browser.m2g.pro/downloads/install-linux.sh

The script runs as a normal user (never root); it verifies a pinned SHA-256 archive, installs pinned dependencies and Chromium, runs a local browser smoke test, accepts a separate one-time worker pairing code in the terminal, and configures a user-level systemd service. Browser Core credentials are not copied into ChatGPT messages.

See https://browser.m2g.pro/docs#linux for the package checksum, supported operating systems and limitations.

## Your own Linux server
The BYO worker runs Chromium on a personal Linux server with an authenticated outbound connection. A personal Linux BYO worker still requires installation and pairing. A public one-click Linux installer is not yet available; the initial BYO setup may require technical assistance.

Manual remote control is a temporary aid for login and verification, not a replacement for working in a normal local browser. Press Done to hand control back to the agent.

Never send passwords, OTPs, cookies, API keys or recovery codes to ChatGPT messages or support.


## Hosted Cloud waiting list

The free Cloud has two isolated simultaneous browser slots. If both are busy,
use cloud_queue_join in ChatGPT to enter the 200-place FIFO waitlist. Poll
cloud_queue_status while you wait, at least every ten minutes. Once
ready_to_claim is true, run profile_create with mode cloud within two minutes.
Use cloud_queue_cancel to give up your place.

After your browser task, call cloud_release to erase temporary profile data.
The queue does not automatically start a browser, notify you via Telegram,
purchase servers or guarantee a start time.
