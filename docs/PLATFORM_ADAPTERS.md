# Platform setup and storage adapters

This page prevents the skill from promising one platform's persistence behavior on another. Platform interfaces and plan limits change; last reviewed 2026-11-24. Check the linked official documentation and the actual tools available in the learner's session before claiming a capability.

## Capability check

Before offering automatic records, check all of these for the current account/workspace:

1. **Read:** can the assistant retrieve the saved learner profile in a later session?
2. **Write:** can the assistant create and update learner-owned records, not only produce a downloadable answer?
3. **Persistence:** do changes survive the chat and remain available to the same learner in later sessions?
4. **Scope:** is storage private to the learner or explicitly isolated by a private project/workspace?
5. **Control:** can the learner inspect, correct, export, and delete records?

Only promise full automatic tracking when all five are established. If any item is absent or unclear, treat the surface as read-only and use the portable handoff in `../references/PROFILE_PERSISTENCE.md`.

## Adapter guide

| Platform surface | Suitable role | Do not assume |
|---|---|---|
| **OpenClaw skill with a private writable agent workspace** | Best fit for the full file workflow. Load companion references from the skill directory; write learner records in a separate private workspace folder, never inside the installed skill. Confirm the agent actually has file read/write tools and that its workspace persists. | ClawHub installation alone does not provide profile storage or grant file tools. A workspace shared by agents is not automatically a per-user store. |
| **Google Drive folder (shared source of truth)** | Recommended cross-platform option when each AI account is separately connected to the same private Drive folder and has verified access to create/read/update the required Docs, Sheets, and files. Use the canonical layout below. | “Sync” is not identical across platforms. Some actions need confirmation; product availability and write scopes vary. A Drive link added as a ChatGPT Project source is not pre-synced for retrieval. Never claim a saved change until read-back verifies it. |
| **ChatGPT Project** | Project instructions, files, and project chat context can provide continuity. A connected Google Drive app may search/read and, where enabled, update source files. Use the Drive connector directly in project chats for the canonical records. | Project memory is not a complete, auditable session ledger. Google Drive app availability depends on plan/workspace permissions. Drive links added as project sources do not sync in advance. Do not assume attached files can be rewritten. |
| **Claude Project** | Project instructions and knowledge files provide reusable context. Claude's Google Workspace connectors can read Drive and support creating/saving or editing Docs/Sheets/Slides in supported surfaces. Use the connector to update the same canonical Drive records. | Project knowledge read access alone is not write access. Connector actions may request approval; editing shared files may require explicit review/confirmation. |
| **Gemini Gem** | Gem instructions and knowledge files provide a reusable setup. Connected Google Workspace features can search/read Drive and write/edit Docs or manage files where enabled. Use the same canonical Drive records. | A Gem or attached knowledge source is not itself a profile-writing system. Workspace/account eligibility and confirmation prompts apply. Google's Gems-to-skills rollout may change the Gem setup flow. |
| **Other assistants** | Load the Markdown core and any linked references; use the platform's supported private project or workspace if it passes the capability check. | Markdown compatibility does not guarantee skill discovery, write access, memory, or cross-platform profile sync. |

## Recommended shared Drive layout

At onboarding, offer one-time storage choices: platform-private storage, a private Google Drive folder, local files if the agent can access them, or no persistent tracking. For Drive, tell the learner that after they opt in, the assistant will search their connected My Drive for this simulator's marked store and reuse it; if none exists, it will create the store and initialize one profile. This consent covers searching and creating only the dedicated simulator folder and its profile records. Each platform still requires its own Google account connection and may require action confirmations. Do not request credentials or OAuth codes in chat. If the connector cannot search but can open/write by direct link, ask once for the folder link; if it cannot create/write, use the portable fallback.

### Search, reuse, or create

1. Search the connected account's My Drive for a `CES_STORE_MANIFEST` file with the expected schema marker. This marker distinguishes the simulator store from unrelated folders with similar names.
2. If exactly one valid manifest exists, read it and its profile index, then reuse the matching learner profile. If one store contains a single profile, use it without asking the learner to choose. If there are several profiles, ask which profile they own/use.
3. If no valid manifest exists, search for the exact folder `Clinical Encounter Simulator - Profile Store`. Reuse it only if it is empty or already has the simulator's expected `profiles/` layout. Do not adopt a folder with unrelated contents.
4. If no suitable folder exists, create `My Drive/Clinical Encounter Simulator - Profile Store/`, then the `profiles/default/` and `profiles/default/sessions/` folders. Add the manifest, profile-index Sheet, profile Doc, progress Doc, and session-index Sheet from the templates. Use a non-identifying profile key; create one default profile unless the learner explicitly says the Drive folder is shared by multiple learners.
5. If multiple candidate stores exist, a candidate has unexpected contents, or the folder's sharing status cannot be checked and the learner needs private storage, stop and ask a short clarifying question. Do not guess or change sharing permissions.
6. Read back the manifest, profile index, and initialized profile/session index. Confirm the setup only after successful verification.

The one-time opt-in must state that the assistant will search the connected Drive and create the dedicated store if needed. Platform-mandated OAuth or per-action confirmations still apply; never bypass them. Once setup succeeds, update files after completed practice without another setup question, subject to any platform-required approval prompt.

Use Google Docs/Sheets as the common editable formats rather than assuming every connector can update `.md` files:

```text
My Drive/Clinical Encounter Simulator - Profile Store/
  CES_STORE_MANIFEST (Google Doc)
  PROFILE_INDEX (Google Sheet)
  profiles/<profile-key>/
    LEARNER_PROFILE (Google Doc)
    PROGRESS_REVIEW (Google Doc)
    SESSIONS_INDEX (Google Sheet)
    sessions/
      <session-id> (Google Doc)
```

Keep the folder private to the learner. If multiple people share it, use separate profile subfolders and resolve the active profile before any read or write. Include a `last_updated` timestamp and schema version in the profile and index. For concurrent sessions, read the latest revision just before writing; if it changed since it was loaded, re-read and merge or pause for the learner rather than silently overwriting another update. Session IDs remain the deduplication key.

In ChatGPT, do not rely on pre-sync from a Drive folder link added as a Project source; use the connected Drive app in the conversation to retrieve the current record. If Drive is unavailable for the account, use a private writable platform workspace or the portable fallback.

## Record locations

For a writable OpenClaw-style workspace, use this layout outside the installed skill directory:

```text
<private-agent-workspace>/clinical-encounter-simulator/
  STORE_MANIFEST.md
  PROFILE_INDEX.md
  profiles/<profile-key>/
    LEARNER_PROFILE.md
    PROGRESS_REVIEW.md
    SESSIONS_INDEX.md
    sessions/<session-id>.md
```

Use the platform's equivalent private project or workspace scope elsewhere. A profile key should be a short, non-identifying label. If the host identity already isolates one learner, use a neutral key such as `default`; do not ask for a second label unnecessarily.

## Official references

- [OpenClaw skills and companion references](https://docs.openclaw.ai/tools/skills)
- [ChatGPT Projects](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), [Google Drive app and setup](https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt), and [Drive access controls](https://help.openai.com/en/articles/20001608-managing-google-drive-access-in-chatgpt)
- [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) and [Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Gemini Gems](https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DDesktop) and [Gemini tasks and Workspace actions](https://support.google.com/gemini/answer/17094507?co=GENIE.Platform%3DDesktop&hl=en)

These links describe platform features, not guarantees that the simulator can write user records. Re-check before release and label any observed capability with the account, plan, date, and test evidence.
