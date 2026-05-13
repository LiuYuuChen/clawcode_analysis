# Repo Map: claude-code

## Scope

### Available Materials
- **完整源码树**：2021 个 TypeScript/TSX/JS/JSX 文件，总计 514,927 行
- **依赖清单**：`package.json`（版本 `999.0.0-restored`，Bun 运行时）
- **配置文件**：`tsconfig.json`（ESM, strict: false, react-jsx, path alias `src/*`）
- **入口文件**：[`src/bootstrap-entry.ts`](/src/src/bootstrap-entry.ts.md)（5 行，启动宏入口）→ [`src/entrypoints/cli.tsx`](/src/src/entrypoints/cli.tsx.md)（303 行，快速路径分发）
- **核心模块**：[`src/main.tsx`](/src/src/main.tsx.md)（4690 行，Commander 注册 + REPL 启动）、[`src/QueryEngine.ts`](/src/src/QueryEngine.ts.md)（1295 行，对话循环引擎）、[`src/query.ts`](/src/src/query.ts.md)（1729 行，底层查询执行）
- **工具注册表**：[`src/tools.ts`](/src/src/tools.ts.md)（389 行，51 个工具 + ant-only 条件导入）
- **命令注册表**：[`src/commands.ts`](/src/src/commands.ts.md)（754 行，80+ slash commands）
- **任务类型定义**：[`src/Task.ts`](/src/src/Task.ts.md)（125 行，7 种 TaskType 枚举）

### Missing Materials
- **无自动化测试套件**：项目内无 test/ 目录，`*.test.ts` 文件被排除（实际不存在）
- **无原始上游仓库**：此为通过 source map 逆向还原的源码树，非 Anthropic 原始仓库
- **无 CI/CD 配置**：无 GitHub Actions、Dockerfile 等部署配置（被原始构建流程剥离）
- **无 CHANGELOG/CONTRIBUTING**：这些文件在还原过程中未包含
- **部分模块为 shim/fallback**：`shims/` 目录包含兼容性替代实现

### Batch Plan
仓库规模适中（51.5 万行），目录结构清晰，无需分批。主线追踪阶段将按 ML 分批执行。

## One-Sentence Summary

**Claude Code** 是 Anthropic 官方推出的**终端 AI 编程助手 CLI 工具**，通过 REPL 交互界面接收用户输入，驱动 Claude API 进行对话推理，并通过 50+ 内置工具（文件编辑、命令执行、代码搜索、MCP 协议等）完成代码生成/修改/分析等编程任务。

## Architecture Diagram (Text)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         User Terminal                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────────┐   │
│  │ CLI Args │  │ REPL     │  │ IDE(Bridge)│  │ Slash Commands  │   │
│  └────┬─────┘  └────┬─────┘  └─────┬─────┘  └───────┬─────────┘   │
│       │              │              │                 │             │
│       ▼              ▼              ▼                 ▼             │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    main.tsx (Commander)                       │   │
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────────────┐  │   │
│  │  │ entrypoints│→ │ QueryEngine  │→ │ query.ts (API Layer) │  │   │
│  │  │ /cli.tsx   │  │ (主循环)     │  │ → Anthropic API      │  │   │
│  │  │ /init.ts   │  └──────┬───────┘  └──────────────────────┘  │   │
│  │  └────────────┘         │                                     │   │
│  │                         ▼                                     │   │
│  │  ┌────────────────────────────────────────────────────────┐  │   │
│  │  │                   Tool Dispatch                        │  │   │
│  │  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌─────┐ ┌─────┐ │  │   │
│  │  │  │Bash  │ │File  │ │Grep  │ │MCP   │ │Web  │ │Agent│ │  │   │
│  │  │  │Tool  │ │Edit  │ │Tool  │ │Tool  │ │Tool │ │Tool │ │  │   │
│  │  │  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬──┘ └──┬──┘ │  │   │
│  │  └─────┼────────┼────────┼────────┼────────┼────────┼────┘  │   │
│  │        ▼        ▼        ▼        ▼        ▼        ▼       │   │
│  │  ┌────────────────────────────────────────────────────────┐ │   │
│  │  │              Permission System (拦截门控)              │ │   │
│  │  │  autoMode / bashClassifier / yoloClassifier / rules    │ │   │
│  │  └────────────────────────────────────────────────────────┘ │   │
│  │                                                             │   │
│  │  ┌──────────┐  ┌───────────┐  ┌───────────────┐           │   │
│  │  │ Task     │  │ Auth/     │  │ Services      │           │   │
│  │  │ System   │  │ Session   │  │ (compact/lsp/ │           │   │
│  │  │ (7 types)│  │ (OAuth)   │  │  analytics/…) │           │   │
│  │  └──────────┘  └───────────┘  └───────────────┘           │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              TUI Layer (ink fork + React Components)          │   │
│  │  src/ink/ (framework) → src/components/ (406 files)          │   │
│  │  src/hooks/ (97 hooks) → src/screens/ (REPL.tsx main)       │   │
│  │  src/state/ (Zustand store)                                  │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              Bridge Layer (IDE Remote Connection)             │   │
│  │  src/bridge/ (33 files) → VSCode/JetBrains IDE plugin        │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Module Map

