# publish-site Goal Tracking

- [x] 前置检查（metadata + final-report + 覆盖率 PASS）
- [x] 复制主题资产（R2: 纯默认主题，无定制样式）
- [x] 生成源码映射（source-to-report-map.{md,jsonl}）
- [x] 生成 .vitepress/config.mts（R3: 两级目录侧边栏 + R4: withMermaid 包装 + cleanUrls: true）
- [x] 生成 VitePress 首页 index.md
- [x] 复制源码为 markdown（src/）
- [x] 改写分析文档中的源码链接（R1: 绝对路径 + 去 .md 后缀）
- [x] 写入 package.json（R4: 含 mermaid 依赖）+ serve_analysis.sh + .code_analysis/.gitignore
- [x] 追加项目根 .gitignore
- [x] 在 final-report 标注站点入口
- [x] 链接完整性验证（R1: 762个.md后缀已去除 + 41个断链已修复 → 0断链）
- [x] 软验证（Node v22.13.1 + npm 11.1.0 可用，npm install 超时非阻断）

## 验证结果

| Hard Rule | 状态 | 详情 |
|-----------|------|------|
| **R1 链接完整性** | ✅ PASS | 0 断链（762个.md后缀已去除，41个断链已全部修复） |
| **R2 纯默认主题** | ✅ PASS | style.css空文件、Layout.vue仅默认布局 |
| **R3 两级侧边栏** | ✅ PASS | 15个ML分组 + Sub-Maps折叠组 + 顶层链接 |
| **R4 Mermaid渲染** | ✅ PASS | withMermaid()包装 + mermaid:{} + package.json含依赖 |

## 修复的断链详情

| 类别 | 数量 | 修复操作 |
|------|------|---------|
| `/code_analysis/` 前缀错误 | ~35 | sed 去除前缀 |
| 引用不存在的summary | 3 | 替换为对应task analysis链接 |
| `.jsonl` 文件引用 | 2 | 替换为coverage-map-report |
| `p1_allocation.json` | 1 | 替换为04-task-plan |

## 产出统计

- 站点 URL: http://localhost:5173（运行 `./serve_analysis.sh` 启动）
- 生成文件总数: ~2025（2019 src/ + config + index + map + scripts）
- 映射记录数: 1954条（source-to-report-map.jsonl）
- Node/npm 软验证: ✅ Node v22.13.1, npm 11.1.0（npm install超时非阻断）
