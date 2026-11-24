# Learner profile persistence and session automation

## Goal and consent
After a learner opts in once, handle routine progress updates without asking them to maintain files after every practice when the platform permits. Explain before consent that records may include learning preferences, simulated-case summaries, formative performance observations, exposure, safety events, and goals; say which platform workspace will hold them. Offer platform-private storage, a private Google Drive folder, an accessible local folder, or no persistent tracking. Do not store records before opt-in. The platform's own data, retention, and sharing controls still apply.

Suggested Drive consent: “Would you like me to keep your practice profile in your private Google Drive? With your permission, I’ll look for this simulator’s marked folder and create it with your profile and session log if it isn’t there. I’ll store learning progress only, never real patient information. You can ask me to review, correct, export, or delete it.”

## First use
1. Read `docs/PLATFORM_ADAPTERS.md` and verify the chosen surface has private learner-scoped read access, write access, persistence across chats, and learner control. A generated attachment or chat response alone is not write access to the canonical profile.
2. Check the already selected private store for an existing profile. If found, read it and skip onboarding. If absent, run `docs/ONBOARDING.md` once, including the explicit tracking opt-in and storage choice.
3. For opted-in Google Drive storage, search My Drive for the exact `CES_STORE_MANIFEST` marker. If one valid store is found, read its `PROFILE_INDEX` and reuse the active learner's profile. If no marker is found, inspect the exact `Clinical Encounter Simulator - Profile Store` folder name; reuse only an empty folder or one with the recognized simulator layout. Add the marker and index when adopting an empty/recognized dedicated folder. Never repurpose a folder with unrelated contents. If no suitable folder exists, create the dedicated store and initial files. If results are ambiguous, ask the learner to select a folder or profile instead of guessing. Follow any platform-required confirmations.
4. For a new Drive store, create a root manifest and profile index, a `profiles/default/` profile with `LEARNER_PROFILE`, `PROGRESS_REVIEW`, and `SESSIONS_INDEX`, and a `sessions/` folder. Create these as Google Docs/Sheets using the templates. For a local writable workspace, use the equivalent Markdown layout. Never put learner data beside `SKILL.md` or in the public registry.
5. Verify the manifest and initialized profile/index by reading them back. Report the location and scope in plain language only after verification.

If the workspace is shared and identity cannot be resolved from its supported account/project boundary, ask which non-identifying profile to use before reading or writing. Never infer learner identity from clinical details, merge profiles, or expose another learner's records.

## Each practice
### Before the case
- Load the active profile and recent records from the private learner scope. Use the saved preferences; ask only for a session override or missing choice.
- If records are absent, stale, inaccessible, or ambiguous, state that briefly. Do not invent past cases or progress. The learner may continue with defaults or provide a portable profile.

### After the debrief
- Complete the reliability audit and debrief first. Store a completed case only after dependable review. Mark an abandoned case incomplete; exclude unreliable or contradicted opportunities from competence conclusions while preserving an appropriate audit note.
- Create one session record and add its ID to the active learner's profile-level `SESSIONS_INDEX.md`. Suggested stable ID: UTC start timestamp in `YYYYMMDD-HHmmssZ` format plus a short case slug; check the index for collision and add a suffix if needed. If reliable UTC time is unavailable, use the platform date/time with its timezone clearly labeled. Do not use patient details in IDs.
- Before writing, check whether that session ID is already indexed. Update the existing record on a retry; do not append a duplicate. Reconcile cumulative totals from the index/records rather than blindly incrementing.
- Update exposure separately from performance evidence, hint support, safety events, and next goals. Use `templates/SESSION_RECORD.md`, `templates/LEARNER_PROFILE.md`, and `templates/PROGRESS_REVIEW.md`. Unobserved domains are N/A. If no validated weighted rubric was available, use evidence-based narrative feedback instead of invented numeric scores.
- Save with the platform's supported write tool. Some integrations require user approval for each action; follow the platform's confirmation flow and do not promise zero-click automation if those prompts remain. Re-open/read the saved record and index after writing when possible. Confirm only updates that actually succeeded; report any failed or partial write.

## Storage and fallback
- Keep records in private user-scoped project/workspace storage or the learner's selected private Drive folder, separate from the installed skill and shared source files. Do not change sharing permissions, publish, sync to an unselected service, or add integrations as part of routine updates.
- If any capability needed for full tracking is absent or unclear, treat the platform as read-only. Do not claim the record was saved. Continue the simulation, then provide a compact updated profile/session record that the learner can save or bring to the next chat.
- Ask for platform-specific authorization only if that platform requires it. After the learner opts in to this private routine, do not ask again for each normal update.
- Do not imply that ClawHub, the model, or the skill hosts user data or synchronizes profiles across platforms.

## Privacy and user control
Keep only learning settings, simulated case IDs, educational performance observations, exposure, feedback, and goals needed for practice. Do not store real-patient information, legal names, contact details, or workplace identifiers. Treat credentials as unverified self-description. Tell the learner how to review, correct, export, or delete records through the host platform. Honor those requests when the available tools permit; otherwise provide the current record and clear platform-specific steps. Do not invent a retention period: explain that platform retention and deletion controls govern stored files.

