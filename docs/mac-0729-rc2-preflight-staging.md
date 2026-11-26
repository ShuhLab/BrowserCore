# Mac 0.7.29 RC2 installer preflight — unreleased (26 November 2026)

Browser Core connects Chrome tabs explicitly authorized by their owner to ChatGPT or Claude to perform actions on websites; it is not a separate AI or a replacement browser. When updating Browser Core on a Mac, a failed dependency or browser check should not switch the active installation to an unready candidate.

Local staging branch `consolidated-0729-rc2-preflight`, commit `1aa94149fb3e6a9a78531d1bbaf953d89c26f661`, parent `d98ea57`. Existing shared runtime requirements and pip consistency are checked without installing dependencies or downloading browser binaries. Candidate platform and isolated local browser smoke checks run before switching the current symlink; an incompatible runtime blocks activation and may require separately approved repair. Fresh installation still provisions dependencies before activation.

Verification on Linux: five new unittest methods, 14 synthetic shell scenarios (including failure injections); 115 Python tests, 66 JS tests, including 27 real isolated Chromium fixture checks in Python discovery. The new tests use fake dependency and browser commands and real temporary symlink operations. Unsigned Mac archive SHA256 `f2cc20b4b8014b6ba638bef43c703f96b89d0136ed30ca771a5d48d05c7e2d48`, held in private staging. RC1 untouched.

**Not a full rollback solution.** Native messaging registration, pairing, launchd and live health failures after activation still require transactional recovery. Concurrent installer/updater coordination and actual Mac compatibility remain unverified. Do not install on the owner's live account or publish this candidate. No new public capability or permission. Latest attended preview remains 0.7.28, signed automatic-update channel 0.7.27.

FAQ: If the candidate checks fail, the simulated pre-activation path leaves the old release selected; do not interpret this as proven live Mac recovery. An existing incompatible runtime is deliberately not modified. No user tabs, credentials or files were accessed.


## Activation consent follow-up (26 November 2026, private staging)
Local branch `consolidated-0729-rc2-activation`, commit `f23a9a1cb742a29a912b51dc043c9adc563f84ea`, parent `1aa9414`. The previous installer asked about deferral after changing the active pointer and native assets. The new gate asks before these changes; cancellation, unknown output and dialog failure defer activation. Health check failure after an approved restart exits 9 instead of showing the final success dialog. Five new unittest methods cover five deferral variants and four health outcomes. 120 Python tests and seven JS suites pass (27 isolated Chromium cases included); the first run had missing archive fixtures, resolved without relaxing tests. No new archive. Full rollback after activation, concurrent installer/updater coordination, same-version artifact identity and real Mac acceptance remain blocked. No production change or new public capability.

FAQ: Does Later activate the new build? In this staging test, no. Does a successful launchd call prove connection? No; a fresh versioned heartbeat is required. This is not yet an available release.


## Release identity follow-up (26 November 2026, private staging)

**Unreleased Mac 0.7.29 RC2 release identity (26 November 2026):** Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude for website actions. The private staging installer rejects same-version directories with different or missing source/assets, unexpected files or symlinks before activation; it does not overwrite the previous code. 124 Python tests and seven JavaScript suites passed in Linux fixtures. No new archive, no real Mac acceptance; full post-activation rollback and installer/updater coordination remain pending. Not released.

Local commit `a8157dc1bcb305f7bfbf30eaa32601210dca350f`, parent `f23a9a1`. Four new test methods cover eight synthetic scenarios: fresh install, identical reuse, generated Python cache, modified or missing source, extra source, file symlink and release-directory symlink. A mismatch stops before user consent, active pointer change or registration; the existing directory is left untouched. Example: two different 0.7.29 candidate payloads must not be treated as interchangeable. Full rollback and concurrent install safety are not established. No package was rebuilt.


## Consolidated private RC2 package acceptance (26 November 2026)

Browser Core connects user-authorized Chrome tabs to ChatGPT or Claude for website actions. Private Mac RC2 packaging now rejects mismatched payload inventories before writing an archive. A consolidated unsigned candidate has passed exact payload verification and 139 Python tests, seven JS suites and 37 isolated Chromium scenarios; it is not a public download or signed update. Real Mac acceptance and complete installer rollback remain open. Do not install it on an active profile.

Local staging commit `b5cfffd0b22ed8357a72d6c036819ce075ece449` on `staging/rc2-package-acceptance-20261126`, based on `b58a284`. Five stale manifest entries were corrected; five new regression tests check exact content, missing rows, symlinks, wrong release and preservation of existing output on rejection. Actual unsigned archive: 526525 bytes, SHA256 `300445c2d2416f4b30e591ec453feedefe12f87bfaa854ccde8edbb96c169c0f`; 40 payload files checked against source and the updater validator, two identical builds. Simulated signatures used ephemeral keys only. No production access, new permissions, file-transfer capability or publication. The older archive references above are historical. This is an internal build-process correction, not another user-facing operation. FAQ: can I install this version now? No: the signed channel and attended preview are unchanged, and the same version number does not make different payloads interchangeable.
