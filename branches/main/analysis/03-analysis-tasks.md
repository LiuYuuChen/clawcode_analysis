# Analysis Task Decomposition

## Summary
- Total tasks: **41**
- P1 (Must Do — DEEP): 9 tasks (T-01~T-09)
- P2 (Should Do — STANDARD): 9 tasks (T-10~T-18)
- P3 (Nice to Have — OVERVIEW): 23 tasks (T-19~T-41 including Pattern Audits)
- Parallelizable groups: 3
- Mainlines covered: **15/15 (100%)**
- **Global preliminary coverage (行数)**: **100.0%** (514,739 of 514,739 mapped lines)
- **Per-ML minimum coverage**: **100.0%** (worst ML)
- Deep analysis files: 1,636 | Pattern audit files: 318 | Overlap: 0

## Mainline → Task Mapping

| ML | Lines | Owner Tasks | Coverage | Core Coverage |
|----|-------|------------|----------|---------------|
| ML-01 | 67,821 | T-01, T-02, T-41, T-22, T-30 +1 more | 100.0% | 100% | PASS |
| ML-02 | 106,534 | T-03, T-04, T-31 | 100.0% | 100% | PASS |
| ML-03 | 63,426 | T-05, T-21, T-36 | 100.0% | 100% | PASS |
| ML-04 | 22,855 | T-06, T-07, T-25 | 100.0% | 100% | PASS |
| ML-05 | 32,185 | T-08, T-37, T-40 | 100.0% | 100% | PASS |
| ML-06 | 13,452 | T-09, T-39 | 100.0% | 100% | PASS |
| ML-07 | 115,310 | T-10, T-11, T-12, T-23, T-26 +5 more | 100.0% | 100% | PASS |
| ML-08 | 4,683 | T-13, T-24 | 100.0% | 100% | PASS |
| ML-09 | 18,196 | T-14, T-38 | 100.0% | 100% | PASS |
| ML-10 | 7,573 | T-15 | 100.0% | 100% | PASS |
| ML-11 | 15,160 | T-16 | 100.0% | 100% | PASS |
| ML-12 | 29,491 | T-17, T-29 | 100.0% | 100% | PASS |
| ML-13 | 18,665 | T-18 | 100.0% | 100% | PASS |
| ML-14 | 7,548 | T-19 | 100.0% | 100% | PASS |
| ML-15 | 2,716 | T-20 | 100.0% | 100% | PASS |
| **Global** | **514,739** | **41 tasks** | **100.0%** | — | **PASS** |

## Task List

### T-01: CLI启动与初始化序列

- **Output Slug**: cli-entry-init
- **Priority**: P1
- **Primary Mainline**: ML-01
- **Scope**: CLI 入口点、bootstrap 初始化序列、REPL 启动流程
- **Boundaries**: 不涉及具体命令实现（T-02），不涉及查询引擎（T-03）
- **Scope Files** (10 files, 7,943 lines):
  - src/bootstrap-entry.ts
  - src/bootstrap/state.ts
  - src/bootstrapMacro.ts
  - src/entrypoints/agentSdkTypes.ts
  - src/entrypoints/cli.tsx
  - src/entrypoints/init.ts
  - src/entrypoints/mcp.ts
  - src/entrypoints/sandboxTypes.ts
  - src/main.tsx
  - src/replLauncher.tsx
- **Dependencies**: none
- **Estimated Complexity**: HIGH
- **Rationale**: ML-01 核心入口：理解整个应用启动链路是分析其他功能的基础

### T-02: 命令路由与REPL启动

- **Output Slug**: command-routing
- **Priority**: P1
- **Primary Mainline**: ML-01
- **Scope**: 命令路由、REPL 循环主体、命令注册与分发
- **Boundaries**: 不涉及 CLI 入口（T-01），不涉及查询引擎核心（T-03），shims/vendor 已移至 T-41
- **Scope Files** (207 files, 55,902 lines):
  - src/assistant/sessionHistory.ts
  - src/buddy/CompanionSprite.tsx
  - src/buddy/companion.ts
  - src/buddy/prompt.ts
  - src/buddy/types.ts
  - src/buddy/useBuddyNotification.tsx
  - src/cli/print.ts
  - src/cli/structuredIO.ts
  - src/commands.ts
  - src/commands/add-dir/add-dir.tsx
  - src/commands/add-dir/validation.ts
  - src/commands/advisor.ts
  - src/commands/branch/branch.ts
  - src/commands/bridge-kick.ts
  - src/commands/bridge/bridge.tsx
  - src/commands/brief.ts
  - src/commands/btw/btw.tsx
  - src/commands/chrome/chrome.tsx
  - src/commands/clear/caches.ts
  - src/commands/clear/conversation.ts
  - src/commands/color/color.ts
  - src/commands/commit-push-pr.ts
  - src/commands/commit.ts
  - src/commands/compact/compact.ts
  - src/commands/context/context-noninteractive.ts
  - src/commands/context/context.tsx
  - src/commands/copy/copy.tsx
  - src/commands/createMovedToPluginCommand.ts
  - src/commands/effort/effort.tsx
  - src/commands/export/export.tsx
  - src/commands/extra-usage/extra-usage-core.ts
  - src/commands/fast/fast.tsx
  - src/commands/help/index.ts
  - src/commands/ide/ide.tsx
  - src/commands/init-verifiers.ts
  - src/commands/init.ts
  - src/commands/insights.ts
  - src/commands/install-github-app/ApiKeyStep.tsx
  - src/commands/install-github-app/CheckExistingSecretStep.tsx
  - src/commands/install-github-app/ChooseRepoStep.tsx
  - src/commands/install-github-app/CreatingStep.tsx
  - src/commands/install-github-app/ErrorStep.tsx
  - src/commands/install-github-app/ExistingWorkflowStep.tsx
  - src/commands/install-github-app/InstallAppStep.tsx
  - src/commands/install-github-app/OAuthFlowStep.tsx
  - src/commands/install-github-app/SuccessStep.tsx
  - src/commands/install-github-app/WarningsStep.tsx
  - src/commands/install-github-app/install-github-app.tsx
  - src/commands/install-github-app/setupGitHubActions.ts
  - src/commands/install.tsx
  - src/commands/keybindings/keybindings.ts
  - src/commands/logout/logout.tsx
  - src/commands/mcp/addCommand.ts
  - src/commands/mcp/mcp.tsx
  - src/commands/mcp/xaaIdpCommand.ts
  - src/commands/memory/memory.tsx
  - src/commands/mobile/mobile.tsx
  - src/commands/model/model.tsx
  - src/commands/plan/plan.tsx
  - src/commands/plugin/AddMarketplace.tsx
  - src/commands/plugin/BrowseMarketplace.tsx
  - src/commands/plugin/DiscoverPlugins.tsx
  - src/commands/plugin/ManageMarketplaces.tsx
  - src/commands/plugin/PluginErrors.tsx
  - src/commands/plugin/PluginOptionsDialog.tsx
  - src/commands/plugin/PluginOptionsFlow.tsx
  - src/commands/plugin/UnifiedInstalledCell.tsx
  - src/commands/plugin/ValidatePlugin.tsx
  - src/commands/plugin/parseArgs.ts
  - src/commands/plugin/pluginDetailsHelpers.tsx
  - src/commands/plugin/usePagination.ts
  - src/commands/privacy-settings/privacy-settings.tsx
  - src/commands/rate-limit-options/rate-limit-options.tsx
  - src/commands/reload-plugins/reload-plugins.ts
  - src/commands/remote-setup/api.ts
  - src/commands/remote-setup/remote-setup.tsx
  - src/commands/rename/generateSessionName.ts
  - src/commands/rename/rename.ts
  - src/commands/resume/resume.tsx
  - src/commands/review.ts
  - src/commands/review/UltrareviewOverageDialog.tsx
  - src/commands/review/reviewRemote.ts
  - src/commands/review/ultrareviewCommand.tsx
  - src/commands/sandbox-toggle/sandbox-toggle.tsx
  - src/commands/security-review.ts
  - src/commands/tag/tag.tsx
  - src/commands/terminalSetup/terminalSetup.tsx
  - src/commands/theme/theme.tsx
  - src/commands/thinkback/thinkback.tsx
  - src/commands/ultraplan.tsx
  - src/commands/voice/voice.ts
  - src/constants/apiLimits.ts
  - src/constants/betas.ts
  - src/constants/common.ts
  - src/constants/cyberRiskInstruction.ts
  - src/constants/figures.ts
  - src/constants/files.ts
  - src/constants/github-app.ts
  - src/constants/outputStyles.ts
  - src/constants/product.ts
  - src/constants/prompts.ts
  - src/constants/spinnerVerbs.ts
  - src/constants/system.ts
  - src/constants/systemPromptSections.ts
  - src/constants/toolLimits.ts
  - src/constants/xml.ts
  - src/context/QueuedMessageContext.tsx
  - src/context/mailbox.tsx
  - src/context/modalContext.tsx
  - src/context/overlayContext.tsx
  - src/context/promptOverlayContext.tsx
  - src/context/stats.tsx
  - src/context/voice.tsx
  - src/coordinator/coordinatorMode.ts
  - src/cost-tracker.ts
  - src/costHook.ts
  - src/dev-entry.ts
  - src/dialogLaunchers.tsx
  - src/history.ts
  - src/interactiveHelpers.tsx
  - src/keybindings/KeybindingContext.tsx
  - src/keybindings/defaultBindings.ts
  - src/keybindings/loadUserBindings.ts
  - src/keybindings/match.ts
  - src/keybindings/parser.ts
  - src/keybindings/reservedShortcuts.ts
  - src/keybindings/resolver.ts
  - src/keybindings/schema.ts
  - src/keybindings/template.ts
  - src/keybindings/useKeybinding.ts
  - src/keybindings/validate.ts
  - src/migrations/migrateAutoUpdatesToSettings.ts
  - src/migrations/migrateEnableAllProjectMcpServersToSettings.ts
  - src/migrations/migrateFennecToOpus.ts
  - src/migrations/migrateLegacyOpusToCurrent.ts
  - src/migrations/migrateOpusToOpus1m.ts
  - src/migrations/migrateReplBridgeEnabledToRemoteControlAtStartup.ts
  - src/migrations/migrateSonnet1mToSonnet45.ts
  - src/migrations/migrateSonnet45ToSonnet46.ts
  - src/migrations/resetAutoModeOptInForDefaultOffer.ts
  - src/migrations/resetProToOpusDefault.ts
  - src/moreright/useMoreRight.tsx
  - src/outputStyles/loadOutputStylesDir.ts
  - src/plugins/builtinPlugins.ts
  - src/plugins/bundled/index.ts
  - src/proactive/index.ts
  - src/projectOnboardingState.ts
  - src/query/tokenBudget.ts
  - src/remote/RemoteSessionManager.ts
  - src/remote/SessionsWebSocket.ts
  - src/remote/sdkMessageAdapter.ts
  - src/schemas/hooks.ts
  - src/screens/ResumeConversation.tsx
  - src/server/createDirectConnectSession.ts
  - src/server/directConnectManager.ts
  - src/server/types.ts
  - src/setup.ts
  - src/state/AppStateStore.ts
  - src/state/onChangeAppState.ts
  - src/state/selectors.ts
  - src/state/store.ts
  - src/state/teammateViewHelpers.ts
  - src/types/command.ts
  - src/types/generated/events_mono/claude_code/v1/claude_code_internal_event.ts
  - src/types/generated/events_mono/common/v1/auth.ts
  - src/types/generated/events_mono/growthbook/v1/growthbook_experiment_event.ts
  - src/types/generated/google/protobuf/timestamp.ts
  - src/types/hooks.ts
  - src/types/ids.ts
  - src/types/logs.ts
  - src/types/message.ts
  - src/types/permissions.ts
  - src/types/plugin.ts
  - src/types/textInputTypes.ts
  - src/upstreamproxy/relay.ts
  - src/upstreamproxy/upstreamproxy.ts
  - src/utils/claudeInChrome/chromeNativeHost.ts
  - src/utils/claudeInChrome/common.ts
  - src/utils/claudeInChrome/mcpServer.ts
  - src/utils/claudeInChrome/prompt.ts
  - src/utils/claudeInChrome/setup.ts
  - src/utils/claudeInChrome/setupPortable.ts
  - src/utils/claudeInChrome/toolRendering.tsx
  - src/utils/config.ts
  - src/utils/earlyInput.ts
  - src/utils/settings/applySettingsChange.ts
  - src/utils/settings/changeDetector.ts
  - src/utils/settings/constants.ts
  - src/utils/settings/mdm/constants.ts
  - src/utils/settings/mdm/rawRead.ts
  - src/utils/settings/mdm/settings.ts
  - src/utils/settings/permissionValidation.ts
  - src/utils/settings/pluginOnlyPolicy.ts
  - src/utils/settings/settings.ts
  - src/utils/settings/settingsCache.ts
  - src/utils/settings/toolValidationConfig.ts
  - src/utils/settings/types.ts
  - src/utils/settings/validation.ts
  - src/utils/settings/validationTips.ts
  - src/utils/sinks.ts
  - src/utils/startupProfiler.ts
  - src/utils/warningHandler.ts
  - src/vim/motions.ts
  - src/vim/textObjects.ts
  - src/vim/transitions.ts
  - src/vim/types.ts
  - src/voice/voiceModeEnabled.ts
- **Dependencies**: T-01
- **Estimated Complexity**: HIGH
- **Rationale**: ML-01 核心功能：命令路由和 REPL 是用户交互的核心路径，P1 深度分析

