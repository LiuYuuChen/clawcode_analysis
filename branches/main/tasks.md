# Branch Tasks (main)

## Analysis Pipeline Progress

- [x] map-repo — 01-repo-map.md + metadata.json + implementation baseline
- [x] sub-map-repo — 15 mainlines decomposed
- [x] trace-mainline — 29 sub-maps across 15 ML (ML-01~ML-15)
- [x] map-repo-guardian — ALL PASS (iteration 5 of 5)
- [x] analyze — branches/main/analysis/02-analysis-report.md (529 lines)
- [x] tasks — analysis/03-analysis-tasks.md (40 tasks: P1=9, P2=9, P3=22)
- [x] implement — task execution pipeline (39 tasks ordered, tmp_workflow.json)
- [x] implement-guardian — FAIL (Catalog Gate: PI-05 13 instances uncovered)
- [x] tasks-supplement — T-40 added, T-12 deduped, T-19 expanded, phantom cleaned
- [x] implement-redo — 40 tasks topological sort, 04-task-plan.md written, workflow created
- [x] implement-guardian-recheck (iter 2) — ALL PASS (99.77% line coverage)
- [x] task-output-guardian — ALL PASS (iter 2, 41 tasks verified)
  - [x] tasks-supplement-T41 — added T-41 for 9 shim/vendor orphan files
  - [x] re-execute-T17 — plugin system rebuilt from scratch (65 files, P2/STANDARD)
  - [x] re-execute-T29 — PI-10 audit rebuilt from scratch (7 instances, P3/OVERVIEW)
  - [x] re-execute-T07 — patched 5 missing File Roles rows
  - [x] re-execute-T12 — removed 14 duplicate File Roles rows
  - [x] patch-audit-file-roles-T21-T22-T31 — verified all 196 rows match manifest (77+107+12)
  - [x] execute-T41-shim-vendor-proxies — OVERVIEW analysis (9 files, 1167 lines)
  - [x] task-output-guardian-recheck-iter2 — ALL PASS
- [~] synthesize-analysis — in progress (3/24 goals done)
- [x] **publish-site** — VitePress 站点打包 ✅
