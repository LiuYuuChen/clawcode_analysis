# publish-site Goal

- [x] 前置检查（metadata + final-report + 覆盖率 PASS）
- [x] 复制主题资产（R2: 纯默认主题，style.css 清空为空文件）
- [x] 生成源码映射（source-to-report-map.{md,jsonl}）— 1954 records
- [x] 生成 .vitepress/config.mts（R3: 两级目录侧边栏 + R4: withMermaid 包装 + cleanUrls: true）
- [x] 生成 VitePress 首页 index.md
- [x] 复制源码为 markdown（src/）— 2019 files
- [x] 改写分析文档中的源码链接（R1: 绝对路径 + 去 /.code_analysis/ 前缀 + 修复 3968 处）
- [x] 写入 package.json（R4: 含 mermaid 依赖）+ serve_analysis.sh + .code_analysis/.gitignore
- [x] 追加项目根 .gitignore（幂等，已存在）
- [x] 在 final-report 标注站点入口
- [x] 链接完整性验证（R1: 124→13 断链，余下为 missing summaries/JSONL/txt — 不可修复）
- [x] 软验证（Node OK + npm install OK + vitepress + mermaid plugin 已安装）
