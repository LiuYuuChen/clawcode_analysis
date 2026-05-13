# Analysis Coverage Report

**Iteration**: 2 (recheck after remediation)
**Date**: 2025-01-28
**Status**: **ALL PASS** ✅

## Coverage Summary (按代码行数)

| Metric | Value |
|--------|-------|
| Mapped files lines (denominator) | 514,739 |
| Task scope files lines (numerator, de-duped) | 513,573 |
| **Analysis coverage (行数)** | **99.77%** |
| **Coverage Status** | **PASS** (threshold: 95%) |

## Four-Gate Result

| Gate | Result | Detail |
|------|--------|--------|
| Line Coverage | ✅ PASS | 513,573 / 514,739 = 99.77% |
| P1 Deep Gate | ✅ PASS | 9/9 P1 tasks configured DEEP |
| Catalog Gate | ✅ PASS | 318/318 instances covered |
| Large File Gate | ✅ PASS | 87/87 large files covered |
| **Overall** | **✅ PASS** | |

## P1 Deep Analysis Gate

- P1 tasks total: 9
- P1 tasks with DEEP mode configured: 9
- **P1 Gate Status: PASS**

| Task | Priority | Primary ML | analysis_depth | Status |
|------|----------|-----------|----------------|--------|
| T-01 | P1 | ML-01 | DEEP | OK |
| T-02 | P1 | ML-01 | DEEP | OK |
| T-03 | P1 | ML-02 | DEEP | OK |
| T-04 | P1 | ML-02 | DEEP | OK |
| T-05 | P1 | ML-03 | DEEP | OK |
| T-06 | P1 | ML-04 | DEEP | OK |
| T-07 | P1 | ML-04 | DEEP | OK |
| T-08 | P1 | ML-05 | DEEP | OK |
| T-09 | P1 | ML-06 | DEEP | OK |

## Catalog Coverage Gate

- Total catalog instances: 318 (19 patterns)
- Pattern Audit tasks: 20 (PI-04 has 0 catalog instances but has audit task T-24)
- Covered by Pattern Audit tasks: 318/318
- Uncovered: 0
- **Catalog Gate Status: PASS**

| Pattern | Instances | Audit Task | Status |
|---------|-----------|-----------|--------|
| PI-01 | 77 | T-21 | covered |
| PI-02 | 107 | T-22 | covered |
| PI-03 | 14 | T-23 | covered |
| PI-04 | 0 (deep traced) | T-24 | covered |
| PI-05 | 13 | T-40 | covered ← NEW (remediation) |
| PI-06 | 5 | T-25 | covered |
| PI-07 | 33 | T-26 | covered |
| PI-08 | 12 | T-27 | covered |
| PI-09 | 4 | T-28 | covered |
| PI-10 | 7 | T-29 | covered |
| PI-11 | 5 | T-30 | covered |
| PI-12 | 12 | T-31 | covered |
| PI-13 | 10 | T-32 | covered |
| PI-14 | 2 | T-33 | covered |
| PI-15 | 1 | T-34 | covered |
| PI-16 | 5 | T-35 | covered |
| PI-18 | 2 | T-36 | covered |
| PI-20 | 3 | T-37 | covered |
| PI-23 | 4 | T-38 | covered |
| PI-24 | 2 | T-39 | covered |

## Large File Coverage Gate

- LARGE_FILE_THRESHOLD: 1000 lines
- Total large mapped files (>1000 lines): 87
- Covered by some task scope: 87
- Uncovered: 0
- **Large File Gate Status: PASS**

## Uncovered Mapped Files (9 files, 1,166 lines = 0.23%)

All 9 uncovered files are shim/vendor proxy files — thin re-export layers for bundled native dependencies:

| File | Lines | Category |
|------|-------|----------|
| shims/ant-computer-use-swift/index.ts | 297 | native shim |
| shims/ant-computer-use-mcp/index.ts | 195 | native shim |
| vendor/image-processor-src/index.ts | 162 | vendor proxy |
| vendor/audio-capture-src/index.ts | 151 | vendor proxy |
| shims/ant-claude-for-chrome-mcp/index.ts | 113 | native shim |
| shims/ant-computer-use-input/index.ts | 93 | native shim |
| vendor/modifiers-napi-src/index.ts | 67 | vendor proxy |
| vendor/url-handler-src/index.ts | 58 | vendor proxy |
| shims/ant-computer-use-mcp/types.ts | 30 | type shim |

**Rationale for not covering**: These are thin re-export proxies for bundled native dependencies (Computer Use plugins, image/audio processing, URL handling). They contain zero application logic — only `export *` or re-exports from native modules. Coverage at 99.77% already exceeds the 95% threshold by a wide margin.

## Effective Coverage Chain

| Layer | Metric | Coverage | Detail |
|-------|--------|---------|--------|
| Implementation → Mapped (map-repo-guardian) | 文件数 | 96.8% | 2019 → 1954 files |
| Mapped → Task Scope (implement-guardian) | **行数** | **99.77%** | 514,739 → 513,573 lines |
| **Effective** | **文件数×行数** | **96.6%** | |

## Per-Task Coverage (行数, top 20)

| Task | Primary ML | Scope Files | Lines | Ratio |
|-------|-----------|-------------|-------|-------|
| T-03 | ML-02 | 341 | ~94,000 | 18.3% |
| T-02 | ML-01 | 207 | ~48,000 | 9.3% |
| T-05 | ML-03 | 142 | ~42,000 | 8.2% |
| T-08 | ML-05 | 85 | ~52,000 | 10.1% |
| T-07 | ML-04 | 55 | ~15,000 | 2.9% |
| T-11 | ML-07 | 321 | ~56,000 | 10.9% |
| T-10 | ML-07 | 80 | ~42,000 | 8.2% |
| T-01 | ML-01 | 10 | ~5,000 | 1.0% |
| T-04 | ML-02 | 7 | ~19,000 | 3.7% |
| T-22 | ML-01 | 107 | ~3,200 | 0.6% |
| T-21 | ML-03 | 77 | ~1,200 | 0.2% |
| T-06 | ML-04 | 23 | ~5,600 | 1.1% |
| T-09 | ML-06 | 40 | ~13,400 | 2.6% |
| T-12 | ML-07 | 63 | ~12,300 | 2.4% |
| T-26 | ML-07 | 33 | ~710 | 0.1% |
| T-14 | ML-09 | 46 | ~12,600 | 2.4% |
| T-17 | ML-12 | 49 | ~25,400 | 4.9% |
| T-18 | ML-13 | 37 | ~17,700 | 3.4% |
| T-19 | ML-14 | 22 | ~7,876 | 1.5% |
| T-20 | ML-15 | 9 | ~2,716 | 0.5% |

## Remediation History

### Iteration 1 → FAIL

- **Catalog Gate FAIL**: PI-05 had 13 catalog instances without audit task
- **Action**: Added T-40 (audit-PI-05), expanded T-12 (+3 hooks), expanded T-19 (+spawnInProcess.ts), cleaned 3 phantom files

### Iteration 2 → PASS

- All four gates PASS after remediation
- No further action needed

## Action Taken

**PASS**: All gates passed. Proceeding to task-output-guardian.
