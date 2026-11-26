# Mac 0.7.29 RC2 installer preflight — unreleased (26 November 2026)

Browser Core connects Chrome tabs explicitly authorized by their owner to ChatGPT or Claude to perform actions on websites; it is not a separate AI or a replacement browser. When updating Browser Core on a Mac, a failed dependency or browser check should not switch the active installation to an unready candidate.

Local staging branch `consolidated-0729-rc2-preflight`, commit `1aa94149fb3e6a9a78531d1bbaf953d89c26f661`, parent `d98ea57`. Existing shared runtime requirements and pip consistency are checked without installing dependencies or downloading browser binaries. Candidate platform and isolated local browser smoke checks run before switching the current symlink; an incompatible runtime blocks activation and may require separately approved repair. Fresh installation still provisions dependencies before activation.

Verification on Linux: five new unittest methods, 14 synthetic shell scenarios (including failure injections); 115 Python tests, 66 JS tests, including 27 real isolated Chromium fixture checks in Python discovery. The new tests use fake dependency and browser commands and real temporary symlink operations. Unsigned Mac archive SHA256 `f2cc20b4b8014b6ba638bef43c703f96b89d0136ed30ca771a5d48d05c7e2d48`, held in private staging. RC1 untouched.

**Not a full rollback solution.** Native messaging registration, pairing, launchd and live health failures after activation still require transactional recovery. Concurrent installer/updater coordination and actual Mac compatibility remain unverified. Do not install on the owner's live account or publish this candidate. No new public capability or permission. Latest attended preview remains 0.7.28, signed automatic-update channel 0.7.27.

FAQ: If the candidate checks fail, the simulated pre-activation path leaves the old release selected; do not interpret this as proven live Mac recovery. An existing incompatible runtime is deliberately not modified. No user tabs, credentials or files were accessed.


## Activation consent follow-up (26 November 2026, private staging)
Local branch `consolidated-0729-rc2-activation`, commit `f23a9a1cb742a29a912b51dc043c9adc563f84ea`, parent `1aa9414`. The previous installer asked about deferral after changing the active pointer and native assets. The new gate asks before these changes; cancellation, unknown output and dialog failure defer activation. Health check failure after an approved restart exits 9 instead of showing the final success dialog. Five new unittest methods cover five deferral variants and four health outcomes. 120 Python tests and seven JS suites pass (27 isolated Chromium cases included); the first run had missing archive fixtures, resolved without relaxing tests. No new archive. Full rollback after activation, concurrent installer/updater coordination, same-version artifact identity and real Mac acceptance remain blocked. No production change or new public capability.

FAQ: Does Later activate the new build? In this staging test, no. Does a successful launchd call prove connection? No; a fresh versioned heartbeat is required. This is not yet an available release.
