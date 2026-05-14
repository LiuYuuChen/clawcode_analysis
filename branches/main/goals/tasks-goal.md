# Tasks Step Goal — claude-code main branch

- [x] 审阅已有上下文：逐条读取所有 sub-map ML-XX.md，提取 expected_mainlines
- [x] 定义分析任务：ML 驱动组织，每个 task 含 primary_mainline 字段
- [x] Pattern Audit task：为每个 pattern category 自动追加 1 个 P3/OVERVIEW task
- [x] 处理共享文件：按 Ownership Rules 决定唯一 owner，secondary_mainlines 标注
- [x] 构建依赖关系图：识别并行任务、排除循环依赖
- [x] 创建待办任务列表：使用 TodoTool_todo_create
- [x] 覆盖率预检：global ≥95% + 每条 ML ≥95% + core_files 100%
- [x] 质量门检查：ML 覆盖、共享文件无重复、验收标准可验证
- [x] 写出 03-analysis-tasks.md
