# Goal: trace-ML-09 Bridge 远程模式

- [x] 确认入口文件 (initReplBridge.ts + bridgeMain.ts)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度（33 files, 12,619 lines）
- [x] 识别跨主线交叉引用（bridgeEnabled→ML-06 auth, transport→ML-05, messaging→ML-02/ML-04）
- [x] 支线发现：评估 Branch Point → 发现 3 条 BL（BL-09-01 故障注入, BL-09-02 终端UI, BL-09-03 Worktree指针）
- [x] 支线追踪：对每条 BL 做 STANDARD 深度内联追踪（BL-09-01: 1 file/135 lines, BL-09-02: 2 files/693 lines, BL-09-03: 1 file/210 lines）
- [x] Pattern instance catalog：ML-09 不拥有任何 Pattern Category，无 catalog
- [x] 构建文件级 map（33 deep files + 0 catalog + 3 BL files = 33 unique files）
- [x] Sub-map 容量校验（总 12,619 行 > 10,000 → 拆分为 ML-09-1: 5,472 行 + ML-09-2: 7,147 行）
- [x] 写出 map/sub-maps/ML-09-1.md + ML-09-2.md（含 Branch Lines 节 + Pattern Instances 节）
- [x] 追加 map/mainline-file-map.jsonl（ML-09-1 + ML-09-2 两条记录）
- [x] 全量重建 map/mapped-files.jsonl（887 files, 228,839 lines）
- [x] 追加/更新 map/call-graph.jsonl（236 entries, 含 33 bridge files）
- [x] 更新 metadata.json（mainline_count=9, mapped_file_count=887, mapped_lines=228,839）
- [x] 验证所有 JSONL 文件格式和字段完整性
