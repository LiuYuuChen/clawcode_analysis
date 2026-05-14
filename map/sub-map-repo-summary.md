# Sub-Map-Repo Decomposition Summary

## Main Lines Parsed

| ML ID | Name | Priority | Entry File | Key Modules | Est. Files | Validation |
|-------|------|----------|-----------|-------------|-----------|------------|
| ML-01 | CLI 启动与命令路由 | P1 | [`src/bootstrap-entry.ts`](/src/src/bootstrap-entry.ts) | entrypoints/cli.tsx, entrypoints/init.ts, main.tsx, commands.ts | ~25 | PASS ✅ |
| ML-02 | 查询引擎主循环 | P1 | [`src/QueryEngine.ts`](/src/src/QueryEngine.ts) | query.ts, services/api/claude.ts, services/compact/ | ~30 | PASS ✅ |
| ML-03 | 工具系统注册与调度 | P1 | [`src/Tool.ts`](/src/src/Tool.ts) | tools.ts, tools/BashTool/, tools/AgentTool/, tools/FileEditTool/ | ~15+189 cat | PASS ✅ |
| ML-04 | 权限系统 | P1 | [`src/utils/permissions/permissions.ts`](/src/src/utils/permissions/permissions.ts) | autoModeState, bashClassifier, yoloClassifier, permissionRuleParser, useCanUseTool | ~40 | PASS ✅ |
| ML-05 | MCP 服务集成 | P1 | [`src/services/mcp/MCPConnectionManager.tsx`](/src/src/services/mcp/MCPConnectionManager.tsx) | mcp/client.ts, mcp/config.ts, tools/MCPTool/ | ~25 | PASS ✅ |
| ML-06 | 认证与会话管理 | P1 | [`src/services/oauth/client.ts`](/src/src/services/oauth/client.ts) | api/bootstrap.ts, bootstrap/state.ts, config.js | ~20 | PASS ✅ |
| ML-07 | TUI 渲染与交互 | P2 | [`src/screens/REPL.tsx`](/src/src/screens/REPL.tsx) | ink/, components/, hooks/, state/ | ~600 | PASS ✅ |
| ML-08 | 任务系统 | P2 | [`src/Task.ts`](/src/src/Task.ts) | tasks/ 7 subdirs | ~15 | PASS ✅ |
| ML-09 | Bridge 远程模式 | P2 | [`src/bridge/initReplBridge.ts`](/src/src/bridge/initReplBridge.ts) | replBridge.ts, remoteBridgeCore.ts | ~33 | PASS ✅ |
| ML-10 | API 客户端与重试层 | P2 | [`src/services/api/client.ts`](/src/src/services/api/client.ts) | claude.ts, withRetry.ts, errors.ts | ~21 | PASS ✅ |
| ML-11 | 上下文与记忆管理 | P2 | [`src/services/compact/autoCompact.ts`](/src/src/services/compact/autoCompact.ts) | compact.ts, memdir/, contextCollapse/ | ~15 | PASS ✅ |

## Validation Results

- **Entry files**: 11/11 exist and readable ✅
- **Key modules**: 33/33 exist (directories verified for dir paths) ✅
- **Scope overlap**: No two main lines have identical scope (some shared files expected, noted as branch points) ✅

## Workflow Created

- **Name**: `trace-mainline-pipeline`
- **Type**: `sequential`
- **Total Actions**: 11 (one per main line)
- **Prompt files per action**:
  - `/Users/liuyuchen/ai/MethodologyAndSkill/methods/code-deep-analysis-workflow/actions/trace-mainline.md`
  - `/Users/liuyuchen/ai/MethodologyAndSkill/methods/code-deep-analysis-workflow/references/organize.md`

| ML ID | Action Name | Entry File | Priority | Owned Patterns | Status |
|-------|-----------|-----------|----------|----------------|--------|
| ML-01 | trace-ML-01 | src/bootstrap-entry.ts | P1 | — | included ✅ |
| ML-02 | trace-ML-02 | src/QueryEngine.ts | P1 | — | included ✅ |
| ML-03 | trace-ML-03 | src/Tool.ts | P1 | PI-01 (189 files) | included ✅ |
| ML-04 | trace-ML-04 | src/utils/permissions/permissions.ts | P1 | PI-06 (53 files) | included ✅ |
| ML-05 | trace-ML-05 | src/services/mcp/MCPConnectionManager.tsx | P1 | — | included ✅ |
| ML-06 | trace-ML-06 | src/services/oauth/client.ts | P1 | — | included ✅ |
| ML-07 | trace-ML-07 | src/screens/REPL.tsx | P2 | PI-03, PI-07, PI-08 (225 files) | included ✅ |
| ML-08 | trace-ML-08 | src/Task.ts | P2 | PI-04 (10 files) | included ✅ |
| ML-09 | trace-ML-09 | src/bridge/initReplBridge.ts | P2 | — | included ✅ |
| ML-10 | trace-ML-10 | src/services/api/client.ts | P2 | PI-05 (subset) | included ✅ |
| ML-11 | trace-ML-11 | src/services/compact/autoCompact.ts | P2 | — | included ✅ |

## Catalog Mode Distribution

| ML ID | Pattern | Catalog Files | Deep Trace Est. |
|-------|---------|--------------|-----------------|
| ML-03 | PI-01 tool-instance | 189 | 3-5 reps |
| ML-04 | PI-06 permission-component | 53 | core path |
| ML-07 | PI-03 react-hook + PI-07 ink-fork + PI-08 message | 225 | 5-8 reps |
| ML-08 | PI-04 task-implementation | 10 | all (small count) |
| Others | — | 0 | all deep |

## Execution Order

P1 main lines (ML-01~06) execute first, followed by P2 (ML-07~11). Within each priority group, execution follows ML ID order.

## Notes

- All 11 main lines validated successfully with no adjustments needed
- ML-03, ML-07 have large catalog populations (189 and 225 files respectively) — catalog mode essential for these
- ML-07 is the largest main line (~600 files) due to extensive ink component and hook system
- Cross-references identified:
  - ML-01 ↔ ML-02: REPL entry point connects to QueryEngine
  - ML-02 ↔ ML-03: QueryEngine dispatches to Tool system
  - ML-02 ↔ ML-11: QueryEngine triggers auto-compact
  - ML-01 ↔ ML-06: CLI init triggers OAuth/bootstrap
  - ML-03 ↔ ML-05: MCP tools integrate via Tool interface
  - ML-10 feeds into ML-02: API client used by QueryEngine
