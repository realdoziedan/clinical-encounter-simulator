#!/usr/bin/env python3
"""Build dist/clinical-encounter-simulator-single.md: SKILL.md plus the files it
uses at runtime, concatenated unchanged, for platforms that accept only one
skill file.

Run from anywhere:  python scripts/build_single_file.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "clinical-encounter-simulator-single.md"

# Runtime files, grouped as SKILL.md routes to them. Left out: README, LICENSE,
# SOURCE_MASTER_STATUS.md, source-masters/ (kept for traceability, "not
# required at runtime"), docs/TEST_PLAN.md, docs/VERSIONING_AND_MAINTENANCE.md,
# tests/, and the release ZIPs.
FILES = [
    "references/CASE_SELECTION.md",
    "references/CONSULTATION_WORKFLOW.md",
    "references/SCORING_AND_DEBRIEF.md",
    "references/COACHING_AND_ADAPTIVE_TRAINING.md",
    "references/SAFETY_AND_QA.md",
    "references/PROFILE_PERSISTENCE.md",
    "docs/ONBOARDING.md",
    "docs/USER_GUIDE.md",
    "docs/PLATFORM_ADAPTERS.md",
    "docs/PORTABILITY.md",
    "templates/LEARNER_PROFILE.md",
    "templates/PROFILE_INDEX.md",
    "templates/PROGRESS_REVIEW.md",
    "templates/SESSIONS_INDEX.md",
    "templates/SESSION_RECORD.md",
    "templates/STORE_MANIFEST.md",
]

NOTE = (
    "\n\n---\n\n# Bundled reference files\n\n"
    "This single-file edition contains the files below in full, unchanged. "
    "Where the instructions point to a file path (for example "
    "references/CASE_SELECTION.md), use the section with that path as its heading.\n"
)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> None:
    parts = [read("SKILL.md"), NOTE]
    for rel in FILES:
        parts.append(f"\n\n---\n\n## File: {rel}\n\n")
        parts.append(read(rel))
    text = "".join(parts)
    for rel in ["SKILL.md", *FILES]:
        assert read(rel) in text, f"{rel} not included verbatim"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(text.encode('utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
