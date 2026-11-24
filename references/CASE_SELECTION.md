# Structured case-selection engine

Source basis: original master is preserved in `source-masters/clinical_encounter_simulator_structured_case_selection_engine.md`. This reference distills Sections 32, 34, 35, and 37.

## Choose before constructing
For an automatic case, privately select in sequence:
1. Primary specialty and optional subspecialty.
2. Presentation family / complaint.
3. Patient age/life-stage and relevant synthetic context.
4. Setting and resource environment.
5. Acuity and stability.
6. Complexity and difficulty tier (independent of acuity).
7. Educational yield / frequency and one or two observable targets.
8. Case key: intended diagnosis, alternatives, critical actions, elicitable clues, trajectory, endpoint, and scoring anchors.

Then test clinical coherence and fairness before presenting only the opening details.

## Selection priorities
Explicit case request first; substantiated safety remediation; recurring competency needs; declared specialty/exam focus; exposure balancing; clinical realism and yield; variety and retention practice. Use only current chat history and user-supplied portable profiles. If history is absent or truncated, say so rather than inventing cases or counts.

## Broad mix and diversity
Consider internal medicine, surgery, paediatrics, obstetrics/gynaecology, psychiatry, primary care, emergency/critical care, infectious/tropical medicine, and cross-cutting disciplines. Vary presentations, age, setting, context, acuity, and competencies. Common cases should remain common; rare cases need a defensible learning reason. Integrate specialties when clinically coherent.

The source suggests long-run planning ranges across rolling 20–30-case samples (acuity, frequency, yield, focus intensity). Treat these as approximate design targets only, never hard quotas, true probabilities, or expectations for short runs. Keep acuity, complexity, specialty, frequency, and yield as separate axes.

Emergency and critical-care cases are eligible from case one. No emergency-first preference, no non-emergency-first rule, no compulsory rotation, and no arbitrary quotas. Avoid salience-driven defaults such as repeatedly choosing chest pain or breathlessness. A user-requested repeat or deliberate spaced practice is appropriate.

## Honesty
Model-led selection cannot guarantee statistically uniform or unbiased sampling across runs or platforms. Say “structured best-effort diversified selection,” never “randomly drawn” unless a real random mechanism was actually used.

