<!-- analysis-version: 0 | commit: a5179f6 | updated: 2025-07-26 | mode: re-execute | task: T-29 -->
# T-29 Pattern Audit: bundled-skill (PI-10)

## Scope Confirmation
- Task ID: T-29
- Primary Mainline: ML-12 (Plugin System)
- ML Priority: P3
- Analysis Depth: OVERVIEW
- Pattern Coverage: PI-10 (bundled-skill)
- Scope Files (confirmed): 7 PI-10 catalog instances
  1. [`src/skills/bundled/claudeInChrome.ts`](/src/src/skills/bundled/claudeInChrome.ts) (34 lines)
  2. [`src/skills/bundled/dream.ts`](/src/src/skills/bundled/dream.ts) (1 line)
  3. [`src/skills/bundled/hunter.ts`](/src/src/skills/bundled/hunter.ts) (1 line)
  4. [`src/skills/bundled/runSkillGenerator.ts`](/src/src/skills/bundled/runSkillGenerator.ts) (1 line)
  5. [`src/skills/bundled/verify.ts`](/src/src/skills/bundled/verify.ts) (30 lines)
  6. [`src/skills/bundled/verifyContent.ts`](/src/src/skills/bundled/verifyContent.ts) (13 lines)
  7. [`src/skills/mcpSkillBuilders.ts`](/src/src/skills/mcpSkillBuilders.ts) (44 lines)
- Scope adjustments: None — all 7 files exist and are readable
- Re-execute reason: FAIL_0 (file completely missing) + FAIL_5 (role_source not verified)

## File Roles

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| src/skills/bundled/claudeInChrome.ts | 34 | Registers Chrome browser automation skill via registerBundledSkill with MCP tool allowlist, activation prompt, and auto-enable gating | OVERVIEW: Pattern Audit full verification |
| src/skills/bundled/dream.ts | 1 | Empty stub: registerDreamSkill() is a no-op function body reserved for future Dream skill | OVERVIEW: Pattern Audit full verification |
| src/skills/bundled/hunter.ts | 1 | Empty stub: registerHunterSkill() is a no-op function body reserved for future Hunter skill | OVERVIEW: Pattern Audit full verification |
| src/skills/bundled/runSkillGenerator.ts | 1 | Empty stub: registerRunSkillGeneratorSkill() is a no-op function body reserved for future skill generator | OVERVIEW: Pattern Audit full verification |
| src/skills/bundled/verify.ts | 30 | Registers verify skill (ant-only) that extracts SKILL.md frontmatter and inlines example files for code-change verification | OVERVIEW: Pattern Audit full verification |
| src/skills/bundled/verifyContent.ts | 13 | Content module for verify skill: imports SKILL.md and example .md files via Bun text loader for build-time inlining | OVERVIEW: Pattern Audit full verification |
| src/skills/mcpSkillBuilders.ts | 44 | Dependency-graph leaf: write-once registry for MCP skill builder functions (createSkillCommand + parseSkillFrontmatterFields), breaks circular dependency between mcpSkills.ts and loadSkillsDir.ts | OVERVIEW: Pattern Audit full verification |

## Analysis Findings

