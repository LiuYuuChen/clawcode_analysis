&lt;!-- analysis-version: 0 | commit: a5179f6588dd03cbe83a8d8b718a61875dba7b24 | updated: 2025-07-14 | mode: full | task: T-02 --&gt;
# T-02 Analysis: 命令路由与REPL启动

## Scope Confirmation
- Task ID: T-02
- Primary Mainline: ML-01
- ML Priority: P1
- Analysis Depth: DEEP
- Secondary Mainlines: ML-02 (print.ts/query interaction), ML-05 (MCP commands), ML-07 (REPL UI), ML-09 (Bridge commands)
- Pattern Coverage: PI-02 (command-handler, 82 catalog files in scope)
- Scope Files (confirmed): 216 files, 57,084 lines, 0 missing
- Scope adjustments: None — all 216 files exist and are readable

### Scope Architecture Groups
| Group | Files | Lines | Core/Supporting |
|-------|-------|-------|----------------|
| Command registry & types | 2 | 970 | Core (DEEP) |
| REPL main loop & I/O | 2 | 6,453 | Core (DEEP) |
| State management | 5 | 991 | Core (DEEP) |
| Session initialization | 1 | 477 | Core (DEEP) |
| Input history | 1 | 464 | Core (DEEP) |
| Keybinding system | 15 | 2,627 | Core (DEEP) |
| Command implementations | 82 | ~24,000 | Supporting (PI-02 catalog) |
| Constants & types | 27 | ~4,500 | Supporting (OVERVIEW) |
| Settings infrastructure | 13 | ~4,200 | Supporting (STANDARD) |
| Chrome integration | 7 | ~2,300 | Supporting (STANDARD) |
| Vim mode | 4 | 957 | Supporting (STANDARD) |
| Remote/Server | 6 | ~1,400 | Supporting (STANDARD) |
| Other supporting | 51 | ~8,700 | Supporting (OVERVIEW/STANDARD) |

