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

## T-01 Assumptions (2025-07-14)

1. **feature() 宏构建时 DCE 策略**: `feature()` 函数在运行时为 identity function，构建时由 Webpack/Terser 插件处理条件删除。具体编译配置在项目 scope 外（构建工具配置目录）。
2. **init() 17步串行依赖**: 假设步骤间的依赖关系是串行的（setEnv → registerShutdown → ...），但实际某些步骤可能无严格依赖，可以并行化。需要运行时 profiling 确认。
3. **STATE 单例初始化**: STATE 对象在模块加载时创建（空/null 初始值），通过 init() 和 action handler 逐步填充。假设没有其他初始化路径。
4. **MDM/Keychain 子进程并行安全**: 假设 Node.js 单线程事件循环保证了子进程 stdout 数据的完整性，不存在部分写入风险。
5. **setup() 外部模块行为**: setup() 来自外部编译模块（dist/），具体逻辑需要反编译或查看源码确认。假设其行为是创建 .claude 目录和 trust 文件。
6. **daemon 模式**: cli.tsx 中 daemon/bridge/bg 模式通过 dynamic import 加载，完整生命周期在 T-02 scope 中分析。
7. **agentSdkTypes.ts stub 函数**: 5 个 stub 函数（isAnthropicRequest, isMcpRequest 等）假设为 API boundary types，实际实现在 agent SDK 包中。
8. **AbortController sessionSwitched**: 假设所有 session switch 的监听者通过 AbortSignal 正确处理取消，没有遗漏的消费者。

## T-02 命令路由与REPL启动 (2025-07-14)

1. **local-jsx onDone 无超时**: local-jsx 命令的 Promise 等待 onDone 回调，但无 timeout/race 保护。如果有 bug 的组件不调用 onDone，用户输入将永久挂起。未确认是否有 Ink 层面的超时机制。(processSlashCommand.tsx:L551)
2. **KAIROS fork unhandled rejection**: `void (async () => { await runAgent() })()` 中未 catch 异常。假设 Bun 的 process-level unhandledRejection handler 会处理，但未验证。(processSlashCommand.tsx:L68)
3. **AppState ~100+ 字段无模块化**: 全局单例 store 管理所有状态（命令、配置、UI、成本等），假设 DeepImmutable proxy 在所有写路径上正确拦截。
4. **findCommand O(n) 可接受**: ~95 个命令的线性搜索在用户输入场景下不会成为瓶颈，因为 memoize 保证命令列表不频繁变化。
5. **6源命令加载完整覆盖**: `loadAllCommands()` 的 Promise.all 6源加载假设覆盖了所有命令来源。未验证是否有其他动态注册路径。
6. **onChangeAppState 副作用无异常隔离**: ~30 个 case 分支中的异常假设不会互相影响。如果某个分支 throw，可能中断后续分支执行。
7. **双白名单手动维护**: REMOTE_SAFE(17) + BRIDGE_SAFE(6) 假设通过人工 review 维护。无自动化检查确保新增命令被正确分类。
8. **doneWasCalled 防重入依赖 JS 单线程**: local-jsx Promise 中的 doneWasCalled flag 假设不会被并发修改。JS 单线程保证这一点。

## T-03 查询引擎核心循环 (2025-07-14)

1. **StreamingToolExecutor 并行度上限未知**: 工具并行执行的并发数量是否有上限未确认。如果 LLM 一次返回 10+ tool_use，StreamingToolExecutor 可能同时启动 10+ 工具进程。(depends on StreamingToolExecutor 完整实现，可能属于 T-04/T-05 scope)
2. **compactAttachment 构建失败语义**: Promise.all(buildAttachments) 中任一附件构建失败时是否 reject 整个 compact 操作未确认。(compact.ts buildAttachments 实现)
3. **state.transition 用途未完全确认**: transitions.ts 的 asTransition() 运行时仅做类型标记，实际语义需要更多上下文确认。(transitions.ts)
4. **queryLoop 无全局超时**: while(true) 循环无内部 escape hatch，完全依赖外部 AbortController 取消。假设消费者（REPL/SDK）会在合理时间内取消。
5. **circuit breaker 无 auto-reset**: autoCompact 的 circuit breaker 打开后永不自动关闭，后续所有 autoCompact 调用被跳过。假设这是有意的退化策略。
6. **PTL reactive compact 仅1次**: hasAttemptedReactiveCompact flag 确保整个 query 生命周期内只尝试1次 reactive compact。如果 compact 后上下文仍超限，查询直接终止。假设这是有意的安全阀。
7. **messages push 在单线程下安全**: state.messages.push(toolResult) 依赖 JS 单线程事件循环保证顺序。假设 StreamingToolExecutor 的结果收集在单线程 async 路径中完成。
8. **compact 3次 PTL retry 后无降级**: compactConversation 重试 x3 失败后直接 abort，无部分压缩或降级策略。假设用户可以重新发起查询。

### T-04 假设 (Query API Streaming & Messages)

- **T-04-A1**: queryModel() 的 ~1875 行 AsyncGenerator 实现中，SSE 事件处理是顺序的（JS 单线程保证），不存在真正的并行事件处理
- **T-04-A2**: message_delta 变异已 yield 对象的 usage 字段是有意设计，transcript writer 依赖引用共享来获取最终 usage 数据
- **T-04-A3**: toolToAPISchema() 的 session-stable 缓存设计假设 GrowthBook 特性开关在一次 session 中不会变化
- **T-04-A4**: StreamingToolExecutor 的 siblingAbort 级联取消仅针对 Bash tool，因为 Bash 的文件系统副作用需要原子性保证
- **T-04-A5**: 90s watchdog 超时值是基于经验设定的，可能需要根据 extended thinking 模型的行为调整
- **T-04-A6**: normalizeMessage() 的 30s bash/powershell 节流使用全局变量 lastProgressSent，假设 CLI 一次只处理一个请求
- **T-04-A7**: ensureToolResultPairing() 的 ~330 行修补逻辑主要解决 CC-1212 相关的 tool_use/tool_result 配对问题
- **T-04-A8**: normalizeMessagesForAPI() 的 10+ 步管线中，步骤顺序是有意义的（后续步骤依赖前序步骤的输出），不能随意重排

### T-05 工具系统核心调度 (2025-01-XX)

