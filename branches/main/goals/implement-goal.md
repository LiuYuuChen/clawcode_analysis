# Implement Goal (main branch — re-optimized)

## Goals

- [x] 审阅任务列表：所有任务ID、优先级、ML Priority、依赖关系 — 41 tasks parsed (P1=9, P2=9, P3=23)
- [x] 确定分析深度：每个 task 基于 Priority 确定 analysis_depth（P1→DEEP, P2→STANDARD, P3→OVERVIEW）
- [x] Scope Files 物理存在性检查（Step 2.5）— PASS, all files exist
- [x] Pattern Coverage 验证（Step 2.6）：每个 PI-XX 都有 audit task，无悬空引用 — PASS (20 audit tasks, 19 with owner_ml + PI-05)
- [x] 任务大小记录：输出每个 task 的 scope 行数（informational，无硬性上限）
- [x] 覆盖校验：所有任务 100% 出现在 workflow 中 — 41/41
- [x] 排序：依赖 + 优先级 + ML Priority + ML 相邻 — topological sort complete
- [x] 创建工作流：一个串行 workflow，每个 task 一个 action（含 ml_priority、analysis_depth、pattern_coverage 参数）— Workflow_create SUCCESS (41 actions)
- [x] 更新任务状态：标记 implement 为完成
- [x] 写出 04-task-plan.md — written with Summary + Task Sizes + Execution Order + Dependency Graph + Verification
