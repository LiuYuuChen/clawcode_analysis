<!-- analysis-version: 0 | commit: a5179f6 | updated: 2026-04-19 | mode: full | task: T-23 -->
# T-23 Analysis: Pattern Audit — react-hook (PI-03)

## Scope Confirmation
- Task ID: T-23
- Primary Mainline: ML-07 (TUI Rendering & Interaction)
- ML Priority: P3
- Analysis Depth: OVERVIEW
- Pattern Coverage: PI-03 (react-hook)
- Scope Files (confirmed):
  - [`src/hooks/useBlink.ts`](/src/src/hooks/useBlink.ts) (34 lines) ✅
  - [`src/hooks/useChromeExtensionNotification.tsx`](/src/src/hooks/useChromeExtensionNotification.tsx) (49 lines) ✅
  - [`src/hooks/useDynamicConfig.ts`](/src/src/hooks/useDynamicConfig.ts) (22 lines) ✅
- Scope adjustments: None. PI-03 has 14 catalog instances. All will be fully verified (14 ≤ 20 threshold for full verification).
- Rationale: PI-03 audit task, verifying all catalog instances conform to the react-hook pattern.
- Dependencies: T-10 (TUI main interface — already completed)

## File Roles

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| src/hooks/useBlink.ts | 34 | Synchronized cursor blink animation hook — derives visibility from shared animation clock via useAnimationFrame; pauses when terminal blurred or disabled | OVERVIEW: § Pattern Audit |
| src/hooks/useChromeExtensionNotification.tsx | 49 | Chrome extension startup notification — checks Claude in Chrome eligibility/subscription/installation status and shows appropriate notification via useStartupNotification | OVERVIEW: § Pattern Audit |
| src/hooks/useDynamicConfig.ts | 22 | GrowthBook dynamic config value hook — returns default initially, async resolves via getDynamicConfig_BLOCKS_ON_INIT, skips in test env | OVERVIEW: § Pattern Audit |
| src/hooks/useElapsedTime.ts | 37 | Elapsed time formatter using useSyncExternalStore — interval-based re-render with formatDuration; supports pause subtraction and end-time freezing | OVERVIEW: § Pattern Audit |
| src/hooks/useExitOnCtrlCDWithKeybindings.ts | 24 | Convenience combinator wiring useExitOnCtrlCD with useKeybindings; exists to avoid import cycles between exit-handling and keybindings modules | OVERVIEW: § Pattern Audit |
| src/hooks/useIdeConnectionStatus.ts | 33 | IDE MCP client status selector — finds 'ide' named client in MCP connections, returns connected/pending/disconnected status with IDE name extraction | OVERVIEW: § Pattern Audit |
| src/hooks/useMemoryUsage.ts | 39 | Memory monitor polling process.memoryUsage() every 10s via useInterval — returns null when normal (bails re-render), warns at 1.5GB heap, critical at 2.5GB | OVERVIEW: § Pattern Audit |
| src/hooks/useMinDisplayTime.ts | 35 | Display value throttle — guarantees each distinct value visible for minMs before replacement; prevents fast-cycling progress text flicker | OVERVIEW: § Pattern Audit |
| src/hooks/useOfficialMarketplaceNotification.tsx | 47 | Official marketplace auto-install startup notification — checks/installs marketplace plugin, shows success/failure/config-save-error notifications | OVERVIEW: § Pattern Audit |
| src/hooks/useSettings.ts | 17 | Thin reactive settings accessor — wraps useAppState selector for s.settings; replaces getSettings_DEPRECATED() in React components | OVERVIEW: § Pattern Audit |
| src/hooks/useSettingsChange.ts | 25 | Settings file change subscription hook — bridges settingsChangeDetector events to React effect lifecycle; reads fresh settings on each change | OVERVIEW: § Pattern Audit |
| src/hooks/useTimeout.ts | 14 | Simple boolean timeout hook — returns true after delay ms; supports resetTrigger for re-arming | OVERVIEW: § Pattern Audit |
| src/hooks/useUpdateNotification.ts | 34 | Version update notification deduplicator — compares semver-stripped version strings, returns new version on first-seen update only | OVERVIEW: § Pattern Audit |
| src/hooks/useVoiceEnabled.ts | 25 | Voice feature gate — combines user intent (settings.voiceEnabled) + OAuth auth check (memoized on authVersion) + GrowthBook kill-switch into single boolean | OVERVIEW: § Pattern Audit |

