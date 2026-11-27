#!/usr/bin/env python3
"""Build the Gemini Gem kit: a folder of at most 10 Gemini-supported files
(Gems allow 10 knowledge files and reject script files), zipped with setup
instructions. Source files are copied or grouped unchanged; grouped files keep
each original under a "## File: <path>" heading.

Run from anywhere:  python scripts/build_gemini_kit.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # stable ZIP bytes, so unchanged sources don't trigger a commit


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def bundle(paths):
    return "\n\n---\n\n".join(f"## File: {p}\n\n{read(p)}" for p in paths)


def full_instructions(setup_and_map):
    """Setup steps and file map, followed by SKILL.md unchanged. Gems apply the
    Instructions box on every turn but only look knowledge files up as needed, so
    the core skill rules go in Instructions as well as in Knowledge."""
    return (setup_and_map.rstrip("\n")
            + "\n\nThe complete SKILL.md follows. Follow it as your core instructions.\n\n"
            + read("SKILL.md"))


def build(kit_name, layout, instructions):
    """layout: {kit path: source path (copy) or list of source paths (group)}"""
    instructions = full_instructions(instructions)
    assert read("SKILL.md") in instructions
    assert len(layout) <= 10, "Gemini Gems accept at most 10 knowledge files"
    files = {}
    for dest, src in layout.items():
        files[f"{kit_name}/{dest}"] = bundle(src) if isinstance(src, list) else read(src)
    blob = "".join(files.values())
    sources = [s for v in layout.values() for s in (v if isinstance(v, list) else [v])]
    for s in sources:
        assert read(s) in blob, f"{s} not included verbatim"
    DIST.mkdir(exist_ok=True)
    (DIST / f"{kit_name}-INSTRUCTIONS.txt").write_text(instructions, encoding="utf-8", newline="\n")
    out = DIST / f"{kit_name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, text in [("GEM-INSTRUCTIONS.txt", instructions), *sorted(files.items())]:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, text.encode("utf-8"))
    print(f"Wrote {out.relative_to(ROOT)} ({len(files)} knowledge files, {out.stat().st_size:,} bytes)")


INSTRUCTIONS = """HOW TO SET UP
1. Unzip clinical-encounter-simulator-gemini-gem.zip.
2. In Gemini: Gems > New Gem. Name it "Clinical Encounter Simulator".
3. Paste everything below the line into Instructions (it includes the full SKILL.md).
4. Under Knowledge, upload the clinical-encounter-simulator-gemini-gem folder (9 files). Save.
--------------------------------------------------------------------------
You are the Clinical Encounter Simulator. Your knowledge files are a structured copy of the skill package. Read SKILL.md first and follow it as your core instructions. When SKILL.md refers to a file, find it as follows:
- The references/ files are separate files with those names.
- The docs/ files (ONBOARDING, USER_GUIDE, PLATFORM_ADAPTERS, PORTABILITY, VERSIONING_AND_MAINTENANCE) are sections headed "## File: <path>" inside docs.md.
- The templates/ files are sections headed "## File: <path>" inside templates.md.

Run fictional cases for medical education only. Never diagnose or manage a real patient.
"""

REFS = [
    "CASE_SELECTION.md",
    "COACHING_AND_ADAPTIVE_TRAINING.md",
    "CONSULTATION_WORKFLOW.md",
    "PROFILE_PERSISTENCE.md",
    "SAFETY_AND_QA.md",
    "SCORING_AND_DEBRIEF.md",
]

LAYOUT = {
    "SKILL.md": "SKILL.md",
    **{f"references/{r}": f"references/{r}" for r in REFS},
    "docs.md": [
        "docs/ONBOARDING.md",
        "docs/USER_GUIDE.md",
        "docs/PLATFORM_ADAPTERS.md",
        "docs/PORTABILITY.md",
        "docs/VERSIONING_AND_MAINTENANCE.md",
    ],
    "templates.md": [
        "templates/LEARNER_PROFILE.md",
        "templates/PROFILE_INDEX.md",
        "templates/PROGRESS_REVIEW.md",
        "templates/SESSIONS_INDEX.md",
        "templates/SESSION_RECORD.md",
        "templates/STORE_MANIFEST.md",
    ],
}

if __name__ == "__main__":
    build("clinical-encounter-simulator-gemini-gem", LAYOUT, INSTRUCTIONS)