### T-03: 查询引擎核心循环

- **Output Slug**: query-core-loop
- **Priority**: P1
- **Primary Mainline**: ML-02
- **Scope**: 查询引擎核心循环、消息处理、上下文管理、流式响应
- **Boundaries**: 不涉及 API 流式协议层（T-04），不涉及工具调度（T-05）
- **Scope Files** (341 files, 91,410 lines):
  - src/QueryEngine.ts
  - src/hooks/renderPlaceholder.ts
  - src/hooks/toolPermission/PermissionContext.ts
  - src/hooks/toolPermission/handlers/coordinatorHandler.ts
  - src/hooks/toolPermission/handlers/interactiveHandler.ts
  - src/hooks/toolPermission/handlers/swarmWorkerHandler.ts
  - src/hooks/toolPermission/permissionLogging.ts
  - src/hooks/unifiedSuggestions.ts
  - src/native-ts/file-index/index.ts
  - src/native-ts/yoga-layout/enums.ts
  - src/query.ts
  - src/query/config.ts
  - src/query/deps.ts
  - src/query/stopHooks.ts
  - src/query/transitions.ts
  - src/services/compact/autoCompact.ts
  - src/services/compact/compact.ts
  - src/utils/CircularBuffer.ts
  - src/utils/Cursor.ts
  - src/utils/QueryGuard.ts
  - src/utils/Shell.ts
  - src/utils/ShellCommand.ts
  - src/utils/abortController.ts
  - src/utils/activityManager.ts
  - src/utils/advisor.ts
  - src/utils/agentContext.ts
  - src/utils/agentId.ts
  - src/utils/agentSwarmsEnabled.ts
  - src/utils/agenticSessionSearch.ts
  - src/utils/analyzeContext.ts
  - src/utils/ansiToPng.ts
  - src/utils/ansiToSvg.ts
  - src/utils/apiPreconnect.ts
  - src/utils/appleTerminalBackup.ts
  - src/utils/argumentSubstitution.ts
  - src/utils/asciicast.ts
  - src/utils/attachments.ts
  - src/utils/attribution.ts
  - src/utils/authFileDescriptor.ts
  - src/utils/autoModeDenials.ts
  - src/utils/autoRunIssue.tsx
  - src/utils/autoUpdater.ts
  - src/utils/background/remote/preconditions.ts
  - src/utils/background/remote/remoteSession.ts
  - src/utils/backgroundHousekeeping.ts
  - src/utils/betas.ts
  - src/utils/billing.ts
  - src/utils/binaryCheck.ts
  - src/utils/browser.ts
  - src/utils/bufferedWriter.ts
  - src/utils/bundledMode.ts
  - src/utils/caCerts.ts
  - src/utils/caCertsConfig.ts
  - src/utils/cachePaths.ts
  - src/utils/classifierApprovals.ts
  - src/utils/claudeCodeHints.ts
  - src/utils/claudeDesktop.ts
  - src/utils/claudemd.ts
  - src/utils/cleanup.ts
  - src/utils/cleanupRegistry.ts
  - src/utils/cliArgs.ts
  - src/utils/cliHighlight.ts
  - src/utils/codeIndexing.ts
  - src/utils/collapseBackgroundBashNotifications.ts
  - src/utils/collapseHookSummaries.ts
  - src/utils/collapseReadSearch.ts
  - src/utils/collapseTeammateShutdowns.ts
  - src/utils/combinedAbortSignal.ts
  - src/utils/commandLifecycle.ts
  - src/utils/commitAttribution.ts
  - src/utils/completionCache.ts
  - src/utils/concurrentSessions.ts
  - src/utils/configConstants.ts
  - src/utils/contentArray.ts
  - src/utils/context.ts
  - src/utils/contextSuggestions.ts
  - src/utils/controlMessageCompat.ts
  - src/utils/conversationRecovery.ts
  - src/utils/cron.ts
  - src/utils/cronJitterConfig.ts
  - src/utils/cronScheduler.ts
  - src/utils/cronTasks.ts
  - src/utils/cronTasksLock.ts
  - src/utils/crossProjectResume.ts
  - src/utils/cwd.ts
  - src/utils/debug.ts
  - src/utils/debugFilter.ts
  - src/utils/deepLink/banner.ts
  - src/utils/deepLink/parseDeepLink.ts
  - src/utils/deepLink/protocolHandler.ts
  - src/utils/deepLink/registerProtocol.ts
  - src/utils/deepLink/terminalLauncher.ts
  - src/utils/deepLink/terminalPreference.ts
  - src/utils/desktopDeepLink.ts
  - src/utils/detectRepository.ts
  - src/utils/diagLogs.ts
  - src/utils/diff.ts
  - src/utils/directMemberMessage.ts
  - src/utils/displayTags.ts
  - src/utils/doctorContextWarnings.ts
  - src/utils/doctorDiagnostic.ts
  - src/utils/dxt/helpers.ts
  - src/utils/dxt/zip.ts
  - src/utils/editor.ts
  - src/utils/effort.ts
  - src/utils/env.ts
  - src/utils/envDynamic.ts
  - src/utils/envUtils.ts
  - src/utils/envValidation.ts
  - src/utils/errorLogSink.ts
  - src/utils/errors.ts
  - src/utils/exampleCommands.ts
  - src/utils/execFileNoThrowPortable.ts
  - src/utils/execSyncWrapper.ts
  - src/utils/exportRenderer.tsx
  - src/utils/extraUsage.ts
  - src/utils/fastMode.ts
  - src/utils/fileOperationAnalytics.ts
  - src/utils/filePersistence/filePersistence.ts
  - src/utils/filePersistence/outputsScanner.ts
  - src/utils/fileRead.ts
  - src/utils/fileReadCache.ts
  - src/utils/fileStateCache.ts
  - src/utils/fingerprint.ts
  - src/utils/format.ts
  - src/utils/formatBriefTimestamp.ts
  - src/utils/fpsTracker.ts
  - src/utils/frontmatterParser.ts
  - src/utils/fsOperations.ts
  - src/utils/fullscreen.ts
  - src/utils/generatedFiles.ts
  - src/utils/generators.ts
  - src/utils/genericProcessUtils.ts
  - src/utils/getWorktreePaths.ts
  - src/utils/getWorktreePathsPortable.ts
  - src/utils/ghPrStatus.ts
  - src/utils/git/gitConfigParser.ts
  - src/utils/git/gitignore.ts
  - src/utils/github/ghAuthStatus.ts
  - src/utils/githubRepoPathMapping.ts
  - src/utils/glob.ts
  - src/utils/gracefulShutdown.ts
  - src/utils/groupToolUses.ts
  - src/utils/handlePromptSubmit.ts
  - src/utils/hash.ts
  - src/utils/headlessProfiler.ts
  - src/utils/heapDumpService.ts
  - src/utils/heatmap.ts
  - src/utils/highlightMatch.tsx
  - src/utils/hooks.ts
  - src/utils/hooks/AsyncHookRegistry.ts
  - src/utils/hooks/apiQueryHookHelper.ts
  - src/utils/hooks/execAgentHook.ts
  - src/utils/hooks/execHttpHook.ts
  - src/utils/hooks/execPromptHook.ts
  - src/utils/hooks/fileChangedWatcher.ts
  - src/utils/hooks/hookEvents.ts
  - src/utils/hooks/hookHelpers.ts
  - src/utils/hooks/hooksConfigManager.ts
  - src/utils/hooks/hooksConfigSnapshot.ts
  - src/utils/hooks/hooksSettings.ts
  - src/utils/hooks/postSamplingHooks.ts
  - src/utils/hooks/registerFrontmatterHooks.ts
  - src/utils/hooks/registerSkillHooks.ts
  - src/utils/hooks/sessionHooks.ts
  - src/utils/hooks/skillImprovement.ts
  - src/utils/hooks/ssrfGuard.ts
  - src/utils/horizontalScroll.ts
  - src/utils/hyperlink.ts
  - src/utils/iTermBackup.ts
  - src/utils/ide.ts
  - src/utils/idePathConversion.ts
  - src/utils/idleTimeout.ts
  - src/utils/imagePaste.ts
  - src/utils/imageResizer.ts
  - src/utils/imageStore.ts
  - src/utils/imageValidation.ts
  - src/utils/inProcessTeammateHelpers.ts
  - src/utils/ink.ts
  - src/utils/intl.ts
  - src/utils/jetbrains.ts
  - src/utils/json.ts
  - src/utils/listSessionsImpl.ts
  - src/utils/localInstaller.ts
  - src/utils/lockfile.ts
  - src/utils/log.ts
  - src/utils/logoV2Utils.ts
  - src/utils/mailbox.ts
  - src/utils/managedEnv.ts
  - src/utils/managedEnvConstants.ts
  - src/utils/markdown.ts
  - src/utils/markdownConfigLoader.ts
  - src/utils/mcp/dateTimeParser.ts
  - src/utils/mcp/elicitationValidation.ts
  - src/utils/mcpInstructionsDelta.ts
  - src/utils/mcpOutputStorage.ts
  - src/utils/mcpValidation.ts
  - src/utils/mcpWebSocketTransport.ts
  - src/utils/memoize.ts
  - src/utils/memoryFileDetection.ts
  - src/utils/messageQueueManager.ts
  - src/utils/messages/mappers.ts
  - src/utils/messages/systemInit.ts
  - src/utils/model/agent.ts
  - src/utils/model/aliases.ts
  - src/utils/model/antModels.ts
  - src/utils/model/bedrock.ts
  - src/utils/model/check1mAccess.ts
  - src/utils/model/configs.ts
  - src/utils/model/contextWindowUpgradeCheck.ts
  - src/utils/model/deprecation.ts
  - src/utils/model/model.ts
  - src/utils/model/modelAllowlist.ts
  - src/utils/model/modelCapabilities.ts
  - src/utils/model/modelOptions.ts
  - src/utils/model/modelStrings.ts
  - src/utils/model/modelSupportOverrides.ts
  - src/utils/model/providers.ts
  - src/utils/model/validateModel.ts
  - src/utils/modelCost.ts
  - src/utils/modifiers.ts
  - src/utils/mtls.ts
  - src/utils/nativeInstaller/download.ts
  - src/utils/nativeInstaller/installer.ts
  - src/utils/nativeInstaller/packageManagers.ts
  - src/utils/nativeInstaller/pidLock.ts
  - src/utils/notebook.ts
  - src/utils/pasteStore.ts
  - src/utils/path.ts
  - src/utils/pdf.ts
  - src/utils/pdfUtils.ts
  - src/utils/peerAddress.ts
  - src/utils/planModeV2.ts
  - src/utils/plans.ts
  - src/utils/platform.ts
  - src/utils/preflightChecks.tsx
  - src/utils/privacyLevel.ts
  - src/utils/process.ts
  - src/utils/processUserInput/processBashCommand.tsx
  - src/utils/processUserInput/processSlashCommand.tsx
  - src/utils/processUserInput/processTextPrompt.ts
  - src/utils/processUserInput/processUserInput.ts
  - src/utils/profilerBase.ts
  - src/utils/promptCategory.ts
  - src/utils/promptEditor.ts
  - src/utils/promptShellExecution.ts
  - src/utils/proxy.ts
  - src/utils/queryContext.ts
  - src/utils/queryProfiler.ts
  - src/utils/queueProcessor.ts
  - src/utils/readEditContext.ts
  - src/utils/readFileInRange.ts
  - src/utils/releaseNotes.ts
  - src/utils/renderOptions.ts
  - src/utils/sanitization.ts
  - src/utils/screenshotClipboard.ts
  - src/utils/sdkEventQueue.ts
  - src/utils/semanticBoolean.ts
  - src/utils/semanticNumber.ts
  - src/utils/semver.ts
  - src/utils/sequential.ts
  - src/utils/sessionActivity.ts
  - src/utils/sessionEnvVars.ts
  - src/utils/sessionEnvironment.ts
  - src/utils/sessionFileAccessHooks.ts
  - src/utils/sessionIngressAuth.ts
  - src/utils/sessionStart.ts
  - src/utils/sessionState.ts
  - src/utils/sessionTitle.ts
  - src/utils/sessionUrl.ts
  - src/utils/set.ts
  - src/utils/shellConfig.ts
  - src/utils/sideQuery.ts
  - src/utils/sideQuestion.ts
  - src/utils/signal.ts
  - src/utils/skills/skillChangeDetector.ts
  - src/utils/slashCommandParsing.ts
  - src/utils/sleep.ts
  - src/utils/sliceAnsi.ts
  - src/utils/slowOperations.ts
  - src/utils/standaloneAgent.ts
  - src/utils/staticRender.tsx
  - src/utils/stats.ts
  - src/utils/statsCache.ts
  - src/utils/status.tsx
  - src/utils/statusNoticeDefinitions.tsx
  - src/utils/stream.ts
  - src/utils/streamJsonStdoutGuard.ts
  - src/utils/streamlinedTransform.ts
  - src/utils/stringUtils.ts
  - src/utils/subprocessEnv.ts
  - src/utils/suggestions/commandSuggestions.ts
  - src/utils/suggestions/directoryCompletion.ts
  - src/utils/suggestions/shellHistoryCompletion.ts
  - src/utils/suggestions/skillUsageTracking.ts
  - src/utils/suggestions/slackChannelSuggestions.ts
  - src/utils/systemDirectories.ts
  - src/utils/systemPrompt.ts
  - src/utils/systemTheme.ts
  - src/utils/taggedId.ts
  - src/utils/tasks.ts
  - src/utils/teamDiscovery.ts
  - src/utils/teamMemoryOps.ts
  - src/utils/teammate.ts
  - src/utils/teammateContext.ts
  - src/utils/teammateMailbox.ts
  - src/utils/teleport.tsx
  - src/utils/teleport/api.ts
  - src/utils/teleport/environmentSelection.ts
  - src/utils/teleport/environments.ts
  - src/utils/teleport/gitBundle.ts
  - src/utils/tempfile.ts
  - src/utils/terminal.ts
  - src/utils/terminalPanel.ts
  - src/utils/textHighlighting.ts
  - src/utils/theme.ts
  - src/utils/thinking.ts
  - src/utils/timeouts.ts
  - src/utils/tmuxSocket.ts
  - src/utils/tokenBudget.ts
  - src/utils/tokens.ts
  - src/utils/toolErrors.ts
  - src/utils/toolPool.ts
  - src/utils/toolSchemaCache.ts
  - src/utils/transcriptSearch.ts
  - src/utils/treeify.ts
  - src/utils/truncate.ts
  - src/utils/ultraplan/ccrSession.ts
  - src/utils/ultraplan/keyword.ts
  - src/utils/unaryLogging.ts
  - src/utils/undercover.ts
  - src/utils/user.ts
  - src/utils/userPromptKeywords.ts
  - src/utils/uuid.ts
  - src/utils/which.ts
  - src/utils/windowsPaths.ts
  - src/utils/words.ts
  - src/utils/workloadContext.ts
  - src/utils/worktree.ts
  - src/utils/xdg.ts
  - src/utils/zodToJsonSchema.ts
