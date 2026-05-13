# implement-redo Goal

## tasks-supplement (completed)
- [x] 新增 T-40 (PI-05 audit task)
- [x] 扩展 T-12 scope (+3 hooks files)
- [x] 扩展 T-19 scope (+1 spawnInProcess.ts)
- [x] 清理 3 phantom 文件 (mapped-files 1957→1954)

## implement-redo (completed)
- [x] 读取 tmp_tasks.json (40 tasks)
- [x] 拓扑排序所有 40 tasks (Kahn + 优先级)
- [x] 确定分析深度 (P1→DEEP/P2→STANDARD/P3→OVERVIEW)
- [x] Scope Files 物理存在性检查 (0/1696 缺失)
- [x] Pattern Coverage 验证 (15 patterns 全部有 audit task)
- [x] 创建 task-execution-pipeline workflow (40 actions)
  - [x] Part 1: 20 actions (T-01~T-18 + T-22 + T-30) — created
  - [x] Part 2: 20 actions (T-33,T-31,T-21,T-36,T-25,T-37,T-40,T-39,T-23,T-26,T-27,T-28,T-32,T-34,T-35,T-24,T-38,T-29,T-19,T-20) — appended
- [x] 写出 04-task-plan.md (执行计划)
- [x] 写出 tmp_ordered_tasks.json (排序后 tasks 含 scope_files)

## Verification
- Total actions in workflow: 40 ✅
- P1 tasks with DEEP: 9/9 ✅
- P2 tasks with STANDARD: 9/9 ✅
- P3 tasks with OVERVIEW: 22/22 ✅
- All dependency constraints respected ✅
- No duplicate task IDs ✅