1. **[假设] checkPermissionsAndCallTool无外部重构计划**: 分析时未发现历史重构记录或TODO标记，假定该函数一直以当前形式存在和维护
2. **[假设] 并发上限10是经验值**: runToolsConcurrently的maxConcurrent=10未发现配置化或文档化依据，假定为经验调优值
3. **[假设] persistToolResult阈值基于API限制**: maybePersistLargeToolResult的阈值假定基于Anthropic API的tool_result大小限制
4. **[假设] deferred tool 10%阈值是平衡决策**: MCP token超过10% context window时启用deferred，假定是prompt cache效率与工具可用性的平衡点
5. **[假设] TOOL_DEFAULTS fail-closed是安全设计**: 8个字段全部默认"最不信任"值，假定是安全优先设计而非临时决策
6. **[假设] contextModifier仅在特定工具中使用**: 分析发现只有少数工具(如WriteTool)使用contextModifier机制，假定大部分工具不依赖此功能
7. **[假设] MCP/非MCP PostHook顺序差异是有意设计**: 两类工具的PostHook执行时机不同，假定是MCP协议要求的特殊处理
8. **[假设] findToolByName线性扫描性能可接受**: O(n)线性扫描在~100工具规模下性能可接受，假定没有工具名查找的性能瓶颈

### T-06 权限规则引擎 (8 条)
1. **[假设] hasPermissionsToUseTool/Inner拆分是为了避免递归**: 两个函数签名几乎相同但拆分为两层，假定是为了避免auto mode递归调用checkRuleBasedPermissions导致重复评估
2. **[假设] deny-first cascade是有意安全设计**: Steps 1a-1g全部bypass-immune，假定是fail-closed安全策略而非编码顺序巧合
3. **[假设] auto mode circuit breaker无自动恢复**: consecutiveDenials/totalDenials达到阈值后只能用户手动切回auto，假定是有意防止自动恢复到不安全状态
4. **[假设] channelPermissions first-resolver-wins足够**: MCP channel权限请求使用first-resolver-wins模式，假定MCP channels不会并发请求同一权限
5. **[假设] GrowthBook killswitch窗口期可接受**: useBypassPermissionsKillswitch异步检查有<100ms窗口期，假定用户不会在此窗口内执行bypass操作
6. **[假设] 内存-磁盘不一致是已知tradeoff**: applyPermissionUpdates先更新内存后写磁盘，假定persist失败场景极少
7. **[假设] FNV-1a 5字母ID+脏词过滤足够**: channelPermissions使用短ID，假定碰撞率和脏词漏检概率可接受
8. **[假设] shellRuleMatching独立文件是为了Bash特殊性**: Bash工具的glob+shell pattern匹配逻辑比其他工具复杂得多，假定单独文件是模块化决策

### T-07 Assumptions (权限AI分类器与文件系统)

1. **[假设] GrowthBook feature gate可用性**: verifyAutoModeGateAccess假定GrowthBook API大多数时候可用，不可用时熔断auto mode是可接受的降级
2. **[假设] Stage 1 classifier对clear case足够准确**: 64 token的Stage 1分类器对明显安全/危险操作足够准确，ambiguous case才需要Stage 2
3. **[假设] denialTracking阈值3/20是经验值**: consecutiveDenials>3和totalDenials>20的阈值是基于经验而非精确校准，可能需要根据实际使用调整
4. **[假设] JS单线程保证module-level state安全**: autoModeState的3个boolean变量依赖JS单线程保证读写安全，不假设Web Worker或Node.js worker_threads场景
5. **[假设] realpathSync在大多数环境下快速完成**: filesystem path safety依赖realpathSync同步调用，假定符号链接层级有限不会阻塞事件循环
6. **[假设] CLAUDE.md注入不会误导classifier**: buildClaudeMdMessage注入用户可控内容但classifier prompt中有"ignore instructions"指导，假定LLM遵循该指导
7. **[假设] 2-stage conditional API调用优于单次大调用**: Stage 1 (64 tokens) + conditional Stage 2 (4096 tokens) 的总成本低于每次都用4096 tokens
8. **[假设] dangerousPatterns硬编码列表覆盖常见场景**: DANGEROUS_BASH_PATTERNS / DANGEROUS_FILES / DANGEROUS_DIRECTORIES是静态列表，假定覆盖了最常见的高风险操作模式

### T-08 (MCP服务集成) Assumptions

1. **[T-08] MCP SDK Client API稳定性**: 分析基于MCP SDK Client的当前API（connect/close/request/notification），假设SDK不会在近期版本中改变这些核心接口。如果SDK升级，connectToServer中的enhanced handler可能需要适配。
2. **[T-08] Transport实现假设**: 7种Transport的创建逻辑分析基于源码中的条件分支，未实际运行每种Transport验证。特别是ws-ide和claudeai-proxy两种Transport的实际行为可能与代码推断有差异。
3. **[T-08] OAuth DCR可用性假设**: OAuth认证依赖RFC 7591 Dynamic Client Registration，假设server支持DCR。如果不支持，认证流程会走不同的分支（可能需要手动client_id配置）。
4. **[T-08] XAA token exchange假设**: XAA认证使用RFC 8693 token exchange + RFC 7523 JWT assertion，假设企业IdP支持这些标准。具体的token endpoint URL和audience从环境变量构建，未验证所有环境组合。
5. **[T-08] memoize缓存一致性假设**: lodash.memoize的缓存键使用serverConfig的hash值，假设hash碰撞概率足够低。如果不同配置产生相同hash，可能导致错误复用连接。
6. **[T-08] deferred工具加载阈值假设**: deferred模式在工具描述token超过context window 10%时触发，此阈值是硬编码的。具体的context window大小从T-04的model配置获取，假设该值在初始化时已确定。
7. **[T-08] flushPendingUpdates原子性假设**: flushPendingUpdates用setTimeout(0)批量更新AppState，假设React的batched rendering能正确处理大批量工具注册的re-render。如果工具数量极大（>100），可能出现渲染性能问题。
8. **[T-08] elicitationHandler安全假设**: URL elicitation允许server打开用户浏览器到任意URL，安全性依赖于server的可信度和用户的判断。未分析是否存在phishing或XSS风险。

### T-11: TUI组件与Ink渲染 (2025-07-26)