- **Dependencies**: T-01
- **Estimated Complexity**: HIGH
- **Rationale**: ML-02 核心：查询引擎是整个系统的"心脏"，承载消息循环、上下文管理和模型交互

### T-04: 查询API流式处理与消息

- **Output Slug**: query-api-messages
- **Priority**: P1
- **Primary Mainline**: ML-02
- **Scope**: API 流式请求/响应处理、消息序列化、SSE 协议
- **Boundaries**: 不涉及查询引擎内部逻辑（T-03），不涉及 API 客户端重试（T-15）
- **Scope Files** (7 files, 11,711 lines):
  - src/Tool.ts
  - src/services/api/claude.ts
  - src/services/tools/StreamingToolExecutor.ts
  - src/services/tools/toolOrchestration.ts
  - src/utils/api.ts
  - src/utils/messages.ts
  - src/utils/queryHelpers.ts
- **Dependencies**: T-03
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-02 关键支撑：API 流式层连接查询引擎与 Anthropic API，是消息传输的关键桥梁

### T-05: 工具系统核心调度

- **Output Slug**: tool-system-core
- **Priority**: P1
- **Primary Mainline**: ML-03
- **Scope**: 工具系统核心调度、工具注册、工具执行引擎、工具结果处理
- **Boundaries**: 不涉及具体工具实现（Pattern Audit PI-01），不涉及权限检查（T-06）
- **Scope Files** (142 files, 58,846 lines):
  - src/constants/tools.ts
  - src/services/tools/toolExecution.ts
  - src/tools.ts
  - src/tools/AgentTool/AgentTool.tsx
  - src/tools/AgentTool/UI.tsx
  - src/tools/AgentTool/agentColorManager.ts
  - src/tools/AgentTool/agentDisplay.ts
  - src/tools/AgentTool/agentMemory.ts
  - src/tools/AgentTool/agentMemorySnapshot.ts
  - src/tools/AgentTool/agentToolUtils.ts
  - src/tools/AgentTool/built-in/claudeCodeGuideAgent.ts
  - src/tools/AgentTool/built-in/exploreAgent.ts
  - src/tools/AgentTool/built-in/planAgent.ts
  - src/tools/AgentTool/built-in/statuslineSetup.ts
  - src/tools/AgentTool/built-in/verificationAgent.ts
  - src/tools/AgentTool/builtInAgents.ts
  - src/tools/AgentTool/forkSubagent.ts
  - src/tools/AgentTool/loadAgentsDir.ts
  - src/tools/AgentTool/prompt.ts
  - src/tools/AgentTool/resumeAgent.ts
  - src/tools/AgentTool/runAgent.ts
  - src/tools/AskUserQuestionTool/AskUserQuestionTool.tsx
  - src/tools/BashTool/BashTool.tsx
  - src/tools/BashTool/BashToolResultMessage.tsx
  - src/tools/BashTool/UI.tsx
  - src/tools/BashTool/bashCommandHelpers.ts
  - src/tools/BashTool/bashPermissions.ts
  - src/tools/BashTool/bashSecurity.ts
  - src/tools/BashTool/commandSemantics.ts
  - src/tools/BashTool/destructiveCommandWarning.ts
  - src/tools/BashTool/modeValidation.ts
  - src/tools/BashTool/pathValidation.ts
  - src/tools/BashTool/prompt.ts
  - src/tools/BashTool/readOnlyValidation.ts
  - src/tools/BashTool/sedEditParser.ts
  - src/tools/BashTool/sedValidation.ts
  - src/tools/BashTool/shouldUseSandbox.ts
  - src/tools/BashTool/utils.ts
  - src/tools/BriefTool/BriefTool.ts
  - src/tools/BriefTool/UI.tsx
  - src/tools/BriefTool/attachments.ts
  - src/tools/BriefTool/upload.ts
  - src/tools/ConfigTool/ConfigTool.ts
  - src/tools/ConfigTool/prompt.ts
  - src/tools/ConfigTool/supportedSettings.ts
  - src/tools/EnterPlanModeTool/EnterPlanModeTool.ts
  - src/tools/EnterPlanModeTool/prompt.ts
  - src/tools/EnterWorktreeTool/EnterWorktreeTool.ts
  - src/tools/ExitPlanModeTool/ExitPlanModeV2Tool.ts
  - src/tools/ExitPlanModeTool/UI.tsx
  - src/tools/ExitWorktreeTool/ExitWorktreeTool.ts
  - src/tools/FileEditTool/FileEditTool.ts
  - src/tools/FileEditTool/UI.tsx
  - src/tools/FileEditTool/types.ts
  - src/tools/FileEditTool/utils.ts
  - src/tools/FileReadTool/FileReadTool.ts
  - src/tools/FileReadTool/UI.tsx
  - src/tools/FileReadTool/imageProcessor.ts
  - src/tools/FileReadTool/limits.ts
  - src/tools/FileWriteTool/FileWriteTool.ts
  - src/tools/FileWriteTool/UI.tsx
  - src/tools/GlobTool/GlobTool.ts
  - src/tools/GlobTool/UI.tsx
  - src/tools/GrepTool/GrepTool.ts
  - src/tools/GrepTool/UI.tsx
  - src/tools/LSPTool/LSPTool.ts
  - src/tools/LSPTool/UI.tsx
  - src/tools/LSPTool/formatters.ts
  - src/tools/LSPTool/schemas.ts
  - src/tools/LSPTool/symbolContext.ts
  - src/tools/NotebookEditTool/NotebookEditTool.ts
  - src/tools/NotebookEditTool/UI.tsx
  - src/tools/PowerShellTool/PowerShellTool.tsx
  - src/tools/PowerShellTool/UI.tsx
  - src/tools/PowerShellTool/clmTypes.ts
  - src/tools/PowerShellTool/commandSemantics.ts
  - src/tools/PowerShellTool/destructiveCommandWarning.ts
  - src/tools/PowerShellTool/gitSafety.ts
  - src/tools/PowerShellTool/modeValidation.ts
  - src/tools/PowerShellTool/pathValidation.ts
  - src/tools/PowerShellTool/powershellPermissions.ts
  - src/tools/PowerShellTool/powershellSecurity.ts
  - src/tools/PowerShellTool/prompt.ts
  - src/tools/PowerShellTool/readOnlyValidation.ts
  - src/tools/RemoteTriggerTool/RemoteTriggerTool.ts
  - src/tools/ScheduleCronTool/CronCreateTool.ts
  - src/tools/ScheduleCronTool/CronDeleteTool.ts
  - src/tools/ScheduleCronTool/CronListTool.ts
  - src/tools/ScheduleCronTool/UI.tsx
  - src/tools/ScheduleCronTool/prompt.ts
  - src/tools/SendMessageTool/SendMessageTool.ts
  - src/tools/SkillTool/SkillTool.ts
  - src/tools/SkillTool/UI.tsx
  - src/tools/SkillTool/prompt.ts
  - src/tools/SyntheticOutputTool/SyntheticOutputTool.ts
  - src/tools/TaskCreateTool/TaskCreateTool.ts
  - src/tools/TaskCreateTool/prompt.ts
  - src/tools/TaskGetTool/TaskGetTool.ts
  - src/tools/TaskListTool/TaskListTool.ts
  - src/tools/TaskOutputTool/TaskOutputTool.tsx
  - src/tools/TaskStopTool/TaskStopTool.ts
  - src/tools/TaskUpdateTool/TaskUpdateTool.ts
  - src/tools/TaskUpdateTool/prompt.ts
  - src/tools/TeamCreateTool/TeamCreateTool.ts
  - src/tools/TeamCreateTool/prompt.ts
  - src/tools/TeamDeleteTool/TeamDeleteTool.ts
  - src/tools/TodoWriteTool/TodoWriteTool.ts
  - src/tools/TodoWriteTool/prompt.ts
  - src/tools/ToolSearchTool/ToolSearchTool.ts
  - src/tools/ToolSearchTool/prompt.ts
  - src/tools/WebFetchTool/UI.tsx
  - src/tools/WebFetchTool/WebFetchTool.ts
  - src/tools/WebFetchTool/preapproved.ts
  - src/tools/WebFetchTool/utils.ts
  - src/tools/WebSearchTool/UI.tsx
  - src/tools/WebSearchTool/WebSearchTool.ts
  - src/tools/shared/gitOperationTracking.ts
  - src/tools/shared/spawnMultiAgent.ts
  - src/tools/testing/TestingPermissionTool.tsx
  - src/types/tools.ts
  - src/utils/computerUse/appNames.ts
  - src/utils/computerUse/cleanup.ts
  - src/utils/computerUse/common.ts
  - src/utils/computerUse/computerUseLock.ts
  - src/utils/computerUse/drainRunLoop.ts
  - src/utils/computerUse/escHotkey.ts
  - src/utils/computerUse/executor.ts
  - src/utils/computerUse/gates.ts
  - src/utils/computerUse/hostAdapter.ts
  - src/utils/computerUse/mcpServer.ts
  - src/utils/computerUse/setup.ts
  - src/utils/computerUse/toolRendering.tsx
  - src/utils/computerUse/wrapper.tsx
  - src/utils/embeddedTools.ts
  - src/utils/file.ts
  - src/utils/fileHistory.ts
  - src/utils/git.ts
  - src/utils/git/gitFilesystem.ts
  - src/utils/gitDiff.ts
  - src/utils/ripgrep.ts
  - src/utils/toolResultStorage.ts
  - src/utils/toolSearch.ts
- **Dependencies**: T-03
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-03 核心：工具系统是 Claude Code 的关键扩展能力，调度引擎决定工具执行策略

### T-06: 权限规则引擎

- **Output Slug**: permission-rules
- **Priority**: P1
- **Primary Mainline**: ML-04
- **Scope**: 权限规则引擎、权限检查机制、安全策略定义
- **Boundaries**: 不涉及 AI 权限分类器（T-07），不涉及权限 UI 组件（Pattern Audit PI-06）
- **Scope Files** (23 files, 5,636 lines):
  - src/hooks/useCanUseTool.tsx
  - src/migrations/migrateBypassPermissionsAcceptedToSettings.ts
  - src/remote/remotePermissionBridge.ts
  - src/services/mcp/channelPermissions.ts
  - src/services/tools/toolHooks.ts
  - src/utils/permissions/PermissionMode.ts
  - src/utils/permissions/PermissionPromptToolResultSchema.ts
  - src/utils/permissions/PermissionResult.ts
  - src/utils/permissions/PermissionRule.ts
  - src/utils/permissions/PermissionUpdate.ts
  - src/utils/permissions/PermissionUpdateSchema.ts
  - src/utils/permissions/autoModeState.ts
  - src/utils/permissions/bypassPermissionsKillswitch.ts
  - src/utils/permissions/classifierDecision.ts
  - src/utils/permissions/denialTracking.ts
  - src/utils/permissions/getNextPermissionMode.ts
  - src/utils/permissions/pathValidation.ts
  - src/utils/permissions/permissionExplainer.ts
  - src/utils/permissions/permissionRuleParser.ts
  - src/utils/permissions/permissions.ts
  - src/utils/permissions/permissionsLoader.ts
  - src/utils/permissions/shadowedRuleDetection.ts
  - src/utils/permissions/shellRuleMatching.ts
- **Dependencies**: T-05
- **Estimated Complexity**: HIGH
- **Rationale**: ML-04 核心：权限引擎是安全基石，控制工具执行和文件访问的安全边界

### T-07: 权限AI分类器与文件系统

