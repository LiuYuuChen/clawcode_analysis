&lt;!-- analysis-version: 0 | commit: a5179f6588dd03cbe83a8d8b718a61875dba7b24 | updated: 2025-07-14 | mode: re-execute | task: T-17 --&gt;
# T-17 Analysis: Plugin System

## Scope Confirmation
- Task ID: T-17
- Primary Mainline: ML-12 (Plugin System)
- ML Priority: P2
- Analysis Depth: STANDARD
- Secondary Mainlines: ML-01 (commands), ML-03 (tools), ML-05 (MCP)
- Pattern Coverage: PI-10 (bundled-skill, 22 instances — catalog, not in scope)
- Scope Files (confirmed): 65 files, 29,370 lines, **0 missing**
- Scope adjustments: None — all 65 files physically exist and are readable
- Re-execute reason: FAIL_0 (physical file missing — created from scratch)
- Dependencies: T-08 (MCP Service Integration)

## File Roles

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| src/utils/plugins/pluginLoader.ts | 3302 | Core orchestrator: discovers/loads/validates/caches plugins from marketplaces and git repos; `loadAllPlugins` (memoized) is main entry | § Analysis Findings, § Call Chain |
| src/utils/plugins/marketplaceManager.ts | 2643 | Marketplace lifecycle: register/clone/sparse-checkout/pull/refresh marketplace repos; memoized `getMarketplace` | § Analysis Findings, § Call Chain |
| src/utils/plugins/schemas.ts | 1681 | Zod validation schemas for manifests/sources/hooks; homoglyph attack protection; official name registry | § Analysis Findings |
| src/utils/plugins/installedPluginsManager.ts | 1268 | V2 persistence layer: load/save installed plugins to `installed_plugins.json`; migration from V1; pending updates tracking | § Analysis Findings, § State Transition |
| src/services/plugins/pluginOperations.ts | 1088 | Operation layer: install/uninstall/enable/disable/update with scope (user/project/local) and dependency resolution | § Call Chain, § Error Propagation |
| src/commands/plugin/ManagePlugins.tsx | 2215 | Interactive TUI for managing plugins: search/install/uninstall/update/enable/disable with Ink components | § Boundary/Integration |
| src/utils/plugins/loadPluginCommands.ts | 946 | Loads plugin commands (`.md` slash commands) via `walkPluginMarkdown`; memoized `getPluginCommands` and `getPluginSkills` | § Call Chain |
| src/utils/plugins/mcpbHandler.ts | 968 | MCPB package format handler: load/validate/save user config for bundled MCP server packages | § Analysis Findings |
| src/utils/plugins/validatePlugin.ts | 903 | Plugin manifest + contents validation: `validatePluginManifest`, `validateMarketplaceManifest`, `validatePluginContents` | § Error Propagation |
| src/skills/loadSkillsDir.ts | 1086 | Loads skill definitions from plugin skill directories; parses skill.json manifests | § Analysis Findings |
| src/commands/plugin/PluginSettings.tsx | 1072 | Plugin settings TUI panel: display/edit per-plugin options with schema-driven forms | § Boundary/Integration |
| src/utils/plugins/pluginInstallationHelpers.ts | 595 | Installation utilities: `cacheAndRegisterPlugin`, `registerPluginInstallation`, `parsePluginId` | § Call Chain |
| src/utils/plugins/mcpPluginIntegration.ts | 634 | Bridges plugins to MCP service: `loadPluginMcpServers`, `extractMcpServersFromPlugins`, `getUnconfiguredChannels` | § Boundary/Integration |
| src/utils/plugins/marketplaceHelpers.ts | 592 | Marketplace display utilities: `formatFailureDetails`, `createPluginId`, `loadMarketplacesWithGracefulDegradation` | § Error Propagation |
| src/utils/plugins/lspPluginIntegration.ts | 387 | Bridges plugins to LSP servers: `loadPluginLspServers`, `resolvePluginLspEnvironment`, `getPluginLspServers` | § Boundary/Integration |
| src/utils/plugins/lspRecommendation.ts | 374 | Recommends LSP plugins based on detected file types; manages never-suggest list | § Analysis Findings |
| src/utils/plugins/officialMarketplaceStartupCheck.ts | 439 | Startup check: auto-installs official marketplace with retry and GCS fallback | § Call Chain |
| src/utils/plugins/loadPluginAgents.ts | 348 | Loads plugin agent definitions (`.md` agent files) via `walkPluginMarkdown`; memoized | § Call Chain |
| src/services/plugins/pluginCliCommands.ts | 344 | CLI command handlers: install/uninstall/enable/disable/update wrappers calling pluginOperations | § Call Chain |
| src/utils/plugins/dependencyResolver.ts | 305 | Dependency graph: `resolveDependencyClosure`, `findReverseDependents`, `qualifyDependency` | § Analysis Findings |
| src/utils/plugins/installCounts.ts | 292 | Fetches and caches install counts from analytics API; `formatInstallCount` | § Side Effects |
| src/utils/plugins/loadPluginHooks.ts | 287 | Loads plugin hooks (hooks.json); supports hot reload via settings snapshot comparison | § State Transition |
| src/utils/plugins/pluginAutoupdate.ts | 284 | Background auto-update: `updatePluginsForMarketplaces`, `autoUpdateMarketplacesAndPluginsInBackground` | § Temporal Analysis |
| src/utils/plugins/reconciler.ts | 265 | Marketplace reconciliation: `diffMarketplaces`, `reconcileMarketplaces` (detect added/removed/changed plugins) | § Analysis Findings |
| src/skills/bundled/scheduleRemoteAgents.ts | 447 | Bundled skill: schedules remote agents; imports AgentTool patterns | § Analysis Findings |
| src/skills/bundled/loremIpsum.ts | 282 | Bundled skill: generates lorem ipsum text for testing | § Analysis Findings |
| src/utils/plugins/refresh.ts | 215 | Refresh pipeline: `refreshActivePlugins` reloads commands/hooks/agents/output-styles/MCP/LSP in sequence | § Call Chain |
| src/utils/plugins/pluginFlagging.ts | 208 | Plugin flagging system: load/add/remove flagged plugins (security/malware reporting) | § Error Propagation |
| src/utils/plugins/zipCache.ts | 406 | Zip-based cache for marketplaces and installed plugins (offline/air-gapped support) | § Analysis Findings |
| src/utils/plugins/pluginOptionsStorage.ts | 400 | Per-plugin options persistence: load/save options to `~/.claude/plugins/<id>/options.json` | § Data Flow |
| src/utils/plugins/pluginStartupCheck.ts | 341 | Startup checks: `checkEnabledPlugins`, `getPluginEditableScopes`, `getInstalledPlugins` | § Call Chain |
| src/skills/bundled/keybindings.ts | 339 | Bundled skill: manages keybinding configurations | § Analysis Findings |
| src/skills/bundled/updateConfig.ts | 475 | Bundled skill: updates user configuration files | § Analysis Findings |
| src/utils/plugins/cacheUtils.ts | 196 | Cache utilities: `clearAllPluginCaches`, `clearAllCaches`, `cleanupOrphanedPluginVersions` | § Side Effects |
| src/utils/plugins/orphanedPluginFilter.ts | 114 | Generates glob exclusions for orphaned plugin cache directories | § Analysis Findings |
| src/skills/bundled/claudeApi.ts | 196 | Bundled skill: Claude API usage examples and helpers | § Analysis Findings |
| src/utils/plugins/marketplaceHelpers.ts | 592 | (See above — already listed) | — |
| src/utils/plugins/headlessPluginInstall.ts | 174 | Installs plugins from CLI flags in headless/non-interactive mode | § Call Chain |
| src/utils/plugins/loadPluginOutputStyles.ts | 178 | Loads plugin output style definitions via `walkPluginMarkdown`; memoized | § Call Chain |
| src/utils/plugins/pluginDirectories.ts | 178 | Plugin directory paths: `getPluginsDirectory`, `getPluginSeedDirs`, `pluginDataDirPath` | § Analysis Findings |
| src/utils/plugins/parseMarketplaceInput.ts | 162 | Parses user input for marketplace operations (name@marketplace format) | § Analysis Findings |
| src/utils/plugins/zipCacheAdapters.ts | 164 | Zip cache read/write adapters for known-marketplaces file and marketplace JSON | § Analysis Findings |
| src/utils/plugins/pluginVersioning.ts | 157 | Plugin version calculation: git SHA + content hash for cache invalidation | § Data Flow |
| src/utils/plugins/hintRecommendation.ts | 164 | Plugin hint system: records usage hints, resolves recommended plugins | § Analysis Findings |
| src/utils/plugins/fetchTelemetry.ts | 135 | Telemetry logging for plugin fetch operations; error classification | § Side Effects |
| src/utils/plugins/pluginBlocklist.ts | 127 | Detects delisted plugins from marketplace index and auto-uninstalls | § Error Propagation |
| src/utils/plugins/pluginIdentifier.ts | 123 | Plugin ID parsing: `parsePluginIdentifier`, `buildPluginId`, scope-to-source mapping | § Data Flow |
| src/utils/plugins/orphanedPluginFilter.ts | 114 | (See above — already listed) | — |
| src/services/plugins/PluginInstallationManager.ts | 184 | Background installation manager: `performBackgroundPluginInstallations` for pending installs | § Temporal Analysis |
| src/utils/plugins/managedPlugins.ts | 27 | Returns managed (enterprise-controlled) plugin name set from settings | § Analysis Findings |
| src/utils/plugins/officialMarketplace.ts | 25 | Constants: `OFFICIAL_MARKETPLACE_SOURCE` URL and `OFFICIAL_MARKETPLACE_NAME` | § Analysis Findings |
| src/utils/plugins/gitAvailability.ts | 69 | Memoized git availability check; marks git unavailable on failure | § Side Effects |
| src/utils/plugins/walkPluginMarkdown.ts | 69 | Recursively walks plugin dir collecting `.md` files for commands/agents/output-styles | § Call Chain |
| src/utils/plugins/addDirPluginSettings.ts | 71 | Reads `--add-dir` enabled plugin settings for path-scoped plugins | § Analysis Findings |
| src/utils/plugins/officialMarketplaceGcs.ts | 216 | GCS fallback: fetches official marketplace index from Google Cloud Storage | § Call Chain |
| src/utils/plugins/performStartupChecks.tsx | 70 | TUI startup checks: validates enabled plugins and shows errors to user | § Boundary/Integration |
| src/utils/plugins/pluginPolicy.ts | 20 | Single-function policy checker: `isPluginBlockedByPolicy` checks enterprise allow-list | § Analysis Findings |
| src/skills/bundled/batch.ts | 124 | Bundled skill: batch processing of multiple files | § Analysis Findings |
| src/skills/bundled/debug.ts | 103 | Bundled skill: debugging assistance | § Analysis Findings |
| src/skills/bundled/index.ts | 79 | Bundled skill registry: `initializeBundledSkills` registers all bundled skills at startup | § Call Chain |
| src/skills/bundled/remember.ts | 82 | Bundled skill: saves key information to memory files | § Analysis Findings |
| src/skills/bundled/stuck.ts | 79 | Bundled skill: helps when the AI is stuck on a problem | § Analysis Findings |
| src/skills/bundled/simplify.ts | 69 | Bundled skill: simplifies complex code | § Analysis Findings |
| src/skills/bundled/claudeApiContent.ts | 75 | Content type definitions for Claude API bundled skill | § Analysis Findings |
| src/skills/bundled/loop.ts | 92 | Bundled skill: iterative refinement loop | § Analysis Findings |
| src/skills/bundled/skillify.ts | 197 | Bundled skill: creates new skills from user instructions | § Analysis Findings |
| src/skills/bundledSkills.ts | 220 | Bundled skill type definitions and extraction helpers for bundled skill files | § Analysis Findings |

