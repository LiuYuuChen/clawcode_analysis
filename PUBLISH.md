# 发布分析站点到 GitHub Pages

将 `.code_analysis/` 内的 VitePress 站点构建并发布到 `LiuYuuChen/clawcode_analysis` 仓库的 `gh-pages` 分支，供 GitHub Pages 服务。

## 一次性准备

1. **本地仓库**：`.code_analysis/` 是独立 git 仓库（不是父 `claude-code` repo 的一部分），remote 已配置：
   ```
   origin  git@github.com:LiuYuuChen/clawcode_analysis.git
   ```
   - `main` 分支：分析源文档（markdown + JSONL 数据）
   - `gh-pages` 分支：渲染好的静态 HTML 站点

2. **GitHub Pages 设置**（手动一次）：
   - 进入 https://github.com/LiuYuuChen/clawcode_analysis/settings/pages
   - Source = `Deploy from a branch`
   - Branch = `gh-pages` / `(root)` → Save
   - 生效后访问 https://liuyuuchen.github.io/clawcode_analysis/

3. **依赖**：`cd .code_analysis && npm install`（首次或依赖变更后）

## 每次发布流程

```bash
cd /Users/liuyuchen/ai/open-resources/claude-code/.code_analysis

# 1) 清理缓存（避免命中旧 token 状态导致误差）
rm -rf .vitepress/cache .vitepress/dist

# 2) 构建（base 必须匹配仓库名，否则 Pages 路径 404）
./node_modules/.bin/vitepress build . --base /clawcode_analysis/

# 3) 用临时 worktree 推送 dist 内容到 gh-pages
git worktree add /tmp/clawcode_ghpages gh-pages
cd /tmp/clawcode_ghpages
git rm -rf .                                            # 清空旧内容
cp -R /Users/liuyuchen/ai/open-resources/claude-code/.code_analysis/.vitepress/dist/. .
touch .nojekyll                                         # 关键：阻止 Jekyll 处理 _ 前缀文件
git add -A
git commit -m "Republish VitePress site"
git push origin gh-pages

# 4) 清理 worktree
cd /Users/liuyuchen/ai/open-resources/claude-code/.code_analysis
git worktree remove /tmp/clawcode_ghpages
```

构建产物约 17 MB，360+ 文件。推送后 GitHub Pages 大约 1–2 分钟生效。

## 配置要点（`.vitepress/config.mts`）

发布所需的几项非默认配置：

```ts
ignoreDeadLinks: true,   // 报告里大量 /src/... 链接指向未发布的源码路径
```

**Vite 预处理插件** —— 把 markdown 里裸写的 TypeScript 泛型（`Map<string, X>`、`Set<Listener>`、`<TInput>` 等）用反引号包起来，避免 Vue 模板编译器把它们当成未闭合标签：

```ts
function transformSegment(s: string): string {
  return s
    .replace(/<([A-Za-z]\w*[\s,<][^<>`\n]*)>/g, '`<$1>`')
    .replace(/<(string|number|boolean|void|undefined|null|any|unknown|never|[A-Z]\w*)>/g, '`<$1>`')
}

vite: {
  plugins: [{
    name: 'escape-bare-generics',
    enforce: 'pre',
    transform(code, id) {
      if (!id.endsWith('.md')) return null
      // 按行扫描，跳过 ``` 围栏与已有的 `...` 内联代码
      // (实现见 config.mts)
    },
  }],
}
```

## 已知问题

- **T-16 暂时被 `srcExclude` 排除**（`branches/main/task-analyses/T-16-context-memory.md`）：该文件触发 Vue 编译器 "Duplicate attribute" 错误，未能定位根因（与 mermaid 块无关，渲染输出里也找不到重复属性）。排除后其他 39 篇 task analysis 正常构建。后续要么找到具体冲突字符、要么按文件粒度切分。
- **裸标签转义副作用**：转义后这些类型在页面上以行内代码样式（等宽字体）显示，与作者原意可能略有出入，但内容完整可读。

## 校验

```bash
# 检查 Pages 是否启用
curl -s -o /dev/null -w "%{http_code}\n" \
  https://api.github.com/repos/LiuYuuChen/clawcode_analysis/pages
# 200 = 已启用，404 = 未启用

# 检查站点首页
curl -sI https://liuyuuchen.github.io/clawcode_analysis/ | head -1
```

## 文件清单

- `.code_analysis/.vitepress/config.mts` — VitePress 配置 + 转义插件（在 `.code_analysis/.gitignore` 中，不进 main 分支）
- `.code_analysis/.vitepress/dist/` — 构建产物（不进任何分支，每次推送从这里复制到 gh-pages worktree）
- `serve_analysis.sh` — 本地预览脚本（dev/build/preview/stop），位于父项目根