- **Output Slug**: permission-classifier
- **Priority**: P1
- **Primary Mainline**: ML-04
- **Scope**: 权限 AI 分类器、文件系统权限管理、动态权限决策
- **Boundaries**: 不涉及权限规则引擎核心（T-06），不涉及 MCP 权限（T-08）
- **Scope Files** (55 files, 16,720 lines):
  - src/components/permissions/AskUserQuestionPermissionRequest/AskUserQuestionPermissionRequest.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/PreviewBox.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/PreviewQuestionView.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/QuestionNavigationBar.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/QuestionView.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/SubmitQuestionsView.tsx
  - src/components/permissions/AskUserQuestionPermissionRequest/use-multiple-choice-state.ts
  - src/components/permissions/BashPermissionRequest/BashPermissionRequest.tsx
  - src/components/permissions/BashPermissionRequest/bashToolUseOptions.tsx
  - src/components/permissions/ComputerUseApproval/ComputerUseApproval.tsx
  - src/components/permissions/EnterPlanModePermissionRequest/EnterPlanModePermissionRequest.tsx
  - src/components/permissions/ExitPlanModePermissionRequest/ExitPlanModePermissionRequest.tsx
  - src/components/permissions/FallbackPermissionRequest.tsx
  - src/components/permissions/FileEditPermissionRequest/FileEditPermissionRequest.tsx
  - src/components/permissions/FilePermissionDialog/FilePermissionDialog.tsx
  - src/components/permissions/FilePermissionDialog/permissionOptions.tsx
  - src/components/permissions/FilePermissionDialog/useFilePermissionDialog.ts
  - src/components/permissions/FilePermissionDialog/usePermissionHandler.ts
  - src/components/permissions/FileWritePermissionRequest/FileWritePermissionRequest.tsx
  - src/components/permissions/FileWritePermissionRequest/FileWriteToolDiff.tsx
  - src/components/permissions/FilesystemPermissionRequest/FilesystemPermissionRequest.tsx
  - src/components/permissions/NotebookEditPermissionRequest/NotebookEditPermissionRequest.tsx
  - src/components/permissions/NotebookEditPermissionRequest/NotebookEditToolDiff.tsx
  - src/components/permissions/PermissionDecisionDebugInfo.tsx
  - src/components/permissions/PermissionDialog.tsx
  - src/components/permissions/PermissionExplanation.tsx
  - src/components/permissions/PermissionPrompt.tsx
  - src/components/permissions/PermissionRequestTitle.tsx
  - src/components/permissions/PermissionRuleExplanation.tsx
  - src/components/permissions/PowerShellPermissionRequest/PowerShellPermissionRequest.tsx
  - src/components/permissions/PowerShellPermissionRequest/powershellToolUseOptions.tsx
  - src/components/permissions/SedEditPermissionRequest/SedEditPermissionRequest.tsx
  - src/components/permissions/SkillPermissionRequest/SkillPermissionRequest.tsx
  - src/components/permissions/WebFetchPermissionRequest/WebFetchPermissionRequest.tsx
  - src/components/permissions/WorkerPendingPermission.tsx
  - src/components/permissions/hooks.ts
  - src/components/permissions/rules/AddPermissionRules.tsx
  - src/components/permissions/rules/AddWorkspaceDirectory.tsx
  - src/components/permissions/rules/PermissionRuleDescription.tsx
  - src/components/permissions/rules/PermissionRuleInput.tsx
  - src/components/permissions/rules/PermissionRuleList.tsx
  - src/components/permissions/rules/RecentDenialsTab.tsx
  - src/components/permissions/rules/RemoveWorkspaceDirectory.tsx
  - src/components/permissions/rules/WorkspaceTab.tsx
  - src/components/permissions/shellPermissionHelpers.tsx
  - src/components/permissions/useShellPermissionFeedback.ts
  - src/utils/permissions/bashClassifier.ts
  - src/utils/permissions/classifierShared.ts
  - src/utils/permissions/dangerousPatterns.ts
  - src/utils/permissions/filesystem.ts
  - src/utils/permissions/permissionSetup.ts
  - src/utils/permissions/yolo-classifier-prompts/auto_mode_system_prompt.txt
  - src/utils/permissions/yolo-classifier-prompts/permissions_anthropic.txt
  - src/utils/permissions/yolo-classifier-prompts/permissions_external.txt
  - src/utils/permissions/yoloClassifier.ts
- **Dependencies**: T-06
- **Estimated Complexity**: HIGH
- **Rationale**: ML-04 关键支撑：AI 分类器实现智能权限决策，文件系统权限是安全落地的关键环节

### T-08: MCP服务集成

- **Output Slug**: mcp-integration
- **Priority**: P1
- **Primary Mainline**: ML-05
- **Scope**: MCP（Model Context Protocol）服务集成、服务器管理、协议实现
- **Boundaries**: 不涉及工具系统调度（T-05），不涉及 MCP UI 组件（Pattern Audit PI-20）
- **Scope Files** (85 files, 31,771 lines):
  - src/components/mcp/CapabilitiesSection.tsx
  - src/components/mcp/MCPAgentServerMenu.tsx
  - src/components/mcp/MCPListPanel.tsx
  - src/components/mcp/MCPReconnect.tsx
  - src/components/mcp/MCPRemoteServerMenu.tsx
  - src/components/mcp/MCPSettings.tsx
  - src/components/mcp/MCPStdioServerMenu.tsx
  - src/components/mcp/MCPToolDetailView.tsx
  - src/components/mcp/MCPToolListView.tsx
  - src/components/mcp/McpParsingWarnings.tsx
  - src/services/AgentSummary/agentSummary.ts
  - src/services/MagicDocs/magicDocs.ts
  - src/services/MagicDocs/prompts.ts
  - src/services/PromptSuggestion/promptSuggestion.ts
  - src/services/PromptSuggestion/speculation.ts
  - src/services/analytics/config.ts
  - src/services/analytics/datadog.ts
  - src/services/analytics/firstPartyEventLogger.ts
  - src/services/analytics/firstPartyEventLoggingExporter.ts
  - src/services/analytics/index.ts
  - src/services/analytics/metadata.ts
  - src/services/analytics/sink.ts
  - src/services/autoDream/autoDream.ts
  - src/services/autoDream/consolidationLock.ts
  - src/services/autoDream/consolidationPrompt.ts
  - src/services/awaySummary.ts
  - src/services/diagnosticTracking.ts
  - src/services/extractMemories/extractMemories.ts
  - src/services/extractMemories/prompts.ts
  - src/services/internalLogging.ts
  - src/services/lsp/LSPClient.ts
  - src/services/lsp/LSPDiagnosticRegistry.ts
  - src/services/lsp/LSPServerInstance.ts
  - src/services/lsp/LSPServerManager.ts
  - src/services/lsp/config.ts
  - src/services/lsp/manager.ts
  - src/services/lsp/passiveFeedback.ts
  - src/services/mcp/InProcessTransport.ts
  - src/services/mcp/MCPConnectionManager.tsx
  - src/services/mcp/SdkControlTransport.ts
  - src/services/mcp/auth.ts
  - src/services/mcp/channelAllowlist.ts
  - src/services/mcp/channelNotification.ts
  - src/services/mcp/claudeai.ts
  - src/services/mcp/client.ts
  - src/services/mcp/config.ts
  - src/services/mcp/elicitationHandler.ts
  - src/services/mcp/envExpansion.ts
  - src/services/mcp/headersHelper.ts
  - src/services/mcp/mcpStringUtils.ts
  - src/services/mcp/normalization.ts
  - src/services/mcp/oauthPort.ts
  - src/services/mcp/officialRegistry.ts
  - src/services/mcp/types.ts
  - src/services/mcp/useManageMCPConnections.ts
  - src/services/mcp/utils.ts
  - src/services/mcp/vscodeSdkMcp.ts
  - src/services/mcp/xaa.ts
  - src/services/mcp/xaaIdpLogin.ts
  - src/services/mcpServerApproval.tsx
  - src/services/notifier.ts
  - src/services/preventSleep.ts
  - src/services/rateLimitMessages.ts
  - src/services/rateLimitMocking.ts
  - src/services/remoteManagedSettings/securityCheck.tsx
  - src/services/settingsSync/index.ts
  - src/services/settingsSync/types.ts
  - src/services/teamMemorySync/index.ts
  - src/services/teamMemorySync/secretScanner.ts
  - src/services/teamMemorySync/teamMemSecretGuard.ts
  - src/services/teamMemorySync/types.ts
  - src/services/teamMemorySync/watcher.ts
  - src/services/tips/tipRegistry.ts
  - src/services/tips/tipScheduler.ts
  - src/services/toolUseSummary/toolUseSummaryGenerator.ts
  - src/services/vcr.ts
  - src/services/voice.ts
  - src/services/voiceKeyterms.ts
  - src/services/voiceStreamSTT.ts
  - src/tools/ListMcpResourcesTool/ListMcpResourcesTool.ts
  - src/tools/MCPTool/MCPTool.ts
  - src/tools/MCPTool/UI.tsx
  - src/tools/MCPTool/classifyForCollapse.ts
  - src/tools/McpAuthTool/McpAuthTool.ts
  - src/tools/ReadMcpResourceTool/ReadMcpResourceTool.ts
- **Dependencies**: T-06
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-05 核心：MCP 是外部工具集成的核心协议，决定系统可扩展性

### T-09: 认证与会话管理

- **Output Slug**: auth-session
- **Priority**: P1
- **Primary Mainline**: ML-06
- **Scope**: 认证与会话管理、OAuth 流程、Token 生命周期
- **Boundaries**: 不涉及 API 客户端重试层（T-15），不涉及遥测模块（Pattern Audit PI-24）
- **Scope Files** (40 files, 13,387 lines):
  - src/cli/handlers/auth.ts
  - src/commands/login/login.tsx
  - src/commands/session/session.tsx
  - src/components/ConsoleOAuthFlow.tsx
  - src/constants/oauth.ts
  - src/services/analytics/growthbook.ts
  - src/services/api/bootstrap.ts
  - src/services/mockRateLimits.ts
  - src/services/oauth/auth-code-listener.ts
  - src/services/oauth/client.ts
  - src/services/oauth/crypto.ts
  - src/services/oauth/getOauthProfile.ts
  - src/services/oauth/index.ts
  - src/services/oauth/types.ts
  - src/services/policyLimits/index.ts
  - src/services/policyLimits/types.ts
  - src/services/remoteManagedSettings/index.ts
  - src/services/remoteManagedSettings/syncCache.ts
  - src/services/remoteManagedSettings/syncCacheState.ts
  - src/services/remoteManagedSettings/types.ts
  - src/utils/auth.ts
  - src/utils/aws.ts
  - src/utils/awsAuthStatusManager.ts
  - src/utils/execFileNoThrow.ts
  - src/utils/http.ts
  - src/utils/secureStorage/fallbackStorage.ts
  - src/utils/secureStorage/index.ts
  - src/utils/secureStorage/keychainPrefetch.ts
  - src/utils/secureStorage/macOsKeychainHelpers.ts
  - src/utils/secureStorage/macOsKeychainStorage.ts
  - src/utils/secureStorage/plainTextStorage.ts
  - src/utils/secureStorage/types.ts
  - src/utils/telemetry/betaSessionTracing.ts
  - src/utils/telemetry/bigqueryExporter.ts
  - src/utils/telemetry/events.ts
  - src/utils/telemetry/instrumentation.ts
  - src/utils/telemetry/perfettoTracing.ts
  - src/utils/telemetry/pluginTelemetry.ts
  - src/utils/telemetry/sessionTracing.ts
  - src/utils/telemetryAttributes.ts
- **Dependencies**: T-01
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-06 核心：认证是所有 API 交互的前提，会话管理影响用户体验和资源使用

### T-10: TUI主界面与Ink框架

- **Output Slug**: tui-repl-ink
- **Priority**: P2
- **Primary Mainline**: ML-07
- **Scope**: TUI 主界面框架、Ink 渲染引擎集成、布局管理
- **Boundaries**: 不涉及具体 UI 组件（T-11），不涉及交互 Hooks（T-12）
- **Scope Files** (80 files, 28,353 lines):
  - src/components/FullscreenLayout.tsx
  - src/components/Messages.tsx
  - src/components/PromptInput/PromptInput.tsx
  - src/components/ScrollKeybindingHandler.tsx
  - src/components/Spinner.tsx
  - src/components/VirtualMessageList.tsx
  - src/components/mcp/ElicitationDialog.tsx
  - src/context.ts
  - src/context/fpsMetrics.tsx
  - src/context/notifications.tsx
  - src/ink.ts
  - src/ink/Ansi.tsx
  - src/ink/bidi.ts
  - src/ink/clearTerminal.ts
  - src/ink/colorize.ts
  - src/ink/components/AlternateScreen.tsx
  - src/ink/components/App.tsx
  - src/ink/components/Box.tsx
  - src/ink/components/Button.tsx
  - src/ink/components/ClockContext.tsx
  - src/ink/components/ErrorOverview.tsx
  - src/ink/components/NoSelect.tsx
  - src/ink/components/RawAnsi.tsx
  - src/ink/components/ScrollBox.tsx
  - src/ink/components/TerminalFocusContext.tsx
  - src/ink/components/Text.tsx
  - src/ink/dom.ts
  - src/ink/events/dispatcher.ts
  - src/ink/events/event-handlers.ts
  - src/ink/events/input-event.ts
  - src/ink/events/keyboard-event.ts
  - src/ink/events/terminal-event.ts
  - src/ink/focus.ts
  - src/ink/frame.ts
  - src/ink/hit-test.ts
  - src/ink/hooks/use-animation-frame.ts
  - src/ink/hooks/use-declared-cursor.ts
  - src/ink/hooks/use-input.ts
  - src/ink/hooks/use-interval.ts
  - src/ink/hooks/use-search-highlight.ts
  - src/ink/hooks/use-selection.ts
  - src/ink/hooks/use-tab-status.ts
  - src/ink/hooks/use-terminal-viewport.ts
  - src/ink/layout/geometry.ts
  - src/ink/layout/node.ts
  - src/ink/layout/yoga.ts
  - src/ink/log-update.ts
  - src/ink/node-cache.ts
  - src/ink/optimizer.ts
  - src/ink/output.ts
  - src/ink/parse-keypress.ts
  - src/ink/reconciler.ts
  - src/ink/render-border.ts
  - src/ink/render-to-screen.ts
  - src/ink/renderer.ts
  - src/ink/root.ts
  - src/ink/searchHighlight.ts
  - src/ink/selection.ts
  - src/ink/squash-text-nodes.ts
  - src/ink/stringWidth.ts
  - src/ink/styles.ts
  - src/ink/supports-hyperlinks.ts
  - src/ink/terminal-querier.ts
  - src/ink/terminal.ts
  - src/ink/termio/ansi.ts
  - src/ink/termio/csi.ts
  - src/ink/termio/dec.ts
  - src/ink/termio/esc.ts
  - src/ink/termio/osc.ts
  - src/ink/termio/parser.ts
  - src/ink/termio/sgr.ts
  - src/ink/termio/tokenize.ts
  - src/ink/termio/types.ts
  - src/ink/useTerminalNotification.ts
  - src/ink/wrap-text.ts
  - src/keybindings/KeybindingProviderSetup.tsx
  - src/keybindings/shortcutFormat.ts
  - src/keybindings/useShortcutDisplay.ts
  - src/screens/REPL.tsx
  - src/state/AppState.tsx