1. **React Compiler 产物**: T-11 scope 中所有 `.tsx` 文件是 React Compiler 编译产物（`_c(N)` + `$[N]`），非原始源码。分析基于编译产物，与源码结构可能有差异。
2. **Markdown LRU 缓存**: Markdown.tsx 使用 500 条目 LRU token 缓存，假设标准 LRU 淘汰策略（最久未用淘汰），但未实读缓存实现确认。
3. **Ink 引擎 fork**: ink/ 目录是 Ink 库的定制 fork，与上游 Ink 有差异（特别是 reconciler 和 diff 算法）。假设差异主要在渲染性能优化方面。
4. **Feature Flag 默认状态**: 大量组件受 `feature('KAIROS')` 门控，假设分析时 feature flags 为启用状态（可看到完整组件树）。
5. **OffscreenFreeze 阈值**: 假设虚拟滚动 freeze 阈值为视窗外 N 行（N 值未确认），冻结后组件不渲染。
6. **File Roles 部分推断**: 321 个文件中约 170 个非常规组件（utils/types/hooks/config）的 File Role 基于文件路径和 basename 推断，标注为 `OVERVIEW (enumerated only)`。
7. **Config.tsx 配置持久化**: 假设配置变更通过 AppState 的 onChange 回调持久化，但具体写盘时机未确认。
8. **AgentsMenu 状态机完整性**: 假设 7 态状态机覆盖所有合法状态，无隐藏或未声明的状态。


### T-13: 任务系统
- ASSUME-T13-01: generateTaskId 随机后缀足以防止碰撞（未见碰撞检测代码）
- ASSUME-T13-02: DreamTask consolidation lock 文件在进程崩溃后被正确清理（lock 文件机制未完整追踪）
- ASSUME-T13-03: autoBackground timeout 对 LocalAgentTask 是用户不可配置的（hardcoded 或由外部配置）
- ASSUME-T13-04: diskOutput 异步 drain loop 崩溃时 task output 不可恢复（无 fallback 机制）
- ASSUME-T13-05: 5GB 磁盘上限对当前所有使用场景足够（硬编码常量，不可配置）
- ASSUME-T13-06: InProcessTeammate 的 AsyncLocalStorage 隔离在所有执行路径下正确传播
- ASSUME-T13-07: 模块级 stall watchdog 在 shell spawn 后立即启动，不考虑首次输出延迟
- ASSUME-T13-08: framework.ts 的 TOCTOU 防御（applyTaskOffsetsAndEvictions 的 fresh re-check）在高并发场景下足够安全

## T-14: Bridge 远程模式 (ML-09, P2 STANDARD)
- ASSUME-T14-01: v1（env-based）和 v2（env-less）路径最终将统一为 v2，当前双路径是过渡态
- ASSUME-T14-02: bridgePointer 4h TTL 对典型 bridge session 时长足够（包括长时间 daemon 模式运行）
- ASSUME-T14-03: SerialBatchEventUploader 的 maxConsecutiveFailures 阈值在生产环境中不会频繁触发
- ASSUME-T14-04: trustedDevice.ts 的 memoize cache 在 login 后 clear 足以避免 stale token（无其他 invalidation 路径）
- ASSUME-T14-05: peerSessions.ts 和 webhookSanitizer.ts 的空桩实现不影响当前功能（未来预留接口）
- ASSUME-T14-06: SSETransport epoch mismatch 的直接断开策略不会导致频繁重连（server 端 epoch 稳定）
- ASSUME-T14-07: GrowthBook feature flag 切换延迟（缓存 TTL）不会导致 v1/v2 路径选择不一致
- ASSUME-T14-08: CLI handlers（agents/autoMode/mcp/plugins/util）与 bridge 核心逻辑的弱耦合是有意设计
- ASSUME-T15-01: consecutive529Count 仅在连续 529 时递增，非 529 错误会重置计数（需确认 withRetry.ts loop 逻辑）
- ASSUME-T15-02: getAnthropicClient() 每次重建客户端的性能开销可接受（SDK 内部可能有 HTTP agent 复用）
- ASSUME-T15-03: Supporting API 静默失败（return null）不会导致上游功能异常（所有调用者都处理 null）
- ASSUME-T15-04: persistent retry 6h cap 对 unattended sessions 足够（不会导致无限阻塞的任务场景）
- ASSUME-T15-05: Bedrock/Vertex Provider 返回 anthropic-ratelimit-unified-* headers（限流逻辑依赖这些 headers）
- ASSUME-T15-06: dumpPrompts.ts 缓存的 5 个 API 请求+响应有隐式大小限制（不会 OOM）
- ASSUME-T15-07: sessionIngress.ts 的 sequentialAppendBySession Map 在 session 结束时清理
- ASSUME-T15-08: errors.ts 的 getAssistantMessageFromError 对未知错误类型有兜底消息（不会返回 undefined）

### T-16 Assumptions
- ASSUME-T16-01: contextCollapse 的 3 个 stub 文件是实验特性预留，非bug（代码结构完整但实现为no-op）
- ASSUME-T16-02: KAIROS 和标准记忆系统不会同时启用（memdir.ts 的模式分发逻辑假设互斥）
- ASSUME-T16-03: sessionStorage.ts 的 compact boundary 标记在 append-only 写入中不会丢失（无 fsync 保证）
- ASSUME-T16-04: findRelevantMemories 的 sideQuery 在记忆文件数 ≤200 时延迟可接受（无性能测试数据）
- ASSUME-T16-05: teamMemPaths.ts 的 symlink 防护覆盖所有攻击向量（realpath + sanitizePathKey，未验证边界case）
- ASSUME-T16-06: GrowthBook gate 缓存过期不影响功能正确性（值可能 stale 但不会导致崩溃）
- ASSUME-T16-07: forked agent 的 CacheSafeParams 能有效命中父级 prompt cache（maxOutputTokens 差异可能导致 miss）
- ASSUME-T16-08: sessionMemoryCompact 的 adjustIndexToPreserveAPIInvariants 覆盖所有 API invariant case（防御性补丁，无测试数据）

### T-17 Plugin System (ASSUME-T17-01~08)

- ASSUME-T17-01: Zip Cache (zipCache.ts) is designed exclusively for headless/container environments; the env var gate CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE is intentional and not expected to be used interactively
- ASSUME-T17-02: installedPluginsManager.ts atomic rename pattern is sufficient for concurrent write safety within a single Claude Code process; cross-instance file locking is out of scope
- ASSUME-T17-03: marketplaceManager.ts uses sparse checkout for large marketplaces; full clone is fallback only when sparse checkout fails
- ASSUME-T17-04: Plugin dependency resolution (dependencyResolver.ts) uses apt-style semantics where dependency = presence guarantee, not module graph — this is by design
- ASSUME-T17-05: Plugin sandboxing is intentionally absent; plugin commands run with full process privileges as an architectural decision, not an oversight
- ASSUME-T17-06: The 7-day orphan TTL (cacheUtils.ts) is chosen to balance disk usage with rollback capability during plugin version transitions
- ASSUME-T17-07: V1-to-V2 migration (installedPluginsManager.ts) is one-way by design; no rollback path is provided because V1 format is considered deprecated
- ASSUME-T17-08: Memoize cache invalidation (clearAllCaches in cacheUtils.ts) is called after every mutation path; scattered calls are acceptable because the central function provides a single invalidation point

