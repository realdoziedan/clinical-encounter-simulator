# Clinical Encounter Simulator skill package
Version 1.4.1 · Built from the preserved Library master.

## Start
Load `SKILL.md` and its references into a capable assistant. Complete brief onboarding once. Persistent progress tracking is opt-in and automatic only when the host can privately read, write, and retain learner records. The learner may use a private Google Drive folder as a shared source of truth when each connected AI platform has verified read/write access. See `docs/PLATFORM_ADAPTERS.md` for surface-specific limits. This is a fictional educational simulator, not clinical decision support.

## Contents
- `SKILL.md`: portable central instructions and routing.
- `source-masters/`: untouched original Library master.
- `references/`: selection, encounter, scoring, coaching, safety.
- `references/PROFILE_PERSISTENCE.md`: one-time setup and automated learner record workflow with platform-specific fallbacks.
- `docs/`: user materials, portability, QA, test and maintenance.
- `docs/PLATFORM_ADAPTERS.md`: platform capability checks, private storage layout, and setup guidance.
- `templates/`: portable learner profile and training records, plus Drive store manifest and profile index.
- `tests/`: manual acceptance fixtures and executable integrity check.

## Build principles carried forward
The source’s six-stage encounter, first-contact onboarding, selected-vs-generated case separation, adaptive difficulty, exposure balancing, safety audit, formative scoring, coaching mode, learner profile, and first-case diversification are represented in the package. The untouched master remains authoritative where the concise portable core omits detail.