- **F-01: Three sub-types identified** — (1) fully-implemented skill (claudeInChrome.ts 34L, verify.ts 30L), (2) content/data module (verifyContent.ts 13L), (3) empty stub (dream.ts/hunter.ts/runSkillGenerator.ts each 1L), (4) infrastructure adapter (mcpSkillBuilders.ts 44L).
- **F-02: registerBundledSkill() is the shared interface** — All non-stub, non-infrastructure instances call `registerBundledSkill()` from `bundledSkills.ts`, passing a `BundledSkillDefinition` object with name, description, and `getPromptForCommand` at minimum.
- **F-03: 3 of 7 files are empty stubs (43%)** — dream.ts, hunter.ts, runSkillGenerator.ts each export a single no-op `register*Skill(): void {}`. These are reserved entry points for future skills.
- **F-04: claudeInChrome.ts is the most complete instance** — Defines allowedTools (MCP tool allowlist), isEnabled (auto-enable gating), whenToUse, userInvocable, and a dynamic prompt builder.
- **F-05: verify.ts has USER_TYPE gate** — `process.env.USER_TYPE !== 'ant'` causes early return for non-Anthropic users, restricting the skill to internal use.
- **F-06: verifyContent.ts uses Bun text loader** — Imports `.md` files as raw strings at build time via Bun's text loader, making the skill content embedded in the binary.
- **F-07: mcpSkillBuilders.ts is not a skill registration** — It is a dependency-graph breaking module that provides `registerMCPSkillBuilders()` / `getMCPSkillBuilders()` for cycle avoidance. It does not call `registerBundledSkill()`.
- **F-08: Extreme size variance** — Lines range from 1 (stubs) to 44 (mcpSkillBuilders), median = 1. The non-stub files average 30.25 lines.
- **F-09: Naming convention consistent** — All bundled skill files use `register<Name>Skill()` as the export name, matching the filename in camelCase.
- **F-10: Zero cross-instance imports** — No PI-10 file imports another PI-10 file (verifyContent is a data dependency of verify, not a cross-skill reference).

## File Dependency Graph

```mermaid
flowchart TD
    subgraph PI-10 Bundled Skills
        CIC[claudeInChrome.ts<br/>34L]
        D[dream.ts<br/>1L]
        H[hunter.ts<br/>1L]
        RSG[runSkillGenerator.ts<br/>1L]
        V[verify.ts<br/>30L]
        VC[verifyContent.ts<br/>13L]
        MSB[mcpSkillBuilders.ts<br/>44L]
    end

    subgraph External
        BS[bundledSkills.ts<br/>registerBundledSkill]
        FP[frontmatterParser.ts]
        BCC[@ant/claude-for-chrome-mcp]
        CIP[claudeInChrome/prompt.ts]
        CIS[claudeInChrome/setup.ts]
        LSD[loadSkillsDir.ts]
        MD[verify/SKILL.md + examples/*.md]
    end

    CIC --> BS
    CIC --> BCC
    CIC --> CIP
    CIC --> CIS

    V --> BS
    V --> FP
    V --> VC

    VC --> MD

    MSB -.->|types only| LSD

    D -.->|no-op stub| BS
    H -.->|no-op stub| BS
    RSG -.->|no-op stub| BS
```

**Dependency summary**: Only 3 files have real imports (claudeInChrome, verify, verifyContent). mcpSkillBuilders imports only types. 3 files are no-op stubs with zero imports.

## Pattern Contract

PI-10 (bundled-skill) defines files that register built-in skills shipped with the CLI binary.

### Conventions

1. **Export name**: `register<Name>Skill(): void` — every file exports exactly one registration function
2. **Registration target**: Calls `registerBundledSkill()` from `../bundledSkills.js` with a `BundledSkillDefinition` object
3. **Required fields**: `name` (string), `description` (string), `getPromptForCommand` (async function)
4. **Optional fields**: `whenToUse`, `allowedTools`, `userInvocable`, `isEnabled`, `files`, `hooks`, `aliases`, `model`, `disableModelInvocation`, `context`, `agent`
5. **Location**: All reside under `src/skills/bundled/` (6 files) or `src/skills/` root (1 file: mcpSkillBuilders.ts)
6. **Module-level side effects**: Registration happens at module initialization time

### Sub-types

| Sub-type | Files | Description |
|----------|-------|-------------|
| fully-implemented-skill | claudeInChrome.ts, verify.ts | Complete skill registration with prompt generation, tool allowlist, and enable gating |
| content-module | verifyContent.ts | Data-only module providing SKILL.md content and example files for a skill |
| empty-stub | dream.ts, hunter.ts, runSkillGenerator.ts | No-op function body reserved for future skill implementation |
| infrastructure-adapter | mcpSkillBuilders.ts | Write-once registry for MCP skill builder functions, breaks circular dependency |

## Pattern Audit: Full Verification

### Instance 1: [`src/skills/bundled/claudeInChrome.ts`](/src/src/skills/bundled/claudeInChrome.ts) (34L) — ✅ PASS

