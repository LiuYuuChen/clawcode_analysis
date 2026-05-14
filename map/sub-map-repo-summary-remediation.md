# Sub-map-repo Remediation Summary

## Context

map-repo-guardian FAILed at iteration 1 (Tier2=15.9% &lt;80%, Tier3=46.2% &lt;90%).
Remediation: add 4 new main lines (ML-12~ML-15) from ml-supplement classification of uncovered files.

## New Main Lines

| ML | Name | Priority | Entry File | Files | Lines | Scope Dirs |
|----|------|----------|-----------|-------|-------|------------|
| ML-12 | Plugin System | P2 | [`src/utils/plugins/pluginLoader.ts`](/src/src/utils/plugins/pluginLoader.ts) | 49 | 25,422 | src/utils/plugins/, src/services/plugins/, src/commands/plugin/ |
| ML-13 | Bash/Shell Engine | P2 | [`src/utils/bash/bashParser.ts`](/src/src/utils/bash/bashParser.ts) | 36 | 17,680 | src/utils/bash/, src/utils/shell/, src/utils/powershell/ |
| ML-14 | Swarm Orchestration | P2 | [`src/utils/swarm/inProcessRunner.ts`](/src/src/utils/swarm/inProcessRunner.ts) | 22 | 7,548 | src/utils/swarm/, src/utils/swarm/backends/ |
| ML-15 | SDK Entry Points | P2 | [`src/entrypoints/sdk/coreSchemas.ts`](/src/src/entrypoints/sdk/coreSchemas.ts) | 9 | 2,716 | src/entrypoints/sdk/ |

**Total**: 116 files, 53,366 lines

## Entry File Verification

| ML | Entry File | Exists | Size | Purpose |
|----|-----------|--------|------|---------|
| ML-12 | src/utils/plugins/pluginLoader.ts | ✅ | 3302L | Plugin discovery, loading, and validation orchestrator |
| ML-13 | src/utils/bash/bashParser.ts | ✅ | 4436L | Pure-TypeScript bash parser producing tree-sitter-compatible ASTs |
| ML-14 | src/utils/swarm/inProcessRunner.ts | ✅ | 1552L | In-process teammate runner with AsyncLocalStorage context isolation |
| ML-15 | src/entrypoints/sdk/coreSchemas.ts | ✅ | 1889L | Zod schemas for serializable SDK data types |

## Cross-References with Existing MLs

| New ML | Cross-references |
|--------|-----------------|
| ML-12 | ML-03 (Tool registration — plugins contribute commands/hooks/agents), ML-01 (CLI — /plugins command), ML-05 (MCP — mcpPluginIntegration.ts) |
| ML-13 | ML-03 (Tool — Bash tool uses parser for safety validation), ML-04 (Permissions — command validation) |
| ML-14 | ML-03 (Tool — swarm spawns agents that use tools), ML-04 (Permissions — leaderPermissionBridge), ML-09 (Bridge — remote swarm) |
| ML-15 | None (pure type definitions, consumed by multiple MLs) |

## Key Modules per ML

### ML-12: Plugin System (49 files)
- **Core**: pluginLoader.ts (3302L), marketplaceManager.ts (2643L), installedPluginsManager.ts (1268L), schemas.ts (1681L), validatePlugin.ts (903L), loadPluginCommands.ts (946L), mcpbHandler.ts (968L), ManagePlugins.tsx (2214L), pluginOperations.ts (1088L)
- **FAIL files (>1000L)**: ManagePlugins.tsx (2214L), PluginSettings.tsx (1071L), marketplaceManager.ts (2643L), pluginLoader.ts (3302L)
- **Pattern candidates**: None identified (plugin files are heterogeneous, not batch-isomorphic)

### ML-13: Bash/Shell Engine (36 files)
- **Core**: bashParser.ts (4436L), ast.ts (2679L), readOnlyCommandValidation.ts (1893L), powershell/parser.ts (1804L), commands.ts (1339L)
- **FAIL files (>1000L)**: bashParser.ts (4436L), ast.ts (2679L), readOnlyCommandValidation.ts (1893L), powershell/parser.ts (1804L), commands.ts (1339L)
- **Pattern candidates**: bash/specs/*.ts (8 small files, alias/nohup/pyright/sleep/srun/time/timeout + index)

### ML-14: Swarm Orchestration (22 files)
- **Core**: inProcessRunner.ts (1552L), permissionSync.ts (928L), TmuxBackend.ts (764L), teamHelpers.ts (683L), backends/registry.ts (464L)
- **FAIL files (>1000L)**: inProcessRunner.ts (1552L)
- **Pattern candidates**: backends/*.ts (6 files, all backend implementations)

### ML-15: SDK Entry Points (9 files)
- **Core**: coreSchemas.ts (1889L), controlSchemas.ts (663L)
- **Generated/small**: coreTypes.generated.ts (10L), settingsTypes.generated.ts (1L), toolTypes.ts (1L), sdkUtilityTypes.ts (6L), runtimeTypes.ts (22L)
- **Pattern candidates**: None (too few files)

## Expected Coverage Impact

After trace-mainline for ML-12~ML-15 (deep + standard trace):
- mapped_file_count: 932 + 116 = ~1,048
- mapped_lines: 238,755 + 53,366 = ~292,121
- Tier 3 (files): 1,048/2,019 = ~51.9% (still &lt;90%, needs catalog-supplement)

After catalog-supplement (850 pattern files + 59 ml-expand files):
- mapped_file_count: ~1,048 + 909 = ~1,957
- Tier 3 (files): ~1,957/2,019 = ~96.9% (PASS ≥90%)

## Next Step

sub-map-repo-remediation: create trace-mainline workflow for ML-12~ML-15.
**Critical**: trace-mainline must produce standard trace files for supporting files (fixing Tier 2 deficiency).
