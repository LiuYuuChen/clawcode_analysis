# Goal: trace-ML-05 MCP 服务集成

- [x] 确认入口文件 (MCPConnectionManager.tsx)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度（30 文件）
- [x] 识别跨主线交叉引用（6 文件共享：Tool.ts/ML-03, commands.ts/ML-01, auth.js/ML-06, AppState.ts/ML-01+ML-07）
- [x] 支线发现：3 条 BL（BL-05-01 XAA认证 3files/1076行, BL-05-02 Elicitation 1file/313行, BL-05-03 Channel 3files/632行）
- [x] 支线追踪：对每条 BL 做 STANDARD 深度内联追踪
- [x] Pattern instance catalog：ML-05 不拥有任何 PI，无 catalog 编目
- [x] 构建文件级 map（30 文件：9 core + 21 supporting，全部 deep trace）
- [x] Sub-map 容量校验（DEEP 部分 ≤10000 行）→ 拆为 3 段（3,452 / 8,114 / 2,326）
- [x] 写出 map/sub-maps/ML-05-1.md, ML-05-2.md, ML-05-3.md（含 Branch Lines 节）
- [x] 追加 map/mainline-file-map.jsonl（3 条 ML-05 记录）
- [x] 追加/更新 map/call-graph.jsonl（30 个文件，总计 109 条目）
- [x] 更新 metadata.json（mainline_count=5, mapped_file_count=543, mapped_lines=142791）
- [x] 重建 mapped-files.jsonl（543 文件：114 deep + 429 catalog）
- [x] 创建 goals/trace-ML-05-goal.md