| Directory | Responsibility | Files | Lines |
|-----------|---------------|-------|-------|
| `src/` (顶层) | 核心引擎：入口、查询引擎、工具注册、命令注册、类型定义 | 21 | 12,131 |
| `src/entrypoints/` | CLI 入口与初始化（cli.tsx 快速路径 + init.ts 遥测/配置/OAuth 初始化） | 14 | 4,153 |
| `src/tools/` | 51 个工具实现子目录（AgentTool, BashTool, FileEditTool, MCPTool 等） | 199 | 50,900 |
| `src/commands/` | 102 个 slash command 实现（help, config, mcp, permissions, review 等） | 213 | 26,479 |
| `src/services/` | 后端服务模块（api, mcp, analytics, compact, oauth, lsp, plugins 等 22 个子目录） | 148 | 53,812 |
| `src/components/` | React TUI 组件（消息渲染、权限对话框、设置、diff 视图、提示输入等） | 406 | 81,637 |
| `src/hooks/` | React hooks（97 个 use*.ts，覆盖工具权限、IDE 集成、语音、MCP 管理等） | 105 | 19,205 |
| `src/ink/` | ink TUI 框架的 fork（100 文件，含自定义组件/hooks/layout/termio） | 99 | 19,879 |
| `src/bridge/` | 远程 IDE 桥接模式（session 管理、消息传输、权限回调） | 33 | 12,619 |
| `src/cli/` | CLI 传输层（stdio, HTTP, 信号处理） | 20 | 12,360 |
| `src/utils/` | 工具函数库（permissions 子目录 25 文件，config, api, diff 等） | 570 | 180,521 |
| `src/tasks/` | 7 种任务类型实现（LocalShell/LocalAgent/RemoteAgent/Dream/InProcessTeammate/LocalWorkflow/MonitorMcp） | 14 | 3,296 |
| `src/screens/` | 顶层屏幕组件（REPL.tsx 主交互界面, Doctor.tsx, ResumeConversation.tsx） | 3 | 6,033 |
| `src/state/` | 全局状态管理（AppState + Zustand store） | 6 | 1,190 |
| `src/bootstrap/` | 启动状态（state.ts，含遥测计数器和全局标志） | 1 | 1,758 |
| `src/context/` | React Context 提供者（mailbox, modal, notifications, voice, stats 等） | 9 | 1,004 |
| `src/types/` | TypeScript 类型定义（message types, tool types, session types） | 19 | 3,617 |
| `src/skills/` | 技能系统（bundled skill 资源 + skill 加载/注册） | 24 | 4,072 |
| `src/keybindings/` | 快捷键定义与处理 | 15 | 3,176 |
| `src/constants/` | 常量定义 | 22 | 2,649 |
| `src/memdir/` | 内存目录管理（CLAUDE.md 会话记忆） | 9 | 1,737 |
| `src/vim/` | Vim 模式支持 | 5 | 1,513 |
| `src/native-ts/` | 原生 TypeScript 模块（文件系统操作、平台检测等） | 4 | 4,081 |
| `src/migrations/` | 数据迁移脚本 | 11 | 603 |
| `src/buddy/` | 后台伙伴系统 | 6 | 1,298 |
| `src/remote/` | 远程环境管理 | 4 | 1,127 |
| `src/coordinator/` | 协调器（Swarm 模式） | 2 | 370 |
| `src/voice/` | 语音输入/输出 | 1 | 54 |
| `src/proactive/` | 主动触发系统 | 2 | 63 |
| `vendor/` | 原生模块源码（audio-capture, image-processor, modifiers-napi, url-handler） | 4 | 438 |
| `shims/` | 兼容性 shim（ant-claude-for-chrome-mcp, ant-computer-use-input/mcp 等） | 9 | 749 |