## T-18 Bash/Shell引擎

- ASSUME-T18-01: PARSE_ABORTED sentinel (bashParser.ts) is designed to always route to too-complex in ast.ts; the legacy shell-quote path is never re-attempted after abort — this is by design
- ASSUME-T18-02: The 6 pre-check regexes in ast.ts (L408-437) are intended to catch all known parser differentials between the pure-TS parser and actual bash behavior; new differentials must be manually added
- ASSUME-T18-03: ShellSnapshot TOCTOU window (bashProvider.ts) is explicitly documented and accepted; the source || true fallback is considered sufficient mitigation
- ASSUME-T18-04: The TREE_SITTER_BASH feature flag is assumed to be enabled in production; the legacy commands.ts path is maintained only as a fallback
- ASSUME-T18-05: readOnlyCommandValidation.ts static maps are assumed to be manually maintained; no automated sync with upstream tool flag changes
- ASSUME-T18-06: The 50ms parse timeout in bashParser.ts is assumed sufficient for all practical command strings; adversarial inputs are handled by the 50K node budget
- ASSUME-T18-07: PowerShell parser (Invoke-Expression + ConvertTo-Json) assumes pwsh is available on Windows; on non-Windows platforms the PowerShell path is not used
- ASSUME-T18-08: Salt placeholders in heredoc.ts use randomBytes(8) which provides sufficient uniqueness; collision probability is considered negligible
- ASSUME-T22-01: PI-02 pattern instances outside the 12 sampled files follow the same structural conventions; this is based on consistent pattern detection rules but not individually source-verified
- ASSUME-T22-02: insights.ts (3200 lines) is assumed to be intentionally monolithic rather than technical debt; it may have been designed as a self-contained analysis pipeline
- ASSUME-T22-03: The `satisfies Command` pattern is assumed to provide compile-time safety for all definition files; runtime behavior depends on TypeScript compilation correctness
- ASSUME-T22-04: Plugin/MCP commands (not in src/commands/) are assumed to implement the same Command interface but are registered through different loading paths
- ASSUME-T22-05: The `load()` lazy-loading convention is assumed to be preserved across all 107 instances; no instance eagerly imports its handler at module load time
- ASSUME-T22-06: Single-file commands (like version.ts, insights.ts) are assumed to be intentionally merged for simplicity rather than due to oversight
- ASSUME-T22-07: The `isEnabled()` and `availability` fields in command definitions are assumed to be checked by the command dispatch system (T-02) before invocation
- ASSUME-T22-08: The 95 non-sampled PI-02 instances are assumed to conform to the same conventions as the 12 verified instances based on pattern detection rule consistency

### T-30 Assumptions (PI-11: settings-module pattern audit)
- ASSUME-T30-01: The `windowMs` parameter in `internalWrites.ts:consumeInternalWrite()` is always provided by the caller (changeDetector.ts) and is assumed to be tuned appropriately for the filesystem watcher latency
- ASSUME-T30-02: `managedPath.ts` env override (`CLAUDE_CODE_MANAGED_SETTINGS_PATH`) is assumed to be Ant-internal only, gated by `USER_TYPE === 'ant'`, and eliminated from external builds
- ASSUME-T30-03: `schemaOutput.ts` relies on `zod/v4` toJSONSchema which is assumed to correctly handle all SettingsSchema field types including union types and optional fields
- ASSUME-T30-04: `validateEditTool.ts` allows edits to already-invalid settings files (escape hatch) — assumed to be intentional design to avoid blocking recovery operations
- ASSUME-T30-05: The extraction pattern (breaking circular dependencies by moving aggregation to a leaf) is assumed to be the primary motivation for all PI-11 modules, confirmed by JSDoc in 3/5 files
- ASSUME-T30-06: `internalWrites.ts` Map is assumed to grow boundedly since it only tracks actively-written settings files (typically 1-3 concurrent writes)
- ASSUME-T30-07: `allErrors.ts` merges errors from 3 scopes (user/project/local) but excludes 'dynamic' scope — assumed correct per comment that dynamic scope throws on CLI startup
- ASSUME-T30-08: `schemaOutput.ts` uses `slowOperations.jsonStringify` instead of native JSON.stringify — assumed to prevent stack overflow on deeply nested schema objects


### T-33 Assumptions (PI-14: misc-leaf pattern audit)
- ASSUME-T33-01: errorIds.ts follows an increment-by-convention pattern where new IDs are appended sequentially; the Next ID counter in JSDoc is assumed to be maintained manually by developers
- ASSUME-T33-02: keybindings/types.ts types are assumed to be consumed exclusively by other modules in src/keybindings/ and TUI components (ML-07), not by core logic
- ASSUME-T33-03: Both PI-14 files are assumed to be stable (rarely changed) given their leaf status and zero imports
- ASSUME-T33-04: The individual const exports pattern in errorIds.ts (vs a single object map) is assumed to be intentional for tree-shaking/DCE optimization
- ASSUME-T33-05: PI-14 misc-leaf catch-all category is assumed to be acceptable at current scale (2 instances); if more instances are discovered, sub-categorization may be warranted
- ASSUME-T33-06: errorIds.ts error ID numbers are assumed to never be reused or reordered once assigned, to maintain backward compatibility with error tracking systems
- ASSUME-T33-07: keybindings/types.ts ParsedKeystroke nested structure (Block then Binding then Keystroke) is assumed to match a specific keybinding configuration schema format
- ASSUME-T33-08: Neither file has side effects at module load time, assumed safe for eager import in any module


### T-41 Assumptions (Shim & Vendor Proxy Layers)
- ASSUME-T41-01: Shim modules are activated via build-time module resolution — the bundler (esbuild/bun) replaces real module paths with shim paths for the open-source build. The exact mechanism is not visible from source alone.
- ASSUME-T41-02: All .node native binaries (audio-capture.node, image-processor.node, modifiers.node, url-handler.node) are distributed alongside the npm package or built during installation. The vendor bridges assume they exist at known paths.
- ASSUME-T41-03: The execFileSync calls in ant-computer-use-swift (osascript, open) are assumed safe for the event loop because they are only invoked during Computer Use tool execution, which is user-initiated and infrequent.
- ASSUME-T41-04: The BLANK_JPEG_BASE64 constant in ant-computer-use-swift is assumed to be a valid minimal JPEG that downstream consumers (screenshot processing, VLM) can handle without errors.
- ASSUME-T41-05: Vendor modules' loadAttempted flag ensures dlopen runs only once per process lifetime — if the initial load fails (missing binary), the feature remains unavailable until process restart.
- ASSUME-T41-06: The bundleId parameter in openBundle() (ant-computer-use-swift:L91) is assumed to be validated/sanitized upstream before reaching this shim.
- ASSUME-T41-07: The three different native module loading strategies across vendor files are assumed to be an artifact of different authors/timelines rather than a deliberate design choice.
- ASSUME-T41-08: Clipboard functions in image-processor-src (readClipboardImage, hasClipboardImage) are assumed macOS-only and gated by feature flags in consuming code.

