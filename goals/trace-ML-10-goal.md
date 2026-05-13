# Trace-ML-10 Goal Tracker

- [x] 确认入口文件 src/services/api/client.ts
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度（20 files deep + 1 cross-ref）
- [x] 识别跨主线交叉引用（claude.ts → ML-02, auth/proxy/model → ML-06/ML-01）
- [x] 支线发现：评估每个 Branch Point 是否构成 BL（无 BL 发现）
- [x] 支线追踪：无 BL 需要追踪
- [x] Pattern instance catalog：本 ML 不拥有任何 PI pattern
- [x] 构建文件级 map（19 deep files + 1 cross-ref claude.ts = 20 files total）
- [x] Sub-map 容量校验（DEEP 7,058 行 ≤10,000；claude.ts 交叉引用不计入）
- [x] 写出 map/sub-maps/ML-10-1.md（单段，含 Cross-References 节）
- [x] 追加 map/mainline-file-map.jsonl（ML-10 条目）
- [x] 追加/更新 map/call-graph.jsonl（21 files）
- [x] 更新 metadata.json（mainline_count=10, mapped_file_count, mapped_lines）
- [x] 重建 mapped-files.jsonl（含 ML-10 的 21 文件）
- [x] 更新 tasks.md（trace-ML-10 标记 [x]）
