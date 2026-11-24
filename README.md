# Clinical Encounter Simulator

**Version 1.4.2** · A portable skill for fictional clinical practice, formative assessment, debrief, adaptive coaching, and learner progress tracking.

This is an educational simulator, not clinical decision support. It must not be used to diagnose or manage a real patient.

## Get started

### Fastest: ask an agent to install it

In a coding agent that can access GitHub and install local skills (such as Codex or Claude Code), paste this prompt:

> Install the Clinical Encounter Simulator from https://github.com/realdoziedan/clinical-encounter-simulator for the current user of this agent. Follow the platform's current skill-installation instructions. Keep the package's folder structure and supporting references, install only in the current user's personal skills area, and do not overwrite an existing installation without asking me. Verify that the installed skill can find its referenced files. If this agent cannot install persistent skills, explain the shortest supported upload steps instead. Do not set up learner-data storage unless I separately opt in.

This works only when the agent has the needed repository access, local-file or installation tools, and permission to make the change. A prompt alone cannot install a skill into a separate ChatGPT or Claude account or bypass that platform's controls.

### Install in Claude

Download the [current ZIP package](https://github.com/realdoziedan/clinical-encounter-simulator/raw/refs/heads/main/Clinical-Encounter-Simulator-1.4.2.zip). In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, select the ZIP, and enable the skill. Skills require Code execution and file creation to be enabled; organization settings may also apply. See [Claude's official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Install in ChatGPT

If Skills are available for your ChatGPT plan and workspace, download the [current ZIP package](https://github.com/realdoziedan/clinical-encounter-simulator/raw/refs/heads/main/Clinical-Encounter-Simulator-1.4.2.zip), then open **Plugins → Skills → Create → Upload from your computer**, select the ZIP, and follow any review prompts. Availability and upload permissions depend on the plan and workspace settings. See [OpenAI's official instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### Try it in a single conversation

If you cannot install skills, ask an assistant with access to public GitHub links:

> Use the Clinical Encounter Simulator for this conversation: https://github.com/realdoziedan/clinical-encounter-simulator. Read README.md and SKILL.md, then follow the relevant reference files. Start with the onboarding questions. Keep cases fictional and educational. Do not claim to save a learner profile or progress unless you can actually write it to storage I have chosen. If you cannot access the repository files, tell me and I will upload the ZIP.

A prompt can guide one conversation, but it does not install a persistent skill. Use the platform's skill upload or local agent installation for repeated use.

## Learner profiles and progress

Each learner controls their own profile and training records. Persistent tracking is opt-in. Automatic updates require the AI platform to have verified private read/write access to a learner-selected location. The package does not create a hosted profile service or sync profiles between users. See [`references/PROFILE_PERSISTENCE.md`](references/PROFILE_PERSISTENCE.md) and [`docs/PLATFORM_ADAPTERS.md`](docs/PLATFORM_ADAPTERS.md).

## Package contents

- [`SKILL.md`](SKILL.md): portable instructions and workflow routing.
- [`references/`](references/): case selection, encounter workflow, scoring, coaching, profile persistence, and safety.
- [`docs/`](docs/): onboarding, user guide, platform adapters, portability, testing, and maintenance.
- [`templates/`](templates/): learner profile and progress/session record templates.
- [`tests/`](tests/): manual fixtures and executable package-integrity checks.
- [`source-masters/`](source-masters/): preserved original Library source master.

## Feedback and contributions

- Open a GitHub **Issue** for a bug report, question, or suggested improvement.
- Open a **Pull Request** with a proposed documentation or skill change. For larger changes, open an Issue first so we can agree on the direction.
- Use **Discussions** for broader ideas if that feature is enabled for this repository.

Please do not include real patient information in issues, discussions, or contributions. Clinical teaching changes should be reviewed against current authoritative guidance and by a qualified educator.

## License

Released under the [MIT License](LICENSE). Contributions are accepted under the same license.
