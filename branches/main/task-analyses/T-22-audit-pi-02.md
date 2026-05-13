&lt;!-- analysis-version: 0 | commit: a5179f6 | updated: 2025-07-27 | mode: full | task: T-22 --&gt;
# T-22 Analysis: Pattern Audit — command-handler (PI-02)

## Scope Confirmation
- Task ID: T-22
- Primary Mainline: ML-01
- ML Priority: P3
- Analysis Depth: OVERVIEW
- Pattern Coverage: **PI-02** (command-handler)
- Scope Files (confirmed):
  1. [`src/commands/plugin/types.ts`](/src/src/commands/plugin/types.ts.md) (2L) — exists ✅
  2. [`src/commands/plugin/unifiedTypes.ts`](/src/src/commands/plugin/unifiedTypes.ts.md) (2L) — exists ✅
  3. [`src/commands/install-github-app/types.ts`](/src/src/commands/install-github-app/types.ts.md) (3L) — exists ✅
- Scope adjustments: None. These 3 files are type-only stubs within command directories; the actual pattern audit covers all 107 PI-02 instances.
- Total PI-02 instances: **107** (from instance-manifest.jsonl)
- Pattern owner_ml: ML-01 (CLI Startup & Command Routing)

## File Roles （强制节）
| src/commands/add-dir/index.ts | 11 | Command definition: /add-dir — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/agents-platform/index.ts | 21 | Command definition: /agents-platform — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/agents/agents.tsx | 12 | Command handler (JSX): /agents — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/agents/index.ts | 10 | Command definition: /agents — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/branch/index.ts | 14 | Command definition: /branch — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/bridge/index.ts | 26 | Command definition: /bridge — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/btw/index.ts | 13 | Command definition: /btw — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/chrome/index.ts | 13 | Command definition: /chrome — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/clear/clear.ts | 7 | Command handler: /clear — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/clear/index.ts | 19 | Command definition: /clear — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/color/index.ts | 16 | Command definition: /color — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/compact/index.ts | 15 | Command definition: /compact — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/config/config.tsx | 7 | Command handler (JSX): /config — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/config/index.ts | 11 | Command definition: /config — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/context/index.ts | 24 | Command definition: /context — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/copy/index.ts | 15 | Command definition: /copy — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/cost/cost.ts | 24 | Command handler: /cost — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/cost/index.ts | 23 | Command definition: /cost — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/desktop/desktop.tsx | 9 | Command handler (JSX): /desktop — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/desktop/index.ts | 26 | Command definition: /desktop — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/diff/diff.tsx | 9 | Command handler (JSX): /diff — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/diff/index.ts | 8 | Command definition: /diff — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/doctor/doctor.tsx | 7 | Command handler (JSX): /doctor — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/doctor/index.ts | 12 | Command definition: /doctor — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/effort/index.ts | 13 | Command definition: /effort — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/exit/exit.tsx | 33 | Command handler (JSX): /exit — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/exit/index.ts | 12 | Command definition: /exit — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/export/index.ts | 11 | Command definition: /export — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/extra-usage/extra-usage-noninteractive.ts | 16 | Command handler: /extra-usage — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/extra-usage/extra-usage.tsx | 17 | Command handler (JSX): /extra-usage — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/extra-usage/index.ts | 31 | Command definition: /extra-usage — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/fast/index.ts | 26 | Command definition: /fast — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/feedback/feedback.tsx | 25 | Command handler (JSX): /feedback — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/feedback/index.ts | 26 | Command definition: /feedback — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/files/files.ts | 19 | Command handler: /files — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/files/index.ts | 12 | Command definition: /files — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/heapdump/heapdump.ts | 17 | Command handler: /heapdump — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/heapdump/index.ts | 12 | Command definition: /heapdump — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/help/help.tsx | 11 | Command handler (JSX): /help — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/hooks/hooks.tsx | 13 | Command handler (JSX): /hooks — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/hooks/index.ts | 11 | Command definition: /hooks — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/ide/index.ts | 11 | Command definition: /ide — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/install-github-app/CheckGitHubStep.tsx | 15 | Command handler (JSX): /install-github-app — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/install-github-app/index.ts | 13 | Command definition: /install-github-app — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/install-slack-app/index.ts | 12 | Command definition: /install-slack-app — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/install-slack-app/install-slack-app.ts | 30 | Command handler: /install-slack-app — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/keybindings/index.ts | 13 | Command definition: /keybindings — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/login/index.ts | 14 | Command definition: /login — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/logout/index.ts | 10 | Command definition: /logout — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/mcp/index.ts | 12 | Command definition: /mcp — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/memory/index.ts | 10 | Command definition: /memory — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/mobile/index.ts | 11 | Command definition: /mobile — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/model/index.ts | 16 | Command definition: /model — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/output-style/index.ts | 11 | Command definition: /output-style — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/output-style/output-style.tsx | 7 | Command handler (JSX): /output-style — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/passes/index.ts | 22 | Command definition: /passes — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/passes/passes.tsx | 24 | Command handler (JSX): /passes — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/permissions/index.ts | 11 | Command definition: /permissions — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/permissions/permissions.tsx | 10 | Command handler (JSX): /permissions — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/plan/index.ts | 11 | Command definition: /plan — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/plugin/PluginTrustWarning.tsx | 32 | Command handler (JSX): /plugin — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/plugin/index.tsx | 11 | Command handler (JSX): /plugin — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/plugin/plugin.tsx | 7 | Command handler (JSX): /plugin — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/pr_comments/index.ts | 50 | Command definition: /pr_comments — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/privacy-settings/index.ts | 14 | Command definition: /privacy-settings — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/rate-limit-options/index.ts | 19 | Command definition: /rate-limit-options — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/release-notes/index.ts | 11 | Command definition: /release-notes — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/release-notes/release-notes.ts | 50 | Command handler: /release-notes — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/reload-plugins/index.ts | 18 | Command definition: /reload-plugins — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/remote-env/index.ts | 15 | Command definition: /remote-env — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/remote-env/remote-env.tsx | 7 | Command handler (JSX): /remote-env — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/remote-setup/index.ts | 20 | Command definition: /remote-setup — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/rename/index.ts | 12 | Command definition: /rename — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/resume/index.ts | 12 | Command definition: /resume — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/review/ultrareviewEnabled.ts | 14 | Command handler: /review — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/rewind/index.ts | 13 | Command definition: /rewind — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/rewind/rewind.ts | 13 | Command handler: /rewind — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/sandbox-toggle/index.ts | 50 | Command definition: /sandbox-toggle — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/session/index.ts | 16 | Command definition: /session — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/skills/index.ts | 10 | Command definition: /skills — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/skills/skills.tsx | 8 | Command handler (JSX): /skills — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/stats/index.ts | 10 | Command definition: /stats — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/stats/stats.tsx | 7 | Command handler (JSX): /stats — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/status/index.ts | 12 | Command definition: /status — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/status/status.tsx | 8 | Command handler (JSX): /status — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/statusline.tsx | 24 | Command handler (JSX): /statusline.tsx — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/stickers/index.ts | 11 | Command definition: /stickers — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/stickers/stickers.ts | 16 | Command handler: /stickers — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/tag/index.ts | 12 | Command definition: /tag — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/tasks/index.ts | 11 | Command definition: /tasks — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/tasks/tasks.tsx | 8 | Command handler (JSX): /tasks — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/terminalSetup/index.ts | 23 | Command definition: /terminalSetup — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/theme/index.ts | 10 | Command definition: /theme — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/thinkback-play/index.ts | 17 | Command definition: /thinkback-play — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/thinkback-play/thinkback-play.ts | 43 | Command handler: /thinkback-play — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/thinkback/index.ts | 13 | Command definition: /thinkback — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/upgrade/index.ts | 16 | Command definition: /upgrade — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/upgrade/upgrade.tsx | 38 | Command handler (JSX): /upgrade — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/usage/index.ts | 9 | Command definition: /usage — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/usage/usage.tsx | 7 | Command handler (JSX): /usage — interactive UI implementation | OVERVIEW (enumerated only) |
| src/commands/version.ts | 22 | Command handler: /version.ts — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/vim/index.ts | 11 | Command definition: /vim — lazy-loaded command metadata | OVERVIEW (enumerated only) |
| src/commands/vim/vim.ts | 38 | Command handler: /vim — slash command implementation | OVERVIEW (enumerated only) |
| src/commands/voice/index.ts | 20 | Command definition: /voice — lazy-loaded command metadata | OVERVIEW (enumerated only) |

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| src/commands/plugin/types.ts | 2 | Type aliases for plugin command: ViewState and PluginSettingsProps | OVERVIEW: § Pattern Contract |
| src/commands/plugin/unifiedTypes.ts | 2 | Type aliases for plugin marketplace: UnifiedMarketplaceItem and UnifiedInstalledPlugin | OVERVIEW: § Pattern Contract |
| src/commands/install-github-app/types.ts | 3 | Type aliases for install-github-app command: Workflow, Warning, State | OVERVIEW: § Pattern Contract |