## Entrypoints and Main Flow

### Startup Chain (事实)
```
bootstrap-entry.ts (5 lines, MACRO.VERSION + ensureBootstrapMacro)
  → entrypoints/cli.tsx (303 lines)
    → Fast path: --version (no module loading), --dump-system-prompt (ant-only)
    → Normal path: loads startupProfiler → entrypoints/init.ts → main.tsx
      → entrypoints/init.ts (340 lines, memoized init)
        → Config enabling, OAuth account, telemetry, policy limits
        → Remote managed settings, CA certs, proxy, mTLS
        → Repository detection, graceful shutdown setup
      → main.tsx (4690 lines)
        → Commander program definition
        → Registers 80+ slash commands (via commands.ts)
        → Default action: launch REPL (screens/REPL.tsx)
        → Subcommand routing: login/logout/config/mcp/init/doctor/etc.
```

### Query Execution Chain (事实)
```
User Input (REPL.tsx TextInput)
  → QueryEngine.ts (1295 lines, state machine)
    → Manages conversation state, streaming responses
    → Handles tool_use dispatch, interruptions, model switching
    → Calls query.ts (1729 lines) for actual API requests
      → query.ts: Builds messages, creates API request
        → services/api/claude.ts → Anthropic Messages API
        → Streaming event processing
        → Tool dispatch loop (find tool by name → execute → append result)
    → Auto-compact when context exceeds limits
      → services/compact/ (context window management)
```

### Tool Dispatch Chain (事实)
```
QueryEngine detects tool_use block
  → Tool.ts: findToolByName() lookup
  → tools.ts: getTools() returns available tool set
    → Tool instance .execute() called with validated params
    → Permission check (hooks/useCanUseTool.tsx → utils/permissions/)
      → If denied: returns PermissionDenied result
      → If allowed: executes tool action
    → Tool result appended to conversation
    → Back to QueryEngine for next iteration
```

## Dependencies and Configuration Sources

### Runtime Dependencies (事实)
- **Bun** ≥1.3.5（主要运行时）/ **Node** ≥24（替代运行时）
- **@anthropic-ai/sdk**：Claude API 客户端
- **React** + **ink**（fork）：TUI 渲染框架
- **Zustand**：状态管理
- **@opentelemetry/api**：遥测基础设施
- **Commander**：CLI 参数解析
- **lodash-es**：工具函数

### Build-time Dependencies
- **Bun bundle**：`feature()` 用于死代码消除（ant-only 功能门控）
- **MACRO**：编译时宏（VERSION, REQUIRE 等）
- **TypeScript**：ESM + strict: false + react-jsx

### Configuration Sources (事实)
- **环境变量**：`CLAUDE_CODE_REMOTE`, `CLAUDE_CODE_ABLATION_BASELINE`, `USER_TYPE=ant`
- **Feature flags**：`feature('KAIROS')`, `feature('PROACTIVE')`, `feature('BRIDGE_MODE')`, `feature('COORDINATOR_MODE')`, `feature('VOICE_MODE')`, `feature('CONTEXT_COLLAPSE')`, `feature('AGENT_TRIGGERS')`, `feature('MONITOR_TOOL')` 等
- **文件配置**：`~/.claude/` 目录（CLAUDE.md, settings.json, credentials）
- **MCP 配置**：`claude_desktop_config.json` 格式

### Conditional Features (事实)
- **ant-only** (`process.env.USER_TYPE === 'ant'`): REPLTool, SuggestBackgroundPRTool, Chrome integration, ablation baseline
- **Feature-gated**: SleepTool (PROACTIVE/KAIROS), CronTools (AGENT_TRIGGERS), MonitorTool (MONITOR_TOOL), PushNotificationTool (KAIROS), VoiceMode (VOICE_MODE)

## Key Risks and Legacy Hotspots