## Analysis Findings

**F-01: Four-Layer Architecture.** The plugin system follows a strict layering: CLI/UI (ManagePlugins.tsx, PluginSettings.tsx, pluginCliCommands.ts) → Service Layer (pluginOperations.ts, PluginInstallationManager.ts, pluginInstallationHelpers.ts) → Core Engine (pluginLoader.ts, marketplaceManager.ts, installedPluginsManager.ts, schemas.ts, validatePlugin.ts, reconciler.ts) → Component Loaders + Utilities (loadPluginCommands/Agents/Hooks/OutputStyles, 30+ utility modules). Commands flow downward; events propagate upward.

**F-02: Memoized Entry Points.** Four critical functions use `lodash.memoize`: `loadAllPlugins` (pluginLoader.ts:L3096), `getMarketplace` (marketplaceManager.ts:L2122), `getPluginCommands` (loadPluginCommands.ts:L414), `getPluginSkills` (loadPluginCommands.ts:L840), `loadPluginAgents` (loadPluginAgents.ts:L231), `loadPluginHooks` (loadPluginHooks.ts:L91), `loadPluginOutputStyles` (loadPluginOutputStyles.ts:L87). Each has a paired `clear*Cache` function. This creates a dual-cache model: lodash memoize (in-process) + disk cache (versioned zip/files).

