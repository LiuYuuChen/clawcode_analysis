# Goal: trace-ML-06 认证与会话管理

- [x] 确认入口文件 src/services/oauth/client.ts 存在 (577行)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度
- [x] 识别跨主线交叉引用（init.ts→ML-01, state.ts→ML-01, config.ts→ML-01）
- [x] 支线发现：评估 Branch Point → BL-06-01(AWS), BL-06-02(SecureStorage), BL-06-03(Telemetry), BL-06-04(GrowthBook)
- [x] 支线追踪：4 条 BL 做 STANDARD 深度内联追踪
- [x] Pattern instance catalog：ML-06 不拥有任何 PI
- [x] 构建文件级 map（31 core/supporting + 12 BL files + 3 cross-ref）
- [x] Sub-map 容量校验（DEEP 8,586行 ≤ 10,000 ✅ 无需拆分）
- [x] 写出 map/sub-maps/ML-06-1.md（含 Branch Lines 节）
- [x] 追加 map/mainline-file-map.jsonl
- [x] 追加/更新 map/call-graph.jsonl
- [x] 更新 metadata.json（mainline_count=6, mapped_file_count, mapped_lines）
- [x] 全量重建 mapped-files.jsonl
- [x] 标记 tasks.md trace-ML-06 完成
