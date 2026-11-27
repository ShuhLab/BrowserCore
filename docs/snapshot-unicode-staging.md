# Unicode-safe page summary — isolated staging only

Browser Core connects Chrome tabs you authorize to ChatGPT or Claude to help with tasks on websites. When a long page summary ends in the middle of an emoji, the local connection can fail to encode the result. We reproduced this with a synthetic Chromium page and the actual Python native-message encoder.

The source-only correction marks repaired descriptive text with `unicode_repaired: true`, substitutes U+FFFD for malformed UTF-16 units, and preserves valid characters and action references. A repaired or truncated summary is not exact source data: verify the original page before copying an identifier. Exact extracted values and draft writes are not changed. No automatic submission or extra permissions.

Server-local staging branch `staging/rc2-snapshot-unicode-20261127`, commit `9b159124c1d419348c508f2f002996889bd89f2a`, based on `1467926c44fbaee875cf5debcaf2af2edf9d66fd`. 140 Python tests (including new Chromium/native-encoder round-trip), seven Node test files pass; source inventory updated. No new archive, signing, installed Mac testing or full native socket acceptance. Grant titles and other exact-data paths require separate review. Not available in production or the current private RC2 archive.

External technical report: [Playwright MCP #1410](https://github.com/microsoft/playwright-mcp/issues/1410). This is a reliability fix, not a paid module or a claim about competitor versions.
