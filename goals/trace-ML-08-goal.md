# Goal: trace-ML-08 (任务系统)

- [x] 确认入口文件 src/Task.ts
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度
- [x] 识别跨主线交叉引用（ML-01, ML-02, ML-03, ML-07, ML-09）
- [x] 支线发现：BL-08-01 (Teleport远程会话, 1 file, 466 lines), BL-08-02 (InProcess Teammate Spawn, 1 file, 328 lines)
- [x] 支线追踪：2 条 BL 做 STANDARD 深度内联追踪
- [x] Pattern instance catalog：PI-04 全部 10 文件 deep trace，不使用 catalog
- [x] 构建文件级 map（21 files: 11 core + 10 supporting + 2 BL + 0 catalog）
- [x] Sub-map 容量校验（DEEP 4,683 行 ≤ 10,000 ✅，单段无需拆分）
- [x] 写出 map/sub-maps/ML-08-1.md（含 Branch Lines 节 + Pattern Instances 节）
- [x] 更新 map/pattern-categories.jsonl（PI-04 owner_ml = ML-08）
- [x] 追加/更新 map/call-graph.jsonl（21 entries）
- [x] 更新 metadata.json（mainline_count=8）
- [x] 追加 mapped-files.jsonl（BL 文件 trace_mode=standard）
- [x] 追加 map/mainline-file-map.jsonl（ML-08 条目）
