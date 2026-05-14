# Task Execution Plan

## Summary
- Total tasks: **41**
- P1: **9** (DEEP), P2: **9** (STANDARD), P3: **23** (OVERVIEW)
- Execution strategy: sequential with dependency-based topological ordering
- Scope files: 1,636 deep files (509,082 lines) + 318 catalog files (5,657 lines) = 100% coverage
- Re-optimized: tasks restructured from scratch with enriched fields and 100% coverage

## Task Sizes (informational)

容量约束已前移到 trace-mainline 的 sub-map 级别（≤10000 行/sub-map），本步骤仅记录不判定。

| Task | Primary ML | ML Priority | Analysis Depth | Scope Files | Lines |
|------|-----------|-------------|---------------|-------------|-------|
| T-01 | ML-01 | P1 | DEEP | 10 files | 7,943 |
| T-02 | ML-01 | P1 | DEEP | 207 files | 55,902 |
| T-03 | ML-02 | P1 | DEEP | 341 files | 91,410 |
| T-04 | ML-02 | P1 | DEEP | 7 files | 11,711 |
| T-05 | ML-03 | P1 | DEEP | 142 files | 58,846 |
| T-06 | ML-04 | P1 | DEEP | 23 files | 5,636 |
| T-07 | ML-04 | P1 | DEEP | 55 files | 16,720 |
| T-08 | ML-05 | P1 | DEEP | 85 files | 31,771 |
| T-09 | ML-06 | P1 | DEEP | 40 files | 13,387 |
| T-10 | ML-07 | P2 | STANDARD | 80 files | 28,353 |
| T-11 | ML-07 | P2 | STANDARD | 321 files | 72,844 |
| T-12 | ML-07 | P2 | STANDARD | 63 files | 12,247 |
| T-13 | ML-08 | P2 | STANDARD | 21 files | 4,683 |
| T-14 | ML-09 | P2 | STANDARD | 46 files | 18,081 |
| T-15 | ML-10 | P2 | STANDARD | 19 files | 7,432 |
| T-16 | ML-11 | P2 | STANDARD | 34 files | 12,654 |
| T-17 | ML-12 | P2 | STANDARD | 65 files | 29,367 |
| T-18 | ML-13 | P2 | STANDARD | 37 files | 18,665 |
| T-19 | ML-14 | P3 | OVERVIEW | 22 files | 7,548 |
| T-20 | ML-15 | P3 | OVERVIEW | 9 files | 2,716 |
| T-21 | ML-03 | P1 | OVERVIEW | catalog (PI-01) | 0 |
| T-22 | ML-01 | P1 | OVERVIEW | catalog (PI-02) | 0 |
| T-23 | ML-07 | P2 | OVERVIEW | catalog (PI-03) | 0 |
| T-24 | ML-08 | P2 | OVERVIEW | catalog (PI-04) | 0 |
| T-25 | ML-04 | P1 | OVERVIEW | catalog (PI-06) | 0 |
| T-26 | ML-07 | P2 | OVERVIEW | catalog (PI-07) | 0 |
| T-27 | ML-07 | P2 | OVERVIEW | catalog (PI-08) | 0 |
| T-28 | ML-07 | P2 | OVERVIEW | catalog (PI-09) | 0 |
| T-29 | ML-12 | P2 | OVERVIEW | catalog (PI-10) | 0 |
| T-30 | ML-01 | P1 | OVERVIEW | catalog (PI-11) | 0 |
| T-31 | ML-02 | P1 | OVERVIEW | catalog (PI-12) | 0 |
| T-32 | ML-07 | P2 | OVERVIEW | catalog (PI-13) | 0 |
| T-33 | ML-01 | P1 | OVERVIEW | catalog (PI-14) | 0 |
| T-34 | ML-07 | P2 | OVERVIEW | catalog (PI-15) | 0 |
| T-35 | ML-07 | P2 | OVERVIEW | catalog (PI-16) | 0 |
| T-36 | ML-03 | P1 | OVERVIEW | catalog (PI-18) | 0 |
| T-37 | ML-05 | P1 | OVERVIEW | catalog (PI-20) | 0 |
| T-38 | ML-09 | P2 | OVERVIEW | catalog (PI-23) | 0 |
| T-39 | ML-06 | P1 | OVERVIEW | catalog (PI-24) | 0 |
| T-40 | ML-05 | P1 | OVERVIEW | catalog (PI-05) | 0 |
| T-41 | ML-01 | P1 | OVERVIEW | 9 files | 1,166 |

**Size distribution**: Max = 91,410 (T-03), Median ≈ 7,432, Total = 509,082 deep lines

## Execution Order

