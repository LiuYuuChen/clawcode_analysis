# publish-site Goal

- [x] 前置检查（metadata + final-report + 覆盖率 PASS）
- [x] 复制主题资产（theme/index.ts, Layout.vue, style.css）
- [x] 生成源码映射（source-to-report-map.{md,jsonl}）
- [x] 生成 .vitepress/config.mts（动态主线枚举）
- [x] 生成 VitePress 首页 index.md
- [x] 复制源码为 markdown（src/）
- [x] 改写分析文档中的源码链接
- [x] 写入 package.json + serve_analysis.sh + .code_analysis/.gitignore
- [x] 追加项目根 .gitignore
- [x] 在 final-report 标注站点入口
- [x] 软验证（node/npm 可选）— Node v22.13.1 ✅, npm 11.1.0 ✅, npm install timed out (non-blocking, user runs ./serve_analysis.sh later)
