# trace-ML-07 Goal Progress

- [x] 确认入口文件 src/screens/REPL.tsx (5061 行，God Component)
- [x] 沿主线追踪文件（import/call chain）— DEEP 深度 (81 files deep traced)
- [x] 识别跨主线交叉引用 (5 files: ink.ts→ML-01, context.ts→ML-01, useCanUseTool→ML-03+04, PermissionRequest→ML-04, SandboxPermission→ML-04)
- [x] 支线发现：评估每个 Branch Point → 4 条 BL (终端标题动画/Transcript搜索/FPS监控/通知子系统)
- [x] 支线追踪：对每条 BL 做 STANDARD 深度内联追踪
- [x] Pattern instance catalog：PI-03 (42 catalog) + PI-07 (90 catalog) + PI-08 (44 catalog) = 176 catalog entries
- [x] Pattern FAIL 强制 deep：5 files (useTypeahead 1385, useVoice 1144, ink.tsx 1723, screen.ts 1486, render-node-to-output.ts 1462)
- [x] 构建文件级 map（81 deep + 5 FAIL + 176 catalog = 262 files）
- [x] Sub-map 容量校验：4 段拆分，均 ≤10,000 行 (7544/7635/3775/7088)
- [x] 写出 map/sub-maps/ML-07-1.md ~ ML-07-4.md
- [x] 追加 map/instance-manifest.jsonl (176 new entries, total 611)
- [x] 追加/更新 map/call-graph.jsonl (180 entries total)
- [x] 更新 map/pattern-categories.jsonl (PI-03/PI-07/PI-08 owner_ml = ML-07)
- [x] 重建 map/mapped-files.jsonl (833 files, 208,846 lines)
- [x] 更新 metadata.json (mainline_count=7, mapped_file_count=833, mapped_lines=208846)
- [x] 更新 tasks.md (trace-ML-07 marked [x])
