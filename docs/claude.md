# Browser Core with Claude

Updated 16 November 2026. Status: server-side MCP/OAuth compatibility verified; the real Claude interface has not yet been tested.

Browser Core uses the same hosted MCP backend for ChatGPT and Claude. No second browser service or copied browser profile is required merely to support a second MCP client. The platform-specific local agent is still needed for Local mode.

## Add a custom connector

Endpoint: `https://m2g.pro/browser-core/mcp`

1. In Claude, open Customize > Connectors and add a custom connector named Browser Core.
2. Use the endpoint above, with OAuth sign-in. When the OAuth client choice is shown, choose **Register automatically**. This backend supports dynamic client registration and public PKCE clients; do not invent a client secret or use a fixed administrator token.
3. Request a one-time Browser Core code using `/browser` in `@OpsTetherBot`. Enter it only on the actual `https://m2g.pro/browser-core/oauth/authorize` consent page. The consent screen identifies Claude from its approved callback URL.
4. Enable the connector in a conversation. First request `execution_status` and `execution_options`. Choose Local, BYO or Cloud explicitly; do not silently move a local task to Cloud.
5. For Local, use a paired online computer and individually authorize the relevant Chrome tab. For an initial protocol check, status and tool-list calls do not require a running browser.

Anthropic's documentation currently permits one custom remote MCP connector on Claude Free. Paid Claude is therefore not a prerequisite for an initial custom-connector test. Availability and usage limits belong to the user's Claude account; no live test of that account is claimed. Adding by URL does not mean the connector is listed or approved in Anthropic's directory.

## Account isolation

Workers and profiles belong to the authenticated Browser Core account, not to the name of the AI client. Existing workers are shared between clients only when both authenticate to the same Browser Core account. Creating another account does not automatically migrate an older private-pilot `owner` account or its paired devices. No tokens, cookies or browser profiles are copied between accounts by this update.

## Compatibility update

- Allow only the exact documented Claude OAuth callbacks, in addition to the existing ChatGPT callbacks: `https://claude.ai/api/mcp/auth_callback` and `https://claude.com/api/mcp/auth_callback`.
- Allow the corresponding exact Claude web origins in both MCP request-validation layers. Lookalike domains remain rejected.
- Keep PKCE S256, one-use authorization codes, token rotation, resource binding and per-account authorization.
- Derive the consent-screen client label from the stored approved redirect, not arbitrary registration text.
- Preserve existing ChatGPT redirect support and current worker credentials.

## Verification performed

The existing 19-check OAuth regression passed, followed by new isolated tests for exact Claude callbacks, nine malicious/unsupported callback variants, PKCE, replay, refresh, tenant separation and consent labels.

At 2026-11-16 08:13:30 UTC, a synthetic-account probe against the public HTTPS deployment passed these checks:

1. Unauthenticated MCP calls rejected with an OAuth discovery challenge.
2. ChatGPT and both exact Claude callbacks accepted by dynamic registration.
3. A lookalike callback domain rejected.
4. Consent page, one-time test authorization and PKCE token exchange.
5. MCP initialize and tools/list using protocol version 2025-06-18.
6. An untrusted Origin rejected.
7. Read-only execution_status returned only the empty synthetic account's workers and sessions.
8. Refresh rotated the token while preserving the account subject.

Synthetic auth records were removed after the test. No existing account data was changed. No browser action, Claude model request, payment or paid cloud purchase was performed. **These checks are not an end-to-end test in the real Claude UI.**

The Windows 0.8.0 preview still supports only a separate Chromium profile; existing Windows Chrome tabs and a self-contained installer remain unfinished. The extension code can be shared across operating systems, but each platform needs its own installed native messaging host/agent integration.

## Official references

- Custom connectors and Claude Free: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- Server transport, authentication and testing: https://claude.com/docs/connectors/building
- Native messaging platform registration: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging
