# Unreleased P0: DOM edit guard — 25 November 2026

Staging branch `p0-dom-edit-0733`, local commit `93089e8`, based on `p0-portal-replay-0732`. **Not in public 0.7.28 or the signed 0.7.27 channel.**

## Problem and demand

A user reported protected input values being destroyed while a competing agent reported success ([agent-browser #1920, 18 September 2026](https://github.com/vercel-labs/agent-browser/issues/1920)). This is related to [#2055](https://github.com/vercel-labs/agent-browser/issues/2055), already tracked. Playwright locator.fill is an alternative for sites with no suitable API. For developers, operators and businesses transferring data, safe refusal is a baseline reliability requirement, not a separately priced feature. No verified willingness to pay.

## Reproduction and correction

Seven adverse cases reproduced unintended mutations in our own isolated Chromium fixture: readonly on focus, readonly/disabled during beforeinput, maxlength overflow (replace/append), invalid number clearing the old value, focus stolen during beforeinput. Recheck editability and inherited disabled state, actual type, maxlength, detached native control sanitization and focus before writing. Refuse when a beforeinput handler changes the existing value. No writes to the live target or input/change events in the nine adverse fixture cases after correction.

## Verification and limitations

10/10 new isolated Chromium cases, 69 existing Python tests (including four Chromium context checks), 60 JS cases passed. No real customer data or live Mac/native extension end-to-end test. Website focus/beforeinput handlers may themselves have effects; the change does not guarantee preventing website autosave or server writes. Unsupported controls need an appropriate supported action or manual intervention. No new permission, API, public download or signed update. Native acceptance and packaging pending. No new user-facing feature/video.