## T-31 — Pattern Audit PI-12 (utility-leaf)
- ASSUME-T31-01: All PI-12 instances are in src/utils/ — no utility-leaf files exist in other directories that were missed by the initial pattern scan.
- ASSUME-T31-02: The extraction rationale documented in JSDoc comments (7/12 files) accurately reflects the actual design intent at time of creation.
- ASSUME-T31-03: The barrel re-export pattern (nativeInstaller/index.ts) is considered a utility-leaf sub-type rather than a separate pattern category.
- ASSUME-T31-04: The 15-20 line size range for PI-12 is a stable characteristic — future additions to these files (e.g., adding exports) would not change their classification.
- ASSUME-T31-05: objectGroupBy.ts polyfill is assumed to be eventually removable when all supported Node.js versions support Object.groupBy natively.
- ASSUME-T31-06: classifierApprovalsHook.ts dependency on React is intentional for the useSyncExternalStore bridge pattern, not an accidental import.
- ASSUME-T31-07: The lazySchema wrapper in todo/types.ts is assumed necessary to prevent Zod circular reference errors during module initialization.
- ASSUME-T31-08: yaml.ts Bun.YAML detection is assumed to work correctly for all Bun runtime versions used in production.

### T-21 Assumptions (PI-01 tool-instance audit)

- ASSUME-T21-01: All 77 PI-01 instances in instance-manifest.jsonl correctly reside within src/tools/ subdirectories. Files not in src/tools/ are not PI-01.
- ASSUME-T21-02: The 10 sampled instances are representative of all 77 instances. The 0-deviation result from sampling suggests high pattern conformance, but does not guarantee it.
- ASSUME-T21-03: The 5 identified file subtypes (main tool, constants, prompt, UI, auxiliary) are the only subtypes in PI-01. No new subtypes will emerge from the remaining 57 inferred instances.
- ASSUME-T21-04: MCPTool/prompt.ts is intentionally a placeholder with runtime override by mcpClient.ts, not an incomplete implementation.
- ASSUME-T21-05: TungstenTool (disabled stub) is intentionally kept for backward compatibility with old transcripts, not abandoned code.
- ASSUME-T21-06: src/tools/utils.ts, while located in the tools root directory rather than a tool subdirectory, is correctly classified as PI-01 because it provides shared tool-support utilities.
- ASSUME-T21-07: The buildTool() interface in src/Tool.ts:L783 is the definitive tool creation API. All main tool files use this function; no alternative creation paths exist.
- ASSUME-T21-08: The constants.ts pattern (breaking circular dependencies) is deliberate architecture, not an accidental pattern that emerged from ad-hoc refactoring.

## T-36 (PI-18: computer-use-module)
- ASSUME-T36-01: Both @ant/computer-use-input and @ant/computer-use-swift are proprietary Anthropic native addons whose source is not in this repository; their internal behavior is documented only via JSDoc comments in the loader shims.
- ASSUME-T36-02: The `unwrapDefaultExport()` function exists to handle CJS/ESM interop differences between the build system and runtime module loading; the specific cause of the dual export shape is not visible in this scope.
- ASSUME-T36-03: The `COMPUTER_USE_INPUT_NODE_PATH` and `COMPUTER_USE_SWIFT_NODE_PATH` environment variables are set by `build-with-plugins.ts` during the build process and are not expected to be set manually by users.
- ASSUME-T36-04: The `drainRunLoop()` requirement for `@MainActor` methods (DispatchQueue.main under libuv) is assumed to be correctly handled by all callers in executor.ts and wrapper.tsx (T-05 scope).
- ASSUME-T36-05: The `require()` calls use synchronous loading because native addons must be available synchronously at the point of use; dynamic import() would not guarantee this.
- ASSUME-T36-06: The `isSupported` flag from @ant/computer-use-input accurately reflects runtime platform compatibility; the exact check logic is inside the native addon.
- ASSUME-T36-07: The missing `ComputerUseInputAPI` type re-export in inputLoader.ts is either intentional (callers import directly from npm) or a minor oversight with no runtime impact.
- ASSUME-T36-08: The `cached ??=` vs `if (cached) return cached` stylistic difference between the two files has no semantic or performance implications.

## T-25 Assumptions (PI-06: permission-component)

- ASSUME-T25-01: MonitorPermissionRequest.tsx and ReviewArtifactPermissionRequest.tsx are intentional null-stub scaffolding, not dead code (no comments or TODOs found)
- ASSUME-T25-02: WorkerBadge.tsx is intentionally committed as React Compiler output; the build pipeline may compile .tsx sources before committing
- ASSUME-T25-03: ideDiffConfig.ts's generic type parameter `IDEiffSupport<TInput extends ToolInput>` is designed for multi-tool extensibility but currently only used by FilePermissionDialog
- ASSUME-T25-04: utils.ts logUnaryPermissionEvent() fire-and-forget (void) pattern is acceptable — telemetry failures should not block permission flow
- ASSUME-T25-05: PI-06's heterogeneity (4 sub-types) is acceptable as a directory-based pattern grouping; no immediate need to split into sub-patterns
- ASSUME-T25-06: The two null-stubs may be re-activated in future releases as the swarm/monitor/review features mature
- ASSUME-T25-07: PermissionRuleList.tsx (1178L) was correctly upgraded to deep-trace in T-06 rather than catalogued as a PI-06 instance
- ASSUME-T25-08: No additional PI-06 instances exist outside src/components/permissions/ (pattern scope is directory-bounded)

## T-37 Assumptions (PI-20: mcp-ui-component)