1. **[`src/main.tsx`](/src/src/main.tsx.md) (4690 行) 巨型文件** — 事实: 包含 Commander 注册 + REPL 启动 + 子命令路由，是最难维护的文件
2. **`src/utils/` (570 文件/180,521 行) 过度膨胀** — 事实: 最大目录，含 permissions(25 文件)、config、diff、api 工具等，职责边界模糊
3. **`src/ink/` fork 的维护风险** — 推测: fork 了 ink 框架（100 文件），可能与上游严重 diverge，升级困难
4. **大量条件导入和死代码消除** — 事实: `process.env.USER_TYPE === 'ant'` 和 `feature()` 散布在 tools.ts、commands.ts、cli.tsx 等核心文件中，增加认知复杂度
5. **还原仓库的完整性** — 推测: 部分模块可能缺失原始实现（shims/ 目录的存在暗示某些功能为兼容性替代），分析结论需谨慎对待
6. **无测试套件** — 事实: 项目无自动化测试，代码质量依赖类型检查和手动验证
7. **`strict: false`** — 事实: TypeScript strict 模式未开启，潜在的类型安全问题

## Recommended Reading Order

1. [`src/entrypoints/cli.tsx`](/src/src/entrypoints/cli.tsx.md) → [`src/entrypoints/init.ts`](/src/src/entrypoints/init.ts.md) → 理解启动链
2. [`src/main.tsx`](/src/src/main.tsx.md) (重点：Commander 定义 + REPL 启动) → 理解命令路由
3. [`src/QueryEngine.ts`](/src/src/QueryEngine.ts.md) → 理解对话主循环
4. [`src/query.ts`](/src/src/query.ts.md) → 理解 API 调用和消息处理
5. [`src/Tool.ts`](/src/src/Tool.ts.md) + [`src/tools.ts`](/src/src/tools.ts.md) → 理解工具类型系统和注册
6. `src/utils/permissions/` → 理解权限系统（自动模式、分类器、规则解析）
7. [`src/services/api/claude.ts`](/src/src/services/api/claude.ts.md) + [`src/services/api/client.ts`](/src/src/services/api/client.ts.md) → 理解 API 客户端
8. `src/services/mcp/` → 理解 MCP 协议集成
9. `src/bridge/` → 理解远程 IDE 模式
10. [`src/screens/REPL.tsx`](/src/src/screens/REPL.tsx.md) + `src/components/` → 理解 TUI 层

## Main Lines (主线列表)

### ML-01: CLI 启动与命令路由
- **Priority**: P1
- **Entry**: [`src/bootstrap-entry.ts`](/src/src/bootstrap-entry.ts.md)
- **Key Modules**: [`src/entrypoints/cli.tsx`](/src/src/entrypoints/cli.tsx.md), [`src/entrypoints/init.ts`](/src/src/entrypoints/init.ts.md), [`src/main.tsx`](/src/src/main.tsx.md), [`src/commands.ts`](/src/src/commands.ts.md)
- **Exit**: Command execution or REPL launch ([`src/screens/REPL.tsx`](/src/src/screens/REPL.tsx.md))
- **Estimated Files**: ~25
- **Description**: 从用户终端输入到命令分发/REPL 启动的完整启动链路，包含环境检测、快速路径分发、初始化序列、Commander 注册
- **Priority Rationale**: 所有用户交互的入口路径，系统可用性的关键路径

### ML-02: 查询引擎主循环
- **Priority**: P1
- **Entry**: [`src/QueryEngine.ts`](/src/src/QueryEngine.ts.md)
- **Key Modules**: [`src/query.ts`](/src/src/query.ts.md), [`src/services/api/claude.ts`](/src/src/services/api/claude.ts.md), [`src/services/api/client.ts`](/src/src/services/api/client.ts.md), `src/services/compact/`
- **Exit**: API response or tool_use dispatch
- **Estimated Files**: ~30
- **Description**: 用户消息 → QueryEngine 状态机 → API 请求构建 → 流式响应处理 → 工具调度循环 → 上下文压缩
- **Priority Rationale**: 核心业务路径，涉及数据持久化（对话历史）和 AI 模型交互的关键链路

### ML-03: 工具系统注册与调度
- **Priority**: P1
- **Entry**: [`src/Tool.ts`](/src/src/Tool.ts.md)
- **Key Modules**: [`src/tools.ts`](/src/src/tools.ts.md), `src/tools/BashTool/`, `src/tools/AgentTool/`, `src/tools/FileEditTool/`
- **Exit**: Tool result (success/permission-denied/error)
- **Estimated Files**: ~15 (核心注册) + ~189 (工具实例, catalog)
- **Description**: Tool 接口定义 → 注册表管理 → 工具发现 → 参数验证 → 权限检查 → 执行 → 结果返回
- **Priority Rationale**: 50+ 工具的注册/权限/执行是核心功能路径