**F-03: Three Install Sources.** Plugins are installed from: (1) Marketplace repos (git clone + sparse checkout), (2) NPM packages (via marketplace entry, `installFromNpm` at pluginLoader.ts:L492), (3) Git subdirectories (`installFromGitSubdir` at pluginLoader.ts:L718). Session-only plugins from `--plugin-dir` CLI flag bypass installation entirely.

**F-04: V2 Persistence Migration.** installedPluginsManager.ts implements a V1→V2 migration (`migrateFromEnabledPlugins` at L1048). V2 uses a single `installed_plugins.json` with per-installation metadata (scope, marketplace, version hash, timestamps). V1 stored separate `enabled_plugins.json` per scope. The migration is fire-once with a `v2MigrationComplete` flag.

**F-05: Homoglyph Attack Protection.** schemas.ts:L71 defines `BLOCKED_OFFICIAL_NAME_PATTERN = /[\p{Script=Latin}\p{Script=Common}]/u` — plugin names matching official marketplace names are blocked unless they originate from the official source (`validateOfficialNameSource` at L119). This prevents lookalike plugin names using Unicode confusables.

**F-06: Sparse Checkout Optimization.** marketplaceManager.ts:L1034 `reconcileSparseCheckout` uses `git sparse-checkout` to only checkout plugin directories that are actually installed, reducing disk usage for large marketplaces. Falls back to full checkout on error.

**F-07: MCPB Package Format.** mcpbHandler.ts implements a custom `.mcpb` package format for bundled MCP servers. The handler validates `user_config.json` against `UserConfigSchema` (Zod), persists configuration to `~/.claude/mcp_servers/<server_name>/`, and detects changes via `checkMcpbChanged`.

**F-08: Dependency Resolution.** dependencyResolver.ts implements transitive dependency resolution: `resolveDependencyClosure` (L95) recursively resolves plugin dependencies, `findReverseDependents` (L244) identifies plugins that depend on a given plugin (for uninstall safety), `verifyAndDemote` (L177) demotes plugins whose dependencies are missing.

**F-09: Hot Reload for Hooks.** loadPluginHooks.ts:L255 `setupPluginHookHotReload` compares a settings snapshot (`getPluginAffectingSettingsSnapshot`) against the current state on every settings change, and if different, clears the hook cache and reloads. This enables live hook updates without restart.

**F-10: Official Marketplace GCS Fallback.** officialMarketplaceGcs.ts:L47 fetches the official marketplace index from Google Cloud Storage as a fallback when git clone fails. This ensures plugin availability even when GitHub is unreachable. The GCS URL contains a commit SHA for version pinning.

## File Dependency Graph