## Analysis Findings

**F-01** — **5 sub-types identified**: The 14 catalog instances cluster into 5 functional sub-types:
1. **UI Effect hooks** (3): useBlink, useMinDisplayTime, useTimeout — pure React effect primitives
2. **Startup Notification hooks** (3): useChromeExtensionNotification, useOfficialMarketplaceNotification, useUpdateNotification — all use useStartupNotification pattern
3. **State Selector hooks** (4): useSettings, useSettingsChange, useVoiceEnabled, useDynamicConfig — thin wrappers over AppState/external state
4. **Status Monitor hooks** (2): useIdeConnectionStatus, useMemoryUsage — poll/derive system status
5. **Combinator hooks** (2): useExitOnCtrlCDWithKeybindings, useElapsedTime — compose other hooks/utilities

**F-02** — **Extreme size uniformity**: Lines range 14-49, mean=31.1, median=34. All are small, focused, single-responsibility hooks. No file exceeds 50 lines.

**F-03** — **useStartupNotification pattern**: 3 hooks (ChromeExtension, OfficialMarketplace, and implicitly UpdateNotification) share the same registration pattern — call useStartupNotification(async callback) at mount time, callback returns notification objects. This is a recurring sub-pattern within PI-03.

**F-04** — **2 files contain embedded source maps**: useChromeExtensionNotification.tsx and useOfficialMarketplaceNotification.tsx both have base64-encoded inline source maps at the end — these are likely compiled artifacts from a build step.

**F-05** — **useExitOnCtrlCDWithKeybindings exists for import cycle avoidance**: Its JSDoc explicitly states the separation exists "to avoid import cycles — useExitOnCtrlCD.ts doesn't import from the keybindings module directly."

**F-06** — **useSettingsChange has N-way thrashing fix**: The comment at L12-14 documents a cache invalidation bug where N subscribers each cleared the cache, re-read from disk, causing cascading thrashing.

**F-07** — **useMemoryUsage optimization**: Returns null when status is 'normal' to avoid re-rendering the entire Notifications subtree every 10 seconds for the 99%+ of users who never reach 1.5GB heap.

**F-08** — **useVoiceEnabled triple-gate pattern**: Combines user intent + auth check (memoized on authVersion to avoid ~60ms security spawn) + GrowthBook kill-switch. The memoization strategy is performance-critical (documented 180ms total in profile v5).

**F-09** — **Zero cross-imports between catalog instances**: All 14 files import from shared utilities or external modules but never from each other — true catalog homogeneity.

**F-10** — **All exports follow `use*` naming convention**: Every file exports exactly one hook function named `use*` matching its filename, plus optionally helper types and utility functions.

## File Dependency Graph

```mermaid
flowchart LR
    subgraph PI-03 Catalog Instances
        direction TB
        UB[useBlink.ts<br/>34L]
        UCEN[useChromeExt...tsx<br/>49L]
        UDC[useDynamicConfig.ts<br/>22L]
        UET[useElapsedTime.ts<br/>37L]
        UEO[useExitOnCtrlCD...ts<br/>24L]
        UICS[useIdeConn...ts<br/>33L]
        UMU[useMemoryUsage.ts<br/>39L]
        UMDT[useMinDisplayTime.ts<br/>35L]
        UOMN[useOfficialMarket...tsx<br/>47L]
        US[useSettings.ts<br/>17L]
        USC[useSettingsChange.ts<br/>25L]
        UT[useTimeout.ts<br/>14L]
        UUN[useUpdateNotif...ts<br/>34L]
        UVE[useVoiceEnabled.ts<br/>25L]
    end

    UB -->|"imports"| INK["ink.js<br/>(T-10 scope)"]
    UDC -->|"imports"| GB["services/analytics/growthbook.js<br/>(T-09 scope)"]
    UEO -->|"imports"| KB["keybindings/useKeybinding.js<br/>(T-12 scope)"]
    UICS -->|"imports"| MCPT["services/mcp/types.js<br/>(T-08 scope)"]
    UMU -->|"imports"| UHTS["usehooks-ts<br/>(npm)"]
    US -->|"imports"| AS["state/AppState.js<br/>(T-01 scope)"]
    USC -->|"imports"| SCD["utils/settings/changeDetector.js<br/>(T-11 scope)"]
    UVE -->|"imports"| VME["voice/voiceModeEnabled.js<br/>(external)"]
    UET -->|"imports"| FMT["utils/format.js<br/>(shared)"]
```

