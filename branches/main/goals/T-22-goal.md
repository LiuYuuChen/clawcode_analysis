# T-22 Goal Tracker: Pattern Audit — command-handler (PI-02)

- [x] 确认 task 范围（验证 scope files、读取定义）
- [x] 确定分析深度（OVERVIEW）
- [x] 读取 PI-02 pattern 定义和 Command type 接口
- [x] 从 instance-manifest.jsonl 读取 PI-02 全部 107 个实例
- [x] 抽样 8 个实例（按文件名首字母均匀分散）
- [x] 实读每个抽样实例，验证 pattern 约定
- [x] 识别 pattern 变体（index.ts / impl.ts/.tsx / createMovedToPluginCommand / standalone）
- [x] 更新 instance-manifest.jsonl 中抽样实例的 role_source = verified
- [x] 写出 ## File Roles 强制节（3 个 scope files）
- [x] 生成文件依赖关系图
- [x] 写出 task-analyses/T-22-audit-pi-02.md
- [x] 修订不准确的 role_one_liner（如需要）
- [x] 更新 task 状态
