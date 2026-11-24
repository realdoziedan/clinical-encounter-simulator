import { readFileSync, readdirSync, statSync } from "node:fs";
import { resolve, join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";
const root=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const required=["README.md","SKILL.md","SOURCE_MASTER_STATUS.md","source-masters/clinical_encounter_simulator_structured_case_selection_engine.md","references/CASE_SELECTION.md","references/CONSULTATION_WORKFLOW.md","references/SCORING_AND_DEBRIEF.md","references/COACHING_AND_ADAPTIVE_TRAINING.md","references/SAFETY_AND_QA.md","references/PROFILE_PERSISTENCE.md","docs/ONBOARDING.md","docs/USER_GUIDE.md","docs/PORTABILITY.md","docs/PLATFORM_ADAPTERS.md","docs/TEST_PLAN.md","docs/VERSIONING_AND_MAINTENANCE.md","templates/LEARNER_PROFILE.md","templates/SESSION_RECORD.md","templates/SESSIONS_INDEX.md","templates/PROFILE_INDEX.md","templates/STORE_MANIFEST.md","templates/PROGRESS_REVIEW.md","tests/MANUAL_FIXTURES.md","tests/validate_package.py"];
const errors=[];
for(const f of required){try{if(!statSync(join(root,f)).isFile())errors.push("Not a file: "+f)}catch{errors.push("Missing: "+f)}}
function walk(dir){for(const e of readdirSync(dir,{withFileTypes:true})){const p=join(dir,e.name);if(e.isDirectory())walk(p);else if(e.name.endsWith(".md")){const s=readFileSync(p,"utf8");for(const m of s.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){const t=m[1];if(/^(https?:|#|mailto:)/.test(t))continue;const l=t.split("#")[0];if(l&&!statSync(resolve(p,"..",l),{throwIfNoEntry:false}))errors.push("Broken link in "+relative(root,p)+": "+t)}}}}
walk(root);
if(errors.length){console.error(errors.join("\n"));process.exit(1)}
console.log("PASS: "+required.length+" required files present; Markdown links resolve.");