| Order | Task | Priority | Primary ML | ML Priority | Analysis Depth | Dependencies | Files | Lines |
|-------|------|----------|-----------|-------------|---------------|--------------|-------|-------|
| 1 | T-01 | P1 | ML-01 | P1 | DEEP | none | 10 | 7,943 |
| 2 | T-02 | P1 | ML-01 | P1 | DEEP | T-01 | 207 | 55,902 |
| 3 | T-03 | P1 | ML-02 | P1 | DEEP | T-01 | 341 | 91,410 |
| 4 | T-04 | P1 | ML-02 | P1 | DEEP | T-03 | 7 | 11,711 |
| 5 | T-05 | P1 | ML-03 | P1 | DEEP | T-03 | 142 | 58,846 |
| 6 | T-06 | P1 | ML-04 | P1 | DEEP | T-05 | 23 | 5,636 |
| 7 | T-07 | P1 | ML-04 | P1 | DEEP | T-06 | 55 | 16,720 |
| 8 | T-08 | P1 | ML-05 | P1 | DEEP | T-06 | 85 | 31,771 |
| 9 | T-09 | P1 | ML-06 | P1 | DEEP | T-01 | 40 | 13,387 |
| 10 | T-10 | P2 | ML-07 | P2 | STANDARD | T-02 | 80 | 28,353 |
| 11 | T-11 | P2 | ML-07 | P2 | STANDARD | T-10 | 321 | 72,844 |
| 12 | T-12 | P2 | ML-07 | P2 | STANDARD | T-10 | 63 | 12,247 |
| 13 | T-13 | P2 | ML-08 | P2 | STANDARD | none | 21 | 4,683 |
| 14 | T-14 | P2 | ML-09 | P2 | STANDARD | T-09 | 46 | 18,081 |
| 15 | T-15 | P2 | ML-10 | P2 | STANDARD | T-03 | 19 | 7,432 |
| 16 | T-16 | P2 | ML-11 | P2 | STANDARD | T-03 | 34 | 12,654 |
| 17 | T-17 | P2 | ML-12 | P2 | STANDARD | T-08 | 65 | 29,367 |
| 18 | T-18 | P2 | ML-13 | P2 | STANDARD | T-05 | 37 | 18,665 |
| 19 | T-22 | P3 | ML-01 | P1 | OVERVIEW | T-01 | catalog | 0 |
| 20 | T-30 | P3 | ML-01 | P1 | OVERVIEW | T-01 | catalog | 0 |
| 21 | T-33 | P3 | ML-01 | P1 | OVERVIEW | T-01 | catalog | 0 |
| 22 | T-41 | P3 | ML-01 | P1 | OVERVIEW | none | 9 | 1,166 |
| 23 | T-31 | P3 | ML-02 | P1 | OVERVIEW | T-03 | catalog | 0 |
| 24 | T-21 | P3 | ML-03 | P1 | OVERVIEW | T-05 | catalog | 0 |
| 25 | T-36 | P3 | ML-03 | P1 | OVERVIEW | T-05 | catalog | 0 |
| 26 | T-25 | P3 | ML-04 | P1 | OVERVIEW | T-06 | catalog | 0 |
| 27 | T-37 | P3 | ML-05 | P1 | OVERVIEW | T-08 | catalog | 0 |
| 28 | T-40 | P3 | ML-05 | P1 | OVERVIEW | T-08 | catalog | 0 |
| 29 | T-39 | P3 | ML-06 | P1 | OVERVIEW | T-09 | catalog | 0 |
| 30 | T-23 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 31 | T-26 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 32 | T-27 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 33 | T-28 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 34 | T-32 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 35 | T-34 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 36 | T-35 | P3 | ML-07 | P2 | OVERVIEW | T-10 | catalog | 0 |
| 37 | T-24 | P3 | ML-08 | P2 | OVERVIEW | T-13 | catalog | 0 |
| 38 | T-38 | P3 | ML-09 | P2 | OVERVIEW | T-14 | catalog | 0 |
| 39 | T-29 | P3 | ML-12 | P2 | OVERVIEW | T-17 | catalog | 0 |
| 40 | T-19 | P3 | ML-14 | P3 | OVERVIEW | T-12 | 22 | 7,548 |
| 41 | T-20 | P3 | ML-15 | P3 | OVERVIEW | none | 9 | 2,716 |

## Dependency Graph

```
T-01 ──→ T-02 ──→ T-10 ──→ T-11
  │                └──→ T-12 ──→ T-19
  ├──→ T-03 ──→ T-04
  │         ├──→ T-05 ──→ T-06 ──→ T-07
  │         │                  └──→ T-08 ──→ T-17
  │         │                           └──→ T-37, T-40
  │         ├──→ T-15                └──→ T-18
  │         └──→ T-16
  └──→ T-09 ──→ T-14 ──→ T-38
                └──→ T-39

T-13 (standalone) ──→ T-24
T-20 (standalone)
T-41 (standalone)

Pattern Audits (ML-grouped):
  ML-01: T-22, T-30, T-33 ← depend on T-01
  ML-02: T-31 ← depends on T-03
  ML-03: T-21, T-36 ← depend on T-05
  ML-04: T-25 ← depends on T-06
  ML-05: T-37, T-40 ← depend on T-08
  ML-06: T-39 ← depends on T-09
  ML-07: T-23, T-26, T-27, T-28, T-32, T-34, T-35 ← depend on T-10
  ML-08: T-24 ← depends on T-13
  ML-09: T-38 ← depends on T-14
  ML-12: T-29 ← depends on T-17
```

## Verification
- [x] All tasks from 03-analysis-tasks.md are in the workflow (41/41)
- [x] No task appears multiple times
- [x] All dependency constraints are respected (DAG, no cycles)
- [x] Task sizes recorded (informational, no hard limit)
- [x] Scope Files physical existence verified (Step 2.5 PASS)
- [x] Pattern Coverage verified (Step 2.6 PASS: 20 audits, 19 owner_ml + PI-05)
- [x] Workflow created successfully