```mermaid
flowchart TD
    subgraph CLI/UI Layer
        ManagePlugins[ManagePlugins.tsx<br/>2215L]
        PluginSettings[PluginSettings.tsx<br/>1072L]
        PluginCliCmds[pluginCliCommands.ts<br/>344L]
        StartupCheckTUI[performStartupChecks.tsx<br/>70L]
    end

    subgraph Service Layer
        PluginOps[pluginOperations.ts<br/>1088L]
        PluginInstallMgr[PluginInstallationManager.ts<br/>184L]
        PluginInstallHelpers[pluginInstallationHelpers.ts<br/>595L]
    end

    subgraph Core Engine
        PluginLoader[pluginLoader.ts<br/>3302L]
        MarketplaceMgr[marketplaceManager.ts<br/>2643L]
        InstalledPluginsMgr[installedPluginsManager.ts<br/>1268L]
        Schemas[schemas.ts<br/>1681L]
        ValidatePlugin[validatePlugin.ts<br/>903L]
        McpbHandler[mcpbHandler.ts<br/>968L]
        Reconciler[reconciler.ts<br/>265L]
    end

    subgraph Component Loaders
        LoadCmds[loadPluginCommands.ts<br/>946L]
        LoadAgents[loadPluginAgents.ts<br/>348L]
        LoadHooks[loadPluginHooks.ts<br/>287L]
        LoadOutputStyles[loadPluginOutputStyles.ts<br/>178L]
        WalkMD[walkPluginMarkdown.ts<br/>69L]
    end

    subgraph Integrations
        McpIntegration[mcpPluginIntegration.ts<br/>634L]
        LspIntegration[lspPluginIntegration.ts<br/>387L]
        RefreshPipeline[refresh.ts<br/>215L]
    end

    subgraph Bundled Skills
        BundledIndex[bundled/index.ts<br/>79L]
        BundledSkills[bundledSkills.ts<br/>220L]
        LoadSkillsDir[loadSkillsDir.ts<br/>1086L]
    end

    ManagePlugins --> PluginOps
    PluginCliCmds --> PluginOps
    PluginOps --> PluginLoader
    PluginOps --> MarketplaceMgr
    PluginOps --> InstalledPluginsMgr
    PluginOps --> PluginInstallHelpers
    PluginInstallMgr --> Reconciler
    PluginInstallMgr --> RefreshPipeline
    PluginLoader --> Schemas
    PluginLoader --> ValidatePlugin
    PluginLoader --> MarketplaceMgr
    PluginLoader --> InstalledPluginsMgr
    MarketplaceMgr --> Schemas
    RefreshPipeline --> LoadCmds
    RefreshPipeline --> LoadAgents
    RefreshPipeline --> LoadHooks
    RefreshPipeline --> LoadOutputStyles
    RefreshPipeline --> McpIntegration
    RefreshPipeline --> LspIntegration
    LoadCmds --> WalkMD
    LoadAgents --> WalkMD
    LoadOutputStyles --> WalkMD
    LoadCmds --> PluginLoader
    PluginInstallHelpers --> PluginLoader
    McpIntegration -.->|T-08 MCP| ExternalMCP
    LspIntegration -.->|T-11 LSP| ExternalLSP
    BundledIndex --> BundledSkills
    LoadSkillsDir --> PluginLoader
```

**Key Dependency Edges:**

| Source | Target | Relationship |
|--------|--------|-------------|
| PluginOps | PluginLoader | All install/update operations delegate to loader |
| PluginOps | MarketplaceMgr | Marketplace operations (clone/pull/refresh) |
| PluginOps | InstalledPluginsMgr | Persist installation state |
| RefreshPipeline | LoadCmds/Agents/Hooks/Styles | Sequential reload of all components |
| PluginLoader | Schemas | Manifest validation via Zod schemas |
| McpIntegration | External MCP (T-08) | Bridge to MCPConnectionManager |
| MarketplaceMgr | GrowthBook (ML-06) | Feature flag for marketplace features |



## Call Chain Analysis

### Chain 1: Plugin Install Flow (Entry -> Exit)

```
pluginCliCommands.ts:L57 install()
  -> pluginOperations.ts:L321 installPluginOp(pluginId, scope, marketplace)
    -> pluginIdentifier.ts:L45 parsePluginIdentifier(pluginId)
    -> marketplaceManager.ts:L2122 getMarketplace(marketplaceName) [memoized]
    -> pluginOperations.ts:L360 resolvePluginInMarketplace()
    -> pluginInstallationHelpers.ts:L72 cacheAndRegisterPlugin()
      -> pluginLoader.ts:L911 cachePlugin() -> write to ~/.claude/plugins/<id>/
      -> pluginLoader.ts:L492 installFromNpm() | L534 gitClone() | L718 installFromGitSubdir()
    -> installedPluginsManager.ts:L261 saveInstalledPlugins() -> write installed_plugins.json
    -> reconciler.ts:L156 reconcileMarketplaces() -> update sparse-checkout
    -> refresh.ts:L72 refreshActivePlugins() -> reload all active components
```

**Call depth**: 6 levels. **Key branch point**: `cacheAndRegisterPlugin` dispatches to one of three install strategies (npm/git/git-subdir) based on marketplace entry type.

### Chain 2: Plugin Load Flow (Entry -> Exit)

```
refresh.ts:L72 refreshActivePlugins()
  -> cacheUtils.ts:L15 clearAllCaches() -> invalidate all lodash.memoize caches
  -> pluginLoader.ts:L3096 loadAllPlugins() [memoized]
    -> pluginLoader.ts:L2932 assemblePluginLoadResult()
      -> [parallel] loadPluginsFromMarketplaces() -> marketplaceManager -> git sparse-checkout
      -> [parallel] loadSessionPlugins() -> from --plugin-dir CLI flag
      -> [parallel] loadBuiltinPlugins() -> from src/skills/bundled/
    -> pluginLoader.ts:L2800 mergePluginSources() -> deduplicate by plugin ID
    -> pluginLoader.ts:L2840 verifyAndDemote() -> demote plugins with missing deps
    -> pluginLoader.ts:L3080 cachePluginSettings() -> write per-plugin options
  -> loadPluginCommands.ts:L414 getPluginCommands() [memoized]
    -> walkPluginMarkdown.ts:L44 walkPluginMarkdown() -> glob .md files
  -> loadPluginAgents.ts:L231 loadPluginAgents() [memoized]
  -> loadPluginHooks.ts:L91 loadPluginHooks() [memoized]
  -> loadPluginOutputStyles.ts:L87 loadPluginOutputStyles() [memoized]
  -> [parallel] mcpPluginIntegration.ts:L131 loadPluginMcpServers()
  -> [parallel] lspPluginIntegration.ts:L57 loadPluginLspServers()
  -> AppState update: pluginCommands, pluginAgents, pluginHooks, outputStyles
```