- ASSUME-T37-01: The 4 unre-exported types in types.ts (ClaudeAIServerInfo, HTTPServerInfo, SSEServerInfo, StdioServerInfo) are either imported directly by external consumers or are dead code pending cleanup
- ASSUME-T37-02: types.ts Record<string, unknown> stubs are intentional UI-side decoupling from services/mcp/types.ts proper interfaces, not technical debt
- ASSUME-T37-03: reconnectHelpers.tsx inline source map is from build tooling committing compiled output; the original source is maintained separately or this is the authoritative source
- ASSUME-T37-04: The MCP UI components re-exported by index.ts (MCPSettings, MCPReconnect, etc.) are all correctly traced in T-08 (ML-05 DEEP) and do not belong in PI-20 catalog
- ASSUME-T37-05: PI-20 scope is limited to ancillary support files in src/components/mcp/; no additional PI-20 instances exist outside this directory
- ASSUME-T37-06: The barrel file pattern (index.ts re-exporting all components) is the standard convention for UI component directories in this codebase
- ASSUME-T37-07: reconnectHelpers.tsx being stateless and side-effect-free is intentional design for testability
- ASSUME-T37-08: No additional PI-20 instances exist in subdirectories of src/components/mcp/ beyond the 3 catalogued files

### T-40 Assumptions (PI-05 service-module Pattern Audit)

- ASSUME-T40-01: All 13 PI-05 catalog instances have been fully verified against source code; no sampling was needed as total count was small enough for exhaustive review
- ASSUME-T40-02: The skillSearch/ subsystem (6 files, 14 lines) is assumed to be a feature-flagged placeholder; the stub implementations are intentional, not accidental omissions
- ASSUME-T40-03: lsp/types.ts and tips/types.ts placeholder types (Record<string, unknown>) are assumed to be temporary; real type definitions will be added when those services are implemented
- ASSUME-T40-04: sinkKillswitch.ts uses a GrowthBook feature flag with mangled name (tengu_frond_boric); the mangling is assumed intentional for A/B testing isolation
- ASSUME-T40-05: autoDream/config.ts was extracted from a larger module to avoid importing heavy dependencies (forked agent, task registry); the JSDoc rationale is taken at face value
- ASSUME-T40-06: claudeAiLimitsHook.ts is classified as PI-05 despite being a React hook rather than a traditional service module; the pattern contract is broad enough to include UI adapters
- ASSUME-T40-07: tipHistory.ts is the only PI-05 instance with mutable state (reads/writes global config tipsHistory field); the state mutation is assumed safe in the single-threaded Node.js REPL context
- ASSUME-T40-08: PI-05 has no owner_ml in the pattern catalog; it was assigned to ML-05 administratively for T-40, not because all instances architecturally belong to MCP integration

### T-39 Assumptions (PI-24 telemetry-module Pattern Audit)

- ASSUME-T39-01: Both PI-24 catalog instances have been fully verified against source code; exhaustive review was feasible given the small count (2 files)
- ASSUME-T39-02: logger.ts implements the OpenTelemetry DiagLogger interface correctly; the 5-level severity filter (error/warn active, info/debug/verbose no-ops) is assumed intentional to prevent OTEL SDK noise
- ASSUME-T39-03: skillLoadedEvent.ts uses PII-aware analytics types (AnalyticsMetadata_I_VERIFIED_THIS_IS_PII_TAGGED) correctly; the PII tagging is assumed to be a compliance requirement verified by the development team
- ASSUME-T39-04: skillLoadedEvent.ts has no error handling for getSkillToolCommands() failure; this is assumed to be an intentional design choice (fire-and-forget), though it could lead to unhandled promise rejections
- ASSUME-T39-05: PI-24 is assigned to ML-06 administratively based on the telemetry initialization chain in init.ts (T-09 scope), not because these files are architecturally part of the authentication/session subsystem
- ASSUME-T39-06: The pattern category "telemetry-module" is broad enough to encompass both OTEL adapter and analytics event emitter sub-types; no split is planned
- ASSUME-T39-07: Both files are stateless utilities with no mutable module-level state; this is assumed stable and not expected to change
- ASSUME-T39-08: The broader telemetry infrastructure (OTEL setup, span creation, exporters) in src/services/telemetry/ is correctly covered by T-09 and not part of PI-24's scope

### T-23 Assumptions (PI-03 react-hook Pattern Audit)

- ASSUME-T23-01: All 14 PI-03 catalog instances have been fully verified against source code; exhaustive review was feasible given the manageable count (14 files, all ≤49 lines)
- ASSUME-T23-02: The use* naming convention is the canonical pattern for React hooks in this codebase; files named use*.ts(x) in src/hooks/ are correctly classified as PI-03 instances
- ASSUME-T23-03: The 38 non-catalog files in src/hooks/ (lines > 50) were correctly excluded from PI-03 and covered by T-10/T-11/T-12 as standard/DEEP trace mode
- ASSUME-T23-04: The 2 files with embedded base64 source maps (useChromeExtensionNotification.tsx, useOfficialMarketplaceNotification.tsx) are assumed to be build artifacts committed accidentally, not intentional design
- ASSUME-T23-05: The useStartupNotification shared registration pattern among 3 hooks (ChromeExtension, OfficialMarketplace, UpdateNotification) is assumed to be a stable convention, not deprecated
- ASSUME-T23-06: useSettingsChange's dependency on getSettings_DEPRECATED() is assumed to be intentional bridge code for backward compatibility, not an oversight
- ASSUME-T23-07: useVoiceEnabled's triple-gate pattern (user intent + auth + kill-switch) is assumed to be the correct authorization model for voice features
- ASSUME-T23-08: The PI-03 pattern definition (React hooks in src/hooks/ matching use*.ts(x)) correctly captures all simple utility hooks; complex stateful hooks with >50 lines are properly classified as standard traces

### T-26 Assumptions (Pattern Audit — ink-fork-component PI-07)

- **ASSUME-T26-01**: The 4 React Compiler output files (Link.tsx, Newline.tsx, Spacer.tsx, TerminalSizeContext.tsx) were intentionally compiled and committed; the build process is assumed correct.
- **ASSUME-T26-02**: cursor.ts no-op stubs (returning empty string) are intentional — Claude Code does not need cursor hiding since the terminal manages cursor visibility.
- **ASSUME-T26-03**: PasteEvent and ResizeEvent 1-line stubs are intentional placeholders for future event types; they are not dead code to be removed.
- **ASSUME-T26-04**: The `src/ink/` directory is a complete fork of the npm `ink` package with local modifications; the original upstream is not analyzed here.
- **ASSUME-T26-05**: instances.ts `Map<WriteStream, Ink>` is the only mutable shared state across the 33 files; no other cross-instance state mutation exists.
- **ASSUME-T26-06**: line-width-cache.ts 4096-entry limit is sufficient for typical terminal widths (≤4096 columns covers all practical cases).
- **ASSUME-T26-07**: wrapAnsi.ts Bun-native fast path is correct when Bun runtime is detected; the npm wrap-ansi fallback is correct for Node.js.
- **ASSUME-T26-08**: All 33 files belong to a single pattern (PI-07) and no instances were missed or miscategorized during the mapping phase.


