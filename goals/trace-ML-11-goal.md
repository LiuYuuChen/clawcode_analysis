# trace-ML-11 Goal Tracker

- [x] 确认入口文件 (autoCompact.ts)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度
- [x] 识别跨主线交叉引用 (context.ts → ML-01/ML-07, tokens.ts → ML-02)
- [x] 支线发现：评估每个 Branch Point — 无满足条件的 BL
- [x] 支线追踪：无 BL 需追踪
- [x] Pattern instance catalog：ML-11 不拥有任何 PI
- [x] 构建文件级 map（33 deep + 2 cross-ref = 35 files）
- [x] Sub-map 容量校验（DEEP 8,261 行 ≤ 10,000 ✅）
- [x] 写出 map/sub-maps/ML-11-1.md
- [x] 追加 map/instance-manifest.jsonl — 无 catalog 实例
- [x] 追加/更新 map/call-graph.jsonl（31 new entries → 281 total）
- [x] 更新 metadata.json（mainline_count=11, mapped_file_count=932, mapped_lines=238,755）
- [x] 追加 mapped-files.jsonl（全量重建：932 entries）
- [x] 追加 map/mainline-file-map.jsonl（ML-11-1 条目）