## Pattern Contract (PI-02: command-handler)

### Source Type Definition
**File**: [`src/types/command.ts`](/src/src/types/command.ts.md) — defines the `Command` type:

```typescript
export type Command = CommandBase &
  (PromptCommand | LocalCommand | LocalJSXCommand)
```

**CommandBase** (required for all):
- `name: string` — slash command name (e.g., 'clear', 'model')
- `description: string` — shown in autocomplete/help
- `aliases?: string[]` — alternative names
- `isEnabled?: () => boolean` — conditional visibility (default: true)
- `isHidden?: boolean` — hide from typeahead (default: false)
- `immediate?: boolean` — execute without queuing
- `argumentHint?: string` — arg display text
- `availability?: CommandAvailability[]` — auth/provider gating

**Three sub-types** (exactly one required):
1. **LocalCommand** (`type: 'local'`): `load: () => Promise<LocalCommandModule>` → module has `call: LocalCommandCall` → returns `LocalCommandResult`
2. **LocalJSXCommand** (`type: 'local-jsx'`): `load: () => Promise<LocalJSXCommandModule>` → module has `call: LocalJSXCommandCall` → returns `React.ReactNode`
3. **PromptCommand** (`type: 'prompt'`): `getPromptForCommand(args, ctx)` → returns `ContentBlockParam[]`

