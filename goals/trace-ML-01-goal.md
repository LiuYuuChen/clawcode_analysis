# trace-ML-01 Goal: CLI 启动与命令路由

- [x] 确认入口文件 (src/bootstrap-entry.ts — 5行，绝对入口)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度 (19 deep files + 1 representative)
- [x] 识别跨主线交叉引用 (ML-02/ML-03/ML-05/ML-06/ML-07/ML-09)
- [x] 支线发现：评估每个 Branch Point 是否构成 BL — 无 BL 产出（分支归其他 ML 或源文件不存在）
- [x] 支线追踪：无 BL 需要追踪
- [x] Pattern instance catalog：PI-02 command-handler 归属 ML-01，代表文件 help/index.ts，189 catalog + 3 FAIL
- [x] 构建文件级 map（20 deep + 189 catalog = 209 files）
- [x] Sub-map 容量校验（DEEP 11,617行 > 10,000 → 拆分为 ML-01-1/2/3，各 722/4052/6843 行）
- [x] 写出 map/sub-maps/ML-01-1.md + ML-01-2.md + ML-01-3.md
- [x] 追加 map/instance-manifest.jsonl（189 条 PI-02 catalog 实例）
- [x] 追加/更新 map/call-graph.jsonl（19 个文件的 imports/called_by）
- [x] 更新 metadata.json（mainline_count=1, mapped_file_count=209, mapped_lines=31665）
- [x] 追加 mapped-files.jsonl（209 文件：20 deep + 189 catalog）
- [x] 更新 pattern-categories.jsonl（PI-02 owner_ml=ML-01）
- [x] 追加 mainline-file-map.jsonl（ML-01 条目，含 split_info）
