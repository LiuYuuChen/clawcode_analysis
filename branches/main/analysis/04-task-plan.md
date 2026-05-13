# Task Execution Plan

## Summary
- Total tasks: 40
- P1: 9 (DEEP), P2: 9 (STANDARD), P3: 22 (OVERVIEW)
- Execution strategy: sequential with dependency-based ordering (Kahn topological sort)
- Coverage remediation: T-40 added for PI-05, T-12 expanded (+3 hooks), T-19 expanded (+1 swarm file)

## Task Sizes (informational)

| Order | Task | Title | Primary ML | Priority | Depth | Scope Files | Lines | Deps | Pattern |
|-------|------|-------|-----------|----------|-------|-------------|-------|------|---------|
| 1 | T-01 | CLI启动与初始化序列 | ML-01 | P1 | DEEP | 10 | 7,941 | none | - |
| 2 | T-02 | 命令路由与REPL启动 | ML-01 | P1 | DEEP | 216 | 57,018 | T-01 | - |
| 3 | T-03 | 查询引擎核心循环 | ML-02 | P1 | DEEP | 341 | 91,410 | T-01 | - |
| 4 | T-04 | 查询API流式处理与消息 | ML-02 | P1 | DEEP | 7 | 11,711 | T-03 | - |
| 5 | T-05 | 工具系统核心调度 | ML-03 | P1 | DEEP | 142 | 58,846 | T-03 | - |
| 6 | T-06 | 权限规则引擎 | ML-04 | P1 | DEEP | 23 | 5,636 | T-05 | - |
| 7 | T-07 | 权限AI分类器与文件系统 | ML-04 | P1 | DEEP | 55 | 16,646 | T-06 | - |
| 8 | T-08 | MCP服务集成 | ML-05 | P1 | DEEP | 85 | 31,771 | T-06 | - |
| 9 | T-09 | 认证与会话管理 | ML-06 | P1 | DEEP | 40 | 13,385 | T-01 | - |
| 10 | T-10 | TUI主界面与Ink框架 | ML-07 | P2 | STANDARD | 80 | 28,340 | T-02 | - |
| 11 | T-11 | TUI组件与Ink渲染 | ML-07 | P2 | STANDARD | 321 | 72,825 | T-10 | - |
| 12 | T-12 | TUI Hooks与交互层 | ML-07 | P2 | STANDARD | 63 | 12,246 | T-10 | - |
| 13 | T-13 | 任务系统 | ML-08 | P2 | STANDARD | 21 | 4,683 | none | - |
| 14 | T-14 | Bridge远程模式 | ML-09 | P2 | STANDARD | 46 | 18,081 | T-09 | - |
| 15 | T-15 | API客户端与重试层 | ML-10 | P2 | STANDARD | 19 | 7,432 | T-03 | - |
| 16 | T-16 | 上下文与记忆管理 | ML-11 | P2 | STANDARD | 34 | 12,654 | T-03 | - |
| 17 | T-17 | 插件系统 | ML-12 | P2 | STANDARD | 65 | 29,367 | T-08 | - |
| 18 | T-18 | Bash/Shell引擎 | ML-13 | P2 | STANDARD | 37 | 18,665 | T-05 | - |
| 19 | T-22 | Pattern Audit — command-handler | ML-01 | P3 | OVERVIEW | 3 | 7 | T-01 | PI-02 |
| 20 | T-30 | Pattern Audit — settings-module | ML-01 | P3 | OVERVIEW | 3 | 103 | T-01 | PI-11 |
| 21 | T-33 | Pattern Audit — misc-leaf | ML-01 | P3 | OVERVIEW | 2 | 32 | T-01 | PI-14 |
| 22 | T-31 | Pattern Audit — utility-leaf | ML-02 | P3 | OVERVIEW | 3 | 54 | T-03 | PI-12 |
| 23 | T-21 | Pattern Audit — tool-instance | ML-03 | P3 | OVERVIEW | 3 | 90 | T-05 | PI-01 |
| 24 | T-36 | Pattern Audit — computer-use-module | ML-03 | P3 | OVERVIEW | 2 | 84 | T-05 | PI-18 |
| 25 | T-25 | Pattern Audit — permission-component | ML-04 | P3 | OVERVIEW | 3 | 48 | T-06 | PI-06 |
| 26 | T-37 | Pattern Audit — mcp-ui-component | ML-05 | P3 | OVERVIEW | 3 | 64 | T-08 | PI-20 |
| 27 | T-40 | Pattern Audit: PI-05 service-module (13 instances, | ML-05 | P3 | OVERVIEW | 1 | 25 | T-08 | PI-05 |
| 28 | T-39 | Pattern Audit — telemetry-module | ML-06 | P3 | OVERVIEW | 2 | 65 | T-09 | PI-24 |
| 29 | T-23 | Pattern Audit — react-hook | ML-07 | P3 | OVERVIEW | 3 | 105 | T-10 | PI-03 |
| 30 | T-26 | Pattern Audit — ink-fork-component | ML-07 | P3 | OVERVIEW | 3 | 94 | T-10 | PI-07 |
| 31 | T-27 | Pattern Audit — message-component | ML-07 | P3 | OVERVIEW | 3 | 50 | T-10 | PI-08 |
| 32 | T-28 | Pattern Audit — agent-component | ML-07 | P3 | OVERVIEW | 3 | 32 | T-10 | PI-09 |
| 33 | T-32 | Pattern Audit — component-leaf | ML-07 | P3 | OVERVIEW | 3 | 17 | T-10 | PI-13 |
| 34 | T-34 | Pattern Audit — design-system-component | ML-07 | P3 | OVERVIEW | 1 | 30 | T-10 | PI-15 |
| 35 | T-35 | Pattern Audit — notification-hook | ML-07 | P3 | OVERVIEW | 3 | 69 | T-10 | PI-16 |
| 36 | T-24 | Pattern Audit — task-implementation | ML-08 | P3 | OVERVIEW | 10 | 2,589 | T-13 | PI-04 |
| 37 | T-38 | Pattern Audit — cli-transport | ML-09 | P3 | OVERVIEW | 3 | 83 | T-14 | PI-23 |
| 38 | T-29 | Pattern Audit — bundled-skill | ML-12 | P3 | OVERVIEW | 3 | 36 | T-17 | PI-10 |
| 39 | T-19 | Swarm编排 | ML-14 | P3 | OVERVIEW | 22 | 7,548 | T-12 | - |
| 40 | T-20 | SDK入口点 | ML-15 | P3 | OVERVIEW | 9 | 2,716 | none | - |

Capacity constraint is enforced at trace-mainline sub-map level (max 10000 lines/sub-map). This step records but does not enforce per-task limits.

## Execution Order



## Dependency Graph



## Verification
- [x] All 40 tasks from 03-analysis-tasks.md are in the workflow
- [x] No task appears multiple times (40 unique task IDs)
- [x] All dependency constraints are respected (topological sort verified)
- [x] Task sizes recorded (informational, no hard limit)
- [x] Scope file existence: 0/1696 missing
- [x] Pattern coverage: all 19 owned patterns have audit tasks
- [x] T-24 PI-04 scope_files filled from pattern-categories (10 deep-traced files)
- [x] Workflow created successfully (40 actions)

## Distribution

| Metric | Value |
|--------|-------|
| Total scope lines (with overlap) | 512,598 |
| Min task lines | 7 |
| Median task lines | 2,716 |
| Max task lines | 91,410 (T-03 ML-02) |
| Avg task lines | 12,814 |