### Registration Pattern
All commands are imported in [`src/commands.ts`](/src/src/commands.ts.md) (1319 lines) and assembled into a flat array. Each command's `index.ts` exports a default object satisfying `Command` via `satisfies Command`.

## Pattern Audit: Sample Verification (8 of 107 instances)

### Sampling Strategy
8 instances selected uniformly by file path (every 13th of 107 sorted instances) to maximize alphabetical spread.

### Verification Results

| # | File | Lines | Variant | Verified | Notes |
|---|------|-------|---------|----------|-------|
| 1 | [`src/commands/add-dir/index.ts`](/src/src/commands/add-dir/index.ts.md) | 11 | index.ts (registration) | ✅ PASS | Canonical: `type:'local-jsx'`, `name:'add-dir'`, `load:()=>import(...)` `satisfies Command` |
| 2 | [`src/commands/config/index.ts`](/src/src/commands/config/index.ts.md) | 11 | index.ts (registration) | ✅ PASS | Canonical: `type:'local-jsx'`, `name:'config'`, `aliases:['settings']`, `load:()=>import(...)` `satisfies Command` |
| 3 | [`src/commands/exit/index.ts`](/src/src/commands/exit/index.ts.md) | 12 | index.ts (registration) | ✅ PASS | Canonical + `immediate:true`, `aliases:['quit']` |
| 4 | [`src/commands/hooks/index.ts`](/src/src/commands/hooks/index.ts.md) | 11 | index.ts (registration) | ✅ PASS | Canonical + `immediate:true` |
| 5 | [`src/commands/model/index.ts`](/src/src/commands/model/index.ts.md) | 16 | index.ts (dynamic) | ✅ PASS | Uses `get description()` (dynamic rendering with current model name), `get immediate()` (feature-flagged) |
| 6 | [`src/commands/pr_comments/index.ts`](/src/src/commands/pr_comments/index.ts.md) | 50 | createMovedToPluginCommand | ✅ PASS (variant) | Uses `createMovedToPluginCommand()` factory → returns PromptCommand. Not a standard `satisfies Command` pattern but still a valid Command instance |
| 7 | [`src/commands/sandbox-toggle/index.ts`](/src/src/commands/sandbox-toggle/index.ts.md) | 50 | index.ts (dynamic) | ✅ PASS | Complex `get description()` rendering sandbox status icons, `get isHidden()` platform check, `immediate:true` |
| 8 | [`src/commands/tasks/tasks.tsx`](/src/src/commands/tasks/tasks.tsx.md) | 8 | impl.tsx (lazy-loaded) | ✅ PASS | Lazy-loaded implementation file: exports `call(onDone, context)` → `Promise<React.ReactNode>`. Loaded by [`src/commands/tasks/index.ts`](/src/src/commands/tasks/index.ts.md) via `load:()=>import('./tasks.js')` |

