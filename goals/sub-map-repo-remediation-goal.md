# Goal: sub-map-repo-remediation

- [x] Parse ML-12~ML-15 main line definitions from 01-repo-map.md
- [x] Validate entry files exist for all 4 MLs
- [x] Extract import relationships for all 116 ml-supplement files (763 total imports, 260 intra-ML)
- [x] Classify core (deep) vs supporting (standard) using centrality (import count)
  - ML-12: 16 core (13,936L) + 33 standard (11,486L)
  - ML-13: 12 core (10,628L) + 24 standard (7,052L)
  - ML-14: 7 core (1,951L) + 15 standard (5,597L)
  - ML-15: 3 core (1,905L) + 6 standard (811L)
  - Total: 38 deep + 78 standard = 116 files
- [x] Write sub-map ML-12-1.md (151 lines) — Plugin System
- [x] Write sub-map ML-13-1.md (74 lines) — Bash/Shell Engine
- [x] Write sub-map ML-14-1.md (117 lines) — Swarm Orchestration
- [x] Write sub-map ML-15-1.md (39 lines) — SDK Entry Points
- [x] Update mainline-file-map.jsonl: 27 entries (23 existing + 4 new)
- [x] Rebuild mapped-files.jsonl: 1048 entries (359 deep + 78 standard + 611 catalog)
- [x] Update call-graph.jsonl: 396 entries (280 existing + 116 new)
- [x] Update metadata.json: mainline_count=15, mapped_file_count=1048, mapped_lines=292,121
- [x] Create this goal file

## Coverage Impact
- Before: 932 mapped (321 deep + 0 standard + 611 catalog)
- After: 1048 mapped (359 deep + **78 standard** + 611 catalog)
- Tier 1 (DEEP+STANDARD+CATALOG): 1048/2019 = 51.9% (target ≥10%) ✅ PASS
- Tier 2 (DEEP+STANDARD): (359+78)/2019 = 21.6% (target ≥80%) ❌ FAIL
- Tier 3 will be addressed by catalog-supplement step