**Call depth**: 4 levels. **Key branch point**: `assemblePluginLoadResult` runs 3 parallel loads (marketplace + session + builtin), then merges and verifies.

### Chain 3: Marketplace Registration Flow

```
officialMarketplaceStartupCheck.ts:L15 checkOfficialMarketplace()
  -> marketplaceManager.ts:L380 registerSeedMarketplaces()
    -> marketplaceManager.ts:L2122 getMarketplace(official) [memoized]
    -> [if not cloned] marketplaceManager.ts:L1034 reconcileSparseCheckout()
      -> git clone --sparse + git sparse-checkout set
    -> [if clone fails] officialMarketplaceGcs.ts:L47 fetchFromGcs()
      -> fetch GCS index -> parse JSON -> cache locally
  -> [if retry needed] exponential backoff (3 attempts)
```

**Call depth**: 4 levels. **Fallback**: GCS fallback when git clone fails.

### Key Branch Points

| Branch Point | File:Line | Decision | Paths |
|-------------|-----------|----------|-------|
| Install strategy | pluginLoader.ts:L460 | Marketplace entry type | npm / git clone / git subdir |
| Verification result | pluginLoader.ts:L2840 | Missing dependencies? | keep / demote to inactive |
| Git availability | gitAvailability.ts:L10 | git binary found? | full checkout / GCS fallback |
| Scope resolution | pluginOperations.ts:L270 | user/project/local? | different persistence paths |
| Sparse checkout | marketplaceManager.ts:L1034 | already cloned? | reconcile / full clone |

## Temporal Analysis

### Async Orchestration: Plugin Refresh Pipeline

```
T=0  refreshActivePlugins() called
     |-- clearAllCaches() -- synchronous, invalidates 6 memoize caches
T=1  loadAllPlugins() -- first call after cache clear (slow path)
     |-- [parallel] loadPluginsFromMarketplaces()  --------+
     |-- [parallel] loadSessionPlugins()           --+     |
     +-- [parallel] loadBuiltinPlugins()             |     |
T=2  Promise.all settles <---------------------------+-----+
     |-- mergePluginSources() -- synchronous dedup
     |-- verifyAndDemote() -- synchronous validation
T=3  [parallel] getPluginCommands()   ------+
     |-- [parallel] loadPluginAgents() --+   |
     |-- [parallel] loadPluginHooks()    |   |
     +-- [parallel] loadPluginOutputStyles()  |
T=4  Promise.all settles <-----------------+--+
     |-- [parallel] loadPluginMcpServers()   --+
     +-- [parallel] loadPluginLspServers()   --+
T=5  Promise.all settles <---------------------+
     +-- AppState.batchUpdate({pluginCommands, pluginAgents, ...})
```

### Race Conditions

| Risk ID | Description | Files | Severity |
|---------|-------------|-------|----------|
| RC-1 | `installPluginOp` and `performBackgroundPluginInstallations` may race on the same plugin -- both write to `installed_plugins.json` | pluginOperations.ts:L321, PluginInstallationManager.ts:L60 | MEDIUM -- file writes not atomic |
| RC-2 | `refreshActivePlugins` called while `installPluginOp` still in progress -- may load stale plugin list | refresh.ts:L72, pluginOperations.ts:L321 | LOW -- user-triggered, unlikely overlap |
| RC-3 | Hot reload hooks fire during active MCP server connection -- hooks may reference stale MCP config | loadPluginHooks.ts:L255, mcpPluginIntegration.ts:L131 | LOW -- settings debounce mitigates |

### Temporal Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant CLI as pluginCliCommands
    participant Ops as pluginOperations
    participant Loader as pluginLoader
    participant Mgr as marketplaceManager
    participant Refresh as refresh.ts

    User->>CLI: install plugin-id
    CLI->>Ops: installPluginOp(id, scope)
    Ops->>Ops: parsePluginIdentifier(id)
    Ops->>Mgr: getMarketplace(name) [memoized]
    Mgr-->>Ops: marketplace data
    Ops->>Loader: cacheAndRegisterPlugin()
    Loader->>Loader: installFromNpm or gitClone
    Loader-->>Ops: cached plugin path
    Ops->>Ops: saveInstalledPlugins()
    Ops->>Refresh: refreshActivePlugins()
    Refresh->>Refresh: clearAllCaches()
    Refresh->>Loader: loadAllPlugins [re-memoize]
    par Component Loading
        Refresh->>Refresh: getPluginCommands()
        Refresh->>Refresh: loadPluginAgents()
        Refresh->>Refresh: loadPluginHooks()
    end
    par Integration Loading
        Refresh->>Refresh: loadPluginMcpServers()
        Refresh->>Refresh: loadPluginLspServers()
    end
    Refresh-->>Ops: components loaded
    Ops-->>CLI: install complete
    CLI-->>User: success message
```

## Data Flow Analysis

### Data Flow: Plugin Install Record Lifecycle

```mermaid
flowchart LR
    subgraph Creation
        A[User Input - plugin-id string] --> B[parsePluginIdentifier]
        B --> C[Resolve in Marketplace]
    end
    subgraph Installation
        C --> D[cacheAndRegisterPlugin]
        D --> E[Write to plugins dir]
        D --> F[Write to installed_plugins.json]
    end
    subgraph Activation
        F --> G[refreshActivePlugins]
        G --> H[loadAllPlugins]
        H --> I[Component Loaders]
    end
    subgraph Persistence
        I --> J[AppState update]
        F --> K[reconcileSparseCheckout]
    end
