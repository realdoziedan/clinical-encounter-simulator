# Versioning and maintenance
Use semantic versions: major for incompatible behavior/structure; minor for backward-compatible capability; patch for corrections.

For changes, log rationale, files, clinical/safety impact, reviewer and date. Review clinical content with a qualified educator using current local guidance. Update manual fixtures and paths, run the integrity checker, manually review affected flows, compare preserved source hash, inspect ZIP listing, and record release. Before any public release, confirm the right to redistribute every included source file and inspect the preserved master and package for private, identifying, confidential, or otherwise unintended content. Source preservation does not itself grant redistribution rights.

## 1.4.1 — 2026-11-24
Aligned the Python and Node integrity checker file inventories and documented both commands, preventing the Python check from overlooking the newer platform and Drive-store files. Made the persistent-record opt-in condition explicit in the main skill workflow so it cannot be read as permission to track users who declined.

## 1.4.0 — 2026-11-24
Added seamless Drive bootstrap: after explicit opt-in, search for a marked simulator store, reuse a unique valid store, or create the dedicated folder and initialize the manifest, profile index, learner profile, progress review, and session index. Added collision/ambiguity handling and setup verification requirements.

## 1.3.0 — 2026-11-24
Added Google Drive as a shared-storage adapter across ChatGPT, Claude, and Gemini when each platform is separately authorized and read/write actions are verified. Standardized shared records on Google Docs and Sheets; documented confirmation prompts, ChatGPT Project-source sync limits, concurrent-edit handling, and cross-platform round-trip tests.

## 1.2.0 — 2026-11-24
Made learner tracking explicitly opt-in; added platform adapter guidance and capability checks; defined a private workspace layout and duplicate-resistant session index/IDs; softened first-use guide burden; aligned user guide with automatic-save behavior; added privacy/control wording; clarified narrative-only scoring when numeric anchors are unavailable; added a safe fallback for unverifiable time-sensitive clinical guidance; documented a public-release content/rights review gate.

## 1.1.0 — 2026-11-24
Added one-time learner setup and automated per-user profile/session/progress persistence when the host platform provides private persistent storage and write tools. Added explicit boundaries for shared workspaces, duplicate-safe session updates, verification, privacy, and portable fallback when file writes are unavailable. The package does not provide cross-platform synchronization or hosted storage.

## 1.0.0 — 2026-11-23
Initial modular package from Library master; untouched source included. Adapted the core into portable files while retaining master as full reference.
Review before institutional deployment and at least annually, or after material guideline/platform changes. Label local adaptations with owner and date.