### ML-04: 权限系统
- **Priority**: P1
- **Entry**: [`src/utils/permissions/permissions.ts`](/src/src/utils/permissions/permissions.ts.md)
- **Key Modules**: [`src/utils/permissions/autoModeState.ts`](/src/src/utils/permissions/autoModeState.ts.md), [`src/utils/permissions/bashClassifier.ts`](/src/src/utils/permissions/bashClassifier.ts.md), [`src/utils/permissions/yoloClassifier.ts`](/src/src/utils/permissions/yoloClassifier.ts.md), [`src/utils/permissions/permissionRuleParser.ts`](/src/src/utils/permissions/permissionRuleParser.ts.md), [`src/hooks/useCanUseTool.tsx`](/src/src/hooks/useCanUseTool.tsx.md)
- **Exit**: Permission allow/deny decision
- **Estimated Files**: ~40 (25 permission utils + 15 hooks/components)
- **Description**: 权限模式管理 → bash 命令分类 → 规则解析匹配 → 用户提示决策 → 自动模式/yolo 模式门控
- **Priority Rationale**: 安全关键路径，控制工具执行的授权决策

### ML-05: MCP 服务集成
- **Priority**: P1
- **Entry**: [`src/services/mcp/MCPConnectionManager.tsx`](/src/src/services/mcp/MCPConnectionManager.tsx.md)
- **Key Modules**: [`src/services/mcp/client.ts`](/src/src/services/mcp/client.ts.md), [`src/services/mcp/config.ts`](/src/src/services/mcp/config.ts.md), `src/tools/MCPTool/`, [`src/services/mcp/claudeai.ts`](/src/src/services/mcp/claudeai.ts.md)
- **Exit**: MCP tool call result
- **Estimated Files**: ~25
- **Description**: MCP 服务器发现 → 连接管理 → 工具注册 → OAuth 认证 → 工具调用 → 结果转发
- **Priority Rationale**: 外部工具协议，核心扩展机制，涉及第三方服务交互

### ML-06: 认证与会话管理
- **Priority**: P1
- **Entry**: [`src/services/oauth/client.ts`](/src/src/services/oauth/client.ts.md)
- **Key Modules**: [`src/services/api/bootstrap.ts`](/src/src/services/api/bootstrap.ts.md), [`src/bootstrap/state.ts`](/src/src/bootstrap/state.ts.md), `src/utils/config.js`, [`src/entrypoints/init.ts`](/src/src/entrypoints/init.ts.md)
- **Exit**: Authenticated API session
- **Estimated Files**: ~20
- **Description**: OAuth 流程 → API key 验证 → 会话创建/恢复 → 遥测初始化 → 策略限制加载
- **Priority Rationale**: 涉及用户认证和 API 授权，系统可用性关键路径

### ML-07: TUI 渲染与交互
- **Priority**: P2
- **Entry**: [`src/screens/REPL.tsx`](/src/src/screens/REPL.tsx.md)
- **Key Modules**: `src/ink/`, `src/components/`, `src/hooks/`, `src/state/`, `src/context/`
- **Exit**: Terminal render output
- **Estimated Files**: ~600 (ink fork 100 + components 406 + hooks 97)
- **Description**: ink 框架渲染 → 组件树构建 → 消息渲染 → 用户输入处理 → 状态管理 → 快捷键绑定
- **Priority Rationale**: 内部交互层，不涉及核心业务逻辑或数据持久化，但影响用户体验

### ML-08: 任务系统
- **Priority**: P2
- **Entry**: [`src/Task.ts`](/src/src/Task.ts.md)
- **Key Modules**: `src/tasks/LocalShellTask/`, `src/tasks/LocalAgentTask/`, `src/tasks/RemoteAgentTask/`, `src/tasks/DreamTask/`, `src/tasks/InProcessTeammateTask/`, `src/tasks/LocalWorkflowTask/`, `src/tasks/MonitorMcpTask/`
- **Exit**: Task completion/failure
- **Estimated Files**: ~15
- **Description**: 7 种任务类型的生命周期管理：创建 → 调度 → 执行 → 监控 → 完成/失败
- **Priority Rationale**: 后台任务执行系统，非主链路但重要

