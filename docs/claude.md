# Browser Core in Claude

Use custom MCP connector `https://m2g.pro/browser-core/mcp`, signing into the **same verified Browser Core account** as ChatGPT. The owner confirmed a real Claude connection and access to the paired Mac worker. This is not an Anthropic listing or a guarantee for all accounts.

The latest server is 0.8.4-beta; Mac/Linux 0.7.19-beta; extension 0.7.19; Windows standalone 0.8.5-beta.

Only individually connected Chrome tabs are available. A paused tab remains in the user's extension list, not available for autonomous actions while paused. Do not create a second worker or merge unrelated identities if Claude initially sees an empty worker list.

When a task authorizes ordinary form submissions or messages, there is no one-message cap or need for a physical click per message. Draft-only user instructions must still be obeyed. Give each deliberate operation a unique operation_id, check the recipient, and verify outcomes rather than retrying uncertain sends.

The Chrome plugin's approximate text-equivalent metric is not Claude's actual model token consumption. Signed Mac/Linux agent auto-update requires a one-time 0.7.19-beta bootstrap. Windows auto-update and browser-to-server key transfer remain unsupported.
