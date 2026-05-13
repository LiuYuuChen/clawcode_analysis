# Goal: trace-ML-02 查询引擎主循环

- [x] 确认入口文件 (src/QueryEngine.ts)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度
- [x] 识别跨主线交叉引用 (ML-03 Tool, ML-11 Compact, ML-10 API client, ML-01 processUserInput)
- [x] 支线发现：评估 Branch Points — identified BL-02-01 (Streaming Tool Execution), BL-02-02 (Model Fallback), BL-02-03 (Reactive Compact Recovery)
- [x] 支线追踪：BL files recorded at STANDARD depth
- [x] Pattern instance catalog：本 ML 无 owned pattern categories
- [x] 构建文件级 map（22 deep files + 0 catalog）
- [x] Sub-map 容量校验 — SPLIT into 4 segments (total 21,604 lines > 10,000)
- [x] 写出 map/sub-maps/ML-02-1.md ~ ML-02-4.md
- [x] 追加 map/mainline-file-map.jsonl (4 entries for ML-02-1 ~ ML-02-4)
- [x] 追加/更新 map/call-graph.jsonl
- [x] 更新 metadata.json（mapped_file_count, mapped_lines）
- [x] 重建 mapped-files.jsonl（ML-01 + ML-02 去重合并）