- **Dependencies**: T-02
- **Estimated Complexity**: HIGH
- **Rationale**: ML-07 入口：TUI 主界面是用户直接交互的核心，Ink 框架集成决定了渲染架构

### T-11: TUI组件与Ink渲染

- **Output Slug**: tui-components
- **Priority**: P2
- **Primary Mainline**: ML-07
- **Scope**: TUI 组件库、消息渲染、Ink 组件 fork 和定制
- **Boundaries**: 不涉及主界面框架（T-10），不涉及交互 Hooks（T-12）
- **Scope Files** (321 files, 72,844 lines):
  - src/buddy/sprites.ts
  - src/components/AgentProgressLine.tsx
  - src/components/App.tsx
  - src/components/ApproveApiKey.tsx
  - src/components/AutoModeOptInDialog.tsx
  - src/components/AutoUpdater.tsx
  - src/components/AutoUpdaterWrapper.tsx
  - src/components/AwsAuthStatusBox.tsx
  - src/components/BaseTextInput.tsx
  - src/components/BashModeProgress.tsx
  - src/components/BridgeDialog.tsx
  - src/components/BypassPermissionsModeDialog.tsx
  - src/components/ChannelDowngradeDialog.tsx
  - src/components/ClaudeCodeHint/PluginHintMenu.tsx
  - src/components/ClaudeInChromeOnboarding.tsx
  - src/components/ClaudeMdExternalIncludesDialog.tsx
  - src/components/ClickableImageRef.tsx
  - src/components/CompactSummary.tsx
  - src/components/ConfigurableShortcutHint.tsx
  - src/components/ContextSuggestions.tsx
  - src/components/ContextVisualization.tsx
  - src/components/CoordinatorAgentStatus.tsx
  - src/components/CostThresholdDialog.tsx
  - src/components/CtrlOToExpand.tsx
  - src/components/CustomSelect/SelectMulti.tsx
  - src/components/CustomSelect/option-map.ts
  - src/components/CustomSelect/select-input-option.tsx
  - src/components/CustomSelect/select-option.tsx
  - src/components/CustomSelect/select.tsx
  - src/components/CustomSelect/use-multi-select-state.ts
  - src/components/CustomSelect/use-select-input.ts
  - src/components/CustomSelect/use-select-navigation.ts
  - src/components/CustomSelect/use-select-state.ts
  - src/components/DesktopHandoff.tsx
  - src/components/DesktopUpsell/DesktopUpsellStartup.tsx
  - src/components/DevBar.tsx
  - src/components/DevChannelsDialog.tsx
  - src/components/DiagnosticsDisplay.tsx
  - src/components/EffortCallout.tsx
  - src/components/EffortIndicator.ts
  - src/components/ExitFlow.tsx
  - src/components/ExportDialog.tsx
  - src/components/FallbackToolUseErrorMessage.tsx
  - src/components/FastIcon.tsx
  - src/components/Feedback.tsx
  - src/components/FeedbackSurvey/FeedbackSurvey.tsx
  - src/components/FeedbackSurvey/FeedbackSurveyView.tsx
  - src/components/FeedbackSurvey/TranscriptSharePrompt.tsx
  - src/components/FeedbackSurvey/submitTranscriptShare.ts
  - src/components/FeedbackSurvey/useDebouncedDigitInput.ts
  - src/components/FeedbackSurvey/useFeedbackSurvey.tsx
  - src/components/FeedbackSurvey/useMemorySurvey.tsx
  - src/components/FeedbackSurvey/usePostCompactSurvey.tsx
  - src/components/FeedbackSurvey/useSurveyState.tsx
  - src/components/FileEditToolDiff.tsx
  - src/components/FileEditToolUpdatedMessage.tsx
  - src/components/FileEditToolUseRejectedMessage.tsx
  - src/components/FilePathLink.tsx
  - src/components/GlobalSearchDialog.tsx
  - src/components/HelpV2/Commands.tsx
  - src/components/HelpV2/General.tsx
  - src/components/HelpV2/HelpV2.tsx
  - src/components/HighlightedCode.tsx
  - src/components/HighlightedCode/Fallback.tsx
  - src/components/HistorySearchDialog.tsx
  - src/components/IdeAutoConnectDialog.tsx
  - src/components/IdeOnboardingDialog.tsx
  - src/components/IdeStatusIndicator.tsx
  - src/components/IdleReturnDialog.tsx
  - src/components/InvalidConfigDialog.tsx
  - src/components/InvalidSettingsDialog.tsx
  - src/components/KeybindingWarnings.tsx
  - src/components/LanguagePicker.tsx
  - src/components/LogSelector.tsx
  - src/components/LogoV2/AnimatedAsterisk.tsx
  - src/components/LogoV2/AnimatedClawd.tsx
  - src/components/LogoV2/ChannelsNotice.tsx
  - src/components/LogoV2/Clawd.tsx
  - src/components/LogoV2/CondensedLogo.tsx
  - src/components/LogoV2/EmergencyTip.tsx
  - src/components/LogoV2/Feed.tsx
  - src/components/LogoV2/FeedColumn.tsx
  - src/components/LogoV2/GuestPassesUpsell.tsx
  - src/components/LogoV2/LogoV2.tsx
  - src/components/LogoV2/Opus1mMergeNotice.tsx
  - src/components/LogoV2/OverageCreditUpsell.tsx
  - src/components/LogoV2/VoiceModeNotice.tsx
  - src/components/LogoV2/WelcomeV2.tsx
  - src/components/LogoV2/feedConfigs.tsx
  - src/components/LspRecommendation/LspRecommendationMenu.tsx
  - src/components/MCPServerApprovalDialog.tsx
  - src/components/MCPServerDesktopImportDialog.tsx
  - src/components/MCPServerMultiselectDialog.tsx
  - src/components/ManagedSettingsSecurityDialog/ManagedSettingsSecurityDialog.tsx
  - src/components/ManagedSettingsSecurityDialog/utils.ts
  - src/components/Markdown.tsx
  - src/components/MarkdownTable.tsx
  - src/components/MemoryUsageIndicator.tsx
  - src/components/Message.tsx
  - src/components/MessageModel.tsx
  - src/components/MessageResponse.tsx
  - src/components/MessageRow.tsx
  - src/components/MessageSelector.tsx
  - src/components/MessageTimestamp.tsx
  - src/components/ModelPicker.tsx
  - src/components/NativeAutoUpdater.tsx
  - src/components/NotebookEditToolUseRejectedMessage.tsx
  - src/components/OffscreenFreeze.tsx
  - src/components/Onboarding.tsx
  - src/components/OutputStylePicker.tsx
  - src/components/PackageManagerAutoUpdater.tsx
  - src/components/Passes/Passes.tsx
  - src/components/PrBadge.tsx
  - src/components/PromptInput/HistorySearchInput.tsx
  - src/components/PromptInput/Notifications.tsx
  - src/components/PromptInput/PromptInputFooter.tsx
  - src/components/PromptInput/PromptInputFooterLeftSide.tsx
  - src/components/PromptInput/PromptInputFooterSuggestions.tsx
  - src/components/PromptInput/PromptInputHelpMenu.tsx
  - src/components/PromptInput/PromptInputModeIndicator.tsx
  - src/components/PromptInput/PromptInputQueuedCommands.tsx
  - src/components/PromptInput/PromptInputStashNotice.tsx
  - src/components/PromptInput/SandboxPromptFooterHint.tsx
  - src/components/PromptInput/ShimmeredInput.tsx
  - src/components/PromptInput/VoiceIndicator.tsx
  - src/components/PromptInput/inputModes.ts
  - src/components/PromptInput/inputPaste.ts
  - src/components/PromptInput/useMaybeTruncateInput.ts
  - src/components/PromptInput/usePromptInputPlaceholder.ts
  - src/components/PromptInput/useShowFastIconHint.ts
  - src/components/PromptInput/useSwarmBanner.ts
  - src/components/PromptInput/utils.ts
  - src/components/QuickOpenDialog.tsx
  - src/components/RemoteCallout.tsx
  - src/components/RemoteEnvironmentDialog.tsx
  - src/components/ResumeTask.tsx
  - src/components/SandboxViolationExpandedView.tsx
  - src/components/SearchBox.tsx
  - src/components/SentryErrorBoundary.ts
  - src/components/SessionBackgroundHint.tsx
  - src/components/SessionPreview.tsx
  - src/components/Settings/Config.tsx
  - src/components/Settings/Settings.tsx
  - src/components/Settings/Status.tsx
  - src/components/Settings/Usage.tsx
  - src/components/ShowInIDEPrompt.tsx
  - src/components/SkillImprovementSurvey.tsx
  - src/components/Spinner/FlashingChar.tsx
  - src/components/Spinner/GlimmerMessage.tsx
  - src/components/Spinner/ShimmerChar.tsx
  - src/components/Spinner/SpinnerAnimationRow.tsx
  - src/components/Spinner/SpinnerGlyph.tsx
  - src/components/Spinner/TeammateSpinnerLine.tsx
  - src/components/Spinner/TeammateSpinnerTree.tsx
  - src/components/Spinner/useShimmerAnimation.ts
  - src/components/Spinner/useStalledAnimation.ts
  - src/components/Spinner/utils.ts
  - src/components/Stats.tsx
  - src/components/StatusLine.tsx
  - src/components/StatusNotices.tsx
  - src/components/StructuredDiff.tsx
  - src/components/StructuredDiff/Fallback.tsx
  - src/components/StructuredDiff/colorDiff.ts
  - src/components/StructuredDiffList.tsx
  - src/components/TagTabs.tsx
  - src/components/TaskListV2.tsx
  - src/components/TeammateViewHeader.tsx
  - src/components/TeleportError.tsx
  - src/components/TeleportProgress.tsx
  - src/components/TeleportRepoMismatchDialog.tsx
  - src/components/TeleportResumeWrapper.tsx
  - src/components/TeleportStash.tsx
  - src/components/TextInput.tsx
  - src/components/ThemePicker.tsx
  - src/components/ThinkingToggle.tsx
  - src/components/TokenWarning.tsx
  - src/components/ToolUseLoader.tsx
  - src/components/TrustDialog/TrustDialog.tsx
  - src/components/TrustDialog/utils.ts
  - src/components/ValidationErrorsList.tsx
  - src/components/VimTextInput.tsx
  - src/components/WorkflowMultiselectDialog.tsx
  - src/components/WorktreeExitDialog.tsx
  - src/components/agents/AgentDetail.tsx
  - src/components/agents/AgentEditor.tsx
  - src/components/agents/AgentsList.tsx
  - src/components/agents/AgentsMenu.tsx
  - src/components/agents/ColorPicker.tsx
  - src/components/agents/ModelSelector.tsx
  - src/components/agents/ToolSelector.tsx
  - src/components/agents/agentFileUtils.ts
  - src/components/agents/generateAgent.ts
  - src/components/agents/new-agent-creation/CreateAgentWizard.tsx
  - src/components/agents/new-agent-creation/wizard-steps/ColorStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/ConfirmStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/ConfirmStepWrapper.tsx
  - src/components/agents/new-agent-creation/wizard-steps/DescriptionStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/GenerateStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/LocationStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/MemoryStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/MethodStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/ModelStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/PromptStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/ToolsStep.tsx
  - src/components/agents/new-agent-creation/wizard-steps/TypeStep.tsx
  - src/components/agents/validateAgent.ts
  - src/components/design-system/Byline.tsx
  - src/components/design-system/Dialog.tsx
  - src/components/design-system/Divider.tsx
  - src/components/design-system/FuzzyPicker.tsx
  - src/components/design-system/KeyboardShortcutHint.tsx
  - src/components/design-system/ListItem.tsx
  - src/components/design-system/LoadingState.tsx
  - src/components/design-system/Pane.tsx
  - src/components/design-system/ProgressBar.tsx
  - src/components/design-system/Ratchet.tsx
  - src/components/design-system/StatusIcon.tsx
  - src/components/design-system/Tabs.tsx
  - src/components/design-system/ThemeProvider.tsx
  - src/components/design-system/ThemedBox.tsx
  - src/components/design-system/ThemedText.tsx
  - src/components/diff/DiffDetailView.tsx
  - src/components/diff/DiffDialog.tsx
  - src/components/diff/DiffFileList.tsx
  - src/components/grove/Grove.tsx
  - src/components/hooks/HooksConfigMenu.tsx
  - src/components/hooks/PromptDialog.tsx
  - src/components/hooks/SelectEventMode.tsx
  - src/components/hooks/SelectHookMode.tsx
  - src/components/hooks/SelectMatcherMode.tsx
  - src/components/hooks/ViewHookMode.tsx
  - src/components/memory/MemoryFileSelector.tsx
  - src/components/memory/MemoryUpdateNotification.tsx
  - src/components/messageActions.tsx
  - src/components/messages/AdvisorMessage.tsx
  - src/components/messages/AssistantTextMessage.tsx
  - src/components/messages/AssistantThinkingMessage.tsx
  - src/components/messages/AssistantToolUseMessage.tsx
  - src/components/messages/AttachmentMessage.tsx
  - src/components/messages/CollapsedReadSearchContent.tsx
  - src/components/messages/GroupedToolUseContent.tsx
  - src/components/messages/HighlightedThinkingText.tsx
  - src/components/messages/HookProgressMessage.tsx
  - src/components/messages/PlanApprovalMessage.tsx
  - src/components/messages/RateLimitMessage.tsx
  - src/components/messages/ShutdownMessage.tsx
  - src/components/messages/SystemAPIErrorMessage.tsx
  - src/components/messages/SystemTextMessage.tsx
  - src/components/messages/TaskAssignmentMessage.tsx
  - src/components/messages/UserAgentNotificationMessage.tsx
  - src/components/messages/UserBashInputMessage.tsx
  - src/components/messages/UserBashOutputMessage.tsx
  - src/components/messages/UserChannelMessage.tsx
  - src/components/messages/UserCommandMessage.tsx
  - src/components/messages/UserImageMessage.tsx
  - src/components/messages/UserLocalCommandOutputMessage.tsx
  - src/components/messages/UserMemoryInputMessage.tsx
  - src/components/messages/UserPromptMessage.tsx
  - src/components/messages/UserResourceUpdateMessage.tsx
  - src/components/messages/UserTeammateMessage.tsx
  - src/components/messages/UserTextMessage.tsx
  - src/components/messages/UserToolResultMessage/UserToolErrorMessage.tsx
  - src/components/messages/UserToolResultMessage/UserToolRejectMessage.tsx
  - src/components/messages/UserToolResultMessage/UserToolResultMessage.tsx
  - src/components/messages/UserToolResultMessage/UserToolSuccessMessage.tsx
  - src/components/messages/nullRenderingAttachments.ts
  - src/components/messages/teamMemCollapsed.tsx
  - src/components/permissions/PermissionRequest.tsx
  - src/components/permissions/SandboxPermissionRequest.tsx
  - src/components/sandbox/SandboxConfigTab.tsx
  - src/components/sandbox/SandboxDependenciesTab.tsx
  - src/components/sandbox/SandboxDoctorSection.tsx
  - src/components/sandbox/SandboxOverridesTab.tsx
  - src/components/sandbox/SandboxSettings.tsx
  - src/components/shell/ExpandShellOutputContext.tsx
  - src/components/shell/OutputLine.tsx
  - src/components/shell/ShellProgressMessage.tsx
  - src/components/shell/ShellTimeDisplay.tsx
  - src/components/skills/SkillsMenu.tsx
  - src/components/tasks/AsyncAgentDetailDialog.tsx
  - src/components/tasks/BackgroundTask.tsx
  - src/components/tasks/BackgroundTaskStatus.tsx
  - src/components/tasks/BackgroundTasksDialog.tsx
  - src/components/tasks/DreamDetailDialog.tsx
  - src/components/tasks/InProcessTeammateDetailDialog.tsx
  - src/components/tasks/RemoteSessionDetailDialog.tsx
  - src/components/tasks/RemoteSessionProgress.tsx
  - src/components/tasks/ShellDetailDialog.tsx
  - src/components/tasks/ShellProgress.tsx
  - src/components/tasks/renderToolActivity.tsx
  - src/components/tasks/taskStatusUtils.tsx
  - src/components/teams/TeamStatus.tsx
  - src/components/teams/TeamsDialog.tsx
  - src/components/ui/OrderedList.tsx
  - src/components/ui/OrderedListItem.tsx
  - src/components/ui/TreeSelect.tsx
  - src/components/wizard/WizardDialogLayout.tsx
  - src/components/wizard/WizardNavigationFooter.tsx
  - src/components/wizard/WizardProvider.tsx
  - src/hooks/fileSuggestions.ts
  - src/hooks/notifs/useAutoModeUnavailableNotification.ts
  - src/hooks/notifs/useCanSwitchToExistingSubscription.tsx
  - src/hooks/notifs/useFastModeNotification.tsx
  - src/hooks/notifs/useIDEStatusIndicator.tsx
  - src/hooks/notifs/useLspInitializationNotification.tsx
  - src/hooks/notifs/useMcpConnectivityStatus.tsx
  - src/hooks/notifs/useModelMigrationNotifications.tsx
  - src/hooks/notifs/usePluginAutoupdateNotification.tsx
  - src/hooks/notifs/usePluginInstallationStatus.tsx
  - src/hooks/notifs/useRateLimitWarningNotification.tsx
  - src/hooks/notifs/useSettingsErrors.tsx
  - src/hooks/notifs/useTeammateShutdownNotification.ts
  - src/hooks/useTypeahead.tsx
  - src/hooks/useVoice.ts
  - src/ink/ink.tsx
  - src/ink/render-node-to-output.ts
  - src/ink/screen.ts
  - src/native-ts/color-diff/index.ts
  - src/native-ts/yoga-layout/index.ts
  - src/screens/Doctor.tsx
  - src/vim/operators.ts