### ML-09: Bridge 远程模式
- **Priority**: P2
- **Entry**: [`src/bridge/initReplBridge.ts`](/src/src/bridge/initReplBridge.ts.md)
- **Key Modules**: [`src/bridge/replBridge.ts`](/src/src/bridge/replBridge.ts.md), [`src/bridge/remoteBridgeCore.ts`](/src/src/bridge/remoteBridgeCore.ts.md), [`src/bridge/sessionRunner.ts`](/src/src/bridge/sessionRunner.ts.md), [`src/bridge/bridgeApi.ts`](/src/src/bridge/bridgeApi.ts.md)
- **Exit**: IDE plugin response
- **Estimated Files**: ~33
- **Description**: IDE 连接建立 → REPL 桥接 → 消息双向传输 → 权限回调 → 会话管理
- **Priority Rationale**: 非所有用户必用，但 IDE 集成是重要功能

### ML-10: API 客户端与重试层
- **Priority**: P2
- **Entry**: [`src/services/api/client.ts`](/src/src/services/api/client.ts.md)
- **Key Modules**: [`src/services/api/claude.ts`](/src/src/services/api/claude.ts.md), [`src/services/api/withRetry.ts`](/src/src/services/api/withRetry.ts.md), [`src/services/api/errors.ts`](/src/src/services/api/errors.ts.md), [`src/services/api/logging.ts`](/src/src/services/api/logging.ts.md)
- **Exit**: API response or error
- **Estimated Files**: ~21
- **Description**: HTTP 客户端 → 请求构建 → 认证头注入 → 重试策略 → 错误处理 → 使用量跟踪
- **Priority Rationale**: 内部服务层，被 ML-02 调用，非直接面向用户

### ML-11: 上下文与记忆管理
- **Priority**: P2
- **Entry**: [`src/services/compact/autoCompact.ts`](/src/src/services/compact/autoCompact.ts.md)
- **Key Modules**: [`src/services/compact/compact.ts`](/src/src/services/compact/compact.ts.md), `src/memdir/`, `src/services/contextCollapse/` (feature-gated)
- **Exit**: Compacted context or memory update
- **Estimated Files**: ~15
- **Description**: 上下文窗口监控 → 自动压缩触发 → 消息摘要 → CLAUDE.md 记忆管理 → context collapse (experimental)
- **Priority Rationale**: 配置/初始化链路，影响长对话质量但不阻塞核心功能


### ML-12: Plugin System
- **Priority**: P2
- **Entry**: [`src/utils/plugins/pluginLoader.ts`](/src/src/utils/plugins/pluginLoader.ts.md)
- **Key Modules**: [`src/utils/plugins/pluginLoader.ts`](/src/src/utils/plugins/pluginLoader.ts.md) (3302L), [`src/utils/plugins/marketplaceManager.ts`](/src/src/utils/plugins/marketplaceManager.ts.md) (2643L), [`src/utils/plugins/installedPluginsManager.ts`](/src/src/utils/plugins/installedPluginsManager.ts.md) (1268L), [`src/utils/plugins/schemas.ts`](/src/src/utils/plugins/schemas.ts.md) (1681L), [`src/utils/plugins/validatePlugin.ts`](/src/src/utils/plugins/validatePlugin.ts.md) (903L), [`src/utils/plugins/loadPluginCommands.ts`](/src/src/utils/plugins/loadPluginCommands.ts.md) (946L), [`src/utils/plugins/mcpbHandler.ts`](/src/src/utils/plugins/mcpbHandler.ts.md) (968L), [`src/commands/plugin/ManagePlugins.tsx`](/src/src/commands/plugin/ManagePlugins.tsx.md) (2214L)
- **Exit**: Plugin loaded/installed/removed with hooks, commands, agents registered
- **Estimated Files**: ~49 (25,422 lines)
- **Description**: Plugin 生命周期管理 — 发现 → 加载验证 → 市场安装 → Agent/Command/Hook 注册 → 自动更新 → Blocklist/Policy 约束
- **Priority Rationale**: 扩展系统，非核心业务路径，但影响用户定制能力
- **Scope Dirs**: `src/utils/plugins/`, `src/services/plugins/`, `src/commands/plugin/`