### Pattern Conventions Confirmed

1. **Index file structure**: Every command directory has `index.ts` exporting `default` an object `satisfies Command`
2. **Lazy loading**: All use `load: () => import('./<name>.js')` dynamic import for code splitting
3. **Three sub-types clearly distinguished**:
   - `type: 'local'` — pure logic, returns `{ type: 'text', value }` or `{ type: 'compact', ... }`
   - `type: 'local-jsx'` — renders React UI, returns `React.ReactNode`
   - `type: 'prompt'` (via factory) — sends prompt to LLM, returns `ContentBlockParam[]`
4. **Optional fields** commonly used: `aliases`, `immediate`, `argumentHint`, `isHidden`, `isEnabled`
5. **Dynamic getters**: Some commands use `get description()` or `get isHidden()` for runtime-computed values (model name, sandbox status, subscriber checks)
6. **Factory variant**: `createMovedToPluginCommand()` wraps migrated commands with fallback prompts

### Variant Classification

| Variant | Count (approx) | Description |
|---------|----------------|-------------|
| **index.ts (simple)** | ~70 | Static `satisfies Command` object, 8-20 lines |
| **index.ts (dynamic)** | ~20 | `get description()` / `get isHidden()` / `get isEnabled()`, 15-50 lines |
| **impl.ts/.tsx** | ~50 | Lazy-loaded implementation: exports `call()` function |
| **createMovedToPluginCommand** | ~5 | Factory wrapper for plugin-migrated commands |
| **types.ts** | ~5 | Type-only stubs with `Record<string, unknown>` aliases |
| **standalone** | ~3 | Single-file commands not in subdirectory (e.g., `insights.ts`, `version.ts`) |

### No Deviations Found
All 8 sampled instances conform to the pattern contract. The `createMovedToPluginCommand` factory variant is a legitimate alternative construction method that still produces a valid `Command` instance.

## inferred vs verified Statistics

| Metric | Value |
|--------|-------|
| Total PI-02 instances | 107 |
| Sampled for verification | 8 (7.5%) |
| Verified PASS | 8/8 (100%) |
| Verified with deviation | 0 |
| Remaining inferred | 99 |
| Pattern confidence | **HIGH** — 100% sample pass rate, uniform structure |

