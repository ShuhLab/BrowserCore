# Browser Core in Claude

Use the same remote OAuth/MCP endpoint as other compatible clients:

```text
https://m2g.pro/browser-core/mcp
```

**Verified scope:** server-side OAuth/MCP checks passed; the project owner reported successful real Claude connection and subsequent access to the linked Mac worker. This is not Anthropic directory approval, a claim about every Claude plan or a guarantee of every browser operation.

## Account and devices

Sign in using the same verified Telegram identity used for Browser Core elsewhere. Access is account-scoped, not a separate device registration for each AI client. An empty worker list must not be fixed by merging arbitrary accounts, revealing another user's tabs or creating repeated workers. Check the signed-in identity, paired device, online state and per-tab permission.

No Skills entry is required for a custom MCP connector to expose its tools. Refresh tool discovery through the client's supported connector controls when its cached schema is stale; do not invent tool fields.

## Current components

Server 0.8.4-beta; Mac/Linux agent 0.7.14-beta; extension 0.7.14; Windows standalone 0.8.1-beta. [Current packages and checksums](../RELEASE.json). Existing Mac agent 0.7.12-beta is compatible with the latest extension.

The extension displays connected tabs only, including paused tabs. Per-tab text-volume estimates are not actual Claude model token usage or cost.

## Authorized sends and reliable results

Server 0.8.3 and later use `confirm_submission=true` as the default for ordinary task-authorized actions. Clients missing this optional parameter use the server default. A user's draft-only instruction must still be respected. Do not repeatedly ask permission for each ordinary action already within the requested workflow, or tell the user a physical click is mandatory because an optional field was omitted.

Use one operation ID per deliberate operation. A previously rejected operation cannot be repurposed with new parameters. Never retry a send whose outcome is uncertain; inspect the actual conversation/form state first. A changed field or button state is not proof of server delivery.

Protect passwords, tokens and raw chat history from logs and model output. The current release does not include the experimental secret-transfer channel. Paid access and billing remain disabled.
