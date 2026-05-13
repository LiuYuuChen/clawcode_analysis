# implement-redo Goal (supplement mode)

- [x] 审阅任务列表：40 tasks (含 T-40 audit-PI-05)
- [x] 确定分析深度：P1→DEEP(9), P2→STANDARD(9), P3→OVERVIEW(22)
- [x] 解析 Pattern Audit deps：19 个 "Task covering ML-XX" → 具体 T-XX
- [x] 填充 Pattern Audit scope_files：18/19 从 instance-manifest (T-24 从 pattern-categories)
- [x] Scope Files 物理存在性检查：0/1696 missing
- [x] Pattern Coverage 验证：19 owned patterns → 19 audit tasks (含 T-40 PI-05)
- [x] 任务大小记录：min=7, median=2,716, max=91,410 lines
- [x] 覆盖校验：40/40 tasks in workflow (100%)
- [x] 拓扑排序：Kahn's algorithm + priority ordering，40 tasks sorted
- [x] 创建工作流：task-execution-pipeline (40 actions, sequential)
- [x] 写出 04-task-plan.md (81 lines)
- [x] 更新 tmp_tasks.json / tmp_ordered_tasks.json / tmp_workflow.json
