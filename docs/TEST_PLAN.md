# Test plan
Run `python tests/validate_package.py` or `node tests/validate_package.mjs` from package root. Both check the required artifacts and relative Markdown links, not clinical quality. Keep their required-file lists in sync when adding package files.

Execute all manual scenarios in `tests/MANUAL_FIXTURES.md`; record platform/model, date, evidence, issues and reviewer. Re-run after edits to onboarding, case selection, safety, scoring, workflow or templates. A qualified clinical educator should review representative cases against current local guidance before formal use. Release review also compares source-master hash and checks ZIP inventory.

For profile automation, specifically verify opt-in before any write; first-use initialization; automatic profile loading on a later session; one unique session record per completed case; cumulative progress reconciliation without duplicates; strict learner separation in a shared workspace; review/export/delete instructions; and the no-write fallback. Confirm that no real patient identifiers are saved and that the assistant only reports a save after verifying it. Test each platform adapter separately; feature support on one platform does not establish support on another.

For the Google Drive adapter, connect each platform independently to the same private test folder, verify read and write permissions with a harmless test document, perform a round-trip update, and confirm it can be read back from another platform. Test automatic marked-folder discovery, reuse, creation on no match, unrelated-name collision handling, confirmation prompts, concurrent edit conflict, duplicate session IDs, revoked access, and ChatGPT's Project-source behavior. Do not run this test against a learner's real profile folder.

For public-release review, record the publisher's redistribution-rights confirmation and content review for the preserved source master and all included materials. The integrity checker cannot determine ownership, licensing, privacy, or suitability for public release.