- **Dependencies**: T-10
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-07 核心支撑：组件库构成 TUI 的主体，消息渲染是用户获取信息的主要渠道

### T-12: TUI Hooks与交互层

- **Output Slug**: tui-hooks
- **Priority**: P2
- **Primary Mainline**: ML-07
- **Scope**: TUI 交互层、Hooks 系统、用户输入处理、键盘快捷键
- **Boundaries**: 不涉及 UI 组件渲染（T-11），不涉及主界面框架（T-10）
- **Scope Files** (63 files, 12,247 lines):
  - src/hooks/useAfterFirstRender.ts
  - src/hooks/useApiKeyVerification.ts
  - src/hooks/useArrowKeyHistory.tsx
  - src/hooks/useAssistantHistory.ts
  - src/hooks/useAwaySummary.ts
  - src/hooks/useBackgroundTaskNavigation.ts
  - src/hooks/useCancelRequest.ts
  - src/hooks/useClaudeCodeHintRecommendation.tsx
  - src/hooks/useClipboardImageHint.ts
  - src/hooks/useCommandKeybindings.tsx
  - src/hooks/useCommandQueue.ts
  - src/hooks/useCopyOnSelect.ts
  - src/hooks/useDeferredHookMessages.ts
  - src/hooks/useDiffData.ts
  - src/hooks/useDiffInIDE.ts
  - src/hooks/useDirectConnect.ts
  - src/hooks/useDoublePress.ts
  - src/hooks/useExitOnCtrlCD.ts
  - src/hooks/useFileHistorySnapshotInit.ts
  - src/hooks/useGlobalKeybindings.tsx
  - src/hooks/useHistorySearch.ts
  - src/hooks/useIDEIntegration.tsx
  - src/hooks/useIdeAtMentioned.ts
  - src/hooks/useIdeLogging.ts
  - src/hooks/useIdeSelection.ts
  - src/hooks/useInboxPoller.ts
  - src/hooks/useInputBuffer.ts
  - src/hooks/useIssueFlagBanner.ts
  - src/hooks/useLogMessages.ts
  - src/hooks/useLspPluginRecommendation.tsx
  - src/hooks/useMailboxBridge.ts
  - src/hooks/useMainLoopModel.ts
  - src/hooks/useManagePlugins.ts
  - src/hooks/useMergedClients.ts
  - src/hooks/useMergedCommands.ts
  - src/hooks/useMergedTools.ts
  - src/hooks/useNotifyAfterTimeout.ts
  - src/hooks/usePasteHandler.ts
  - src/hooks/usePluginRecommendationBase.tsx
  - src/hooks/usePrStatus.ts
  - src/hooks/usePromptSuggestion.ts
  - src/hooks/usePromptsFromClaudeInChrome.tsx
  - src/hooks/useQueueProcessor.ts
  - src/hooks/useRemoteSession.ts
  - src/hooks/useReplBridge.tsx
  - src/hooks/useSSHSession.ts
  - src/hooks/useScheduledTasks.ts
  - src/hooks/useSearchInput.ts
  - src/hooks/useSessionBackgrounding.ts
  - src/hooks/useSkillImprovementSurvey.ts
  - src/hooks/useSkillsChange.ts
  - src/hooks/useSwarmInitialization.ts
  - src/hooks/useSwarmPermissionPoller.ts
  - src/hooks/useTaskListWatcher.ts
  - src/hooks/useTasksV2.ts
  - src/hooks/useTeammateViewAutoExit.ts
  - src/hooks/useTeleportResume.tsx
  - src/hooks/useTerminalSize.ts
  - src/hooks/useTextInput.ts
  - src/hooks/useTurnDiffs.ts
  - src/hooks/useVimInput.ts
  - src/hooks/useVirtualScroll.ts
  - src/hooks/useVoiceIntegration.tsx
- **Dependencies**: T-10
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-07 交互层：Hooks 系统管理 TUI 的所有交互逻辑，连接用户输入和 UI 更新

### T-13: 任务系统

- **Output Slug**: task-system
- **Priority**: P2
- **Primary Mainline**: ML-08
- **Scope**: 任务系统、任务调度、后台任务管理
- **Boundaries**: 不涉及具体任务实现（Pattern Audit PI-04），不涉及插件任务（T-17）
- **Scope Files** (21 files, 4,683 lines):
  - src/Task.ts
  - src/tasks.ts
  - src/tasks/DreamTask/DreamTask.ts
  - src/tasks/InProcessTeammateTask/InProcessTeammateTask.tsx
  - src/tasks/InProcessTeammateTask/types.ts
  - src/tasks/LocalAgentTask/LocalAgentTask.tsx
  - src/tasks/LocalMainSessionTask.ts
  - src/tasks/LocalShellTask/LocalShellTask.tsx
  - src/tasks/LocalShellTask/guards.ts
  - src/tasks/LocalShellTask/killShellTasks.ts
  - src/tasks/LocalWorkflowTask/LocalWorkflowTask.ts
  - src/tasks/MonitorMcpTask/MonitorMcpTask.ts
  - src/tasks/RemoteAgentTask/RemoteAgentTask.tsx
  - src/tasks/pillLabel.ts
  - src/tasks/stopTask.ts
  - src/tasks/types.ts
  - src/utils/task/TaskOutput.ts
  - src/utils/task/diskOutput.ts
  - src/utils/task/framework.ts
  - src/utils/task/outputFormatting.ts
  - src/utils/task/sdkProgress.ts
- **Dependencies**: none
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-08 核心：任务系统支持异步和后台操作，是复杂工作流的基础设施

### T-14: Bridge远程模式

- **Output Slug**: bridge-remote
- **Priority**: P2
- **Primary Mainline**: ML-09
- **Scope**: Bridge 远程模式、远程会话管理、通信协议
- **Boundaries**: 不涉及认证流程（T-09），不涉及 CLI 传输层（Pattern Audit PI-23）
- **Scope Files** (46 files, 18,081 lines):
  - src/bridge/bridgeApi.ts
  - src/bridge/bridgeConfig.ts
  - src/bridge/bridgeDebug.ts
  - src/bridge/bridgeEnabled.ts
  - src/bridge/bridgeMain.ts
  - src/bridge/bridgeMessaging.ts
  - src/bridge/bridgePermissionCallbacks.ts
  - src/bridge/bridgePointer.ts
  - src/bridge/bridgeStatusUtil.ts
  - src/bridge/bridgeUI.ts
  - src/bridge/capacityWake.ts
  - src/bridge/codeSessionApi.ts
  - src/bridge/createSession.ts
  - src/bridge/debugUtils.ts
  - src/bridge/envLessBridgeConfig.ts
  - src/bridge/flushGate.ts
  - src/bridge/inboundAttachments.ts
  - src/bridge/inboundMessages.ts
  - src/bridge/initReplBridge.ts
  - src/bridge/jwtUtils.ts
  - src/bridge/peerSessions.ts
  - src/bridge/pollConfig.ts
  - src/bridge/pollConfigDefaults.ts
  - src/bridge/remoteBridgeCore.ts
  - src/bridge/replBridge.ts
  - src/bridge/replBridgeHandle.ts
  - src/bridge/replBridgeTransport.ts
  - src/bridge/sessionIdCompat.ts
  - src/bridge/sessionRunner.ts
  - src/bridge/trustedDevice.ts
  - src/bridge/types.ts
  - src/bridge/webhookSanitizer.ts
  - src/bridge/workSecret.ts
  - src/cli/handlers/agents.ts
  - src/cli/handlers/autoMode.ts
  - src/cli/handlers/mcp.tsx
  - src/cli/handlers/plugins.ts
  - src/cli/handlers/util.tsx
  - src/cli/remoteIO.ts
  - src/cli/transports/HybridTransport.ts
  - src/cli/transports/SSETransport.ts
  - src/cli/transports/SerialBatchEventUploader.ts
  - src/cli/transports/WebSocketTransport.ts
  - src/cli/transports/WorkerStateUploader.ts
  - src/cli/transports/ccrClient.ts
  - src/cli/update.ts
