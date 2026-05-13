# trace-ML-03 Goals: 工具系统注册与调度

- [x] 确认入口文件 src/Tool.ts 存在且可读
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度（16 core/supporting + 5 representative）
- [x] 识别跨主线交叉引用（4 个：src/tools.ts↔ML-01, src/Tool.ts/toolOrchestration.ts/StreamingToolExecutor.ts↔ML-02）
- [x] 支线发现：无 BL（工具系统是注册+分发层，分支归入各工具自身的子模块）
- [x] 支线追踪：N/A（0 条 BL）
- [x] Pattern instance catalog：PI-01 tool-instance，199 个文件，5 representative deep + 194 catalog
- [x] 构建文件级 map（含 ML core/supporting + catalog instances）
- [x] Sub-map 容量校验：deep 10,070 行 > 10,000 → 拆分为 ML-03-1 (3,014) + ML-03-2 (7,056)
- [x] 写出 map/sub-maps/ML-03-1.md + ML-03-2.md（含 Pattern Instances 节）
- [x] 追加 map/instance-manifest.jsonl（194 catalog 实例）
- [x] 追加/更新 map/call-graph.jsonl（16 条新记录）
- [x] 更新 metadata.json（mainline_count=3, mapped_file_count, mapped_lines）
- [x] 追加 mapped-files.jsonl（去重合并重建，含交叉引用更新）
