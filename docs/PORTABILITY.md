# Platform portability

The simulation core is Markdown, but platform support for discovering companion files, retaining history, and writing learner records differs. Read `PLATFORM_ADAPTERS.md` before claiming persistent automation.

Progress tracking is opt-in. After opt-in, initialize and update records automatically only if the current platform has verified private read/write storage that persists across chats. A project or Gem with attached knowledge may provide reusable reference context without providing writeback. If support is missing or unclear, use the portable profile handoff and state the limit. Profiles do not sync across platforms.

Keep profiles separate from the published skill and from shared instructions. The optional integrity checker is for package maintainers, not required to run cases. For guidance verification, use a reliable current source when available; otherwise label time-sensitive content unverified and omit unsafe specifics.