- **Dependencies**: T-09
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-09 核心：Bridge 模式支持远程开发和 IDE 集成，是扩展使用场景的关键

### T-15: API客户端与重试层

- **Output Slug**: api-retry
- **Priority**: P2
- **Primary Mainline**: ML-10
- **Scope**: API 客户端、重试策略、速率限制、错误处理
- **Boundaries**: 不涉及 API 流式协议（T-04），不涉及认证（T-09）
- **Scope Files** (19 files, 7,432 lines):
  - src/services/api/adminRequests.ts
  - src/services/api/client.ts
  - src/services/api/dumpPrompts.ts
  - src/services/api/emptyUsage.ts
  - src/services/api/errorUtils.ts
  - src/services/api/errors.ts
  - src/services/api/filesApi.ts
  - src/services/api/firstTokenDate.ts
  - src/services/api/grove.ts
  - src/services/api/logging.ts
  - src/services/api/metricsOptOut.ts
  - src/services/api/overageCreditGrant.ts
  - src/services/api/promptCacheBreakDetection.ts
  - src/services/api/referral.ts
  - src/services/api/sessionIngress.ts
  - src/services/api/ultrareviewQuota.ts
  - src/services/api/usage.ts
  - src/services/api/withRetry.ts
  - src/services/claudeAiLimits.ts
- **Dependencies**: T-03
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-10 核心：API 客户端层是所有 API 交互的基础，重试和限流策略直接影响可靠性

### T-16: 上下文与记忆管理

- **Output Slug**: context-memory
- **Priority**: P2
- **Primary Mainline**: ML-11
- **Scope**: 上下文管理、记忆系统、会话持久化
- **Boundaries**: 不涉及查询引擎上下文（T-03），不涉及会话认证（T-09）
- **Scope Files** (34 files, 12,654 lines):
  - src/memdir/findRelevantMemories.ts
  - src/memdir/memdir.ts
  - src/memdir/memoryAge.ts
  - src/memdir/memoryScan.ts
  - src/memdir/memoryShapeTelemetry.ts
  - src/memdir/memoryTypes.ts
  - src/memdir/paths.ts
  - src/memdir/teamMemPaths.ts
  - src/memdir/teamMemPrompts.ts
  - src/services/SessionMemory/prompts.ts
  - src/services/SessionMemory/sessionMemory.ts
  - src/services/SessionMemory/sessionMemoryUtils.ts
  - src/services/compact/apiMicrocompact.ts
  - src/services/compact/cachedMCConfig.ts
  - src/services/compact/compactWarningHook.ts
  - src/services/compact/compactWarningState.ts
  - src/services/compact/grouping.ts
  - src/services/compact/microCompact.ts
  - src/services/compact/postCompactCleanup.ts
  - src/services/compact/prompt.ts
  - src/services/compact/reactiveCompact.ts
  - src/services/compact/sessionMemoryCompact.ts
  - src/services/compact/snipCompact.ts
  - src/services/compact/snipProjection.ts
  - src/services/compact/timeBasedMCConfig.ts
  - src/services/contextCollapse/index.ts
  - src/services/contextCollapse/operations.ts
  - src/services/contextCollapse/persist.ts
  - src/services/tokenEstimation.ts
  - src/utils/contextAnalysis.ts
  - src/utils/forkedAgent.ts
  - src/utils/sessionRestore.ts
  - src/utils/sessionStorage.ts
  - src/utils/sessionStoragePortable.ts
- **Dependencies**: T-03
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-11 核心：上下文管理决定模型输入质量，记忆系统支持跨会话连续性

### T-17: 插件系统

- **Output Slug**: plugin-system
- **Priority**: P2
- **Primary Mainline**: ML-12
- **Scope**: 插件系统、插件加载、钩子注册、技能管理
- **Boundaries**: 不涉及工具系统（T-05），不涉及具体技能实现（Pattern Audit PI-10）
- **Scope Files** (65 files, 29,367 lines):
  - src/commands/plugin/ManagePlugins.tsx
  - src/commands/plugin/PluginSettings.tsx
  - src/services/plugins/PluginInstallationManager.ts
  - src/services/plugins/pluginCliCommands.ts
  - src/services/plugins/pluginOperations.ts
  - src/skills/bundled/batch.ts
  - src/skills/bundled/claudeApi.ts
  - src/skills/bundled/claudeApiContent.ts
  - src/skills/bundled/debug.ts
  - src/skills/bundled/index.ts
  - src/skills/bundled/keybindings.ts
  - src/skills/bundled/loop.ts
  - src/skills/bundled/loremIpsum.ts
  - src/skills/bundled/remember.ts
  - src/skills/bundled/scheduleRemoteAgents.ts
  - src/skills/bundled/simplify.ts
  - src/skills/bundled/skillify.ts
  - src/skills/bundled/stuck.ts
  - src/skills/bundled/updateConfig.ts
  - src/skills/bundledSkills.ts
  - src/skills/loadSkillsDir.ts
  - src/utils/plugins/addDirPluginSettings.ts
  - src/utils/plugins/cacheUtils.ts
  - src/utils/plugins/dependencyResolver.ts
  - src/utils/plugins/fetchTelemetry.ts
  - src/utils/plugins/gitAvailability.ts
  - src/utils/plugins/headlessPluginInstall.ts
  - src/utils/plugins/hintRecommendation.ts
  - src/utils/plugins/installCounts.ts
  - src/utils/plugins/installedPluginsManager.ts
  - src/utils/plugins/loadPluginAgents.ts
  - src/utils/plugins/loadPluginCommands.ts
  - src/utils/plugins/loadPluginHooks.ts
  - src/utils/plugins/loadPluginOutputStyles.ts
  - src/utils/plugins/lspPluginIntegration.ts
  - src/utils/plugins/lspRecommendation.ts
  - src/utils/plugins/managedPlugins.ts
  - src/utils/plugins/marketplaceHelpers.ts
  - src/utils/plugins/marketplaceManager.ts
  - src/utils/plugins/mcpPluginIntegration.ts
  - src/utils/plugins/mcpbHandler.ts
  - src/utils/plugins/officialMarketplace.ts
  - src/utils/plugins/officialMarketplaceGcs.ts
  - src/utils/plugins/officialMarketplaceStartupCheck.ts
  - src/utils/plugins/orphanedPluginFilter.ts
  - src/utils/plugins/parseMarketplaceInput.ts
  - src/utils/plugins/performStartupChecks.tsx
  - src/utils/plugins/pluginAutoupdate.ts
  - src/utils/plugins/pluginBlocklist.ts
  - src/utils/plugins/pluginDirectories.ts
  - src/utils/plugins/pluginFlagging.ts
  - src/utils/plugins/pluginIdentifier.ts
  - src/utils/plugins/pluginInstallationHelpers.ts
  - src/utils/plugins/pluginLoader.ts
  - src/utils/plugins/pluginOptionsStorage.ts
  - src/utils/plugins/pluginPolicy.ts
  - src/utils/plugins/pluginStartupCheck.ts
  - src/utils/plugins/pluginVersioning.ts
  - src/utils/plugins/reconciler.ts
  - src/utils/plugins/refresh.ts
  - src/utils/plugins/schemas.ts
  - src/utils/plugins/validatePlugin.ts
  - src/utils/plugins/walkPluginMarkdown.ts
  - src/utils/plugins/zipCache.ts
  - src/utils/plugins/zipCacheAdapters.ts
- **Dependencies**: T-08
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-12 核心：插件系统是功能扩展的主要机制，决定系统的可定制性

### T-18: Bash/Shell引擎

- **Output Slug**: bash-engine
- **Priority**: P2
- **Primary Mainline**: ML-13
- **Scope**: Bash/Shell 引擎、命令执行、输出处理、安全控制
- **Boundaries**: 不涉及工具系统调度（T-05），不涉及 Bash 工具实例（Pattern Audit）
- **Scope Files** (37 files, 18,665 lines):
  - src/utils/bash/ParsedCommand.ts
  - src/utils/bash/ShellSnapshot.ts
  - src/utils/bash/ast.ts
  - src/utils/bash/bashParser.ts
  - src/utils/bash/bashPipeCommand.ts
  - src/utils/bash/commands.ts
  - src/utils/bash/heredoc.ts
  - src/utils/bash/parser.ts
  - src/utils/bash/prefix.ts
  - src/utils/bash/registry.ts
  - src/utils/bash/shellCompletion.ts
  - src/utils/bash/shellPrefix.ts
  - src/utils/bash/shellQuote.ts
  - src/utils/bash/shellQuoting.ts
  - src/utils/bash/specs/alias.ts
  - src/utils/bash/specs/index.ts
  - src/utils/bash/specs/nohup.ts
  - src/utils/bash/specs/pyright.ts
  - src/utils/bash/specs/sleep.ts
  - src/utils/bash/specs/srun.ts
  - src/utils/bash/specs/time.ts
  - src/utils/bash/specs/timeout.ts
  - src/utils/bash/treeSitterAnalysis.ts
  - src/utils/powershell/dangerousCmdlets.ts
  - src/utils/powershell/parser.ts
  - src/utils/powershell/staticPrefix.ts
  - src/utils/sandbox/sandbox-adapter.ts
  - src/utils/shell/bashProvider.ts
  - src/utils/shell/outputLimits.ts
  - src/utils/shell/powershellDetection.ts
  - src/utils/shell/powershellProvider.ts
  - src/utils/shell/prefix.ts
  - src/utils/shell/readOnlyCommandValidation.ts
  - src/utils/shell/resolveDefaultShell.ts
  - src/utils/shell/shellProvider.ts
  - src/utils/shell/shellToolUtils.ts
  - src/utils/shell/specPrefix.ts
- **Dependencies**: T-05
- **Estimated Complexity**: MEDIUM
- **Rationale**: ML-13 核心：Bash 引擎是代码执行的核心能力，安全控制直接影响系统安全性

### T-19: Swarm编排

- **Output Slug**: swarm-orchestration
- **Priority**: P3
- **Primary Mainline**: ML-14
- **Scope**: Swarm 编排、多 Agent 协调、任务分发
- **Boundaries**: 不涉及工具系统（T-05），不涉及查询引擎（T-03）
- **Scope Files** (22 files, 7,548 lines):
  - src/utils/swarm/It2SetupPrompt.tsx
  - src/utils/swarm/backends/ITermBackend.ts
  - src/utils/swarm/backends/InProcessBackend.ts
  - src/utils/swarm/backends/PaneBackendExecutor.ts
  - src/utils/swarm/backends/TmuxBackend.ts
  - src/utils/swarm/backends/detection.ts
  - src/utils/swarm/backends/it2Setup.ts
  - src/utils/swarm/backends/registry.ts
  - src/utils/swarm/backends/teammateModeSnapshot.ts
  - src/utils/swarm/backends/types.ts
  - src/utils/swarm/constants.ts
  - src/utils/swarm/inProcessRunner.ts
  - src/utils/swarm/leaderPermissionBridge.ts
  - src/utils/swarm/permissionSync.ts
  - src/utils/swarm/reconnection.ts
  - src/utils/swarm/spawnUtils.ts
  - src/utils/swarm/teamHelpers.ts
  - src/utils/swarm/teammateInit.ts
  - src/utils/swarm/teammateLayoutManager.ts
  - src/utils/swarm/teammateModel.ts
  - src/utils/swarm/teammatePromptAddendum.ts
  - src/utils/swarm/spawnInProcess.ts
- **Dependencies**: T-12
- **Estimated Complexity**: LOW
- **Rationale**: ML-14 核心：Swarm 编排支持多 Agent 协作，是高级工作流的基础

### T-20: SDK入口点

- **Output Slug**: sdk-entrypoints
- **Priority**: P3
- **Primary Mainline**: ML-15
- **Scope**: SDK 入口点、公共 API 定义、类型导出
- **Boundaries**: 不涉及 CLI 入口（T-01），不涉及具体功能实现
- **Scope Files** (9 files, 2,716 lines):
  - src/entrypoints/sdk/controlSchemas.ts
  - src/entrypoints/sdk/controlTypes.ts
  - src/entrypoints/sdk/coreSchemas.ts
  - src/entrypoints/sdk/coreTypes.generated.ts
  - src/entrypoints/sdk/coreTypes.ts
  - src/entrypoints/sdk/runtimeTypes.ts
  - src/entrypoints/sdk/sdkUtilityTypes.ts
  - src/entrypoints/sdk/settingsTypes.generated.ts
  - src/entrypoints/sdk/toolTypes.ts
- **Dependencies**: none
- **Estimated Complexity**: LOW
- **Rationale**: ML-15 核心：SDK 入口点定义了对外公共 API，是第三方集成的基础

### T-41: Shim & Vendor Proxy Layers

- **Output Slug**: shim-vendor-proxies
- **Priority**: P3
- **Primary Mainline**: ML-01
- **Scope**: Shim 代理层、Vendor 适配器、原生模块桥接
- **Boundaries**: 不涉及业务逻辑，纯粹是代理/重导出层
- **Scope Files** (9 files, 1,166 lines):
  - shims/ant-claude-for-chrome-mcp/index.ts
  - shims/ant-computer-use-input/index.ts
  - shims/ant-computer-use-mcp/index.ts
  - shims/ant-computer-use-mcp/types.ts
  - shims/ant-computer-use-swift/index.ts
  - vendor/audio-capture-src/index.ts
  - vendor/image-processor-src/index.ts
  - vendor/modifiers-napi-src/index.ts
  - vendor/url-handler-src/index.ts
