# Windows standalone beta 0.8.4-beta

Download: https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.5-beta.zip

SHA-256: `9884d0d81f835cfadff39eec1cca4ea7dd90459acf4ba1abefe69ad9cd8db51d`

The package includes worker 0.7.19-beta. The standalone browser uses Playwright Chromium and an outbound worker, with encrypted local profile storage and manual takeover for login. Python 3.10–3.13 must already be installed.

Not included: attachment to existing Chrome/Edge tabs; a user-level always-on Windows updater; signed installer; bundled Python runtime; arbitrary provider credential capture.

Extract to a user-owned folder. From non-administrator PowerShell run:

```powershell
.\installers\windows\check.ps1
.\installers\windows\install.ps1
.\installers\windows\start.ps1
```

This exact package was built and tested on Linux for source imports. A **new Windows GitHub Actions smoke test must pass** for this exact checksum before describing it as Windows-verified. The historical Windows 0.8.1 run is not evidence for 0.8.4.

[Current release](current-release.md) · [Signed updates on Mac/Linux](auto-updates.md)