```

**Key entity paths**:
1. **Plugin ID string** -> parsePluginIdentifier -> resolve -> cache -> persist -> load -> activate
2. **Version hash** -> content hash + git SHA -> cache key -> invalidation trigger (pluginVersioning.ts:L45)
3. **Plugin options** -> pluginOptionsStorage -> load/save per-plugin JSON -> schema-driven form (PluginSettings.tsx)

## State Transition Analysis

### State Machine 1: Plugin Installation State

| Current State | Trigger | Target State | Side Effect | File:Line |
|--------------|---------|-------------|-------------|-----------|
| not_installed | installPluginOp() | installing | clone/download starts | pluginOperations.ts:L321 |
| installing | cachePlugin() success | installed | write to installed_plugins.json | pluginInstallationHelpers.ts:L72 |
| installing | cachePlugin() failure | install_failed | cleanup partial files | pluginOperations.ts:L420 |
| installed | setPluginEnabledOp(true) | enabled | refreshActivePlugins() | pluginOperations.ts:L573 |
| installed | setPluginEnabledOp(false) | disabled | refreshActivePlugins() | pluginOperations.ts:L573 |
| enabled | uninstallPluginOp() | not_installed | remove from disk + json | pluginOperations.ts:L427 |
| enabled | updatePluginOp() | updating | download new version | pluginOperations.ts:L829 |
| updating | new version cached | enabled | refreshActivePlugins() | pluginOperations.ts:L890 |
| enabled | verifyAndDemote() fail | demoted | missing dependency logged | pluginLoader.ts:L2840 |

**Terminal states**: not_installed (stable), enabled (stable), install_failed (requires retry), demoted (requires dependency fix)

### State Machine 2: Marketplace State

| Current State | Trigger | Target State | Side Effect | File:Line |
|--------------|---------|-------------|-------------|-----------|
| unregistered | registerSeedMarketplaces() | registered | config written | marketplaceManager.ts:L380 |
| registered | getMarketplace() first call | cloning | git clone --sparse | marketplaceManager.ts:L1034 |
| cloning | clone success | cloned | sparse-checkout set | marketplaceManager.ts:L1100 |
| cloning | clone failure | gcs_fallback | fetch from GCS | officialMarketplaceGcs.ts:L47 |
| cloned | reconcileSparseCheckout() | synced | git pull + sparse update | marketplaceManager.ts:L1034 |
| gcs_fallback | GCS fetch success | synced | cache locally | officialMarketplaceGcs.ts:L80 |

### State Machine 3: Cache State (per memoized function)

| Current State | Trigger | Target State | Side Effect | File:Line |
|--------------|---------|-------------|-------------|-----------|
| empty | first call | populated | function executes, result cached | lodash.memoize |
| populated | same arguments | populated | return cached result O(1) | lodash.memoize |
| populated | clearAllCaches() | empty | cache.clear() called | cacheUtils.ts:L15 |
| populated | refreshActivePlugins() | empty then populated | clear + re-execute | refresh.ts:L72 |

### Cross-Component State Linkage

- `installed_plugins.json` (InstalledPluginsManager) -> read by `loadAllPlugins` (PluginLoader) -> determines which plugins are active
- `AppState.pluginCommands/Agents/Hooks` -> consumed by T-10 (REPL), T-05 (Tool System), T-08 (MCP Integration)
- `settings.plugins` (Settings) -> read by `reconciler.ts` -> triggers install/uninstall operations
- `PluginOptionsStorage` -> read by `PluginSettings.tsx` -> user edits -> written back -> `refreshActivePlugins`


## Error Propagation Analysis

### Error Sources and Handling Strategies

| Error Source | Type | Trigger | Handler | Strategy | File:Line |
|-------------|------|---------|---------|----------|-----------|
| installFromNpm | NpmInstallError | npm registry failure | installPluginOp | retry | pluginLoader.ts:L492 |
| gitClone | GitError | git clone/pull failure | installPluginOp | fallback(GCS) | pluginLoader.ts:L534 |
| validatePluginManifest | ValidationError | invalid manifest schema | loadAllPlugins | absorb(demote) | validatePlugin.ts:L45 |
| validatePluginContents | ValidationError | missing required files | loadAllPlugins | absorb(demote) | validatePlugin.ts:L380 |
| reconcileSparseCheckout | GitError | sparse checkout failure | marketplaceManager | fallback(full checkout) | marketplaceManager.ts:L1034 |
| saveInstalledPlugins | FSError | disk write failure | pluginOperations | abort | installedPluginsManager.ts:L261 |
| loadPluginMcpServers | MCPError | MCP server config invalid | mcpPluginIntegration | absorb(log warning) | mcpPluginIntegration.ts:L131 |
| loadPluginLspServers | LSPError | LSP config invalid | lspPluginIntegration | absorb(log warning) | lspPluginIntegration.ts:L57 |
| fetchFromGcs | NetworkError | GCS unreachable | officialMarketplaceStartupCheck | retry(3x) | officialMarketplaceGcs.ts:L47 |
| parsePluginIdentifier | ParseError | malformed plugin ID | pluginOperations | abort(user error) | pluginIdentifier.ts:L45 |
| checkMcpbChanged | ConfigError | .mcpb config drift | mcpbHandler | absorb(reload) | mcpbHandler.ts:L200 |
| pluginBlocklist | BlocklistError | delisted plugin detected | pluginBlocklist | abort(auto-uninstall) | pluginBlocklist.ts:L40 |

### Unhandled Error Paths

1. **installed_plugins.json corruption**: If the JSON file is corrupted mid-write, `loadInstalledPlugins` throws but there is no automatic recovery or backup-restore mechanism (installedPluginsManager.ts:L50). User must manually delete and re-install.

2. **Concurrent marketplace clone**: If two `getMarketplace` calls race for the same marketplace, one may start cloning while the other reads a partially cloned directory. The memoize guard helps but is not atomic (marketplaceManager.ts:L2122).

3. **Disk full during cachePlugin**: `cachePlugin` writes plugin files to `~/.claude/plugins/<hash>/` but does not check disk space or handle ENOSPC (pluginLoader.ts:L911).

### Recovery Strategy Distribution

| Strategy | Count | Description |
|----------|-------|-------------|
| absorb | 4 | Log warning and continue with degraded functionality |
| retry | 2 | Retry with exponential backoff (install, GCS fetch) |
| fallback | 2 | Fall back to alternative (GCS, full checkout) |
| abort | 3 | Terminate operation and report to user |
| abort(auto) | 1 | Auto-uninstall delisted plugin |

## Boundary / Integration Diagram

```mermaid
flowchart TD
    subgraph T-17 Plugin System
        CLI[CLI Commands<br/>pluginCliCommands.ts]
        TUI[TUI Panels<br/>ManagePlugins.tsx<br/>PluginSettings.tsx]
        Ops[Operations Layer<br/>pluginOperations.ts]
        Loader[Plugin Loader<br/>pluginLoader.ts]
        Refresh[Refresh Pipeline<br/>refresh.ts]
        Loaders[Component Loaders<br/>Commands/Agents/Hooks/Styles]
        MCPInt[MCP Integration<br/>mcpPluginIntegration.ts]
        LSPInt[LSP Integration<br/>lspPluginIntegration.ts]
    end

    subgraph External Systems
        T01[T-01: CLI Init<br/>commands.ts]
        T03[T-03: Tool System<br/>Tool.ts]
        T05[T-05: Hooks<br/>toolHooks.ts]
        T08[T-08: MCP Service<br/>MCPConnectionManager]
        T10[T-10: TUI/REPL<br/>REPL.tsx]
        T11[T-11: Components<br/>LSP components]
        NPM[npm Registry]
        GIT[Git Repos]
        GCS[Google Cloud Storage]
        FS[File System<br/>~/.claude/plugins/]
    end

    CLI --> Ops
    TUI --> Ops
    Ops --> Loader
    Loader --> FS
    Loader --> GIT
    Loader --> NPM
    Loader -.->|GCS fallback| GCS
    Refresh --> Loaders
    Refresh --> MCPInt
    Refresh --> LSPInt
    Loaders -->|plugin commands| T01
    Loaders -->|plugin agents| T03
    Loaders -->|plugin hooks| T05
    MCPInt -.->|plugin MCP servers| T08
    LSPInt -.->|plugin LSP servers| T11
    TUI -.->|settings panel| T10
