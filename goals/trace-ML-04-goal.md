# Goal: trace-ML-04 权限系统

- [x] 确认入口文件 (permissions.ts + permissionSetup.ts)
- [x] 沿主线追踪文件 (import/call chain) — DEEP 深度 (28 deep files)
- [x] 识别跨主线交叉引用 (useCanUseTool.tsx ↔ ML-03, Tool.ts ↔ ML-03)
- [x] 支线发现：BL-04-01 (远程权限桥接), BL-04-02 (MCP 频道权限)
- [x] 支线追踪：2 条 BL STANDARD 深度内联追踪
- [x] Pattern instance catalog：PI-06 permission-component (52 catalog + 1 forced-deep)
- [x] 构建文件级 map (28 deep + 52 catalog + 2 BL = 82 unique)
- [x] Sub-map 容量校验 (ML-04 deep 12,009 lines > 10,000 → 拆为 2 段)
- [x] 写出 sub-maps (ML-04-1.md + ML-04-2.md)
- [x] 追加 instance-manifest.jsonl (52 PI-06 catalog entries)
- [x] 追加/更新 call-graph.jsonl (81 entries, 6 cross-ref)
- [x] 更新 metadata.json (mainline_count=4, mapped_file_count=521, mapped_lines=130721)
- [x] 追加 mapped-files.jsonl (rebuilt: 521 files, 86 deep + 435 catalog)
- [x] 追加 mainline-file-map.jsonl (ML-04-1 + ML-04-2)
- [x] 更新 pattern-categories.jsonl (PI-06 owner_ml = ML-04)
- [x] 更新 tasks.md (trace-ML-04 marked [x])
