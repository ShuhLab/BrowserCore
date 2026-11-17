# Coordinated release checklist

The hosted service, installers, extension, website, plugin instructions and registry have separate versions. Their compatibility and distribution references must agree; identical version strings are not required.

1. Audit current runtime versions and source/artifact hashes. Do not promote an experimental higher-numbered archive without its own approval and tests.
2. Build Mac/Linux/Windows packages from an explicit reviewed file allowlist. Exclude secrets, user state, private environment files and experimental credential/media modules.
3. Extract the actual archives and test imports and browser smoke behavior. Confirm the Mac-bundled extension equals the extension-only ZIP byte for byte.
4. Publish immutable versioned files and SHA-256 companions to both hosted download paths. Re-download each over HTTPS and verify the digest.
5. Update RELEASE.json, RELEASE_SHA256.txt, all ten landing pages, docs, Linux install-script URL and embedded digest. Preserve previous versioned downloads for rollback.
6. Update source generators too, so rebuilding the website does not restore old links. Do not overwrite unrelated legal, billing or project pages.
7. Update README, getting-started, Claude and Windows docs, plugin skills and server.json. Keep old release notes explicitly historical; do not rewrite past evidence as a new test.
8. Run Windows CI against the new exact ZIP and verify its result. Run release-consistency CI against public downloads, all ten pages and the bundled extension.
9. Publish registry metadata through its OIDC workflow and verify the resulting registry version/status. A source commit alone is not a successful registry publication.
10. Record unfinished gates honestly. This release does not enable checkout, secret transfer, new browser permissions, desktop signing or automatically restart a user's worker.

The backend remains proprietary. Public repository updates include documentation, release metadata and QA workflows only.