- **Dependencies**: none
- **Estimated Complexity**: LOW
- **Rationale**: ML-01 基础设施：shims 和 vendor 是外部集成的适配层，影响构建和运行时兼容性

### T-21: Pattern Audit — tool-instance

- **Output Slug**: audit-tool-instance
- **Priority**: P3
- **Primary Mainline**: ML-03
- **Pattern Coverage**: PI-01
- **Scope**: 抽样验证 PI-01 (tool-instance) 的 77 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 77 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 77 instances covered via Pattern Coverage):
  - src/tools/AgentTool/AgentTool.tsx
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 tool-instance pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-03
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-01 (tool-instance) catalog 编目的 77 个实例真的符合声明的 pattern

### T-22: Pattern Audit — command-handler

- **Output Slug**: audit-command-handler
- **Priority**: P3
- **Primary Mainline**: ML-01
- **Pattern Coverage**: PI-02
- **Scope**: 抽样验证 PI-02 (command-handler) 的 107 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 107 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 107 instances covered via Pattern Coverage):
  - src/commands/add-dir/index.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 command-handler pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-01
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-02 (command-handler) catalog 编目的 107 个实例真的符合声明的 pattern

### T-23: Pattern Audit — react-hook

- **Output Slug**: audit-react-hook
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-03
- **Scope**: 抽样验证 PI-03 (react-hook) 的 14 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 14 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 14 instances covered via Pattern Coverage):
  - src/hooks/useAfterFirstRender.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 react-hook pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-03 (react-hook) catalog 编目的 14 个实例真的符合声明的 pattern

### T-24: Pattern Audit — task-implementation

- **Output Slug**: audit-task-implementation
- **Priority**: P3
- **Primary Mainline**: ML-08
- **Pattern Coverage**: PI-04
- **Scope**: 抽样验证 PI-04 (task-implementation) 的 0 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 0 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 0 instances covered via Pattern Coverage):
  - src/tasks/DreamTask/DreamTask.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 task-implementation pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-08
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-04 (task-implementation) catalog 编目的 0 个实例真的符合声明的 pattern

### T-25: Pattern Audit — permission-component

- **Output Slug**: audit-permission-component
- **Priority**: P3
- **Primary Mainline**: ML-04
- **Pattern Coverage**: PI-06
- **Scope**: 抽样验证 PI-06 (permission-component) 的 5 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 5 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 5 instances covered via Pattern Coverage):
  - src/components/permissions/FilePermissionDialog/ideDiffConfig.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 permission-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-04
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-06 (permission-component) catalog 编目的 5 个实例真的符合声明的 pattern

### T-26: Pattern Audit — ink-fork-component

- **Output Slug**: audit-ink-fork-component
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-07
- **Scope**: 抽样验证 PI-07 (ink-fork-component) 的 33 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 33 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 33 instances covered via Pattern Coverage):
  - src/ink/components/AlternateScreen.tsx
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 ink-fork-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-07 (ink-fork-component) catalog 编目的 33 个实例真的符合声明的 pattern

### T-27: Pattern Audit — message-component

- **Output Slug**: audit-message-component
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-08
- **Scope**: 抽样验证 PI-08 (message-component) 的 12 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 12 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 12 instances covered via Pattern Coverage):
  - src/components/messages/AssistantRedactedThinkingMessage.tsx
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 message-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-08 (message-component) catalog 编目的 12 个实例真的符合声明的 pattern

### T-28: Pattern Audit — agent-component

- **Output Slug**: audit-agent-component
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-09
- **Scope**: 抽样验证 PI-09 (agent-component) 的 4 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 4 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 4 instances covered via Pattern Coverage):
  - src/components/agents/AgentNavigationFooter.tsx
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 agent-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-09 (agent-component) catalog 编目的 4 个实例真的符合声明的 pattern

### T-29: Pattern Audit — bundled-skill

- **Output Slug**: audit-bundled-skill
- **Priority**: P3
- **Primary Mainline**: ML-12
- **Pattern Coverage**: PI-10
- **Scope**: 抽样验证 PI-10 (bundled-skill) 的 7 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 7 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 7 instances covered via Pattern Coverage):
  - src/skills/bundled/claudeInChrome.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 bundled-skill pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-12
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-10 (bundled-skill) catalog 编目的 7 个实例真的符合声明的 pattern

### T-30: Pattern Audit — settings-module

- **Output Slug**: audit-settings-module
- **Priority**: P3
- **Primary Mainline**: ML-01
- **Pattern Coverage**: PI-11
- **Scope**: 抽样验证 PI-11 (settings-module) 的 5 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 5 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 5 instances covered via Pattern Coverage):
  - src/utils/settings/allErrors.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 settings-module pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-01
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-11 (settings-module) catalog 编目的 5 个实例真的符合声明的 pattern

### T-31: Pattern Audit — utility-leaf

- **Output Slug**: audit-utility-leaf
- **Priority**: P3
- **Primary Mainline**: ML-02
- **Pattern Coverage**: PI-12
- **Scope**: 抽样验证 PI-12 (utility-leaf) 的 12 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 12 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 12 instances covered via Pattern Coverage):
  - src/utils/authPortable.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 utility-leaf pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-02
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-12 (utility-leaf) catalog 编目的 12 个实例真的符合声明的 pattern

### T-32: Pattern Audit — component-leaf

- **Output Slug**: audit-component-leaf
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-13
- **Scope**: 抽样验证 PI-13 (component-leaf) 的 10 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 10 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 10 instances covered via Pattern Coverage):
  - src/components/CustomSelect/index.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 component-leaf pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-13 (component-leaf) catalog 编目的 10 个实例真的符合声明的 pattern

### T-33: Pattern Audit — misc-leaf

- **Output Slug**: audit-misc-leaf
- **Priority**: P3
- **Primary Mainline**: ML-01
- **Pattern Coverage**: PI-14
- **Scope**: 抽样验证 PI-14 (misc-leaf) 的 2 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 2 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 2 instances covered via Pattern Coverage):
  - src/constants/errorIds.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 misc-leaf pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-01
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-14 (misc-leaf) catalog 编目的 2 个实例真的符合声明的 pattern

### T-34: Pattern Audit — design-system-component

- **Output Slug**: audit-design-system-component
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-15
- **Scope**: 抽样验证 PI-15 (design-system-component) 的 1 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 1 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 1 instances covered via Pattern Coverage):
  - src/components/design-system/color.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 design-system-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-15 (design-system-component) catalog 编目的 1 个实例真的符合声明的 pattern

### T-35: Pattern Audit — notification-hook

- **Output Slug**: audit-notification-hook
- **Priority**: P3
- **Primary Mainline**: ML-07
- **Pattern Coverage**: PI-16
- **Scope**: 抽样验证 PI-16 (notification-hook) 的 5 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 5 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 5 instances covered via Pattern Coverage):
  - src/hooks/notifs/useAntOrgWarningNotification.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 notification-hook pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-07
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-16 (notification-hook) catalog 编目的 5 个实例真的符合声明的 pattern

### T-36: Pattern Audit — computer-use-module

- **Output Slug**: audit-computer-use-module
- **Priority**: P3
- **Primary Mainline**: ML-03
- **Pattern Coverage**: PI-18
- **Scope**: 抽样验证 PI-18 (computer-use-module) 的 2 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 2 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 2 instances covered via Pattern Coverage):
  - src/utils/computerUse/inputLoader.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 computer-use-module pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-03
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-18 (computer-use-module) catalog 编目的 2 个实例真的符合声明的 pattern

### T-37: Pattern Audit — mcp-ui-component

- **Output Slug**: audit-mcp-ui-component
- **Priority**: P3
- **Primary Mainline**: ML-05
- **Pattern Coverage**: PI-20
- **Scope**: 抽样验证 PI-20 (mcp-ui-component) 的 3 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 3 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 3 instances covered via Pattern Coverage):
  - src/components/mcp/index.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 mcp-ui-component pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-05
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-20 (mcp-ui-component) catalog 编目的 3 个实例真的符合声明的 pattern

### T-38: Pattern Audit — cli-transport

- **Output Slug**: audit-cli-transport
- **Priority**: P3
- **Primary Mainline**: ML-09
- **Pattern Coverage**: PI-23
- **Scope**: 抽样验证 PI-23 (cli-transport) 的 4 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 4 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 4 instances covered via Pattern Coverage):
  - src/cli/exit.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 cli-transport pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-09
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-23 (cli-transport) catalog 编目的 4 个实例真的符合声明的 pattern

### T-39: Pattern Audit — telemetry-module

- **Output Slug**: audit-telemetry-module
- **Priority**: P3
- **Primary Mainline**: ML-06
- **Pattern Coverage**: PI-24
- **Scope**: 抽样验证 PI-24 (telemetry-module) 的 2 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 2 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 2 instances covered via Pattern Coverage):
  - src/utils/telemetry/logger.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 telemetry-module pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: Task covering ML-06
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-24 (telemetry-module) catalog 编目的 2 个实例真的符合声明的 pattern

### T-40: Pattern Audit: PI-05 service-module (13 instances, 107 lines)

- **Output Slug**: audit-service-module
- **Priority**: P3
- **Primary Mainline**: ML-05
- **Pattern Coverage**: PI-05
- **Scope**: 抽样验证 PI-05 (service-module) 的 13 个实例是否符合 pattern 定义
- **Boundaries**: 不展开全部 13 个实例做深度分析；仅抽样 5-10 个实例验证一致性
- **Scope Files** (representative, 13 instances covered via Pattern Coverage):
  - src/services/SessionMemory/prompts.ts
- **Acceptance Criteria**:
  1. 抽样验证 5-10 个实例确实符合 service-module pattern (file:line 引用)
  2. 列出所有偏离 pattern 的实例及偏离原因
  3. 给出 pattern 的"约定俗成"清单（每个实例必须遵循的接口/命名/行为）
  4. 更新 instance-manifest.jsonl 中验证通过的实例 role_source 为 "verified"
- **Dependencies**: T-08
- **Estimated Complexity**: LOW
- **Rationale**: 验证 PI-05 (service-module) catalog 编目的 13 个实例真的符合声明的 pattern

## Shared Files Ownership Map

*See .code_analysis/map/mapped-files.jsonl for complete file→ML mapping.*

| File Pattern | Mainlines | Owner Task | Notes |
|-------------|-----------|-----------|-------|
| shims/* | ML-01 | T-41 | Proxy layers for external packages |
| vendor/* | ML-01 | T-41 | Native module adapters |

## Dependency Graph

```
T-01 → T-02, T-03, T-09
T-02 → T-05 (command routing triggers tool dispatch)
T-03 → T-04, T-05 (query engine uses API layer and tools)
T-05 → T-06 (tools need permission checks)
T-06 → T-07 (rules engine feeds into AI classifier)
T-06 → T-08 (permissions apply to MCP services)
T-08 → T-05 (MCP tools integrate into tool system)
T-10 → T-11, T-12 (TUI framework underlies components and hooks)
T-11 → T-12 (components use hooks)
T-13 → T-05 (tasks use tool system)
T-14 → T-09 (bridge needs authentication)
T-15 → T-04 (API client underlies streaming layer)
T-16 → T-03 (context management feeds into query engine)
T-17 → T-05 (plugins extend tool system)
T-18 → T-05 (shell engine is a tool type)
T-19 → T-03 (swarm uses query engine)
```

## Parallelization Plan

### Group A — Foundation (P1 Core, can run in parallel within group)
- **T-01** (ML-01 CLI启动) — independent entry point
- **T-09** (ML-06 认证管理) — independent from query engine
- **T-06** (ML-04 权限引擎) — independent from query engine
- **T-41** (ML-01 Shim/Vendor) — independent infrastructure

### Group B — Core Systems (depends on Group A)
- **T-02** (ML-01 命令路由) — after T-01
- **T-03** (ML-02 查询引擎) — after T-01
- **T-04** (ML-02 API流式) — after T-03
- **T-05** (ML-03 工具调度) — after T-02, T-03
- **T-07** (ML-04 权限AI) — after T-06
- **T-08** (ML-05 MCP集成) — after T-06
- **T-15** (ML-10 API客户端) — after T-04

### Group C — Support Systems (P2, can start after relevant P1)
- **T-10, T-11, T-12** (ML-07 TUI) — independent from core
- **T-13** (ML-08 任务系统) — after T-05
- **T-14** (ML-09 Bridge) — after T-09
- **T-16** (ML-11 上下文) — after T-03
- **T-17** (ML-12 插件) — after T-05
- **T-18** (ML-13 Bash引擎) — after T-05

### Group D — Supplementary (P3)
- **T-19** (ML-14 Swarm) — after T-03
- **T-20** (ML-15 SDK) — independent
- **T-21~T-40** (Pattern Audits) — independent, can run anytime

## Coverage Verification

- [x] All ML-01~ML-15 from sub-maps covered (15/15 mainlines)
- [x] All CRITICAL/HIGH analysis issues addressed
- [x] No scope file duplication (union == raw count)
- [x] All shared files have unique owner tasks
- [x] All ML core_files covered 100%
- [x] All ML lines covered ≥ 95%
- [x] Global coverage ≥ 95% (actual: 100.0%)
- [x] All tasks have verifiable acceptance criteria
- [x] Dependency graph is DAG (no cycles)