### ML-13: Bash/Shell Engine
- **Priority**: P2
- **Entry**: [`src/utils/bash/bashParser.ts`](/src/src/utils/bash/bashParser.ts.md)
- **Key Modules**: [`src/utils/bash/bashParser.ts`](/src/src/utils/bash/bashParser.ts.md) (4436L), [`src/utils/bash/ast.ts`](/src/src/utils/bash/ast.ts.md) (2679L), [`src/utils/shell/readOnlyCommandValidation.ts`](/src/src/utils/shell/readOnlyCommandValidation.ts.md) (1893L), [`src/utils/powershell/parser.ts`](/src/src/utils/powershell/parser.ts.md) (1804L), [`src/utils/bash/commands.ts`](/src/src/utils/bash/commands.ts.md) (1339L)
- **Exit**: Parsed command AST, validated safety prefix, shell execution provider
- **Estimated Files**: ~36 (17,680 lines)
- **Description**: Shell 命令解析引擎 — Bash AST 解析 (tree-sitter 兼容) → 安全验证 → PowerShell 解析 → Shell Provider 抽象 → 命令补全
- **Priority Rationale**: 核心工具依赖的底层引擎，非用户直接面向路径，但影响 Bash tool 的安全性
- **Scope Dirs**: `src/utils/bash/`, `src/utils/shell/`, `src/utils/powershell/`

### ML-14: Swarm Orchestration
- **Priority**: P2
- **Entry**: [`src/utils/swarm/inProcessRunner.ts`](/src/src/utils/swarm/inProcessRunner.ts.md)
- **Key Modules**: [`src/utils/swarm/inProcessRunner.ts`](/src/src/utils/swarm/inProcessRunner.ts.md) (1552L), [`src/utils/swarm/permissionSync.ts`](/src/src/utils/swarm/permissionSync.ts.md) (928L), [`src/utils/swarm/backends/TmuxBackend.ts`](/src/src/utils/swarm/backends/TmuxBackend.ts.md) (764L), [`src/utils/swarm/teamHelpers.ts`](/src/src/utils/swarm/teamHelpers.ts.md) (683L), [`src/utils/swarm/backends/registry.ts`](/src/src/utils/swarm/backends/registry.ts.md) (464L)
- **Exit**: Multi-agent teammate spawned and running in tmux/in-process pane
- **Estimated Files**: ~22 (7,548 lines)
- **Description**: 多 Agent 协作编排 — Backend 检测 (Tmux/ITerm/InProcess) → Teammate 启动 → 权限同步 → Reconnection → Layout 管理
- **Priority Rationale**: 高级功能，多 Agent 模式，非核心单 Agent 路径
- **Scope Dirs**: `src/utils/swarm/`, `src/utils/swarm/backends/`

### ML-15: SDK Entry Points
- **Priority**: P2
- **Entry**: [`src/entrypoints/sdk/coreSchemas.ts`](/src/src/entrypoints/sdk/coreSchemas.ts.md)
- **Key Modules**: [`src/entrypoints/sdk/coreSchemas.ts`](/src/src/entrypoints/sdk/coreSchemas.ts.md) (1889L), [`src/entrypoints/sdk/controlSchemas.ts`](/src/src/entrypoints/sdk/controlSchemas.ts.md) (663L)
- **Exit**: Zod-validated SDK types and schemas for external consumption
- **Estimated Files**: ~9 (2,716 lines)
- **Description**: SDK 类型定义和 Zod Schema — Core Types (Message/Content/Tool) → Control Schemas → Runtime/Settings Types → 生成类型
- **Priority Rationale**: API 边界定义，对外接口契约，影响 SDK 用户但非运行时主路径
- **Scope Dirs**: `src/entrypoints/sdk/`

## Implementation Code Baseline

- **Total source files** (glob): 2021
- **Implementation files** (after exclusions): 2019
- **Implementation total lines**: 514,917
- **Exclusion rules**:
  - `*.d.ts` (TypeScript ambient type declarations — 2 files excluded: `src/globals.d.ts`, `src/ink/global.d.ts`)
  - `*.test.ts`, `*.test.tsx`, `*.spec.ts`, `*.spec.tsx` (test files — none found in this repo)
  - `node_modules/**` (third-party dependencies)
  - `.code_analysis/**` (analysis artifacts)