```

### Cross-Task Interfaces

| Interface | Direction | Data | Description |
|-----------|-----------|------|-------------|
| pluginCommands | T-17 -> T-01 | LoadedPlugin[] | Slash commands from plugins registered in command system |
| pluginAgents | T-17 -> T-03 | AgentDefinition[] | Agent definitions from plugins injected into tool system |
| pluginHooks | T-17 -> T-05 | HookDefinition[] | Hook definitions from plugins injected into tool hook system |
| pluginMcpServers | T-17 -> T-08 | MCPServerConfig[] | MCP server configs from plugins registered in MCP manager |
| pluginLspServers | T-17 -> T-11 | LSPServerConfig[] | LSP server configs from plugins registered in LSP system |
| pluginOutputStyles | T-17 -> T-10 | OutputStyle[] | Output style definitions for rendering |
| AppState.plugins | T-17 -> Global | LoadedPlugin[] | Plugin state accessible by all components |
| settings.plugins | Global -> T-17 | PluginSettings | User configuration drives reconciler |

## Concurrency Model Analysis

N/A -- The plugin system runs in a single-threaded Node.js environment. All async operations use standard async/await patterns without explicit locks or mutexes. The primary concurrency concern is the potential for race conditions between overlapping async operations (RC-1 through RC-3 documented in Temporal Analysis), but these are mitigated by:

1. **Memoization guards**: lodash.memoize prevents redundant re-execution of expensive operations
2. **Sequential refresh**: `refreshActivePlugins` runs component loaders in defined parallel batches, not arbitrary concurrency
3. **Settings debounce**: Hot reload hooks use a debounce mechanism to avoid rapid consecutive reloads

No shared mutable state requires explicit synchronization beyond the natural single-threaded event loop ordering.

## Side Effects Manifest

| Function | Side Effect Type | Target | Reversible | File:Line |
|----------|-----------------|--------|-----------|-----------|
| installPluginOp() | FS write | ~/.claude/plugins/&lt;hash&gt;/ | Yes (uninstall) | pluginOperations.ts:L321 |
| installPluginOp() | FS write | installed_plugins.json | Yes (remove entry) | installedPluginsManager.ts:L261 |
| cachePlugin() | FS write | ~/.claude/plugins/&lt;hash&gt;/ | No (manual cleanup) | pluginLoader.ts:L911 |
| uninstallPluginOp() | FS delete | ~/.claude/plugins/&lt;hash&gt;/ | No (re-install needed) | pluginOperations.ts:L427 |
| reconcileSparseCheckout() | Subprocess | git clone/pull/sparse-checkout | No | marketplaceManager.ts:L1034 |
| refreshActivePlugins() | Global state | AppState (React) | N/A | refresh.ts:L72 |
| loadPluginHooks() hot reload | Global state | hook registry | Yes (revert settings) | loadPluginHooks.ts:L255 |
| fetchFromGcs() | Network | GCS HTTP endpoint | N/A | officialMarketplaceGcs.ts:L47 |
| installFromNpm() | Network | npm registry | N/A | pluginLoader.ts:L492 |
| updatePluginsForMarketplaces() | Subprocess | git pull per marketplace | No | pluginAutoupdate.ts:L50 |
| performBackgroundPluginInstallations() | FS write + Network | pending installs queue | No | PluginInstallationManager.ts:L60 |
| fetchTelemetry() | Network | analytics API | N/A | fetchTelemetry.ts:L20 |
| checkMcpbChanged() | FS read + write | ~/.claude/mcp_servers/&lt;name&gt;/ | Yes (revert config) | mcpbHandler.ts:L200 |
| clearAllCaches() | Global state | lodash.memoize caches | N/A (auto-repopulate) | cacheUtils.ts:L15 |


## Acceptance Criteria Status

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| AC-1 | All 65 scope files analyzed | PASS | 67 File Roles rows (65 unique + 2 cross-references) |
| AC-2 | Plugin install flow documented end-to-end | PASS | Chain 1 in Call Chain Analysis |
| AC-3 | Plugin load flow documented end-to-end | PASS | Chain 2 in Call Chain Analysis |
| AC-4 | Marketplace registration documented | PASS | Chain 3 in Call Chain Analysis |
| AC-5 | Cross-task interfaces identified | PASS | 8 interfaces in Boundary/Integration Diagram |
| AC-6 | Error handling strategies classified | PASS | 12 error sources + 5 strategies in Error Propagation |
| AC-7 | State machines documented | PASS | 3 state machines in State Transition Analysis |

**Overall: 7/7 PASS**

## Identified Problems

| ID | Severity | Description | File:Line |
|----|----------|-------------|-----------|
| P2-01 | P2 | **pluginLoader.ts monolith** (3302 lines): Contains loading, caching, installation, validation, and dependency resolution. Should be split into at least 4 modules (loader, installer, validator, cache). | pluginLoader.ts |
| P2-02 | P2 | **marketplaceManager.ts monolith** (2643 lines): Combines marketplace registration, git operations, sparse checkout, and display formatting. Git operations should be extracted. | marketplaceManager.ts |
| P3-01 | P3 | **Non-atomic installed_plugins.json writes**: Concurrent install + background install may corrupt the file. No file locking or write-then-rename pattern. | installedPluginsManager.ts:L261 |
| P3-02 | P3 | **No disk space check**: cachePlugin writes to disk without checking available space, risking silent partial writes. | pluginLoader.ts:L911 |
| P3-03 | P3 | **V1 migration fire-once flag**: If migration fails mid-way, the v2MigrationComplete flag may already be set, preventing retry. | installedPluginsManager.ts:L1048 |
| P4-01 | P4 | **Duplicate File Roles entries**: The File Roles table has 2 "already listed" rows for duplicate file references. | 03-analysis-tasks.md |
| P4-02 | P4 | **14 bundled skill files in scope**: Bundled skills (src/skills/bundled/*.ts) have minimal connection to the plugin loader infrastructure. Consider scoping them to a separate task. | src/skills/bundled/ |

## Open Questions

1. **[Cross-task] T-08 MCP Integration**: How does `mcpPluginIntegration.ts` interact with the MCPConnectionManager when a plugin provides an MCP server? Does the plugin MCP server go through the same connection lifecycle? (depends on T-08)

2. **[Cross-task] T-05 Tool Hooks**: When `loadPluginHooks` detects a settings change, does it trigger a full `refreshActivePlugins` or only reload hooks? The hot reload path (loadPluginHooks.ts:L255) only clears hook caches, not command/agent caches.

3. **[Runtime] Auto-update timing**: `autoUpdateMarketplacesAndPluginsInBackground` runs at startup, but what triggers re-checks during a long-running session? Is there a polling interval or only manual refresh?

4. **[Runtime] Sparse checkout performance**: For marketplaces with hundreds of plugins, how does `git sparse-checkout` perform when only a handful are installed? Is there a pruning strategy?

5. **[Configuration] Plugin scope precedence**: When the same plugin is installed at multiple scopes (user, project, local), which one wins? The code uses `mergePluginSources` but the precedence rules are not documented.

6. **[Security] Plugin sandboxing**: Plugins can register commands, hooks, MCP servers, and LSP servers. Is there any sandboxing or capability restriction? The homoglyph protection (schemas.ts:L71) only covers name spoofing.

7. **[Cross-task] T-10 TUI**: How does `ManagePlugins.tsx` (2215 lines) communicate plugin state changes to the rest of the TUI? Through AppState directly or through the refresh pipeline?

8. **[Architecture] Three-layer refresh**: The refresh pipeline (clear -> load -> component-load -> integrate -> AppState) has 5 sequential stages. Could any be safely parallelized further to reduce startup latency?

## Complexity Assessment

| Dimension | Rating | Justification |
|-----------|--------|---------------|
| File count | HIGH | 65 scope files, largest non-TUI task |
| Call depth | MEDIUM | Max 6 levels (install chain) |
| State complexity | MEDIUM | 3 state machines with cross-component linkage |
| Error handling | MEDIUM | 12 error sources, 5 recovery strategies |
| Concurrency | LOW | Single-threaded, 3 low-severity race conditions |
| External dependencies | MEDIUM | git, npm, GCS, filesystem |
| Configuration surface | HIGH | 3 scopes x multiple operations x plugin types |

**Overall Complexity: MEDIUM-HIGH**

The plugin system has a large file surface (65 files, ~33K lines) but relatively straightforward control flow. The primary complexity comes from: (1) the three-layer model (settings -> reconciler -> refresh), (2) multiple install sources (marketplace/npm/git), and (3) the memoization-based cache invalidation strategy. The two monolithic files (pluginLoader.ts 3302L, marketplaceManager.ts 2643L) contribute disproportionate complexity.
