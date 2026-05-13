# Assumptions & Unknowns

## 事实缺口 (Confirmed Unknowns)

- 事实缺口: 此为通过 source map 逆向还原的源码树（非 Anthropic 原始上游仓库），部分模块可能缺失原始实现
- 事实缺口: `shims/` 目录包含 9 个兼容性替代文件，原始功能可能由闭源模块提供（如 `ant-chrome-mcp`, `ant-computer-use-input`）
- 事实缺口: `vendor/` 目录的 4 个原生模块（audio-capture, image-processor, modifiers-napi, url-handler）的具体编译和加载机制未验证
- 事实缺口: 项目无自动化测试套件，无法通过测试用例验证行为推断
- 事实缺口: `feature()` 函数的具体 flag 值集未完全枚举（已知 KAIROS/PROACTIVE/BRIDGE_MODE/COORDINATOR_MODE/VOICE_MODE/AGENT_TRIGGERS/MONITOR_TOOL/CONTEXT_COLLAPSE/DUMP_SYSTEM_PROMPT/ABLATION_BASELINE）
- 事实缺口: `process.env.USER_TYPE === 'ant'` 触发的内部版功能完整列表未完全验证
- 事实缺口: `src/services/api/grove.ts` 的用途未确认（推测为 Anthropic 内部 API endpoint）

## 推测 (Inferences)

- 推测: `src/ink/` 是 ink TUI 框架的 fork，可能包含针对 Claude Code 的定制修改（如 `src/ink/focus/`, `src/ink/terminal/` 等）
- 推测: `src/buddy/` 目录实现的后台伙伴系统可能是 KAIROS 功能的一部分（定时/触发式后台任务）
- 推测: `src/coordinator/` 实现的 Swarm 模式可能是多 Agent 协调机制（COODINATOR_MODE feature flag）
- 推测: `src/proactive/` 的主动触发系统可能与 SleepTool/CronTools 配合实现定时/条件触发
- 推测: `src/services/api/ultrareviewQuota.ts` 和 `src/services/api/overageCreditGrant.ts` 可能涉及 Anthropic 内部的配额/计费管理
- 推测: `src/services/api/grove.ts` 可能是 Anthropic 的内部服务 API（名称暗示某种树状结构服务）
- 推测: `src/remote/` 目录可能与 Bridge 模式共享部分远程会话管理逻辑
