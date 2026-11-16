# Browser Core with Claude

Updated 16 November 2026. Status: public MCP/OAuth protocol and real Chromium consent-form checks passed. A connection through the user's actual Claude interface is still unverified.

Browser Core uses the same hosted MCP backend for ChatGPT and Claude. The platform-specific agent is needed for Local mode; supporting another AI client does not require a separate browser service.

## Connect

Endpoint: `https://m2g.pro/browser-core/mcp`

1. In Claude, add a custom connector named Browser Core using this endpoint and OAuth. Choose **Register automatically** when prompted for OAuth client registration. Do not invent a client secret or use an administrator token.
2. Keep the Browser Core authorization page open. Its Telegram button opens a separate tab. Do not replace the authorization page with Telegram and then rely on the browser Back button.
3. Send `/browser` to `@OpsTetherBot`, use **Copy code**, and paste the code into the still-open Browser Core authorization form. This is an account sign-in code, not a Telegram login code or local-worker pairing code. Never paste it into an AI conversation.
4. A repeat `/browser` request re-delivers an unconsumed code while it has sufficient validity remaining, without extending its expiry. Codes and consent requests expire; a consumed code cannot authorize another connection. Incidental copy/paste whitespace is ignored, but wrong codes are not accepted.
5. Enable the connector in Claude. Start with `execution_status` and `execution_options`, then explicitly choose Local, BYO or Cloud. Local requires a paired online agent and per-tab Chrome permission.

Claude account features and limits are controlled by Anthropic. Adding a custom connector by URL is not directory approval. Refer to Anthropic's current documentation rather than assuming all account plans have identical connector limits.

## Login retry fix — 16 November

The previous issuance cap of three new codes per hour could block legitimate retries after the earlier code expired. New-code issuance for an already verified Telegram identity now allows up to 12 per hour and 30 per day, with a ten-second issuance cooldown. Independent delivery throttles, HMAC verification, global anti-abuse limits, single-use codes, code expiry, per-form attempt limits and PKCE remain enforced. Re-delivery of an existing code does not consume another new-code allowance.

A rate-limit rejection is not evidence of an incorrect user password. The bot never requests a password for Telegram, the computer, or Claude.

## Actual verification scope

The existing 19-check OAuth suite and isolated tests for exact callbacks, malicious redirect variants, PKCE, refresh, token replay, tenant isolation, stable code re-delivery, expiry and quota boundaries passed.

A public HTTPS protocol probe verified registration, consent, token exchange, MCP initialization, tools/list, a read-only execution_status call, refresh rotation and rejection of untrusted origins. The real Claude app was not used in that probe.

At **2026-11-16 09:04:21 UTC**, a separate test used the deployed Node bot-code issuer and a real headless Chromium browser to verify:

- Stable code re-delivery through the actual signed internal bot adapter.
- Opening the Telegram link in a separate tab without replacing the authorization form; the Telegram destination itself was simulated, not logged into.
- Rejection of an incorrect code while retaining a retryable form.
- Acceptance of the issued code with incidental whitespace and a browser-enforced CSP redirect to Claude's documented callback address.
- PKCE exchange and a read-only MCP call scoped to the synthetic test account.
- Rejection of replayed authorization codes.

The callback destination was intercepted to avoid sending a synthetic flow to a real Claude account. No real Telegram message delivery, real Claude UI sign-in, Claude model request, purchase, or automated website action is claimed. Synthetic account and authorization records were removed; existing users were not modified. **The user's final Claude connection still needs a real UI acceptance check.**

## Account and security boundaries

Only exact approved ChatGPT and Claude callbacks are accepted. Claude callbacks are `https://claude.ai/api/mcp/auth_callback` and `https://claude.com/api/mcp/auth_callback`. Both request-validation layers retain exact allowed-origin checks. Consent labels derive from the registered callback, not arbitrary client-supplied HTML.

Workers and profiles belong to the authenticated Browser Core account. Using another AI client does not grant access to another account's devices. A new self-service account does not silently migrate an old private-pilot `owner` account. No profile, cookie or token copying is performed.

## Trial versus paid use

Current technical-beta use has no charges. This is **not a promise of permanently free or unlimited Local/BYO**. Ongoing use is intended to have published paid plans; the user must see the terms and explicitly purchase. Website trial wording has been aligned across ten languages. No payments, automatic subscriptions or new usage charges were enabled by these fixes.

Windows 0.8.0 remains a separate-Chromium preview, not an existing-Windows-Chrome integration or self-contained installer.

## Official references

- https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- https://claude.com/docs/connectors/building/authentication
- https://core.telegram.org/bots/api#copytextbutton
- https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging
