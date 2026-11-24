#!/usr/bin/env python3
"""Standard-library integrity check; this does not validate clinical content."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
required=['README.md','SKILL.md','SOURCE_MASTER_STATUS.md','source-masters/clinical_encounter_simulator_structured_case_selection_engine.md','references/CASE_SELECTION.md','references/CONSULTATION_WORKFLOW.md','references/SCORING_AND_DEBRIEF.md','references/COACHING_AND_ADAPTIVE_TRAINING.md','references/SAFETY_AND_QA.md','references/PROFILE_PERSISTENCE.md','docs/ONBOARDING.md','docs/USER_GUIDE.md','docs/PORTABILITY.md','docs/PLATFORM_ADAPTERS.md','docs/TEST_PLAN.md','docs/VERSIONING_AND_MAINTENANCE.md','templates/LEARNER_PROFILE.md','templates/SESSION_RECORD.md','templates/SESSIONS_INDEX.md','templates/PROFILE_INDEX.md','templates/STORE_MANIFEST.md','templates/PROGRESS_REVIEW.md','tests/MANUAL_FIXTURES.md','tests/validate_package.py']
errors=[]
for rel in required:
    if not (ROOT/rel).is_file(): errors.append(f'Missing: {rel}')
for md in ROOT.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','#','mailto:')): continue
        local=target.split('#',1)[0]
        if local and not (md.parent/local).resolve().is_file():
            errors.append(f'Broken link in {md.relative_to(ROOT)}: {target}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(required)} required files present; Markdown links resolve.')

