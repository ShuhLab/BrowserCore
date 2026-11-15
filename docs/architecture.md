# Architecture and security model

ChatGPT / MCP client -> OAuth-protected Browser Core control plane -> authenticated outbound worker -> browser.

Local: user-authorized worker on a computer can operate Chromium or a specifically granted native Chrome tab through the extension. Local Chrome cookies and passwords are not wholesale exported to the control plane.

BYO: Chromium runs on the user's own Linux machine or VPS, with an encrypted, persistent profile and one-owner worker identity.

When the agent needs help, it pauses. The user opens a one-time, expiring remote-control link for the same browser context, enters a password, completes 2FA or CAPTCHA, clicks Done, and the agent resumes after verification.

The remote viewer is not optimized for prolonged browsing and may experience network latency. Prefer native local Chrome for normal interactive use.

Current controls include tab-scoped permissions, expiry and revocation, authenticated workers, CSRF protection in the human handoff, and metadata-only job journaling. No independent security certification is claimed. Commercial multi-tenant Cloud isolation is not complete.