## File Roles

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| [`shims/ant-claude-for-chrome-mcp/index.ts`](/src/shims/ant-claude-for-chrome-mcp/index.ts.md) | 113 | Build shim: index | OVERVIEW: § Build Shims |
| [`shims/ant-computer-use-input/index.ts`](/src/shims/ant-computer-use-input/index.ts.md) | 93 | Build shim: index | OVERVIEW: § Build Shims |
| [`shims/ant-computer-use-mcp/index.ts`](/src/shims/ant-computer-use-mcp/index.ts.md) | 195 | Build shim: index | OVERVIEW: § Build Shims |
| [`shims/ant-computer-use-mcp/types.ts`](/src/shims/ant-computer-use-mcp/types.ts.md) | 30 | Build shim: types | OVERVIEW: § Build Shims |
| [`shims/ant-computer-use-swift/index.ts`](/src/shims/ant-computer-use-swift/index.ts.md) | 297 | Build shim: index | OVERVIEW: § Build Shims |
| [`src/assistant/sessionHistory.ts`](/src/src/assistant/sessionHistory.ts.md) | 87 | Session history: persistence and retrieval | STANDARD: § Supporting Modules |
| [`src/buddy/CompanionSprite.tsx`](/src/src/buddy/CompanionSprite.tsx.md) | 371 | Buddy companion: CompanionSpritex | STANDARD: § Buddy Companion |
| [`src/buddy/companion.ts`](/src/src/buddy/companion.ts.md) | 133 | Buddy companion: companion | STANDARD: § Buddy Companion |
| [`src/buddy/prompt.ts`](/src/src/buddy/prompt.ts.md) | 36 | Buddy companion: prompt | STANDARD: § Buddy Companion |
| [`src/buddy/types.ts`](/src/src/buddy/types.ts.md) | 148 | Buddy companion: types | STANDARD: § Buddy Companion |
| [`src/buddy/useBuddyNotification.tsx`](/src/src/buddy/useBuddyNotification.tsx.md) | 98 | Buddy companion: useBuddyNotificationx | STANDARD: § Buddy Companion |
| [`src/cli/print.ts`](/src/src/cli/print.ts.md) | 5594 | REPL main loop: input handling, command dispatch, slash-command routing | DEEP: § Function-Level Analysis |
| [`src/cli/structuredIO.ts`](/src/src/cli/structuredIO.ts.md) | 859 | Structured I/O: terminal escape codes, pasted content management | DEEP: § Function-Level Analysis |
| [`src/commands.ts`](/src/src/commands.ts.md) | 754 | Command registry: loads 70+ commands from 5 sources, filters by availability/enabled | DEEP: § Function-Level Analysis |
| [`src/commands/add-dir/add-dir.tsx`](/src/src/commands/add-dir/add-dir.tsx.md) | 126 | /add-dir command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/add-dir/validation.ts`](/src/src/commands/add-dir/validation.ts.md) | 110 | /add-dir command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/advisor.ts`](/src/src/commands/advisor.ts.md) | 109 | Supporting: advisor | OVERVIEW: § Supporting Modules |
| [`src/commands/branch/branch.ts`](/src/src/commands/branch/branch.ts.md) | 296 | /branch command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/bridge-kick.ts`](/src/src/commands/bridge-kick.ts.md) | 200 | Supporting: bridge-kick | OVERVIEW: § Supporting Modules |
| [`src/commands/bridge/bridge.tsx`](/src/src/commands/bridge/bridge.tsx.md) | 509 | /bridge command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/brief.ts`](/src/src/commands/brief.ts.md) | 130 | Supporting: brief | OVERVIEW: § Supporting Modules |
| [`src/commands/btw/btw.tsx`](/src/src/commands/btw/btw.tsx.md) | 243 | /btw command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/chrome/chrome.tsx`](/src/src/commands/chrome/chrome.tsx.md) | 285 | /chrome command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/clear/caches.ts`](/src/src/commands/clear/caches.ts.md) | 144 | /clear command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/clear/conversation.ts`](/src/src/commands/clear/conversation.ts.md) | 251 | /clear command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/color/color.ts`](/src/src/commands/color/color.ts.md) | 93 | /color command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/commit-push-pr.ts`](/src/src/commands/commit-push-pr.ts.md) | 158 | Supporting: commit-push-pr | OVERVIEW: § Supporting Modules |
| [`src/commands/commit.ts`](/src/src/commands/commit.ts.md) | 92 | Supporting: commit | OVERVIEW: § Supporting Modules |
| [`src/commands/compact/compact.ts`](/src/src/commands/compact/compact.ts.md) | 287 | /compact command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/context/context-noninteractive.ts`](/src/src/commands/context/context-noninteractive.ts.md) | 325 | /context command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/context/context.tsx`](/src/src/commands/context/context.tsx.md) | 64 | /context command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/copy/copy.tsx`](/src/src/commands/copy/copy.tsx.md) | 371 | /copy command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/createMovedToPluginCommand.ts`](/src/src/commands/createMovedToPluginCommand.ts.md) | 65 | Supporting: createMovedToPluginCommand | OVERVIEW: § Supporting Modules |
| [`src/commands/effort/effort.tsx`](/src/src/commands/effort/effort.tsx.md) | 183 | /effort command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/export/export.tsx`](/src/src/commands/export/export.tsx.md) | 91 | /export command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/extra-usage/extra-usage-core.ts`](/src/src/commands/extra-usage/extra-usage-core.ts.md) | 118 | /extra-usage command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/fast/fast.tsx`](/src/src/commands/fast/fast.tsx.md) | 269 | /fast command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/help/index.ts`](/src/src/commands/help/index.ts.md) | 10 | /help command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/ide/ide.tsx`](/src/src/commands/ide/ide.tsx.md) | 646 | /ide command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/init-verifiers.ts`](/src/src/commands/init-verifiers.ts.md) | 262 | Supporting: init-verifiers | OVERVIEW: § Supporting Modules |
| [`src/commands/init.ts`](/src/src/commands/init.ts.md) | 256 | Supporting: init | OVERVIEW: § Supporting Modules |
| [`src/commands/insights.ts`](/src/src/commands/insights.ts.md) | 3200 | Supporting: insights | OVERVIEW: § Supporting Modules |
| [`src/commands/install-github-app/ApiKeyStep.tsx`](/src/src/commands/install-github-app/ApiKeyStep.tsx.md) | 231 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/CheckExistingSecretStep.tsx`](/src/src/commands/install-github-app/CheckExistingSecretStep.tsx.md) | 190 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/ChooseRepoStep.tsx`](/src/src/commands/install-github-app/ChooseRepoStep.tsx.md) | 211 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/CreatingStep.tsx`](/src/src/commands/install-github-app/CreatingStep.tsx.md) | 65 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/ErrorStep.tsx`](/src/src/commands/install-github-app/ErrorStep.tsx.md) | 85 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/ExistingWorkflowStep.tsx`](/src/src/commands/install-github-app/ExistingWorkflowStep.tsx.md) | 103 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/InstallAppStep.tsx`](/src/src/commands/install-github-app/InstallAppStep.tsx.md) | 94 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/OAuthFlowStep.tsx`](/src/src/commands/install-github-app/OAuthFlowStep.tsx.md) | 276 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/SuccessStep.tsx`](/src/src/commands/install-github-app/SuccessStep.tsx.md) | 96 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/WarningsStep.tsx`](/src/src/commands/install-github-app/WarningsStep.tsx.md) | 73 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/install-github-app.tsx`](/src/src/commands/install-github-app/install-github-app.tsx.md) | 587 | /install-github-app command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install-github-app/setupGitHubActions.ts`](/src/src/commands/install-github-app/setupGitHubActions.ts.md) | 325 | /install-github-app command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/install.tsx`](/src/src/commands/install.tsx.md) | 300 | Supporting: installx | OVERVIEW: § Supporting Modules |
| [`src/commands/keybindings/keybindings.ts`](/src/src/commands/keybindings/keybindings.ts.md) | 53 | /keybindings command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/logout/logout.tsx`](/src/src/commands/logout/logout.tsx.md) | 82 | /logout command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/mcp/addCommand.ts`](/src/src/commands/mcp/addCommand.ts.md) | 280 | /mcp command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/mcp/mcp.tsx`](/src/src/commands/mcp/mcp.tsx.md) | 85 | /mcp command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/mcp/xaaIdpCommand.ts`](/src/src/commands/mcp/xaaIdpCommand.ts.md) | 266 | /mcp command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/memory/memory.tsx`](/src/src/commands/memory/memory.tsx.md) | 90 | /memory command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/mobile/mobile.tsx`](/src/src/commands/mobile/mobile.tsx.md) | 274 | /mobile command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/model/model.tsx`](/src/src/commands/model/model.tsx.md) | 297 | /model command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plan/plan.tsx`](/src/src/commands/plan/plan.tsx.md) | 122 | /plan command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/AddMarketplace.tsx`](/src/src/commands/plugin/AddMarketplace.tsx.md) | 162 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/BrowseMarketplace.tsx`](/src/src/commands/plugin/BrowseMarketplace.tsx.md) | 802 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/DiscoverPlugins.tsx`](/src/src/commands/plugin/DiscoverPlugins.tsx.md) | 781 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/ManageMarketplaces.tsx`](/src/src/commands/plugin/ManageMarketplaces.tsx.md) | 838 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/PluginErrors.tsx`](/src/src/commands/plugin/PluginErrors.tsx.md) | 124 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/PluginOptionsDialog.tsx`](/src/src/commands/plugin/PluginOptionsDialog.tsx.md) | 357 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/PluginOptionsFlow.tsx`](/src/src/commands/plugin/PluginOptionsFlow.tsx.md) | 135 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/UnifiedInstalledCell.tsx`](/src/src/commands/plugin/UnifiedInstalledCell.tsx.md) | 565 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/ValidatePlugin.tsx`](/src/src/commands/plugin/ValidatePlugin.tsx.md) | 98 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/parseArgs.ts`](/src/src/commands/plugin/parseArgs.ts.md) | 103 | /plugin command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/pluginDetailsHelpers.tsx`](/src/src/commands/plugin/pluginDetailsHelpers.tsx.md) | 117 | /plugin command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/plugin/usePagination.ts`](/src/src/commands/plugin/usePagination.ts.md) | 171 | /plugin command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/privacy-settings/privacy-settings.tsx`](/src/src/commands/privacy-settings/privacy-settings.tsx.md) | 58 | /privacy-settings command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/rate-limit-options/rate-limit-options.tsx`](/src/src/commands/rate-limit-options/rate-limit-options.tsx.md) | 210 | /rate-limit-options command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/reload-plugins/reload-plugins.ts`](/src/src/commands/reload-plugins/reload-plugins.ts.md) | 61 | /reload-plugins command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/remote-setup/api.ts`](/src/src/commands/remote-setup/api.ts.md) | 182 | /remote-setup command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/remote-setup/remote-setup.tsx`](/src/src/commands/remote-setup/remote-setup.tsx.md) | 187 | /remote-setup command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/rename/generateSessionName.ts`](/src/src/commands/rename/generateSessionName.ts.md) | 67 | /rename command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/rename/rename.ts`](/src/src/commands/rename/rename.ts.md) | 87 | /rename command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/resume/resume.tsx`](/src/src/commands/resume/resume.tsx.md) | 275 | /resume command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/review.ts`](/src/src/commands/review.ts.md) | 57 | Supporting: review | OVERVIEW: § Supporting Modules |
| [`src/commands/review/UltrareviewOverageDialog.tsx`](/src/src/commands/review/UltrareviewOverageDialog.tsx.md) | 96 | /review command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/review/reviewRemote.ts`](/src/src/commands/review/reviewRemote.ts.md) | 316 | /review command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/review/ultrareviewCommand.tsx`](/src/src/commands/review/ultrareviewCommand.tsx.md) | 58 | /review command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/sandbox-toggle/sandbox-toggle.tsx`](/src/src/commands/sandbox-toggle/sandbox-toggle.tsx.md) | 83 | /sandbox-toggle command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/security-review.ts`](/src/src/commands/security-review.ts.md) | 243 | Supporting: security-review | OVERVIEW: § Supporting Modules |
| [`src/commands/tag/tag.tsx`](/src/src/commands/tag/tag.tsx.md) | 215 | /tag command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/terminalSetup/terminalSetup.tsx`](/src/src/commands/terminalSetup/terminalSetup.tsx.md) | 531 | /terminalSetup command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/theme/theme.tsx`](/src/src/commands/theme/theme.tsx.md) | 57 | /theme command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/thinkback/thinkback.tsx`](/src/src/commands/thinkback/thinkback.tsx.md) | 554 | /thinkback command (local-jsx) | OVERVIEW: § Command Pattern Catalog |
| [`src/commands/ultraplan.tsx`](/src/src/commands/ultraplan.tsx.md) | 471 | Supporting: ultraplanx | OVERVIEW: § Supporting Modules |
| [`src/commands/voice/voice.ts`](/src/src/commands/voice/voice.ts.md) | 150 | /voice command (local/prompt) | OVERVIEW: § Command Pattern Catalog |
| [`src/constants/apiLimits.ts`](/src/src/constants/apiLimits.ts.md) | 94 | Constants: apiLimits | OVERVIEW: § Constants |
| [`src/constants/betas.ts`](/src/src/constants/betas.ts.md) | 52 | Constants: betas | OVERVIEW: § Constants |
| [`src/constants/common.ts`](/src/src/constants/common.ts.md) | 33 | Constants: common | OVERVIEW: § Constants |
| [`src/constants/cyberRiskInstruction.ts`](/src/src/constants/cyberRiskInstruction.ts.md) | 24 | Constants: cyberRiskInstruction | OVERVIEW: § Constants |
| [`src/constants/figures.ts`](/src/src/constants/figures.ts.md) | 45 | Constants: figures | OVERVIEW: § Constants |
| [`src/constants/files.ts`](/src/src/constants/files.ts.md) | 156 | Constants: files | OVERVIEW: § Constants |
| [`src/constants/github-app.ts`](/src/src/constants/github-app.ts.md) | 144 | Constants: github-app | OVERVIEW: § Constants |
| [`src/constants/outputStyles.ts`](/src/src/constants/outputStyles.ts.md) | 216 | Constants: outputStyles | OVERVIEW: § Constants |
| [`src/constants/product.ts`](/src/src/constants/product.ts.md) | 76 | Constants: product | OVERVIEW: § Constants |
| [`src/constants/prompts.ts`](/src/src/constants/prompts.ts.md) | 914 | Constants: prompts | OVERVIEW: § Constants |
| [`src/constants/spinnerVerbs.ts`](/src/src/constants/spinnerVerbs.ts.md) | 204 | Constants: spinnerVerbs | OVERVIEW: § Constants |
| [`src/constants/system.ts`](/src/src/constants/system.ts.md) | 95 | Constants: system | OVERVIEW: § Constants |
| [`src/constants/systemPromptSections.ts`](/src/src/constants/systemPromptSections.ts.md) | 68 | Constants: systemPromptSections | OVERVIEW: § Constants |
| [`src/constants/toolLimits.ts`](/src/src/constants/toolLimits.ts.md) | 56 | Constants: toolLimits | OVERVIEW: § Constants |
| [`src/constants/xml.ts`](/src/src/constants/xml.ts.md) | 86 | Constants: xml | OVERVIEW: § Constants |
| [`src/context/QueuedMessageContext.tsx`](/src/src/context/QueuedMessageContext.tsx.md) | 63 | React context: QueuedMessageContextx | STANDARD: § React Contexts |
| [`src/context/mailbox.tsx`](/src/src/context/mailbox.tsx.md) | 38 | React context: mailboxx | STANDARD: § React Contexts |
| [`src/context/modalContext.tsx`](/src/src/context/modalContext.tsx.md) | 58 | React context: modalContextx | STANDARD: § React Contexts |
| [`src/context/overlayContext.tsx`](/src/src/context/overlayContext.tsx.md) | 151 | React context: overlayContextx | STANDARD: § React Contexts |
| [`src/context/promptOverlayContext.tsx`](/src/src/context/promptOverlayContext.tsx.md) | 125 | React context: promptOverlayContextx | STANDARD: § React Contexts |
| [`src/context/stats.tsx`](/src/src/context/stats.tsx.md) | 220 | React context: statsx | STANDARD: § React Contexts |
| [`src/context/voice.tsx`](/src/src/context/voice.tsx.md) | 88 | React context: voicex | STANDARD: § React Contexts |
| [`src/coordinator/coordinatorMode.ts`](/src/src/coordinator/coordinatorMode.ts.md) | 369 | Coordinator mode: multi-agent dispatch | STANDARD: § Supporting Modules |
| [`src/cost-tracker.ts`](/src/src/cost-tracker.ts.md) | 323 | Cost tracker: API cost accumulation per session | STANDARD: § Supporting Modules |
| [`src/costHook.ts`](/src/src/costHook.ts.md) | 22 | Cost hook: cost tracker ↔ query engine bridge | STANDARD: § Supporting Modules |
| [`src/dev-entry.ts`](/src/src/dev-entry.ts.md) | 122 | Dev entry: alternative bootstrap | STANDARD: § Supporting Modules |
| [`src/dialogLaunchers.tsx`](/src/src/dialogLaunchers.tsx.md) | 133 | Dialog launchers: Ink UI dialog utilities | STANDARD: § Supporting Modules |
| [`src/history.ts`](/src/src/history.ts.md) | 464 | Input history: paste ref parsing, reverse line reading, lock-based access | DEEP: § Function-Level Analysis |
| [`src/interactiveHelpers.tsx`](/src/src/interactiveHelpers.tsx.md) | 366 | Interactive helpers: REPL UI components | STANDARD: § Supporting Modules |
| [`src/keybindings/KeybindingContext.tsx`](/src/src/keybindings/KeybindingContext.tsx.md) | 243 | React Context: resolved keybindings tree | DEEP: § Function-Level Analysis |
| [`src/keybindings/defaultBindings.ts`](/src/src/keybindings/defaultBindings.ts.md) | 340 | Default keybindings: action-to-keystroke mapping | DEEP: § Function-Level Analysis |
| [`src/keybindings/loadUserBindings.ts`](/src/src/keybindings/loadUserBindings.ts.md) | 472 | User bindings: read ~/.claude/keybindings.json | DEEP: § Function-Level Analysis |
| [`src/keybindings/match.ts`](/src/src/keybindings/match.ts.md) | 120 | Key matcher: modifier-aware binding matching | DEEP: § Function-Level Analysis |
| [`src/keybindings/parser.ts`](/src/src/keybindings/parser.ts.md) | 203 | Keystroke parser: string to ParsedKeystroke | DEEP: § Function-Level Analysis |
| [`src/keybindings/reservedShortcuts.ts`](/src/src/keybindings/reservedShortcuts.ts.md) | 127 | Reserved: system shortcuts that cannot be overridden | DEEP: § Function-Level Analysis |
| [`src/keybindings/resolver.ts`](/src/src/keybindings/resolver.ts.md) | 244 | Key resolver: resolveKey() last-match-wins | DEEP: § Function-Level Analysis |
| [`src/keybindings/schema.ts`](/src/src/keybindings/schema.ts.md) | 236 | Keybinding JSON schema for config validation | DEEP: § Function-Level Analysis |
| [`src/keybindings/template.ts`](/src/src/keybindings/template.ts.md) | 52 | Keybinding templates: reusable patterns | DEEP: § Function-Level Analysis |
| [`src/keybindings/useKeybinding.ts`](/src/src/keybindings/useKeybinding.ts.md) | 196 | React hook: registers keybindings per lifecycle | DEEP: § Function-Level Analysis |
| [`src/keybindings/validate.ts`](/src/src/keybindings/validate.ts.md) | 498 | Validator: conflict detection, context validation | DEEP: § Function-Level Analysis |
| [`src/migrations/migrateAutoUpdatesToSettings.ts`](/src/src/migrations/migrateAutoUpdatesToSettings.ts.md) | 61 | Migration: migrateAutoUpdatesToSettings | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateEnableAllProjectMcpServersToSettings.ts`](/src/src/migrations/migrateEnableAllProjectMcpServersToSettings.ts.md) | 118 | Migration: migrateEnableAllProjectMcpServersToSettings | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateFennecToOpus.ts`](/src/src/migrations/migrateFennecToOpus.ts.md) | 45 | Migration: migrateFennecToOpus | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateLegacyOpusToCurrent.ts`](/src/src/migrations/migrateLegacyOpusToCurrent.ts.md) | 57 | Migration: migrateLegacyOpusToCurrent | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateOpusToOpus1m.ts`](/src/src/migrations/migrateOpusToOpus1m.ts.md) | 43 | Migration: migrateOpusToOpus1m | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateReplBridgeEnabledToRemoteControlAtStartup.ts`](/src/src/migrations/migrateReplBridgeEnabledToRemoteControlAtStartup.ts.md) | 22 | Migration: migrateReplBridgeEnabledToRemoteControlAtStartup | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateSonnet1mToSonnet45.ts`](/src/src/migrations/migrateSonnet1mToSonnet45.ts.md) | 48 | Migration: migrateSonnet1mToSonnet45 | OVERVIEW: § Settings Migrations |
| [`src/migrations/migrateSonnet45ToSonnet46.ts`](/src/src/migrations/migrateSonnet45ToSonnet46.ts.md) | 67 | Migration: migrateSonnet45ToSonnet46 | OVERVIEW: § Settings Migrations |
| [`src/migrations/resetAutoModeOptInForDefaultOffer.ts`](/src/src/migrations/resetAutoModeOptInForDefaultOffer.ts.md) | 51 | Migration: resetAutoModeOptInForDefaultOffer | OVERVIEW: § Settings Migrations |
| [`src/migrations/resetProToOpusDefault.ts`](/src/src/migrations/resetProToOpusDefault.ts.md) | 51 | Migration: resetProToOpusDefault | OVERVIEW: § Settings Migrations |
| [`src/moreright/useMoreRight.tsx`](/src/src/moreright/useMoreRight.tsx.md) | 26 | More-right panel: collapsible side panel | STANDARD: § Supporting Modules |
| [`src/outputStyles/loadOutputStylesDir.ts`](/src/src/outputStyles/loadOutputStylesDir.ts.md) | 98 | Output style loader: custom .claude/ styles | STANDARD: § Supporting Modules |
| [`src/plugins/builtinPlugins.ts`](/src/src/plugins/builtinPlugins.ts.md) | 159 | Builtin plugins: registry | STANDARD: § Supporting Modules |
| [`src/plugins/bundled/index.ts`](/src/src/plugins/bundled/index.ts.md) | 23 | Bundled plugins: loading and registration | STANDARD: § Supporting Modules |
| [`src/proactive/index.ts`](/src/src/proactive/index.ts.md) | 57 | Proactive mode: feature-gated assistance entry | STANDARD: § Supporting Modules |
| [`src/projectOnboardingState.ts`](/src/src/projectOnboardingState.ts.md) | 83 | Onboarding state: first-run tracking | STANDARD: § Supporting Modules |
| [`src/query/tokenBudget.ts`](/src/src/query/tokenBudget.ts.md) | 93 | Token budget: context window calculation | STANDARD: § Supporting Modules |
| [`src/remote/RemoteSessionManager.ts`](/src/src/remote/RemoteSessionManager.ts.md) | 343 | Remote session: RemoteSessionManager | STANDARD: § Remote Infrastructure |
| [`src/remote/SessionsWebSocket.ts`](/src/src/remote/SessionsWebSocket.ts.md) | 404 | Remote session: SessionsWebSocket | STANDARD: § Remote Infrastructure |
| [`src/remote/sdkMessageAdapter.ts`](/src/src/remote/sdkMessageAdapter.ts.md) | 302 | Remote session: sdkMessageAdapter | STANDARD: § Remote Infrastructure |
| [`src/schemas/hooks.ts`](/src/src/schemas/hooks.ts.md) | 222 | Hook schemas: Zod validation for hook config | STANDARD: § Supporting Modules |
| [`src/screens/ResumeConversation.tsx`](/src/src/screens/ResumeConversation.tsx.md) | 399 | Resume screen: session selection UI | STANDARD: § Supporting Modules |
| [`src/server/createDirectConnectSession.ts`](/src/src/server/createDirectConnectSession.ts.md) | 88 | Server: createDirectConnectSession | STANDARD: § Server Infrastructure |
| [`src/server/directConnectManager.ts`](/src/src/server/directConnectManager.ts.md) | 213 | Server: directConnectManager | STANDARD: § Server Infrastructure |
| [`src/server/types.ts`](/src/src/server/types.ts.md) | 57 | Server: types | STANDARD: § Server Infrastructure |
| [`src/setup.ts`](/src/src/setup.ts.md) | 477 | Session init: Node check, UDS, worktree, prefetch, safety check | DEEP: § Function-Level Analysis |
| [`src/state/AppStateStore.ts`](/src/src/state/AppStateStore.ts.md) | 569 | Global app state: 60+ fields (settings/permissions/MCP/bridge/speculation) | DEEP: § Function-Level Analysis |
| [`src/state/onChangeAppState.ts`](/src/src/state/onChangeAppState.ts.md) | 171 | State side-effects: permission sync, model persist, cache clear | DEEP: § Function-Level Analysis |
| [`src/state/selectors.ts`](/src/src/state/selectors.ts.md) | 76 | State selectors: typed AppState accessors | DEEP: § Function-Level Analysis |
| [`src/state/store.ts`](/src/src/state/store.ts.md) | 34 | Minimal reactive store: createStore&lt;T&gt; with listener pattern | DEEP: § Function-Level Analysis |
| [`src/state/teammateViewHelpers.ts`](/src/src/state/teammateViewHelpers.ts.md) | 141 | Teammate view helpers: mode resolution for multi-agent | DEEP: § Function-Level Analysis |
| [`src/types/command.ts`](/src/src/types/command.ts.md) | 216 | Command type system: Prompt/Local/LocalJSX union with CommandBase | DEEP: § Function-Level Analysis |
| [`src/types/generated/events_mono/claude_code/v1/claude_code_internal_event.ts`](/src/src/types/generated/events_mono/claude_code/v1/claude_code_internal_event.ts.md) | 865 | Type definitions: claude_code_internal_event | OVERVIEW: § Type System |
| [`src/types/generated/events_mono/common/v1/auth.ts`](/src/src/types/generated/events_mono/common/v1/auth.ts.md) | 100 | Type definitions: auth | OVERVIEW: § Type System |
| [`src/types/generated/events_mono/growthbook/v1/growthbook_experiment_event.ts`](/src/src/types/generated/events_mono/growthbook/v1/growthbook_experiment_event.ts.md) | 223 | Type definitions: growthbook_experiment_event | OVERVIEW: § Type System |
| [`src/types/generated/google/protobuf/timestamp.ts`](/src/src/types/generated/google/protobuf/timestamp.ts.md) | 187 | Type definitions: timestamp | OVERVIEW: § Type System |
| [`src/types/hooks.ts`](/src/src/types/hooks.ts.md) | 290 | Type definitions: hooks | OVERVIEW: § Type System |
| [`src/types/ids.ts`](/src/src/types/ids.ts.md) | 44 | Type definitions: ids | OVERVIEW: § Type System |
| [`src/types/logs.ts`](/src/src/types/logs.ts.md) | 330 | Type definitions: logs | OVERVIEW: § Type System |
| [`src/types/message.ts`](/src/src/types/message.ts.md) | 134 | Type definitions: message | OVERVIEW: § Type System |
| [`src/types/permissions.ts`](/src/src/types/permissions.ts.md) | 441 | Type definitions: permissions | OVERVIEW: § Type System |
| [`src/types/plugin.ts`](/src/src/types/plugin.ts.md) | 363 | Type definitions: plugin | OVERVIEW: § Type System |
| [`src/types/textInputTypes.ts`](/src/src/types/textInputTypes.ts.md) | 387 | Type definitions: textInputTypes | OVERVIEW: § Type System |
| [`src/upstreamproxy/relay.ts`](/src/src/upstreamproxy/relay.ts.md) | 455 | Upstream proxy relay: HTTP proxy for API | STANDARD: § Supporting Modules |
| [`src/upstreamproxy/upstreamproxy.ts`](/src/src/upstreamproxy/upstreamproxy.ts.md) | 285 | Upstream proxy: config and lifecycle | STANDARD: § Supporting Modules |
| [`src/utils/claudeInChrome/chromeNativeHost.ts`](/src/src/utils/claudeInChrome/chromeNativeHost.ts.md) | 527 | Chrome integration: chromeNativeHost | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/common.ts`](/src/src/utils/claudeInChrome/common.ts.md) | 540 | Chrome integration: common | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/mcpServer.ts`](/src/src/utils/claudeInChrome/mcpServer.ts.md) | 293 | Chrome integration: mcpServer | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/prompt.ts`](/src/src/utils/claudeInChrome/prompt.ts.md) | 83 | Chrome integration: prompt | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/setup.ts`](/src/src/utils/claudeInChrome/setup.ts.md) | 400 | Chrome integration: setup | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/setupPortable.ts`](/src/src/utils/claudeInChrome/setupPortable.ts.md) | 233 | Chrome integration: setupPortable | STANDARD: § Chrome Integration |
| [`src/utils/claudeInChrome/toolRendering.tsx`](/src/src/utils/claudeInChrome/toolRendering.tsx.md) | 262 | Chrome integration: toolRenderingx | STANDARD: § Chrome Integration |
| [`src/utils/config.ts`](/src/src/utils/config.ts.md) | 1817 | Utility: config | STANDARD: § Utility Functions |
| [`src/utils/earlyInput.ts`](/src/src/utils/earlyInput.ts.md) | 191 | Utility: earlyInput | STANDARD: § Utility Functions |
| [`src/utils/settings/applySettingsChange.ts`](/src/src/utils/settings/applySettingsChange.ts.md) | 92 | Settings: applySettingsChange | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/changeDetector.ts`](/src/src/utils/settings/changeDetector.ts.md) | 488 | Settings: changeDetector | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/constants.ts`](/src/src/utils/settings/constants.ts.md) | 202 | Settings: constants | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/mdm/constants.ts`](/src/src/utils/settings/mdm/constants.ts.md) | 81 | Settings: constants | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/mdm/rawRead.ts`](/src/src/utils/settings/mdm/rawRead.ts.md) | 130 | Settings: rawRead | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/mdm/settings.ts`](/src/src/utils/settings/mdm/settings.ts.md) | 316 | Settings: settings | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/permissionValidation.ts`](/src/src/utils/settings/permissionValidation.ts.md) | 262 | Settings: permissionValidation | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/pluginOnlyPolicy.ts`](/src/src/utils/settings/pluginOnlyPolicy.ts.md) | 60 | Settings: pluginOnlyPolicy | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/settings.ts`](/src/src/utils/settings/settings.ts.md) | 1015 | Settings: settings | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/settingsCache.ts`](/src/src/utils/settings/settingsCache.ts.md) | 80 | Settings: settingsCache | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/toolValidationConfig.ts`](/src/src/utils/settings/toolValidationConfig.ts.md) | 103 | Settings: toolValidationConfig | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/types.ts`](/src/src/utils/settings/types.ts.md) | 1148 | Settings: types | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/validation.ts`](/src/src/utils/settings/validation.ts.md) | 265 | Settings: validation | STANDARD: § Settings Infrastructure |
| [`src/utils/settings/validationTips.ts`](/src/src/utils/settings/validationTips.ts.md) | 164 | Settings: validationTips | STANDARD: § Settings Infrastructure |
| [`src/utils/sinks.ts`](/src/src/utils/sinks.ts.md) | 16 | Utility: sinks | STANDARD: § Utility Functions |
| [`src/utils/startupProfiler.ts`](/src/src/utils/startupProfiler.ts.md) | 194 | Utility: startupProfiler | STANDARD: § Utility Functions |
| [`src/utils/warningHandler.ts`](/src/src/utils/warningHandler.ts.md) | 121 | Utility: warningHandler | STANDARD: § Utility Functions |
| [`src/vim/motions.ts`](/src/src/vim/motions.ts.md) | 82 | Vim mode: motions | STANDARD: § Vim Mode |
| [`src/vim/textObjects.ts`](/src/src/vim/textObjects.ts.md) | 186 | Vim mode: textObjects | STANDARD: § Vim Mode |
| [`src/vim/transitions.ts`](/src/src/vim/transitions.ts.md) | 490 | Vim mode: transitions | STANDARD: § Vim Mode |
| [`src/vim/types.ts`](/src/src/vim/types.ts.md) | 199 | Vim mode: types | STANDARD: § Vim Mode |
| [`src/voice/voiceModeEnabled.ts`](/src/src/voice/voiceModeEnabled.ts.md) | 54 | Voice mode: feature flag check | STANDARD: § Supporting Modules |
| [`vendor/audio-capture-src/index.ts`](/src/vendor/audio-capture-src/index.ts.md) | 151 | Vendor native addon: index | OVERVIEW: § Vendor Addons |
| [`vendor/image-processor-src/index.ts`](/src/vendor/image-processor-src/index.ts.md) | 163 | Vendor native addon: index | OVERVIEW: § Vendor Addons |
| [`vendor/modifiers-napi-src/index.ts`](/src/vendor/modifiers-napi-src/index.ts.md) | 67 | Vendor native addon: index | OVERVIEW: § Vendor Addons |
| [`vendor/url-handler-src/index.ts`](/src/vendor/url-handler-src/index.ts.md) | 58 | Vendor native addon: index | OVERVIEW: § Vendor Addons |
