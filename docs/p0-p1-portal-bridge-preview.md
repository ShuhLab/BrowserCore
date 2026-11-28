# Browser Core 0.7.28 — P0 reliability and P1 Portal Bridge (attended preview)

**Private RC2 staging — 28 November 2026:** Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude. Its test snapshot now distinguishes the main page from uninspected embedded forms, without reading those forms or changing permissions. 149 Python tests and 7 Node suites passed in Linux; Mac acceptance and installer rollback remain open. Not released. [Scope and limitations](embedded-frame-scope-staging.md).

**Limit:** A same-document order/account switch at an identical URL can evade document-context checks. Inspect the actual business record and avoid forms that may autosave. The experimental record guard is **not included** in this attended preview. [Staging evidence and limits](p1-portal-context-staging.md).

**Status as of 25 November 2026:** source implemented in a separate staging build, packaged and tested. This is an **attended, unsigned/not-notarized Mac beta**. The current signed auto-update channel still distributes **0.7.27-beta**. This is NOT a general-availability rollout, not yet independently security audited, and no real seller-portal acceptance has been completed.

Downloads with independent SHA-256 check files:

- [Mac OneClick 0.7.28-beta](https://browser.m2g.pro/downloads/BrowserCore-Mac-OneClick-0.7.28-beta.zip)
- [Chrome/Edge/Opera unpacked extension 0.7.28](https://browser.m2g.pro/downloads/BrowserCore-Extension-0.7.28.zip)
- [Linux BYO 0.7.28-beta](https://browser.m2g.pro/downloads/BrowserCore-Linux-BYO-0.7.28-beta.tar.gz)

## P0 — reliable task execution

The existing per-tab command ledger now includes an **operation receipt** endpoint and a sanitized, local-only **action event journal**. It records the action type, bounded status/reason, and a hash of the operation ID, **never page text, screenshot, password, URL query, selector, file contents, or credentials**. It tracks extension reconnect/disconnect counters and offers a bounded diagnostic summary. Parent pause immediately propagates to agent-created children in the native bridge; user takeover blocks the descendants until resumed.

Use `existing_tab_action` on a user-shared tab with `action="operation_receipt"` and `value="<previous operation_id>"`. It returns verified/recorded/unknown state, but never interprets an uncertain browser write as proof of network delivery. **Unknown outcomes must be manually verified; automatic replay is prohibited.** For summary counters, use `action="reliability_status"` on a shared tab.

## P1 — Portal Bridge: one authorized browser session, two separately shared tabs

The first phase handles **bounded, verified text-field transfer to a draft**. It does not publish, submit forms, change listings or automatically upload files. The user must be signed into the source and target websites in their normal Chrome, explicitly share **both** tabs with Browser Core, and provide the intended mapping. Cross-site transport runs inside the owner's local agent. No text values appear in the preview reply or are persisted as plan contents.

1. Preview: call `existing_tab_action` with `tab_handle` pointing to the **destination** tab, `action="portal_preview"`, and `value` containing JSON similar to:
   ```json
   {
     "source_tab_handle": "tab_<source UUID>",
     "fields": [
       {"name": "title", "source_selector": "input[name=title]", "target_selector": "input[name=title]"},
       {"name": "description", "source_selector": "#description", "target_selector": "textarea[name=description]"}
     ]
   }
   ```
   Preview returns only a one-use `plan_id`, field names and character counts, media element counts, and a 10-minute TTL. The plan binds exact source/destination tab handles and sanitized URLs and uses a SHA-256 digest to detect source changes.

2. Fill draft: once the mapping is reviewed, call `existing_tab_action` on the **same destination** with `action="portal_apply"`, `value='{"plan_id":"pb_..."}'` and a **new unique** `operation_id` of at least 12 characters. The local agent rechecks both grants and the source fingerprint, fills each mapped destination editor, and requires verified read-back before proceeding to the next. **No form submission**.

3. Inspect with `action="portal_status"` and the same plan JSON. A plan cannot be reused for a different write. If a field's outcome is uncertain, automation stops and requires manual review.

4. User-selected files: the separate **read-only** `action="portal_file_status"`, with `selector` targeting a visible destination `input[type=file]`, returns file counts, total selected byte size and broad media types. It does **not** read filenames/bytes, click the picker, perform uploads or claim server-side upload success.

Unsupported and intentionally blocked: protected/hidden/password/OTP/API-key fields; arbitrary injected scripts; unshared or paused tabs; source/destination on different local extension connections; HTTP origins; automatic likes, comments, payments, submission, or publication; binary photo/video transfer. For rich category-specific portals and automated uploads, use official APIs/feed imports first and add site adapters after acceptance testing.

## Real acceptance and commercialization gates

Before public availability, validate against two **owned, consenting test accounts** with representative category forms and media, test logout, network failure, CAPTCHA/human takeover, site redesign, refresh, duplicate operation IDs, partial results and recovery. Complete the signed-release and rollback review; do not expand Chrome permissions silently. Payment and quotas for Browser Core are separately gated and are not activated by this preview.

> **Unreleased follow-up, 25 November 2026:** [P0 delegated-tab isolation correction](p0-delegated-tab-isolation-staging.md) is undergoing staging acceptance. It is not part of 0.7.28. Do not treat staged pause/revoke behavior as released.


> **Unreleased P1 safety follow-up:** [document/route context binding](p1-portal-context-staging.md) is tested in staging only. In the current 0.7.28 preview, inspect both actual accounts and re-preview after navigation or reload; do not rely on matching path alone. Do not retry uncertain writes.


**Unreleased P0 native connection isolation (25 November 2026, staging only):** [Connection-bound commands and results](p0-native-port-isolation-staging.md) reject stale messages after reconnect. Mocked tests passed; installed-extension restart and uncertain-outcome reconciliation remain pending. Not in 0.7.28.



**Private RC2 staging correction (27 November 2026):** [Unicode-safe page summary](snapshot-unicode-staging.md) prevents malformed UTF-16 in descriptive snapshot output and flags repaired text. 140 Python tests and seven Node test files passed in isolation. Exact draft values unchanged; included in a later private unsigned RC2 candidate, not the earlier archive, public downloads or production. Mac end-to-end validation pending.

**Private RC2 staging correction (28 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude for website actions. [Bounded snapshot coverage](snapshot-coverage-staging.md) reports text/action-reference/shadow-root limits and labels the rendered DOM scope; a false truncation flag never proves complete records. 141 Python tests and seven Node suites passed. Private unsigned candidate only, not a public release or attended preview; Mac installation and rollback unverified. Exact Portal Bridge transfer is unchanged.

**Private RC2 staging safety correction (28 November 2026):** Browser Core connects authorized Chrome tabs to ChatGPT or Claude for website actions. [Safer target resolution](target-resolution-staging.md) stops an incomplete search before acting. Recheck the intended control and draft values; no change to grant scope or submission permissions. Private unsigned candidate only, not public availability; Mac installation and rollback unverified.
