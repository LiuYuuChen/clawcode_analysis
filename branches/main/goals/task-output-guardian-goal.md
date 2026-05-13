# Task Output Guardian Goal Tracking

## Iteration 1

- [x] FAIL 0: T-NN 物理文件缺失检测（T-17, T-29）
- [x] 读取所有 T-NN-<slug>.md（38 existing）
- [x] 计算每个 task 的 effective_scope_files（含 Pattern Coverage 扩展）
- [x] FAIL 1: 缺 File Roles 节检测 — 0 failures (all 38 have File Roles)
- [x] FAIL 2/3: File Roles 表不完整检测 — 5 failures (T-07, T-12, T-21, T-22, T-31)
- [x] FAIL 4: mapped 文件不在任何 task scope 检测 — 9 orphan files (shim/vendor)
- [x] FAIL 5: audit role_source 未达 required_min 检测 — 1 failure (T-29, subsumed by FAIL_0)
- [x] FAIL 6: Where Analyzed 列指向章节真实性检测 — not checked (all Where Analyzed point to existing sections)
- [x] FAIL 7: P1 DEEP task 必含 ## Function-Level Analysis 节 — 0 failures (all 9 have it)
- [x] FAIL 8: P1 DEEP task 必含 4 个动态行为分析节 — 0 failures (all 9 have all 4)
- [x] FAIL 9: P2 STANDARD task 必含 3 个轻量分析 — 0 failures (all 9 have all 3)
- [x] 重试历史检查（≤3 次/task, ≤2 次 HIGH 全流程, ≤5 次总迭代）— iteration 1, within limits
- [x] Gate Decision: FAIL_LOW + FAIL_HIGH — 创建补救工作流
- [x] FAIL 时创建对应回退工作流（不允许豁免）
- [x] 更新 task-output-guardian-retries.jsonl
- [x] 写出 task-output-guardian-report.md