| Edge | From | To | Type |
|------|------|----|------|
| 1 | useBlink.ts | ink.js | External (T-10 scope) |
| 2 | useChromeExtensionNotification.tsx | utils/auth.js, utils/claudeInChrome/setup.js, hooks/notifs/* | External (mixed) |
| 3 | useDynamicConfig.ts | services/analytics/growthbook.js | External (T-09 scope) |
| 4 | useElapsedTime.ts | utils/format.js | External (shared utility) |
| 5 | useExitOnCtrlCDWithKeybindings.ts | keybindings/useKeybinding.js, hooks/useExitOnCtrlCD.js | External (T-12 scope) |
| 6 | useIdeConnectionStatus.ts | services/mcp/types.js | External (T-08 scope) |
| 7 | useMemoryUsage.ts | usehooks-ts (npm) | External (npm) |
| 8 | useMinDisplayTime.ts | react | External (npm) |
| 9 | useOfficialMarketplaceNotification.tsx | utils/plugins/officialMarketplaceStartupCheck.js, hooks/notifs/* | External (T-17 scope) |
| 10 | useSettings.ts | state/AppState.js | External (T-01 scope) |
| 11 | useSettingsChange.ts | utils/settings/changeDetector.js | External (T-11 scope) |
| 12 | useVoiceEnabled.ts | state/AppState.js, voice/voiceModeEnabled.js | External (T-01 scope + external) |

## Pattern Contract

**PI-03: react-hook** — Files matching `use*.ts(x)` in `src/hooks/` implementing React hooks for UI state and effects.

### Shared Characteristics

| Convention | Description | Verified |
|-----------|-------------|----------|
| File naming use*.ts(x) | All files match `use{Name}.ts` or `use{Name}.tsx` | ✅ All 14 |
| Single hook export | Each file exports exactly one hook function matching filename | ✅ All 14 |
| Small file size | 14-49 lines, all ≤ 50 lines | ✅ All 14 |
| Zero cross-imports | No catalog instance imports another catalog instance | ✅ All 14 |
| Single responsibility | Each hook does one focused thing | ✅ All 14 |
| React dependency | All import from 'react' or use React patterns (useState/useEffect/useMemo/useCallback/useSyncExternalStore) | ✅ All 14 |

### Sub-types

| Sub-type | Count | Files |
|----------|-------|-------|
| ui-effect | 3 | useBlink, useMinDisplayTime, useTimeout |
| startup-notification | 3 | useChromeExtensionNotification, useOfficialMarketplaceNotification, useUpdateNotification |
| state-selector | 4 | useSettings, useSettingsChange, useVoiceEnabled, useDynamicConfig |
| status-monitor | 2 | useIdeConnectionStatus, useMemoryUsage |
| combinator | 2 | useExitOnCtrlCDWithKeybindings, useElapsedTime |

## Pattern Audit: Full Verification (14/14 = 100%)

| # | File | Lines | Verified | Pass | Notes |
|---|------|-------|----------|------|-------|
| 1 | useBlink.ts | 34 | ✅ | ✅ | Synced blink via useAnimationFrame + terminal focus. Fits pattern. |
| 2 | useChromeExtensionNotification.tsx | 49 | ✅ | ✅ | Chrome extension eligibility checker + startup notification. Fits pattern. |
| 3 | useDynamicConfig.ts | 22 | ✅ | ✅ | GrowthBook config async resolver. Fits pattern. |
| 4 | useElapsedTime.ts | 37 | ✅ | ✅ | useSyncExternalStore + interval for time display. Fits pattern. |
| 5 | useExitOnCtrlCDWithKeybindings.ts | 24 | ✅ | ✅ | Combinator for exit+keybindings. Fits pattern. |
| 6 | useIdeConnectionStatus.ts | 33 | ✅ | ✅ | MCP IDE client status selector. Fits pattern. |
| 7 | useMemoryUsage.ts | 39 | ✅ | ✅ | Memory polling via useInterval with bail optimization. Fits pattern. |
| 8 | useMinDisplayTime.ts | 35 | ✅ | ✅ | Display throttle with setTimeout. Fits pattern. |
| 9 | useOfficialMarketplaceNotification.tsx | 47 | ✅ | ✅ | Marketplace auto-install + startup notification. Fits pattern. |
| 10 | useSettings.ts | 17 | ✅ | ✅ | Thin AppState selector for settings. Fits pattern. |
| 11 | useSettingsChange.ts | 25 | ✅ | ✅ | Settings change detector subscription. Fits pattern. |
| 12 | useTimeout.ts | 14 | ✅ | ✅ | Simple boolean timeout with reset. Fits pattern. |
| 13 | useUpdateNotification.ts | 34 | ✅ | ✅ | Semver deduplication for version updates. Fits pattern. |
| 14 | useVoiceEnabled.ts | 25 | ✅ | ✅ | Triple-gate voice feature flag. Fits pattern. |

**Pass rate**: 14/14 = **100%**

**Deviations**: None. All instances conform to the pattern contract.

## inferred vs verified Statistics

| Metric | Value |
|--------|-------|
| Total PI-03 catalog instances | 14 |
| Verified by T-23 | 14 (100%) |
| Remaining inferred | 0 |
| Verification confidence | **COMPLETE** — all instances directly read and verified |

## Acceptance Criteria Status

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | All scope files analyzed | ✅ PASS | 3/3 scope files + 11 additional catalog instances read in full |
| 2 | Pattern contract documented | ✅ PASS | § Pattern Contract: 6 conventions + 5 sub-types |
| 3 | Sample verification ≥ min(5, total) | ✅ PASS | 14/14 = 100% (full verification) |
| 4 | instance-manifest.jsonl updated | ✅ PASS | All 14 instances: role_source→verified, verified_by→T-23 |
| 5 | File Roles complete | ✅ PASS | 14 rows = 14 catalog instances |
| 6 | Dependency graph generated | ✅ PASS | § File Dependency Graph (mermaid + 12 edges) |
| 7 | Problems and open questions identified | ✅ PASS | § Identified Problems, § Open Questions |

## Identified Problems

| ID | Severity | Description | file:line |
|----|----------|-------------|-----------|
| P3-01 | P3 | useChromeExtensionNotification.tsx contains hardcoded `true &&` condition (L23) — likely a leftover from a feature flag removal that should be cleaned up | useChromeExtensionNotification.tsx:L23 |
| P4-01 | P4 | 2 files (useChromeExtensionNotification.tsx, useOfficialMarketplaceNotification.tsx) contain embedded base64 source maps — these should not be in version control as they bloat file size by ~40% | useChromeExtensionNotification.tsx, useOfficialMarketplaceNotification.tsx |
| P4-02 | P4 | useUpdateNotification.ts uses MACRO.VERSION (build-time substitution) which is not a standard React pattern — the value is baked at build time, not reactive | useUpdateNotification.ts:L18 |

## Open Questions

1. **Why do 2 .tsx files have inline source maps?** — useChromeExtensionNotification.tsx and useOfficialMarketplaceNotification.tsx end with base64-encoded `# sourceMappingURL=data:application/json...`. This suggests they were compiled from TSX but the source maps were not stripped. Other .tsx files (e.g., useTypeahead.tsx) don't have this. (build process question)

2. **PI-03 has 52 total files but only 14 catalog instances** — the remaining 38 files were assigned `standard` trace mode (lines > 50) and analyzed in T-10/T-11/T-12. Are the 14 catalog instances truly "simple enough" or should any have been upgraded? (design decision — all are ≤49L, so the lines>50 threshold correctly excluded them)

3. **useStartupNotification sub-pattern** — 3 hooks share the same registration pattern via useStartupNotification. This could be its own sub-pattern (startup-notification-hook) for more granular classification. (classification decision)

4. **useSettingsChange uses getSettings_DEPRECATED()** — The hook name suggests it bridges legacy code. Should new components use useSettings() exclusively? (depends on T-10/T-11 analysis)

## Complexity Assessment

| Dimension | Rating | Justification |
|-----------|--------|---------------|
| Code complexity | TRIVIAL | 435 total lines; max 49 lines per file |
| Pattern homogeneity | HIGH | All follow use* naming + single export + small size |
| Risk level | NONE | Stateless utility hooks; no mutable module state |
| Integration surface | LOW | 12 external import edges to well-known modules |
| Overall | **TRIVIAL** | Smallest average file size in the project; highly uniform pattern |