**Exports**: `registerClaudeInChromeSkill(): void`
**Pattern compliance**: Calls `registerBundledSkill()` with all required fields (name, description, getPromptForCommand) plus optional fields (allowedTools, whenToUse, userInvocable, isEnabled).
**Unique aspects**: Imports from external npm package `@ant/claude-for-chrome-mcp` and internal `claudeInChrome/` utils. Has `isEnabled()` callback that gates on `shouldAutoEnableClaudeInChrome()`.
**role_one_liner update**: "Chrome browser automation skill with MCP tool allowlist and auto-enable gating"

### Instance 2: [`src/skills/bundled/dream.ts`](/src/src/skills/bundled/dream.ts) (1L) — ✅ PASS (stub)

**Exports**: `registerDreamSkill(): void {}` — empty function body.
**Pattern compliance**: Follows naming convention (`register<Name>Skill`). Stub does not call `registerBundledSkill()` — acceptable as reserved entry point.
**role_one_liner update**: "Empty stub reserved for future Dream skill registration"

### Instance 3: [`src/skills/bundled/hunter.ts`](/src/src/skills/bundled/hunter.ts) (1L) — ✅ PASS (stub)

**Exports**: `registerHunterSkill(): void {}` — empty function body.
**Pattern compliance**: Same as dream.ts. Follows naming convention.
**role_one_liner update**: "Empty stub reserved for future Hunter skill registration"

### Instance 4: [`src/skills/bundled/runSkillGenerator.ts`](/src/src/skills/bundled/runSkillGenerator.ts) (1L) — ✅ PASS (stub)

**Exports**: `registerRunSkillGeneratorSkill(): void {}` — empty function body.
**Pattern compliance**: Same as dream.ts/hunter.ts. Follows naming convention.
**role_one_liner update**: "Empty stub reserved for future skill generator registration"

### Instance 5: [`src/skills/bundled/verify.ts`](/src/src/skills/bundled/verify.ts) (30L) — ✅ PASS

**Exports**: `registerVerifySkill(): void`
**Pattern compliance**: Calls `registerBundledSkill()` with required fields. Uses `process.env.USER_TYPE !== 'ant'` guard for early return.
**Unique aspects**: Extracts description from SKILL.md frontmatter via `parseFrontmatter()`. Inlines example files via `files` field.
**role_one_liner update**: "Verify skill (ant-only) that parses SKILL.md frontmatter and inlines example files"

### Instance 6: [`src/skills/bundled/verifyContent.ts`](/src/src/skills/bundled/verifyContent.ts) (13L) — ✅ PASS

**Exports**: `SKILL_MD` (string constant) and `SKILL_FILES` (Record&lt;string, string&gt;)
**Pattern compliance**: Data-only module — does not export a `register*Skill` function but provides content consumed by verify.ts. Essential supporting file for the verify skill.
**Unique aspects**: Uses Bun's text loader to import `.md` files as raw strings at build time.
**role_one_liner update**: "Content module importing SKILL.md and example .md files via Bun text loader"

### Instance 7: [`src/skills/mcpSkillBuilders.ts`](/src/src/skills/mcpSkillBuilders.ts) (44L) — ⚠️ DEVIATES

**Exports**: `registerMCPSkillBuilders()` and `getMCPSkillBuilders()` — NOT a `register*Skill(): void` function.
**Pattern compliance**: Does NOT call `registerBundledSkill()`. Does NOT follow the naming convention. Serves a different purpose (cycle-breaking registry for MCP skill builders).
**Deviation reason**: Classified as PI-10 due to location (`src/skills/`) and skill-related purpose, but architecturally it is an infrastructure module, not a bundled skill registration.
**role_one_liner update**: "Cycle-breaking write-once registry for MCP skill builder functions (createSkillCommand + parseSkillFrontmatterFields)"

### Verification Summary

