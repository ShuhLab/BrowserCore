# Browser Core Windows standalone beta 0.8.0

**Status: publicly downloadable, experimental Windows runner-tested preview.**
This is NOT a signed EXE/MSI, not a general-availability Windows release
and not yet verified on an independent customer Windows PC.

- [Download Windows beta ZIP](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.0-beta.zip)
- [SHA-256 checksum](https://browser.m2g.pro/downloads/BrowserCore-Windows-Standalone-0.8.0-beta.sha256)
- [Windows 2025 GitHub CI success](https://github.com/ShuhLab/BrowserCore/actions/runs/43757022984)
- [Website installation guide](https://browser.m2g.pro/docs#windows)

SHA-256: e80e0f1710971d399837598522996bd72cf7746dc29a3c53d50eadf05661c93d

## Capabilities and limitations

This ZIP can automate a **separate Playwright Chromium profile** from a
Windows machine after OAuth and per-user pairing. The code does NOT connect
to existing browser tabs in Windows: its Unix-domain native-messaging bridge
was deliberately disabled to avoid pretending this is supported. A
Windows-specific consent-aware native messaging implementation and real
device acceptance tests are required before claiming that feature.

Python 3.10–3.13 and PowerShell are required; there is no bundled runtime,
signed installer, or automatic version update yet. Windows 11 is the primary
target; Windows 10 with up-to-date installed Chrome/Edge is experimental.

## Install

Unzip into a trusted folder. Inspect its source and README-Windows.md.
In a PowerShell terminal opened in the extracted folder:

1. Run installers/windows/check.ps1
2. Run installers/windows/install.ps1
3. Run installers/windows/start.ps1

Use the Telegram /browser one-use code to authenticate the MCP connection.
Use a separate one-use Local worker pairing code from ChatGPT. Enter codes
only in their authorized forms or terminal prompts, never in ChatGPT chat.

## Code-signing roadmap

To release a signed Windows app, we must package a reproducible binary
on a Windows build runner, register a verified publisher and use trusted
Authenticode signing with an RFC 3161 timestamp. Candidates are Microsoft's
Artifact Signing where eligibility allows, or an OV certificate from a
trusted CA; a Microsoft Store MSIX is a separate packaging and distribution
route. Self-signed signatures are **not** a substitute for public trust.

Windows signing guidance:
https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options

macOS signing requires an Apple Developer ID, hardened runtime and a
notarization workflow, which is separate from Windows Authenticode.

No payment or signing certificate has been purchased.