### T-27 Assumptions (Pattern Audit — message-component PI-08)

- **ASSUME-T27-01**: The 12 catalog instances in `src/components/messages/` represent the complete set of message-component files; no additional message components exist outside this directory.
- **ASSUME-T27-02**: The 4 null-rendering stubs (SnipBoundaryMessage, UserCrossSessionMessage, UserForkBoilerplateMessage, UserGitHubWebhookMessage) are intentional dead-code-elimination placeholders, not bugs.
- **ASSUME-T27-03**: teamMemSaved.ts is correctly categorized under PI-08 despite not being a React component — it provides a pure function consumed by message rendering.
- **ASSUME-T27-04**: The UserToolResultMessage/ subdirectory files (RejectedPlanMessage, RejectedToolUseMessage, UserToolCanceledMessage, utils) are all part of the same message-component pattern despite the nested directory structure.
- **ASSUME-T27-05**: The useGetToolFromMessages hook in utils.tsx is a legitimate PI-08 instance (shared utility for multiple message components) rather than a separate pattern.
- **ASSUME-T27-06**: All PI-08 files are rendered exclusively through the Message.tsx dispatcher (analyzed in T-11) and no other entry point exists.
- **ASSUME-T27-07**: The React Compiler output in some PI-08 files (memoization slots, source maps) is generated by the build process and not hand-written.
- **ASSUME-T27-08**: CompactBoundaryMessage dynamic keybinding lookup via useSnapshot(config) is the standard way to display user-configurable shortcuts in message components.


### T-28 Assumptions (Pattern Audit — agent-component PI-09)

- **ASSUME-T28-01**: The 4 catalog instances in src/components/agents/ represent the complete set of agent-component files; the main AgentList/AgentDetail components are part of T-11 scope (PI-08 message-component or direct T-11 analysis).
- **ASSUME-T28-02**: new-agent-creation/types.ts with its single-line type alias is a legitimate PI-09 instance serving as a type stub for the agent creation wizard.
- **ASSUME-T28-03**: types.ts exporting AGENT_PATHS and ModeState is correctly categorized as agent-component utility despite not being a React component.
- **ASSUME-T28-04**: utils.ts getAgentSourceDisplayName() pure function is the only utility in the agents directory and is correctly cataloged under PI-09.
- **ASSUME-T28-05**: AgentNavigationFooter.tsx containing React Compiler output (memoization slots _c) is auto-generated build output, not hand-written optimization.
- **ASSUME-T28-06**: All PI-09 files are consumed exclusively by the agents UI subsystem rendered in REPL.tsx, with no server-side or non-UI consumers.
- **ASSUME-T28-07**: The agents/ directory has no sub-directories beyond new-agent-creation/ that might contain uncataloged agent components.
- **ASSUME-T28-08**: The pattern contract (directory-based, utility + type + component mix) is stable and no new agent components are expected to deviate from the observed conventions.

## T-32 Assumptions (PI-13 component-leaf audit)

- ASSUME-T32-01: All 10 PI-13 catalog instances are correctly cataloged — verified by full source read of each file
- ASSUME-T32-02: MonitorMcpDetailDialog and WorkflowDetailDialog null stubs are intentional placeholders for future implementation — no TODO/JSDoc found to confirm intent
- ASSUME-T32-03: useFrustrationDetection always-false hook is a planned feature stub — no implementation timeline known
- ASSUME-T32-04: IssueFlagBanner ANT-only feature gate (`external !== 'ant'`) is intentional compile-time DCE — external builds get `return null`
- ASSUME-T32-05: FeedbackSurveyResponse loose typing (`'good'|'bad'|'neutral'|'dismissed'|string`) is intentional for forward compatibility — not a bug
- ASSUME-T32-06: Spinner/index.ts DCE comment about teammate components is intentional tree-shaking strategy
- ASSUME-T32-07: FallbackToolUseRejectedMessage.tsx React Compiler output ($ = _c(1)) is correct compiled form — source map verified
- ASSUME-T32-08: PI-13 pattern name "component-leaf" is a legacy designation — 8/10 instances are not React components

## T-34 Assumptions (PI-15 design-system-component audit)

- ASSUME-T34-01: PI-15 catalog is complete — only color.ts qualifies as a design-system-component leaf; all other design-system/ files are React components traced in T-10/T-11
- ASSUME-T34-02: color.ts dual-path resolution (raw CSS values vs theme keys) is the intended behavior — not a fallback
- ASSUME-T34-03: The type assertion `c as keyof Theme` on L28 is safe because the runtime branch checks falsy/raw prefixes first, narrowing remaining values to valid theme keys
- ASSUME-T34-04: getTheme(theme)[c] returning undefined would be handled by ink's colorize() function — no explicit guard needed in color.ts
- ASSUME-T34-05: The `type: ColorType = 'foreground'` default is intentional — most callers want foreground coloring
- ASSUME-T34-06: PI-15 singleton status (1 instance) is a cataloging artifact, not a design choice — pattern could be merged into PI-12 or PI-05
- ASSUME-T34-07: color.ts is consumed exclusively by design-system/ components (ThemedText, etc.) — no external consumers outside the design system
- ASSUME-T34-08: The curried API `(c, type?) => (text: string) => string` is intentional for composability with Ink's styling system

## T-35 Assumptions (PI-16 notification-hook audit)

- ASSUME-T35-01: PI-16 catalog is complete — all notification hooks in src/hooks/notifs/ are cataloged; no notification hooks exist outside this directory
- ASSUME-T35-02: useStartupNotification was intentionally created as a consolidation hook — its JSDoc mentions "10+ notifs/ hooks" that previously hand-rolled the pattern
- ASSUME-T35-03: useDeprecationWarningNotification's direct useNotifications() approach is a legacy pattern that hasn't been migrated yet, not a deliberate design choice
- ASSUME-T35-04: useAntOrgWarningNotification's empty stub is a placeholder for future implementation, not dead code to be removed
- ASSUME-T35-05: The notification object shape {key, text, color, priority, timeoutMs?} is the canonical interface across all notification hooks
- ASSUME-T35-06: Remote-mode gating via getIsRemoteMode() is the correct mechanism to suppress notifications in bridge/remote sessions
- ASSUME-T35-07: React Compiler output ($ = _c(N) memoization slots) in 3 .tsx files is expected build artifact, not hand-written code
- ASSUME-T35-08: The "10+ notifs/ hooks" referenced in useStartupNotification's JSDoc refers to hooks that may have been removed or consolidated before this analysis