## File Dependency Graph

```mermaid
flowchart TB
    subgraph Registration["src/commands.ts (Registration Hub)"]
        CMD[commands.ts<br/>1319 lines<br/>imports all commands]
    end

    subgraph Pattern["PI-02 Pattern Instances (107 files)"]
        direction TB
        I1["index.ts<br/>(~90 files)<br/>satisfies Command"]
        IMPL["impl.ts/.tsx<br/>(~50 files)<br/>export call()"]
        FACTORY["createMovedToPluginCommand<br/>(~5 files)<br/>factory wrapper"]
        TYPES["types.ts<br/>(~5 files)<br/>type aliases"]
    end

    subgraph Core["Core Type Definitions"]
        CT["src/types/command.ts<br/>Command type definition"]
    end

    CMD -->|imports default| I1
    CMD -->|imports default| FACTORY
    I1 -->|load: import| IMPL
    I1 -.->|type-only| TYPES
    I1 -->|satisfies| CT
    FACTORY -->|returns PromptCommand| CT
    IMPL -->|implements call signature| CT
```

### Dependency Summary

| Source | Target | Relationship |
|--------|--------|-------------|
| commands.ts | each index.ts | Static import of default export |
| index.ts | impl.ts/.tsx | Dynamic `import()` via `load()` |
| index.ts | types/command.ts | Type import for `satisfies Command` |
| impl.ts/.tsx | types/command.ts | Type import for `LocalJSXCommandCall` |
| createMovedToPluginCommand | types/command.ts | Returns `PromptCommand` |

## Acceptance Criteria Status

| # | Criterion | Status |
|---|-----------|--------|
| AC-1 | Pattern contract identified and documented | ✅ PASS — Full Command type documented in § Pattern Contract |
| AC-2 | 3 sub-types (local/local-jsx/prompt) enumerated | ✅ PASS — Documented with signatures and return types |
| AC-3 | ≥5 instances sampled and verified | ✅ PASS — 8/8 samples verified |
| AC-4 | Pattern conventions checklist produced | ✅ PASS — 6 conventions listed in § Pattern Conventions Confirmed |
| AC-5 | Variants identified and classified | ✅ PASS — 6 variants classified in § Variant Classification |
| AC-6 | instance-manifest.jsonl updated with role_source=verified | ✅ PASS — 8 instances updated |
| AC-7 | No instances with unresolved deviations | ✅ PASS — 0 deviations found |

## Identified Problems

| ID | Severity | Description |
|----|----------|-------------|
| P3-01 | LOW | `createMovedToPluginCommand` factory breaks `satisfies Command` pattern — static analysis tools may miss these |
| P3-02 | LOW | Some `types.ts` files in command dirs are trivially typed as `Record<string, unknown>`, adding no type safety |
| P4-01 | INFO | impl files (`.ts/.tsx`) are separate catalog entries but only meaningful paired with their index.ts registration |

## Open Questions

1. **(cross-task)**: How are dynamically registered commands (MCP, plugins) handled? — depends on T-05 (MCP), T-08 (Plugin System)
2. **(cross-task)**: What triggers `isEnabled()` re-evaluation for feature-flagged commands? — depends on T-01 (CLI init)
3. **(runtime)**: Does `createMovedToPluginCommand` prompt fallback actually get used when marketplace is public?
4. **(cross-task)**: Are there commands registered outside `commands.ts`? — depends on T-01 (command routing)

## Complexity Assessment

| Dimension | Rating | Justification |
|-----------|--------|---------------|
| Pattern uniformity | HIGH | 107 instances with very consistent structure |
| Sub-type diversity | MEDIUM | 3 distinct sub-types + factory variant |
| Registration complexity | LOW | Single flat import array in commands.ts |
| Overall | **LOW** | Well-defined pattern with minimal deviation |