- **Included**:
  - `vendor/` (4 files, 438 lines) — native module source code that is part of the project
  - `shims/` (9 files, 749 lines) — compatibility layers that are runtime-loaded
  - `src/ink/` (99 files, 19,879 lines) — fork of ink framework, treated as project source

### Breakdown by Top-Level Directory

| Directory | Impl Files | Lines | % of Total |
|-----------|-----------|-------|------------|
| src/utils | 570 | 180,521 | 35.1% |
| src/components | 406 | 81,637 | 15.9% |
| src/services | 148 | 53,812 | 10.5% |
| src/tools | 199 | 50,900 | 9.9% |
| src/commands | 213 | 26,479 | 5.1% |
| src/ink | 99 | 19,879 | 3.9% |
| src/hooks | 105 | 19,205 | 3.7% |
| src/bridge | 33 | 12,619 | 2.5% |
| src/cli | 20 | 12,360 | 2.4% |
| src (顶层) | 21 | 12,131 | 2.4% |
| src/screens | 3 | 6,033 | 1.2% |
| src/entrypoints | 14 | 4,153 | 0.8% |
| src/native-ts | 4 | 4,081 | 0.8% |
| src/skills | 24 | 4,072 | 0.8% |
| src/types | 19 | 3,617 | 0.7% |
| src/tasks | 14 | 3,296 | 0.6% |
| src/keybindings | 15 | 3,176 | 0.6% |
| src/constants | 22 | 2,649 | 0.5% |
| src/bootstrap | 1 | 1,758 | 0.3% |
| src/memdir | 9 | 1,737 | 0.3% |
| src/vim | 5 | 1,513 | 0.3% |
| src/buddy | 6 | 1,298 | 0.3% |
| src/state | 6 | 1,190 | 0.2% |
| src/remote | 4 | 1,127 | 0.2% |
| src/context | 9 | 1,004 | 0.2% |
| shims | 9 | 749 | 0.1% |
| src/upstreamproxy | 2 | 740 | 0.1% |
| src/query | 5 | 655 | 0.1% |
| src/migrations | 11 | 603 | 0.1% |
| vendor | 4 | 438 | 0.1% |
| 其他（coordinator, server, schemas, plugins 等 7 个小目录） | 15 | 1,406 | 0.3% |
| **Total** | **2019** | **514,917** | **100%** |

## Candidate Paths for Deep Analysis

### Path 1: User Request → AI Response (ML-02 核心)
- **Why it matters**: 这是产品的核心价值链，从用户输入到 AI 响应的完整路径
- **Likely entry**: [`src/QueryEngine.ts`](/src/src/QueryEngine.ts.md) → `query()` function
- **Key files**: QueryEngine.ts, query.ts, services/api/claude.ts, services/api/client.ts

### Path 2: Tool Permission Decision (ML-04 安全关键)
- **Why it matters**: 权限系统决定工具是否可执行，直接影响安全性
- **Likely entry**: [`src/hooks/useCanUseTool.tsx`](/src/src/hooks/useCanUseTool.tsx.md)
- **Key files**: hooks/useCanUseTool.tsx, utils/permissions/permissions.ts, utils/permissions/bashClassifier.ts

### Path 3: MCP Server Connection (ML-05 扩展机制)
- **Why it matters**: MCP 是外部工具扩展的核心协议
- **Likely entry**: [`src/services/mcp/MCPConnectionManager.tsx`](/src/src/services/mcp/MCPConnectionManager.tsx.md)
- **Key files**: services/mcp/MCPConnectionManager.tsx, services/mcp/client.ts, services/mcp/config.ts

### Path 4: IDE Bridge Communication (ML-09)
- **Why it matters**: IDE 集成是企业用户的核心使用场景
- **Likely entry**: [`src/bridge/initReplBridge.ts`](/src/src/bridge/initReplBridge.ts.md)
- **Key files**: bridge/initReplBridge.ts, bridge/replBridge.ts, bridge/remoteBridgeCore.ts

### Path 5: Context Window Management (ML-11)
- **Why it matters**: 长对话的上下文压缩直接影响 AI 响应质量
- **Likely entry**: [`src/services/compact/autoCompact.ts`](/src/src/services/compact/autoCompact.ts.md)
- **Key files**: services/compact/autoCompact.ts, services/compact/compact.ts