| Instance | File | Lines | Result | Notes |
|----------|------|-------|--------|-------|
| 1 | claudeInChrome.ts | 34 | ✅ PASS | Fully implemented, all fields present |
| 2 | dream.ts | 1 | ✅ PASS | Empty stub, naming convention followed |
| 3 | hunter.ts | 1 | ✅ PASS | Empty stub, naming convention followed |
| 4 | runSkillGenerator.ts | 1 | ✅ PASS | Empty stub, naming convention followed |
| 5 | verify.ts | 30 | ✅ PASS | Fully implemented, ant-only gate |
| 6 | verifyContent.ts | 13 | ✅ PASS | Data-only supporting module |
| 7 | mcpSkillBuilders.ts | 44 | ⚠️ DEVIATES | Not a skill registration; infrastructure adapter |

**Pass rate**: 6/7 strict pass + 1 deviation = **86% strict, 100% with documented deviation**

## inferred vs verified Statistics

| Metric | Value |
|--------|-------|
| Total instances | 7 |
| Verified in this audit | 7 (100%) |
| Strict pass | 6 (86%) |
| Deviation (documented) | 1 (14%) — mcpSkillBuilders.ts |
| Inferred remaining | 0 |
| Confidence | HIGH — all files fully read and analyzed |

## Acceptance Criteria Status

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| AC-1 | All 7 PI-10 instances listed in File Roles | PASS | 7 rows, one per instance |
| AC-2 | Pattern contract documented | PASS | 6 conventions + 4 sub-types |
| AC-3 | Full verification of all instances | PASS | 7/7 verified (100%) |
| AC-4 | instance-manifest.jsonl updated with role_source=verified | PASS | All 7 entries updated |
| AC-5 | role_one_liner revised for accuracy | PASS | All 7 revised from generic to specific |
| AC-6 | File Dependency Graph generated | PASS | mermaid flowchart with 7 nodes |
| AC-7 | Deviations documented | PASS | mcpSkillBuilders.ts deviation recorded |

**Overall: 7/7 PASS**

## Identified Problems

| ID | Severity | Description | File:Line |
|----|----------|-------------|-----------|
| P3-01 | P3 | **mcpSkillBuilders.ts miscategorized as PI-10** — It does not register a bundled skill, does not follow the naming convention, and serves a fundamentally different purpose (cycle-breaking registry). Should be reclassified to PI-12 (utility-leaf) or a new PI-25 (skill-infrastructure). | src/skills/mcpSkillBuilders.ts |
| P4-01 | P4 | **43% of PI-10 instances are empty stubs** — 3 of 7 files (dream.ts, hunter.ts, runSkillGenerator.ts) are no-op functions with zero implementation. These inflate the pattern's file count without contributing to pattern understanding. | src/skills/bundled/{dream,hunter,runSkillGenerator}.ts |
| P4-02 | P4 | **verify.ts USER_TYPE gate is hardcoded** — `process.env.USER_TYPE !== 'ant'` is a compile-time-style check at runtime. No fallback or documentation for non-ant users who might want verify functionality. | src/skills/bundled/verify.ts:L17 |

## Open Questions

1. **[Runtime] Stub activation timeline**: When will dream.ts, hunter.ts, and runSkillGenerator.ts be implemented? Are they actively being developed or permanently reserved?

2. **[Configuration] USER_TYPE scope**: How many other bundled skills use the `process.env.USER_TYPE` gate? Is this a standard pattern for Anthropic-internal features, or specific to verify?

3. **[Classification] mcpSkillBuilders.ts**: Should this file be reclassified out of PI-10? Its architectural purpose is fundamentally different from bundled skill registration. (Recommend: move to PI-12 utility-leaf or create new PI)

## Complexity Assessment

| Dimension | Rating | Justification |
|-----------|--------|---------------|
| File count | TRIVIAL | 7 files, 124 total lines |
| Pattern consistency | LOW | 4 sub-types, 1 deviation |
| Code complexity | TRIVIAL | Max 44 lines per file, median 1 line |
| Cross-instance coupling | TRIVIAL | Zero cross-imports (verify→verifyContent is data, not pattern) |
| External dependencies | LOW | claudeInChrome.ts depends on external npm + internal utils |

**Overall Complexity: TRIVIAL**

PI-10 is the second-simplest pattern in the project after PI-14 (misc-leaf, 2 files). The combination of 43% empty stubs and a max file size of 44 lines makes this pattern straightforward to understand. The only notable complexity is the mcpSkillBuilders.ts misclassification.
