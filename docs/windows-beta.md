# Windows standalone beta 0.8.1

Download: https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.1-beta.zip

SHA-256: `22e5c7f3fb7d926e3c51f89800efc1aa10478af9226c611e91fd050a14869dec`

Contains current agent code 0.7.14-beta. The package number is separate from the agent number. It remains an unsigned experimental standalone browser distribution, not a complete Windows desktop product.

## Available

- A separate Playwright Chromium browser, outbound paired worker connection and user-scoped profile storage.
- MCP navigation, forms, snapshots, screenshots and brief manual takeover.
- Shared account access from ChatGPT and Claude.

## Not available

- Attachment to existing Windows Chrome/Edge tabs; the Unix peer-credential bridge is explicitly not started on Windows.
- Authenticode signing, bundled Python, silent updates or a commercial SLA.
- Secure browser-to-server credential capture or enabled paid checkout.

## Install

Extract the archive to a folder you own. Python 3.10–3.13 must already be installed. Use normal-user PowerShell, not an Administrator session:

```powershell
.\installers\windows\check.ps1
.\installers\windows\install.ps1
.\installers\windows\start.ps1
```

Create a separate Local worker-pairing code through the authenticated Browser Core MCP client. Enter it at the local prompt. Never paste passwords or API keys in chat. Stop the foreground worker with Ctrl+C.

## Verification

The exact 0.8.1 archive has passed extracted-module imports and real local Chromium smoke tests on Linux. The Windows workflow now downloads this archive with its pinned digest and runs a real Chromium smoke test on Windows. Its current run result is authoritative; do not treat the historical 0.8.0 Windows pass as a pass for 0.8.1.

[Current Windows workflow](../.github/workflows/windows-standalone-qa.yml) · [Current release](current-release.md)