## T-24 Assumptions (PI-04 task-implementation audit)

- ASSUME-T24-01: PI-04 has 0 catalog instances in instance-manifest.jsonl by design - all 10 task files were deep-traced during ML-08 trace-mainline and did not get individual manifest entries
- ASSUME-T24-02: The Task interface contract { name, type, kill() } defined in src/Task.ts is the authoritative interface - no task implementation extends or modifies it
- ASSUME-T24-03: LocalWorkflowTask and MonitorMcpTask null stubs are feature-gated placeholders controlled by GrowthBook flags, not dead code to be removed
- ASSUME-T24-04: The directory convention `src/tasks/<Name>/<Name>.tsx|.ts` is enforced by convention only - no build-time or runtime validation
- ASSUME-T24-05: RemoteAgentTask 5 sub-types (remote-agent, ultraplan, ultrareview, autofix-pr, background-pr) share the same completionChecker registry pattern intentionally
- ASSUME-T24-06: The guards.ts and killShellTasks.ts extractions from LocalShellTask.tsx are deliberate architectural decisions to avoid React/ink dependency pollution in non-React consumers
- ASSUME-T24-07: DreamTask different registerDreamTask() pattern is specific to the dream mode consolidation lock rollback mechanism, not a design oversight
- ASSUME-T24-08: The BQ round 9 memory optimization reference in InProcessTeammateTask/types.ts refers to an internal production optimization context not documented in the codebase

## T-38 Assumptions (PI-23 cli-transport audit)

- ASSUME-T38-01: PI-23 is a catch-all pattern grouping heterogeneous CLI infrastructure leaf modules that serve unrelated concerns (transport, exit, serialization)
- ASSUME-T38-02: Transport.ts with all-optional methods is intentionally permissive to allow partial implementations rather than being an incomplete design
- ASSUME-T38-03: The env-gated 3-tier transport selection in transportUtils.ts covers all production transport modes (SSE/Hybrid/WS)
- ASSUME-T38-04: exit.ts cliError/cliOk consolidation of ~60 copy-pasted blocks is complete and no legacy exit blocks remain
- ASSUME-T38-05: ndjsonSafeStringify.ts U+2028/U+2029 escape is sufficient for NDJSON safety (gh-28405 is the only known edge case)
- ASSUME-T38-06: Zero cross-instance imports is intentional architectural isolation, not accidental lack of code sharing
- ASSUME-T38-07: HybridTransport, SSETransport, WebSocketTransport implementations (in T-14 scope) are NOT PI-23 instances because they are complex implementations rather than leaf modules
- ASSUME-T38-08: The pattern name "cli-transport" is misleading since exit.ts and ndjsonSafeStringify.ts are not transport-related; a better name would be "cli-infrastructure-leaf"

## T-29 Assumptions (PI-10 bundled-skill audit)

- ASSUME-T29-01: The 3 empty stubs (dream.ts, hunter.ts, runSkillGenerator.ts) are intentionally reserved entry points for future bundled skills, not abandoned code
- ASSUME-T29-02: registerBundledSkill() from bundledSkills.ts is the sole registration mechanism for bundled skills; no alternative registration paths exist
- ASSUME-T29-03: The USER_TYPE gate in verify.ts (ant-only) is a deliberate access control decision, not a temporary restriction
- ASSUME-T29-04: mcpSkillBuilders.ts was classified as PI-10 due to its location in src/skills/ and skill-related purpose, despite not following the bundled-skill registration pattern
- ASSUME-T29-05: The Bun text loader import pattern in verifyContent.ts is specific to the Bun runtime and will not work with other JS runtimes
- ASSUME-T29-06: The allowedTools MCP tool allowlist in claudeInChrome.ts is the complete list of permitted MCP tools for that skill
- ASSUME-T29-07: Zero cross-instance imports between PI-10 files is an intentional architectural decision for skill isolation
- ASSUME-T29-08: The isEnabled() callback in claudeInChrome.ts is evaluated at skill registration time, not at prompt generation time

## T-19 Assumptions (Swarm Orchestration)

- ASSUME-T19-01: The three-backend architecture (tmux/iTerm2/in-process) represents the complete set of execution backends; no additional backends are planned
- ASSUME-T19-02: File-based mailbox communication is sufficient for all teammate coordination; no real-time IPC (sockets/pipes) is needed beyond the mailbox system
- ASSUME-T19-03: The teammateModeSnapshot freeze-at-startup pattern is intentional to prevent mid-session backend switching inconsistencies
- ASSUME-T19-04: Fire-and-forget agent execution is acceptable; the leader does not need to await teammate task completion synchronously
- ASSUME-T19-05: AsyncLocalStorage provides sufficient context isolation for in-process teammates; no memory leak concerns from long-running teammates
- ASSUME-T19-06: The detection.ts module-level caching of tmux/iTerm2 availability is acceptable because terminal environment changes during a session are not expected
- ASSUME-T19-07: Team file JSON persistence without atomic writes is acceptable because concurrent writes to the same team file are not expected
- ASSUME-T19-08: The pane creation lock (module-level singleton) serializing all pane creation is acceptable for the expected number of concurrent teammate spawns

### T-20: SDK入口点 (ASSUME-T20)

- ASSUME-T20-01: coreSchemas.ts 中的 ~80 个 Zod schema 是唯一的数据类型真相来源，Python SDK 从生成的 .generated.ts 文件读取
- ASSUME-T20-02: lazySchema() 延迟构建机制的性能收益假设了大多数 schema 不会在每次运行时都被访问
- ASSUME-T20-03: runtimeTypes.ts 中的 17 个 Record<string,unknown> 占位是有意为之，为了保持与 CLI 内部的松耦合
- ASSUME-T20-04: HOOK_EVENTS 和 EXIT_REASONS const 数组与 coreSchemas.ts 中的 Zod enum 必须手动保持同步，无自动化漂移检测
- ASSUME-T20-05: settingsTypes.generated.ts 和 toolTypes.ts 为空占位符，类型生成管线尚未覆盖这些领域
- ASSUME-T20-06: controlTypes.ts 的手动类型定义与 controlSchemas.ts 的 Zod schema 存在结构对应关系，但无自动同步机制
- ASSUME-T20-07: SDK 消费者（Python SDK 用户）仅通过 coreTypes.ts 的公共 API 访问类型，不直接依赖 Zod schema 层
- ASSUME-T20-08: scripts/generate-sdk-types.ts 是唯一从 coreSchemas.ts 生成类型的工具，无其他构建时消费者
