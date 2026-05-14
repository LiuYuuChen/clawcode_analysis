# Source ↔ Report Mapping

## Overview

- **Total files**: 1954
- **Mainlines**: 34
- **Summaries**: 5

## ML-01 (345 files)

📋 **Summary**: [summary-ML-01-cli-entry-routing](/branches/main/report/summary-ML-01-cli-entry-routing)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `shims/ant-claude-for-chrome-mcp/index.ts` | 113 | PI-14 | LOW |
| 2 | `shims/ant-computer-use-input/index.ts` | 93 | PI-14 | LOW |
| 3 | `shims/ant-computer-use-mcp/index.ts` | 195 | PI-14 | LOW |
| 4 | `shims/ant-computer-use-mcp/types.ts` | 30 | PI-14 | LOW |
| 5 | `shims/ant-computer-use-swift/index.ts` | 297 | PI-14 | MEDIUM |
| 6 | `src/assistant/sessionHistory.ts` | 87 | PI-14 | LOW |
| 7 | `src/bootstrap-entry.ts` | 5 |  | LOW |
| 8 | `src/bootstrap/state.ts` | 1758 |  | HIGH |
| 9 | `src/bootstrapMacro.ts` | 29 |  | LOW |
| 10 | `src/buddy/CompanionSprite.tsx` | 370 | PI-14 | MEDIUM |
| 11 | `src/buddy/companion.ts` | 133 | PI-14 | LOW |
| 12 | `src/buddy/prompt.ts` | 36 | PI-14 | LOW |
| 13 | `src/buddy/types.ts` | 148 | PI-14 | LOW |
| 14 | `src/buddy/useBuddyNotification.tsx` | 97 | PI-14 | LOW |
| 15 | `src/cli/print.ts` | 5594 |  | HIGH |
| 16 | `src/cli/structuredIO.ts` | 859 |  | MEDIUM |
| 17 | `src/commands.ts` | 754 |  | MEDIUM |
| 18 | `src/commands/add-dir/add-dir.tsx` | 126 |  | LOW |
| 19 | `src/commands/add-dir/index.ts` | 11 | PI-02 | LOW |
| 20 | `src/commands/add-dir/validation.ts` | 110 |  | LOW |
| 21 | `src/commands/advisor.ts` | 109 |  | LOW |
| 22 | `src/commands/agents-platform/index.ts` | 21 | PI-02 | LOW |
| 23 | `src/commands/agents/agents.tsx` | 12 | PI-02 | LOW |
| 24 | `src/commands/agents/index.ts` | 10 | PI-02 | LOW |
| 25 | `src/commands/branch/branch.ts` | 296 |  | MEDIUM |
| 26 | `src/commands/branch/index.ts` | 14 | PI-02 | LOW |
| 27 | `src/commands/bridge-kick.ts` | 200 |  | LOW |
| 28 | `src/commands/bridge/bridge.tsx` | 509 |  | MEDIUM |
| 29 | `src/commands/bridge/index.ts` | 26 | PI-02 | LOW |
| 30 | `src/commands/brief.ts` | 130 |  | LOW |
| 31 | `src/commands/btw/btw.tsx` | 243 |  | MEDIUM |
| 32 | `src/commands/btw/index.ts` | 13 | PI-02 | LOW |
| 33 | `src/commands/chrome/chrome.tsx` | 285 |  | MEDIUM |
| 34 | `src/commands/chrome/index.ts` | 13 | PI-02 | LOW |
| 35 | `src/commands/clear/caches.ts` | 144 |  | LOW |
| 36 | `src/commands/clear/clear.ts` | 7 | PI-02 | LOW |
| 37 | `src/commands/clear/conversation.ts` | 251 |  | MEDIUM |
| 38 | `src/commands/clear/index.ts` | 19 | PI-02 | LOW |
| 39 | `src/commands/color/color.ts` | 93 |  | LOW |
| 40 | `src/commands/color/index.ts` | 16 | PI-02 | LOW |
| 41 | `src/commands/commit-push-pr.ts` | 158 |  | LOW |
| 42 | `src/commands/commit.ts` | 92 |  | LOW |
| 43 | `src/commands/compact/compact.ts` | 287 |  | MEDIUM |
| 44 | `src/commands/compact/index.ts` | 15 | PI-02 | LOW |
| 45 | `src/commands/config/config.tsx` | 7 | PI-02 | LOW |
| 46 | `src/commands/config/index.ts` | 11 | PI-02 | LOW |
| 47 | `src/commands/context/context-noninteractive.ts` | 325 |  | MEDIUM |
| 48 | `src/commands/context/context.tsx` | 64 |  | LOW |
| 49 | `src/commands/context/index.ts` | 24 | PI-02 | LOW |
| 50 | `src/commands/copy/copy.tsx` | 371 |  | MEDIUM |
| 51 | `src/commands/copy/index.ts` | 15 | PI-02 | LOW |
| 52 | `src/commands/cost/cost.ts` | 24 | PI-02 | LOW |
| 53 | `src/commands/cost/index.ts` | 23 | PI-02 | LOW |
| 54 | `src/commands/createMovedToPluginCommand.ts` | 65 |  | LOW |
| 55 | `src/commands/desktop/desktop.tsx` | 9 | PI-02 | LOW |
| 56 | `src/commands/desktop/index.ts` | 26 | PI-02 | LOW |
| 57 | `src/commands/diff/diff.tsx` | 9 | PI-02 | LOW |
| 58 | `src/commands/diff/index.ts` | 8 | PI-02 | LOW |
| 59 | `src/commands/doctor/doctor.tsx` | 7 | PI-02 | LOW |
| 60 | `src/commands/doctor/index.ts` | 12 | PI-02 | LOW |
| 61 | `src/commands/effort/effort.tsx` | 183 |  | LOW |
| 62 | `src/commands/effort/index.ts` | 13 | PI-02 | LOW |
| 63 | `src/commands/exit/exit.tsx` | 33 | PI-02 | LOW |
| 64 | `src/commands/exit/index.ts` | 12 | PI-02 | LOW |
| 65 | `src/commands/export/export.tsx` | 91 |  | LOW |
| 66 | `src/commands/export/index.ts` | 11 | PI-02 | LOW |
| 67 | `src/commands/extra-usage/extra-usage-core.ts` | 118 |  | LOW |
| 68 | `src/commands/extra-usage/extra-usage-noninteractive.ts` | 16 | PI-02 | LOW |
| 69 | `src/commands/extra-usage/extra-usage.tsx` | 17 | PI-02 | LOW |
| 70 | `src/commands/extra-usage/index.ts` | 31 | PI-02 | LOW |
| 71 | `src/commands/fast/fast.tsx` | 269 |  | MEDIUM |
| 72 | `src/commands/fast/index.ts` | 26 | PI-02 | LOW |
| 73 | `src/commands/feedback/feedback.tsx` | 25 | PI-02 | LOW |
| 74 | `src/commands/feedback/index.ts` | 26 | PI-02 | LOW |
| 75 | `src/commands/files/files.ts` | 19 | PI-02 | LOW |
| 76 | `src/commands/files/index.ts` | 12 | PI-02 | LOW |
| 77 | `src/commands/heapdump/heapdump.ts` | 17 | PI-02 | LOW |
| 78 | `src/commands/heapdump/index.ts` | 12 | PI-02 | LOW |
| 79 | `src/commands/help/help.tsx` | 11 | PI-02 | LOW |
| 80 | `src/commands/help/index.ts` | 10 |  | LOW |
| 81 | `src/commands/hooks/hooks.tsx` | 13 | PI-02 | LOW |
| 82 | `src/commands/hooks/index.ts` | 11 | PI-02 | LOW |
| 83 | `src/commands/ide/ide.tsx` | 646 |  | MEDIUM |
| 84 | `src/commands/ide/index.ts` | 11 | PI-02 | LOW |
| 85 | `src/commands/init-verifiers.ts` | 262 |  | MEDIUM |
| 86 | `src/commands/init.ts` | 256 |  | MEDIUM |
| 87 | `src/commands/insights.ts` | 3200 |  | HIGH |
| 88 | `src/commands/install-github-app/ApiKeyStep.tsx` | 231 |  | MEDIUM |
| 89 | `src/commands/install-github-app/CheckExistingSecretStep.tsx` | 190 |  | LOW |
| 90 | `src/commands/install-github-app/CheckGitHubStep.tsx` | 15 | PI-02 | LOW |
| 91 | `src/commands/install-github-app/ChooseRepoStep.tsx` | 211 |  | MEDIUM |
| 92 | `src/commands/install-github-app/CreatingStep.tsx` | 65 |  | LOW |
| 93 | `src/commands/install-github-app/ErrorStep.tsx` | 85 |  | LOW |
| 94 | `src/commands/install-github-app/ExistingWorkflowStep.tsx` | 103 |  | LOW |
| 95 | `src/commands/install-github-app/InstallAppStep.tsx` | 94 |  | LOW |
| 96 | `src/commands/install-github-app/OAuthFlowStep.tsx` | 276 |  | MEDIUM |
| 97 | `src/commands/install-github-app/SuccessStep.tsx` | 96 |  | LOW |
| 98 | `src/commands/install-github-app/WarningsStep.tsx` | 73 |  | LOW |
| 99 | `src/commands/install-github-app/index.ts` | 13 | PI-02 | LOW |
| 100 | `src/commands/install-github-app/install-github-app.tsx` | 587 |  | MEDIUM |
| 101 | `src/commands/install-github-app/setupGitHubActions.ts` | 325 |  | MEDIUM |
| 102 | `src/commands/install-github-app/types.ts` | 3 | PI-02 | LOW |
| 103 | `src/commands/install-slack-app/index.ts` | 12 | PI-02 | LOW |
| 104 | `src/commands/install-slack-app/install-slack-app.ts` | 30 | PI-02 | LOW |
| 105 | `src/commands/install.tsx` | 300 |  | MEDIUM |
| 106 | `src/commands/keybindings/index.ts` | 13 | PI-02 | LOW |
| 107 | `src/commands/keybindings/keybindings.ts` | 53 |  | LOW |
| 108 | `src/commands/login/index.ts` | 14 | PI-02 | LOW |
| 109 | `src/commands/login/login.tsx` | 104 |  | LOW |
| 110 | `src/commands/logout/index.ts` | 10 | PI-02 | LOW |
| 111 | `src/commands/logout/logout.tsx` | 82 |  | LOW |
| 112 | `src/commands/mcp/addCommand.ts` | 280 |  | MEDIUM |
| 113 | `src/commands/mcp/index.ts` | 12 | PI-02 | LOW |
| 114 | `src/commands/mcp/mcp.tsx` | 85 |  | LOW |
| 115 | `src/commands/mcp/xaaIdpCommand.ts` | 266 |  | MEDIUM |
| 116 | `src/commands/memory/index.ts` | 10 | PI-02 | LOW |
| 117 | `src/commands/memory/memory.tsx` | 90 |  | LOW |
| 118 | `src/commands/mobile/index.ts` | 11 | PI-02 | LOW |
| 119 | `src/commands/mobile/mobile.tsx` | 274 |  | MEDIUM |
| 120 | `src/commands/model/index.ts` | 16 | PI-02 | LOW |
| 121 | `src/commands/model/model.tsx` | 297 |  | MEDIUM |
| 122 | `src/commands/output-style/index.ts` | 11 | PI-02 | LOW |
| 123 | `src/commands/output-style/output-style.tsx` | 7 | PI-02 | LOW |
| 124 | `src/commands/passes/index.ts` | 22 | PI-02 | LOW |
| 125 | `src/commands/passes/passes.tsx` | 24 | PI-02 | LOW |
| 126 | `src/commands/permissions/index.ts` | 11 | PI-02 | LOW |
| 127 | `src/commands/permissions/permissions.tsx` | 10 | PI-02 | LOW |
| 128 | `src/commands/plan/index.ts` | 11 | PI-02 | LOW |
| 129 | `src/commands/plan/plan.tsx` | 122 |  | LOW |
| 130 | `src/commands/plugin/AddMarketplace.tsx` | 162 |  | LOW |
| 131 | `src/commands/plugin/BrowseMarketplace.tsx` | 802 |  | MEDIUM |
| 132 | `src/commands/plugin/DiscoverPlugins.tsx` | 781 |  | MEDIUM |
| 133 | `src/commands/plugin/ManageMarketplaces.tsx` | 838 |  | MEDIUM |
| 134 | `src/commands/plugin/PluginErrors.tsx` | 124 |  | LOW |
| 135 | `src/commands/plugin/PluginOptionsDialog.tsx` | 357 |  | MEDIUM |
| 136 | `src/commands/plugin/PluginOptionsFlow.tsx` | 135 |  | LOW |
| 137 | `src/commands/plugin/PluginTrustWarning.tsx` | 32 | PI-02 | LOW |
| 138 | `src/commands/plugin/UnifiedInstalledCell.tsx` | 565 |  | MEDIUM |
| 139 | `src/commands/plugin/ValidatePlugin.tsx` | 98 |  | LOW |
| 140 | `src/commands/plugin/index.tsx` | 11 | PI-02 | LOW |
| 141 | `src/commands/plugin/parseArgs.ts` | 103 |  | LOW |
| 142 | `src/commands/plugin/plugin.tsx` | 7 | PI-02 | LOW |
| 143 | `src/commands/plugin/pluginDetailsHelpers.tsx` | 117 |  | LOW |
| 144 | `src/commands/plugin/types.ts` | 2 | PI-02 | LOW |
| 145 | `src/commands/plugin/unifiedTypes.ts` | 2 | PI-02 | LOW |
| 146 | `src/commands/plugin/usePagination.ts` | 171 |  | LOW |
| 147 | `src/commands/pr_comments/index.ts` | 50 | PI-02 | LOW |
| 148 | `src/commands/privacy-settings/index.ts` | 14 | PI-02 | LOW |
| 149 | `src/commands/privacy-settings/privacy-settings.tsx` | 58 |  | LOW |
| 150 | `src/commands/rate-limit-options/index.ts` | 19 | PI-02 | LOW |
| 151 | `src/commands/rate-limit-options/rate-limit-options.tsx` | 210 |  | MEDIUM |
| 152 | `src/commands/release-notes/index.ts` | 11 | PI-02 | LOW |
| 153 | `src/commands/release-notes/release-notes.ts` | 50 | PI-02 | LOW |
| 154 | `src/commands/reload-plugins/index.ts` | 18 | PI-02 | LOW |
| 155 | `src/commands/reload-plugins/reload-plugins.ts` | 61 |  | LOW |
| 156 | `src/commands/remote-env/index.ts` | 15 | PI-02 | LOW |
| 157 | `src/commands/remote-env/remote-env.tsx` | 7 | PI-02 | LOW |
| 158 | `src/commands/remote-setup/api.ts` | 182 |  | LOW |
| 159 | `src/commands/remote-setup/index.ts` | 20 | PI-02 | LOW |
| 160 | `src/commands/remote-setup/remote-setup.tsx` | 187 |  | LOW |
| 161 | `src/commands/rename/generateSessionName.ts` | 67 |  | LOW |
| 162 | `src/commands/rename/index.ts` | 12 | PI-02 | LOW |
| 163 | `src/commands/rename/rename.ts` | 87 |  | LOW |
| 164 | `src/commands/resume/index.ts` | 12 | PI-02 | LOW |
| 165 | `src/commands/resume/resume.tsx` | 275 |  | MEDIUM |
| 166 | `src/commands/review.ts` | 57 |  | LOW |
| 167 | `src/commands/review/UltrareviewOverageDialog.tsx` | 96 |  | LOW |
| 168 | `src/commands/review/reviewRemote.ts` | 316 |  | MEDIUM |
| 169 | `src/commands/review/ultrareviewCommand.tsx` | 58 |  | LOW |
| 170 | `src/commands/review/ultrareviewEnabled.ts` | 14 | PI-02 | LOW |
| 171 | `src/commands/rewind/index.ts` | 13 | PI-02 | LOW |
| 172 | `src/commands/rewind/rewind.ts` | 13 | PI-02 | LOW |
| 173 | `src/commands/sandbox-toggle/index.ts` | 50 | PI-02 | LOW |
| 174 | `src/commands/sandbox-toggle/sandbox-toggle.tsx` | 83 |  | LOW |
| 175 | `src/commands/security-review.ts` | 243 |  | MEDIUM |
| 176 | `src/commands/session/index.ts` | 16 | PI-02 | LOW |
| 177 | `src/commands/session/session.tsx` | 140 |  | LOW |
| 178 | `src/commands/skills/index.ts` | 10 | PI-02 | LOW |
| 179 | `src/commands/skills/skills.tsx` | 8 | PI-02 | LOW |
| 180 | `src/commands/stats/index.ts` | 10 | PI-02 | LOW |
| 181 | `src/commands/stats/stats.tsx` | 7 | PI-02 | LOW |
| 182 | `src/commands/status/index.ts` | 12 | PI-02 | LOW |
| 183 | `src/commands/status/status.tsx` | 8 | PI-02 | LOW |
| 184 | `src/commands/statusline.tsx` | 24 | PI-02 | LOW |
| 185 | `src/commands/stickers/index.ts` | 11 | PI-02 | LOW |
| 186 | `src/commands/stickers/stickers.ts` | 16 | PI-02 | LOW |
| 187 | `src/commands/tag/index.ts` | 12 | PI-02 | LOW |
| 188 | `src/commands/tag/tag.tsx` | 215 |  | MEDIUM |
| 189 | `src/commands/tasks/index.ts` | 11 | PI-02 | LOW |
| 190 | `src/commands/tasks/tasks.tsx` | 8 | PI-02 | LOW |
| 191 | `src/commands/terminalSetup/index.ts` | 23 | PI-02 | LOW |
| 192 | `src/commands/terminalSetup/terminalSetup.tsx` | 531 |  | MEDIUM |
| 193 | `src/commands/theme/index.ts` | 10 | PI-02 | LOW |
| 194 | `src/commands/theme/theme.tsx` | 57 |  | LOW |
| 195 | `src/commands/thinkback-play/index.ts` | 17 | PI-02 | LOW |
| 196 | `src/commands/thinkback-play/thinkback-play.ts` | 43 | PI-02 | LOW |
| 197 | `src/commands/thinkback/index.ts` | 13 | PI-02 | LOW |
| 198 | `src/commands/thinkback/thinkback.tsx` | 554 |  | MEDIUM |
| 199 | `src/commands/ultraplan.tsx` | 471 |  | MEDIUM |
| 200 | `src/commands/upgrade/index.ts` | 16 | PI-02 | LOW |
| 201 | `src/commands/upgrade/upgrade.tsx` | 38 | PI-02 | LOW |
| 202 | `src/commands/usage/index.ts` | 9 | PI-02 | LOW |
| 203 | `src/commands/usage/usage.tsx` | 7 | PI-02 | LOW |
| 204 | `src/commands/version.ts` | 22 | PI-02 | LOW |
| 205 | `src/commands/vim/index.ts` | 11 | PI-02 | LOW |
| 206 | `src/commands/vim/vim.ts` | 38 | PI-02 | LOW |
| 207 | `src/commands/voice/index.ts` | 20 | PI-02 | LOW |
| 208 | `src/commands/voice/voice.ts` | 150 |  | LOW |
| 209 | `src/constants/apiLimits.ts` | 94 | PI-14 | LOW |
| 210 | `src/constants/betas.ts` | 52 | PI-14 | LOW |
| 211 | `src/constants/common.ts` | 33 | PI-14 | LOW |
| 212 | `src/constants/cyberRiskInstruction.ts` | 24 | PI-14 | LOW |
| 213 | `src/constants/errorIds.ts` | 15 | PI-14 | LOW |
| 214 | `src/constants/figures.ts` | 45 | PI-14 | LOW |
| 215 | `src/constants/files.ts` | 156 | PI-14 | LOW |
| 216 | `src/constants/github-app.ts` | 144 | PI-14 | LOW |
| 217 | `src/constants/outputStyles.ts` | 216 | PI-14 | MEDIUM |
| 218 | `src/constants/product.ts` | 76 | PI-14 | LOW |
| 219 | `src/constants/prompts.ts` | 914 |  | MEDIUM |
| 220 | `src/constants/spinnerVerbs.ts` | 204 | PI-14 | MEDIUM |
| 221 | `src/constants/system.ts` | 95 | PI-14 | LOW |
| 222 | `src/constants/systemPromptSections.ts` | 68 | PI-14 | LOW |
| 223 | `src/constants/toolLimits.ts` | 56 | PI-14 | LOW |
| 224 | `src/constants/xml.ts` | 86 | PI-14 | LOW |
| 225 | `src/context.ts` | 189 |  | LOW |
| 226 | `src/context/QueuedMessageContext.tsx` | 62 | PI-14 | LOW |
| 227 | `src/context/mailbox.tsx` | 37 | PI-14 | LOW |
| 228 | `src/context/modalContext.tsx` | 57 | PI-14 | LOW |
| 229 | `src/context/overlayContext.tsx` | 150 | PI-14 | LOW |
| 230 | `src/context/promptOverlayContext.tsx` | 124 | PI-14 | LOW |
| 231 | `src/context/stats.tsx` | 219 | PI-14 | MEDIUM |
| 232 | `src/context/voice.tsx` | 87 | PI-14 | LOW |
| 233 | `src/coordinator/coordinatorMode.ts` | 369 | PI-14 | MEDIUM |
| 234 | `src/cost-tracker.ts` | 323 | PI-14 | MEDIUM |
| 235 | `src/costHook.ts` | 22 | PI-14 | LOW |
| 236 | `src/dev-entry.ts` | 122 | PI-14 | LOW |
| 237 | `src/dialogLaunchers.tsx` | 132 |  | LOW |
| 238 | `src/entrypoints/agentSdkTypes.ts` | 443 | PI-14 | MEDIUM |
| 239 | `src/entrypoints/cli.tsx` | 303 |  | MEDIUM |
| 240 | `src/entrypoints/init.ts` | 340 |  | MEDIUM |
| 241 | `src/entrypoints/mcp.ts` | 196 | PI-14 | LOW |
| 242 | `src/entrypoints/sandboxTypes.ts` | 156 | PI-14 | LOW |
| 243 | `src/history.ts` | 464 | PI-14 | MEDIUM |
| 244 | `src/ink.ts` | 85 |  | LOW |
| 245 | `src/interactiveHelpers.tsx` | 365 |  | MEDIUM |
| 246 | `src/keybindings/KeybindingContext.tsx` | 242 | PI-14 | MEDIUM |
| 247 | `src/keybindings/defaultBindings.ts` | 340 | PI-14 | MEDIUM |
| 248 | `src/keybindings/loadUserBindings.ts` | 472 | PI-14 | MEDIUM |
| 249 | `src/keybindings/match.ts` | 120 | PI-14 | LOW |
| 250 | `src/keybindings/parser.ts` | 203 | PI-14 | MEDIUM |
| 251 | `src/keybindings/reservedShortcuts.ts` | 127 | PI-14 | LOW |
| 252 | `src/keybindings/resolver.ts` | 244 | PI-14 | MEDIUM |
| 253 | `src/keybindings/schema.ts` | 236 | PI-14 | MEDIUM |
| 254 | `src/keybindings/template.ts` | 52 | PI-14 | LOW |
| 255 | `src/keybindings/types.ts` | 17 | PI-14 | LOW |
| 256 | `src/keybindings/useKeybinding.ts` | 196 | PI-14 | LOW |
| 257 | `src/keybindings/validate.ts` | 498 | PI-14 | MEDIUM |
| 258 | `src/main.tsx` | 4690 |  | HIGH |
| 259 | `src/migrations/migrateAutoUpdatesToSettings.ts` | 61 | PI-14 | LOW |
| 260 | `src/migrations/migrateEnableAllProjectMcpServersToSettings.ts` | 118 | PI-14 | LOW |
| 261 | `src/migrations/migrateFennecToOpus.ts` | 45 | PI-14 | LOW |
| 262 | `src/migrations/migrateLegacyOpusToCurrent.ts` | 57 | PI-14 | LOW |
| 263 | `src/migrations/migrateOpusToOpus1m.ts` | 43 | PI-14 | LOW |
| 264 | `src/migrations/migrateReplBridgeEnabledToRemoteControlAtStartup.ts` | 22 | PI-14 | LOW |
| 265 | `src/migrations/migrateSonnet1mToSonnet45.ts` | 48 | PI-14 | LOW |
| 266 | `src/migrations/migrateSonnet45ToSonnet46.ts` | 67 | PI-14 | LOW |
| 267 | `src/migrations/resetAutoModeOptInForDefaultOffer.ts` | 51 | PI-14 | LOW |
| 268 | `src/migrations/resetProToOpusDefault.ts` | 51 | PI-14 | LOW |
| 269 | `src/moreright/useMoreRight.tsx` | 25 | PI-14 | LOW |
| 270 | `src/outputStyles/loadOutputStylesDir.ts` | 98 | PI-14 | LOW |
| 271 | `src/plugins/builtinPlugins.ts` | 159 | PI-14 | LOW |
| 272 | `src/plugins/bundled/index.ts` | 23 | PI-14 | LOW |
| 273 | `src/proactive/index.ts` | 57 | PI-14 | LOW |
| 274 | `src/projectOnboardingState.ts` | 83 | PI-14 | LOW |
| 275 | `src/query/tokenBudget.ts` | 93 | PI-14 | LOW |
| 276 | `src/remote/RemoteSessionManager.ts` | 343 | PI-14 | MEDIUM |
| 277 | `src/remote/SessionsWebSocket.ts` | 404 | PI-14 | MEDIUM |
| 278 | `src/remote/sdkMessageAdapter.ts` | 302 | PI-14 | MEDIUM |
| 279 | `src/replLauncher.tsx` | 23 |  | LOW |
| 280 | `src/schemas/hooks.ts` | 222 | PI-14 | MEDIUM |
| 281 | `src/screens/ResumeConversation.tsx` | 398 | PI-14 | MEDIUM |
| 282 | `src/server/createDirectConnectSession.ts` | 88 | PI-14 | LOW |
| 283 | `src/server/directConnectManager.ts` | 213 | PI-14 | MEDIUM |
| 284 | `src/server/types.ts` | 57 | PI-14 | LOW |
| 285 | `src/setup.ts` | 477 | PI-14 | MEDIUM |
| 286 | `src/state/AppStateStore.ts` | 569 |  | MEDIUM |
| 287 | `src/state/onChangeAppState.ts` | 171 | PI-14 | LOW |
| 288 | `src/state/selectors.ts` | 76 | PI-14 | LOW |
| 289 | `src/state/store.ts` | 34 | PI-14 | LOW |
| 290 | `src/state/teammateViewHelpers.ts` | 141 | PI-14 | LOW |
| 291 | `src/tools.ts` | 389 |  | MEDIUM |
| 292 | `src/types/command.ts` | 216 |  | MEDIUM |
| 293 | `src/types/generated/events_mono/claude_code/v1/claude_code_internal_event.ts` | 865 | PI-14 | MEDIUM |
| 294 | `src/types/generated/events_mono/common/v1/auth.ts` | 100 | PI-14 | LOW |
| 295 | `src/types/generated/events_mono/growthbook/v1/growthbook_experiment_event.ts` | 223 | PI-14 | MEDIUM |
| 296 | `src/types/generated/google/protobuf/timestamp.ts` | 187 | PI-14 | LOW |
| 297 | `src/types/hooks.ts` | 290 | PI-14 | MEDIUM |
| 298 | `src/types/ids.ts` | 44 | PI-14 | LOW |
| 299 | `src/types/logs.ts` | 330 | PI-14 | MEDIUM |
| 300 | `src/types/message.ts` | 134 | PI-14 | LOW |
| 301 | `src/types/permissions.ts` | 441 | PI-14 | MEDIUM |
| 302 | `src/types/plugin.ts` | 363 | PI-14 | MEDIUM |
| 303 | `src/types/textInputTypes.ts` | 387 | PI-14 | MEDIUM |
| 304 | `src/upstreamproxy/relay.ts` | 455 | PI-14 | MEDIUM |
| 305 | `src/upstreamproxy/upstreamproxy.ts` | 285 | PI-14 | MEDIUM |
| 306 | `src/utils/claudeInChrome/chromeNativeHost.ts` | 527 | PI-14 | MEDIUM |
| 307 | `src/utils/claudeInChrome/common.ts` | 540 | PI-14 | MEDIUM |
| 308 | `src/utils/claudeInChrome/mcpServer.ts` | 293 | PI-14 | MEDIUM |
| 309 | `src/utils/claudeInChrome/prompt.ts` | 83 | PI-14 | LOW |
| 310 | `src/utils/claudeInChrome/setup.ts` | 400 | PI-14 | MEDIUM |
| 311 | `src/utils/claudeInChrome/setupPortable.ts` | 233 | PI-14 | MEDIUM |
| 312 | `src/utils/claudeInChrome/toolRendering.tsx` | 261 | PI-14 | MEDIUM |
| 313 | `src/utils/config.ts` | 1817 |  | HIGH |
| 314 | `src/utils/earlyInput.ts` | 191 |  | LOW |
| 315 | `src/utils/settings/allErrors.ts` | 32 | PI-11 | LOW |
| 316 | `src/utils/settings/applySettingsChange.ts` | 92 |  | LOW |
| 317 | `src/utils/settings/changeDetector.ts` | 488 |  | MEDIUM |
| 318 | `src/utils/settings/constants.ts` | 202 |  | MEDIUM |
| 319 | `src/utils/settings/internalWrites.ts` | 37 | PI-11 | LOW |
| 320 | `src/utils/settings/managedPath.ts` | 34 | PI-11 | LOW |
| 321 | `src/utils/settings/mdm/constants.ts` | 81 |  | LOW |
| 322 | `src/utils/settings/mdm/rawRead.ts` | 130 |  | LOW |
| 323 | `src/utils/settings/mdm/settings.ts` | 316 |  | MEDIUM |
| 324 | `src/utils/settings/permissionValidation.ts` | 262 |  | MEDIUM |
| 325 | `src/utils/settings/pluginOnlyPolicy.ts` | 60 |  | LOW |
| 326 | `src/utils/settings/schemaOutput.ts` | 8 | PI-11 | LOW |
| 327 | `src/utils/settings/settings.ts` | 1015 |  | HIGH |
| 328 | `src/utils/settings/settingsCache.ts` | 80 |  | LOW |
| 329 | `src/utils/settings/toolValidationConfig.ts` | 103 |  | LOW |
| 330 | `src/utils/settings/types.ts` | 1148 |  | HIGH |
| 331 | `src/utils/settings/validateEditTool.ts` | 45 | PI-11 | LOW |
| 332 | `src/utils/settings/validation.ts` | 265 |  | MEDIUM |
| 333 | `src/utils/settings/validationTips.ts` | 164 |  | LOW |
| 334 | `src/utils/sinks.ts` | 16 |  | LOW |
| 335 | `src/utils/startupProfiler.ts` | 194 |  | LOW |
| 336 | `src/utils/warningHandler.ts` | 121 |  | LOW |
| 337 | `src/vim/motions.ts` | 82 | PI-14 | LOW |
| 338 | `src/vim/textObjects.ts` | 186 | PI-14 | LOW |
| 339 | `src/vim/transitions.ts` | 490 | PI-14 | MEDIUM |
| 340 | `src/vim/types.ts` | 199 | PI-14 | LOW |
| 341 | `src/voice/voiceModeEnabled.ts` | 54 | PI-14 | LOW |
| 342 | `vendor/audio-capture-src/index.ts` | 151 | PI-14 | LOW |
| 343 | `vendor/image-processor-src/index.ts` | 162 | PI-14 | LOW |
| 344 | `vendor/modifiers-napi-src/index.ts` | 67 | PI-14 | LOW |
| 345 | `vendor/url-handler-src/index.ts` | 58 | PI-14 | LOW |

## ML-02 (342 files)

📋 **Summary**: [summary-ML-02-query-engine-core](/branches/main/report/summary-ML-02-query-engine-core)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/hooks/renderPlaceholder.ts` | 51 | PI-12 | LOW |
| 2 | `src/hooks/toolPermission/PermissionContext.ts` | 388 | PI-12 | MEDIUM |
| 3 | `src/hooks/toolPermission/handlers/coordinatorHandler.ts` | 65 | PI-12 | LOW |
| 4 | `src/hooks/toolPermission/handlers/interactiveHandler.ts` | 536 | PI-12 | MEDIUM |
| 5 | `src/hooks/toolPermission/handlers/swarmWorkerHandler.ts` | 159 | PI-12 | LOW |
| 6 | `src/hooks/toolPermission/permissionLogging.ts` | 238 | PI-12 | MEDIUM |
| 7 | `src/hooks/unifiedSuggestions.ts` | 202 | PI-12 | MEDIUM |
| 8 | `src/native-ts/file-index/index.ts` | 370 | PI-12 | MEDIUM |
| 9 | `src/native-ts/yoga-layout/enums.ts` | 134 | PI-12 | LOW |
| 10 | `src/utils/CircularBuffer.ts` | 84 | PI-12 | LOW |
| 11 | `src/utils/Cursor.ts` | 1530 |  | HIGH |
| 12 | `src/utils/QueryGuard.ts` | 121 | PI-12 | LOW |
| 13 | `src/utils/Shell.ts` | 474 | PI-12 | MEDIUM |
| 14 | `src/utils/ShellCommand.ts` | 465 | PI-12 | MEDIUM |
| 15 | `src/utils/abortController.ts` | 99 | PI-12 | LOW |
| 16 | `src/utils/activityManager.ts` | 164 | PI-12 | LOW |
| 17 | `src/utils/advisor.ts` | 145 | PI-12 | LOW |
| 18 | `src/utils/agentContext.ts` | 178 | PI-12 | LOW |
| 19 | `src/utils/agentId.ts` | 99 | PI-12 | LOW |
| 20 | `src/utils/agentSwarmsEnabled.ts` | 44 | PI-12 | LOW |
| 21 | `src/utils/agenticSessionSearch.ts` | 307 | PI-12 | MEDIUM |
| 22 | `src/utils/analyzeContext.ts` | 1382 |  | HIGH |
| 23 | `src/utils/ansiToPng.ts` | 334 | PI-12 | MEDIUM |
| 24 | `src/utils/ansiToSvg.ts` | 272 | PI-12 | MEDIUM |
| 25 | `src/utils/apiPreconnect.ts` | 71 | PI-12 | LOW |
| 26 | `src/utils/appleTerminalBackup.ts` | 124 | PI-12 | LOW |
| 27 | `src/utils/argumentSubstitution.ts` | 145 | PI-12 | LOW |
| 28 | `src/utils/asciicast.ts` | 239 | PI-12 | MEDIUM |
| 29 | `src/utils/attachments.ts` | 3997 |  | HIGH |
| 30 | `src/utils/attribution.ts` | 393 | PI-12 | MEDIUM |
| 31 | `src/utils/authFileDescriptor.ts` | 196 | PI-12 | LOW |
| 32 | `src/utils/authPortable.ts` | 19 | PI-12 | LOW |
| 33 | `src/utils/autoModeDenials.ts` | 26 | PI-12 | LOW |
| 34 | `src/utils/autoRunIssue.tsx` | 121 | PI-12 | LOW |
| 35 | `src/utils/autoUpdater.ts` | 561 |  | MEDIUM |
| 36 | `src/utils/background/remote/preconditions.ts` | 235 | PI-12 | MEDIUM |
| 37 | `src/utils/background/remote/remoteSession.ts` | 98 | PI-12 | LOW |
| 38 | `src/utils/backgroundHousekeeping.ts` | 94 | PI-12 | LOW |
| 39 | `src/utils/betas.ts` | 434 | PI-12 | MEDIUM |
| 40 | `src/utils/billing.ts` | 78 | PI-12 | LOW |
| 41 | `src/utils/binaryCheck.ts` | 53 | PI-12 | LOW |
| 42 | `src/utils/browser.ts` | 68 | PI-12 | LOW |
| 43 | `src/utils/bufferedWriter.ts` | 100 | PI-12 | LOW |
| 44 | `src/utils/bundledMode.ts` | 22 | PI-12 | LOW |
| 45 | `src/utils/caCerts.ts` | 115 | PI-12 | LOW |
| 46 | `src/utils/caCertsConfig.ts` | 88 | PI-12 | LOW |
| 47 | `src/utils/cachePaths.ts` | 38 | PI-12 | LOW |
| 48 | `src/utils/classifierApprovals.ts` | 88 | PI-12 | LOW |
| 49 | `src/utils/classifierApprovalsHook.ts` | 17 | PI-12 | LOW |
| 50 | `src/utils/claudeCodeHints.ts` | 193 | PI-12 | LOW |
| 51 | `src/utils/claudeDesktop.ts` | 152 | PI-12 | LOW |
| 52 | `src/utils/claudemd.ts` | 1479 |  | HIGH |
| 53 | `src/utils/cleanup.ts` | 602 |  | MEDIUM |
| 54 | `src/utils/cleanupRegistry.ts` | 25 | PI-12 | LOW |
| 55 | `src/utils/cliArgs.ts` | 60 | PI-12 | LOW |
| 56 | `src/utils/cliHighlight.ts` | 54 | PI-12 | LOW |
| 57 | `src/utils/codeIndexing.ts` | 206 | PI-12 | MEDIUM |
| 58 | `src/utils/collapseBackgroundBashNotifications.ts` | 84 | PI-12 | LOW |
| 59 | `src/utils/collapseHookSummaries.ts` | 59 | PI-12 | LOW |
| 60 | `src/utils/collapseReadSearch.ts` | 1109 |  | HIGH |
| 61 | `src/utils/collapseTeammateShutdowns.ts` | 55 | PI-12 | LOW |
| 62 | `src/utils/combinedAbortSignal.ts` | 47 | PI-12 | LOW |
| 63 | `src/utils/commandLifecycle.ts` | 21 | PI-12 | LOW |
| 64 | `src/utils/commitAttribution.ts` | 961 |  | MEDIUM |
| 65 | `src/utils/completionCache.ts` | 166 | PI-12 | LOW |
| 66 | `src/utils/concurrentSessions.ts` | 204 | PI-12 | MEDIUM |
| 67 | `src/utils/configConstants.ts` | 21 | PI-12 | LOW |
| 68 | `src/utils/contentArray.ts` | 51 | PI-12 | LOW |
| 69 | `src/utils/context.ts` | 221 | PI-12 | MEDIUM |
| 70 | `src/utils/contextSuggestions.ts` | 235 | PI-12 | MEDIUM |
| 71 | `src/utils/controlMessageCompat.ts` | 32 | PI-12 | LOW |
| 72 | `src/utils/conversationRecovery.ts` | 597 |  | MEDIUM |
| 73 | `src/utils/cron.ts` | 308 | PI-12 | MEDIUM |
| 74 | `src/utils/cronJitterConfig.ts` | 75 | PI-12 | LOW |
| 75 | `src/utils/cronScheduler.ts` | 565 |  | MEDIUM |
| 76 | `src/utils/cronTasks.ts` | 458 | PI-12 | MEDIUM |
| 77 | `src/utils/cronTasksLock.ts` | 195 | PI-12 | LOW |
| 78 | `src/utils/crossProjectResume.ts` | 75 | PI-12 | LOW |
| 79 | `src/utils/cwd.ts` | 32 | PI-12 | LOW |
| 80 | `src/utils/debug.ts` | 268 | PI-12 | MEDIUM |
| 81 | `src/utils/debugFilter.ts` | 157 | PI-12 | LOW |
| 82 | `src/utils/deepLink/banner.ts` | 123 | PI-12 | LOW |
| 83 | `src/utils/deepLink/parseDeepLink.ts` | 170 | PI-12 | LOW |
| 84 | `src/utils/deepLink/protocolHandler.ts` | 136 | PI-12 | LOW |
| 85 | `src/utils/deepLink/registerProtocol.ts` | 348 | PI-12 | MEDIUM |
| 86 | `src/utils/deepLink/terminalLauncher.ts` | 557 | PI-12 | MEDIUM |
| 87 | `src/utils/deepLink/terminalPreference.ts` | 54 | PI-12 | LOW |
| 88 | `src/utils/desktopDeepLink.ts` | 236 | PI-12 | MEDIUM |
| 89 | `src/utils/detectRepository.ts` | 178 | PI-12 | LOW |
| 90 | `src/utils/diagLogs.ts` | 94 | PI-12 | LOW |
| 91 | `src/utils/diff.ts` | 177 | PI-12 | LOW |
| 92 | `src/utils/directMemberMessage.ts` | 69 | PI-12 | LOW |
| 93 | `src/utils/displayTags.ts` | 51 | PI-12 | LOW |
| 94 | `src/utils/doctorContextWarnings.ts` | 265 | PI-12 | MEDIUM |
| 95 | `src/utils/doctorDiagnostic.ts` | 625 |  | MEDIUM |
| 96 | `src/utils/dxt/helpers.ts` | 88 | PI-12 | LOW |
| 97 | `src/utils/dxt/zip.ts` | 226 | PI-12 | MEDIUM |
| 98 | `src/utils/editor.ts` | 183 | PI-12 | LOW |
| 99 | `src/utils/effort.ts` | 329 | PI-12 | MEDIUM |
| 100 | `src/utils/env.ts` | 347 | PI-12 | MEDIUM |
| 101 | `src/utils/envDynamic.ts` | 151 | PI-12 | LOW |
| 102 | `src/utils/envUtils.ts` | 183 | PI-12 | LOW |
| 103 | `src/utils/envValidation.ts` | 38 | PI-12 | LOW |
| 104 | `src/utils/errorLogSink.ts` | 235 | PI-12 | MEDIUM |
| 105 | `src/utils/errors.ts` | 238 | PI-12 | MEDIUM |
| 106 | `src/utils/exampleCommands.ts` | 184 | PI-12 | LOW |
| 107 | `src/utils/execFileNoThrowPortable.ts` | 89 | PI-12 | LOW |
| 108 | `src/utils/execSyncWrapper.ts` | 38 | PI-12 | LOW |
| 109 | `src/utils/exportRenderer.tsx` | 97 | PI-12 | LOW |
| 110 | `src/utils/extraUsage.ts` | 23 | PI-12 | LOW |
| 111 | `src/utils/fastMode.ts` | 532 |  | MEDIUM |
| 112 | `src/utils/fileOperationAnalytics.ts` | 71 | PI-12 | LOW |
| 113 | `src/utils/filePersistence/filePersistence.ts` | 287 | PI-12 | MEDIUM |
| 114 | `src/utils/filePersistence/outputsScanner.ts` | 126 | PI-12 | LOW |
| 115 | `src/utils/fileRead.ts` | 102 | PI-12 | LOW |
| 116 | `src/utils/fileReadCache.ts` | 96 | PI-12 | LOW |
| 117 | `src/utils/fileStateCache.ts` | 142 | PI-12 | LOW |
| 118 | `src/utils/findExecutable.ts` | 17 | PI-12 | LOW |
| 119 | `src/utils/fingerprint.ts` | 76 | PI-12 | LOW |
| 120 | `src/utils/format.ts` | 308 | PI-12 | MEDIUM |
| 121 | `src/utils/formatBriefTimestamp.ts` | 81 | PI-12 | LOW |
| 122 | `src/utils/fpsTracker.ts` | 47 | PI-12 | LOW |
| 123 | `src/utils/frontmatterParser.ts` | 370 | PI-12 | MEDIUM |
| 124 | `src/utils/fsOperations.ts` | 770 |  | MEDIUM |
| 125 | `src/utils/fullscreen.ts` | 202 | PI-12 | MEDIUM |
| 126 | `src/utils/generatedFiles.ts` | 136 | PI-12 | LOW |
| 127 | `src/utils/generators.ts` | 88 | PI-12 | LOW |
| 128 | `src/utils/genericProcessUtils.ts` | 184 | PI-12 | LOW |
| 129 | `src/utils/getWorktreePaths.ts` | 70 | PI-12 | LOW |
| 130 | `src/utils/getWorktreePathsPortable.ts` | 27 | PI-12 | LOW |
| 131 | `src/utils/ghPrStatus.ts` | 106 | PI-12 | LOW |
| 132 | `src/utils/git/gitConfigParser.ts` | 277 | PI-12 | MEDIUM |
| 133 | `src/utils/git/gitignore.ts` | 99 | PI-12 | LOW |
| 134 | `src/utils/gitSettings.ts` | 18 | PI-12 | LOW |
| 135 | `src/utils/github/ghAuthStatus.ts` | 29 | PI-12 | LOW |
| 136 | `src/utils/githubRepoPathMapping.ts` | 162 | PI-12 | LOW |
| 137 | `src/utils/glob.ts` | 130 | PI-12 | LOW |
| 138 | `src/utils/gracefulShutdown.ts` | 529 |  | MEDIUM |
| 139 | `src/utils/groupToolUses.ts` | 182 | PI-12 | LOW |
| 140 | `src/utils/handlePromptSubmit.ts` | 610 |  | MEDIUM |
| 141 | `src/utils/hash.ts` | 46 | PI-12 | LOW |
| 142 | `src/utils/headlessProfiler.ts` | 178 | PI-12 | LOW |
| 143 | `src/utils/heapDumpService.ts` | 303 | PI-12 | MEDIUM |
| 144 | `src/utils/heatmap.ts` | 198 | PI-12 | LOW |
| 145 | `src/utils/highlightMatch.tsx` | 27 | PI-12 | LOW |
| 146 | `src/utils/hooks.ts` | 5022 | PI-12 | HIGH |
| 147 | `src/utils/hooks/AsyncHookRegistry.ts` | 309 | PI-12 | MEDIUM |
| 148 | `src/utils/hooks/apiQueryHookHelper.ts` | 141 | PI-12 | LOW |
| 149 | `src/utils/hooks/execAgentHook.ts` | 339 | PI-12 | MEDIUM |
| 150 | `src/utils/hooks/execHttpHook.ts` | 242 | PI-12 | MEDIUM |
| 151 | `src/utils/hooks/execPromptHook.ts` | 211 | PI-12 | MEDIUM |
| 152 | `src/utils/hooks/fileChangedWatcher.ts` | 191 | PI-12 | LOW |
| 153 | `src/utils/hooks/hookEvents.ts` | 192 | PI-12 | LOW |
| 154 | `src/utils/hooks/hookHelpers.ts` | 83 | PI-12 | LOW |
| 155 | `src/utils/hooks/hooksConfigManager.ts` | 400 | PI-12 | MEDIUM |
| 156 | `src/utils/hooks/hooksConfigSnapshot.ts` | 133 | PI-12 | LOW |
| 157 | `src/utils/hooks/hooksSettings.ts` | 271 | PI-12 | MEDIUM |
| 158 | `src/utils/hooks/postSamplingHooks.ts` | 70 | PI-12 | LOW |
| 159 | `src/utils/hooks/registerFrontmatterHooks.ts` | 67 | PI-12 | LOW |
| 160 | `src/utils/hooks/registerSkillHooks.ts` | 64 | PI-12 | LOW |
| 161 | `src/utils/hooks/sessionHooks.ts` | 447 | PI-12 | MEDIUM |
| 162 | `src/utils/hooks/skillImprovement.ts` | 267 | PI-12 | MEDIUM |
| 163 | `src/utils/hooks/ssrfGuard.ts` | 294 | PI-12 | MEDIUM |
| 164 | `src/utils/horizontalScroll.ts` | 137 | PI-12 | LOW |
| 165 | `src/utils/hyperlink.ts` | 39 | PI-12 | LOW |
| 166 | `src/utils/iTermBackup.ts` | 73 | PI-12 | LOW |
| 167 | `src/utils/ide.ts` | 1494 |  | HIGH |
| 168 | `src/utils/idePathConversion.ts` | 90 | PI-12 | LOW |
| 169 | `src/utils/idleTimeout.ts` | 53 | PI-12 | LOW |
| 170 | `src/utils/imagePaste.ts` | 416 | PI-12 | MEDIUM |
| 171 | `src/utils/imageResizer.ts` | 880 |  | MEDIUM |
| 172 | `src/utils/imageStore.ts` | 167 | PI-12 | LOW |
| 173 | `src/utils/imageValidation.ts` | 104 | PI-12 | LOW |
| 174 | `src/utils/immediateCommand.ts` | 15 | PI-12 | LOW |
| 175 | `src/utils/inProcessTeammateHelpers.ts` | 102 | PI-12 | LOW |
| 176 | `src/utils/ink.ts` | 26 | PI-12 | LOW |
| 177 | `src/utils/intl.ts` | 94 | PI-12 | LOW |
| 178 | `src/utils/jetbrains.ts` | 191 | PI-12 | LOW |
| 179 | `src/utils/json.ts` | 277 | PI-12 | MEDIUM |
| 180 | `src/utils/jsonRead.ts` | 16 | PI-12 | LOW |
| 181 | `src/utils/listSessionsImpl.ts` | 454 | PI-12 | MEDIUM |
| 182 | `src/utils/localInstaller.ts` | 162 | PI-12 | LOW |
| 183 | `src/utils/lockfile.ts` | 43 | PI-12 | LOW |
| 184 | `src/utils/log.ts` | 362 | PI-12 | MEDIUM |
| 185 | `src/utils/logoV2Utils.ts` | 350 | PI-12 | MEDIUM |
| 186 | `src/utils/mailbox.ts` | 73 | PI-12 | LOW |
| 187 | `src/utils/managedEnv.ts` | 199 | PI-12 | LOW |
| 188 | `src/utils/managedEnvConstants.ts` | 191 | PI-12 | LOW |
| 189 | `src/utils/markdown.ts` | 381 | PI-12 | MEDIUM |
| 190 | `src/utils/markdownConfigLoader.ts` | 600 |  | MEDIUM |
| 191 | `src/utils/mcp/dateTimeParser.ts` | 121 | PI-12 | LOW |
| 192 | `src/utils/mcp/elicitationValidation.ts` | 336 | PI-12 | MEDIUM |
| 193 | `src/utils/mcpInstructionsDelta.ts` | 130 | PI-12 | LOW |
| 194 | `src/utils/mcpOutputStorage.ts` | 189 | PI-12 | LOW |
| 195 | `src/utils/mcpValidation.ts` | 208 | PI-12 | MEDIUM |
| 196 | `src/utils/mcpWebSocketTransport.ts` | 200 | PI-12 | LOW |
| 197 | `src/utils/memoize.ts` | 269 | PI-12 | MEDIUM |
| 198 | `src/utils/memoryFileDetection.ts` | 289 | PI-12 | MEDIUM |
| 199 | `src/utils/messageQueueManager.ts` | 547 |  | MEDIUM |
| 200 | `src/utils/messages/mappers.ts` | 290 | PI-12 | MEDIUM |
| 201 | `src/utils/messages/systemInit.ts` | 96 | PI-12 | LOW |
| 202 | `src/utils/model/agent.ts` | 157 | PI-12 | LOW |
| 203 | `src/utils/model/aliases.ts` | 25 | PI-12 | LOW |
| 204 | `src/utils/model/antModels.ts` | 64 | PI-12 | LOW |
| 205 | `src/utils/model/bedrock.ts` | 265 | PI-12 | MEDIUM |
| 206 | `src/utils/model/check1mAccess.ts` | 72 | PI-12 | LOW |
| 207 | `src/utils/model/configs.ts` | 118 | PI-12 | LOW |
| 208 | `src/utils/model/contextWindowUpgradeCheck.ts` | 47 | PI-12 | LOW |
| 209 | `src/utils/model/deprecation.ts` | 101 | PI-12 | LOW |
| 210 | `src/utils/model/model.ts` | 618 | PI-12 | MEDIUM |
| 211 | `src/utils/model/modelAllowlist.ts` | 170 | PI-12 | LOW |
| 212 | `src/utils/model/modelCapabilities.ts` | 118 | PI-12 | LOW |
| 213 | `src/utils/model/modelOptions.ts` | 540 | PI-12 | MEDIUM |
| 214 | `src/utils/model/modelStrings.ts` | 166 | PI-12 | LOW |
| 215 | `src/utils/model/modelSupportOverrides.ts` | 50 | PI-12 | LOW |
| 216 | `src/utils/model/providers.ts` | 40 | PI-12 | LOW |
| 217 | `src/utils/model/validateModel.ts` | 159 | PI-12 | LOW |
| 218 | `src/utils/modelCost.ts` | 231 | PI-12 | MEDIUM |
| 219 | `src/utils/modifiers.ts` | 36 | PI-12 | LOW |
| 220 | `src/utils/mtls.ts` | 179 | PI-12 | LOW |
| 221 | `src/utils/nativeInstaller/download.ts` | 523 | PI-12 | MEDIUM |
| 222 | `src/utils/nativeInstaller/index.ts` | 18 | PI-12 | LOW |
| 223 | `src/utils/nativeInstaller/installer.ts` | 1708 | PI-12 | HIGH |
| 224 | `src/utils/nativeInstaller/packageManagers.ts` | 336 | PI-12 | MEDIUM |
| 225 | `src/utils/nativeInstaller/pidLock.ts` | 433 | PI-12 | MEDIUM |
| 226 | `src/utils/notebook.ts` | 224 | PI-12 | MEDIUM |
| 227 | `src/utils/objectGroupBy.ts` | 18 | PI-12 | LOW |
| 228 | `src/utils/pasteStore.ts` | 104 | PI-12 | LOW |
| 229 | `src/utils/path.ts` | 155 | PI-12 | LOW |
| 230 | `src/utils/pdf.ts` | 300 | PI-12 | MEDIUM |
| 231 | `src/utils/pdfUtils.ts` | 70 | PI-12 | LOW |
| 232 | `src/utils/peerAddress.ts` | 21 | PI-12 | LOW |
| 233 | `src/utils/planModeV2.ts` | 95 | PI-12 | LOW |
| 234 | `src/utils/plans.ts` | 397 | PI-12 | MEDIUM |
| 235 | `src/utils/platform.ts` | 150 | PI-12 | LOW |
| 236 | `src/utils/preflightChecks.tsx` | 150 | PI-12 | LOW |
| 237 | `src/utils/privacyLevel.ts` | 55 | PI-12 | LOW |
| 238 | `src/utils/process.ts` | 68 | PI-12 | LOW |
| 239 | `src/utils/processUserInput/processBashCommand.tsx` | 139 | PI-12 | LOW |
| 240 | `src/utils/processUserInput/processSlashCommand.tsx` | 921 |  | MEDIUM |
| 241 | `src/utils/processUserInput/processTextPrompt.ts` | 100 | PI-12 | LOW |
| 242 | `src/utils/profilerBase.ts` | 46 | PI-12 | LOW |
| 243 | `src/utils/promptCategory.ts` | 49 | PI-12 | LOW |
| 244 | `src/utils/promptEditor.ts` | 188 | PI-12 | LOW |
| 245 | `src/utils/promptShellExecution.ts` | 183 | PI-12 | LOW |
| 246 | `src/utils/proxy.ts` | 426 | PI-12 | MEDIUM |
| 247 | `src/utils/queryProfiler.ts` | 301 | PI-12 | MEDIUM |
| 248 | `src/utils/queueProcessor.ts` | 95 | PI-12 | LOW |
| 249 | `src/utils/readEditContext.ts` | 227 | PI-12 | MEDIUM |
| 250 | `src/utils/readFileInRange.ts` | 383 | PI-12 | MEDIUM |
| 251 | `src/utils/releaseNotes.ts` | 360 | PI-12 | MEDIUM |
| 252 | `src/utils/renderOptions.ts` | 77 | PI-12 | LOW |
| 253 | `src/utils/sanitization.ts` | 91 | PI-12 | LOW |
| 254 | `src/utils/screenshotClipboard.ts` | 121 | PI-12 | LOW |
| 255 | `src/utils/sdkEventQueue.ts` | 134 | PI-12 | LOW |
| 256 | `src/utils/semanticBoolean.ts` | 29 | PI-12 | LOW |
| 257 | `src/utils/semanticNumber.ts` | 36 | PI-12 | LOW |
| 258 | `src/utils/semver.ts` | 59 | PI-12 | LOW |
| 259 | `src/utils/sequential.ts` | 56 | PI-12 | LOW |
| 260 | `src/utils/sessionActivity.ts` | 133 | PI-12 | LOW |
| 261 | `src/utils/sessionEnvVars.ts` | 22 | PI-12 | LOW |
| 262 | `src/utils/sessionEnvironment.ts` | 166 | PI-12 | LOW |
| 263 | `src/utils/sessionFileAccessHooks.ts` | 250 | PI-12 | MEDIUM |
| 264 | `src/utils/sessionIngressAuth.ts` | 140 | PI-12 | LOW |
| 265 | `src/utils/sessionStart.ts` | 232 | PI-12 | MEDIUM |
| 266 | `src/utils/sessionState.ts` | 150 | PI-12 | LOW |
| 267 | `src/utils/sessionTitle.ts` | 129 | PI-12 | LOW |
| 268 | `src/utils/sessionUrl.ts` | 64 | PI-12 | LOW |
| 269 | `src/utils/set.ts` | 53 | PI-12 | LOW |
| 270 | `src/utils/shellConfig.ts` | 167 | PI-12 | LOW |
| 271 | `src/utils/sideQuery.ts` | 222 | PI-12 | MEDIUM |
| 272 | `src/utils/sideQuestion.ts` | 155 | PI-12 | LOW |
| 273 | `src/utils/signal.ts` | 43 | PI-12 | LOW |
| 274 | `src/utils/skills/skillChangeDetector.ts` | 311 | PI-12 | MEDIUM |
| 275 | `src/utils/slashCommandParsing.ts` | 60 | PI-12 | LOW |
| 276 | `src/utils/sleep.ts` | 84 | PI-12 | LOW |
| 277 | `src/utils/sliceAnsi.ts` | 91 | PI-12 | LOW |
| 278 | `src/utils/slowOperations.ts` | 286 | PI-12 | MEDIUM |
| 279 | `src/utils/standaloneAgent.ts` | 23 | PI-12 | LOW |
| 280 | `src/utils/staticRender.tsx` | 115 | PI-12 | LOW |
| 281 | `src/utils/stats.ts` | 1061 |  | HIGH |
| 282 | `src/utils/statsCache.ts` | 434 | PI-12 | MEDIUM |
| 283 | `src/utils/status.tsx` | 361 | PI-12 | MEDIUM |
| 284 | `src/utils/statusNoticeDefinitions.tsx` | 197 | PI-12 | LOW |
| 285 | `src/utils/statusNoticeHelpers.ts` | 20 | PI-12 | LOW |
| 286 | `src/utils/stream.ts` | 76 | PI-12 | LOW |
| 287 | `src/utils/streamJsonStdoutGuard.ts` | 123 | PI-12 | LOW |
| 288 | `src/utils/streamlinedTransform.ts` | 201 | PI-12 | MEDIUM |
| 289 | `src/utils/stringUtils.ts` | 235 | PI-12 | MEDIUM |
| 290 | `src/utils/subprocessEnv.ts` | 99 | PI-12 | LOW |
| 291 | `src/utils/suggestions/commandSuggestions.ts` | 567 |  | MEDIUM |
| 292 | `src/utils/suggestions/directoryCompletion.ts` | 263 | PI-12 | MEDIUM |
| 293 | `src/utils/suggestions/shellHistoryCompletion.ts` | 119 | PI-12 | LOW |
| 294 | `src/utils/suggestions/skillUsageTracking.ts` | 55 | PI-12 | LOW |
| 295 | `src/utils/suggestions/slackChannelSuggestions.ts` | 209 | PI-12 | MEDIUM |
| 296 | `src/utils/systemDirectories.ts` | 74 | PI-12 | LOW |
| 297 | `src/utils/systemPrompt.ts` | 123 | PI-12 | LOW |
| 298 | `src/utils/systemTheme.ts` | 119 | PI-12 | LOW |
| 299 | `src/utils/taggedId.ts` | 54 | PI-12 | LOW |
| 300 | `src/utils/tasks.ts` | 862 |  | MEDIUM |
| 301 | `src/utils/teamDiscovery.ts` | 81 | PI-12 | LOW |
| 302 | `src/utils/teamMemoryOps.ts` | 88 | PI-12 | LOW |
| 303 | `src/utils/teammate.ts` | 292 | PI-12 | MEDIUM |
| 304 | `src/utils/teammateContext.ts` | 96 | PI-12 | LOW |
| 305 | `src/utils/teammateMailbox.ts` | 1183 |  | HIGH |
| 306 | `src/utils/teleport.tsx` | 1225 |  | HIGH |
| 307 | `src/utils/teleport/api.ts` | 466 | PI-12 | MEDIUM |
| 308 | `src/utils/teleport/environmentSelection.ts` | 77 | PI-12 | LOW |
| 309 | `src/utils/teleport/environments.ts` | 120 | PI-12 | LOW |
| 310 | `src/utils/teleport/gitBundle.ts` | 292 | PI-12 | MEDIUM |
| 311 | `src/utils/tempfile.ts` | 31 | PI-12 | LOW |
| 312 | `src/utils/terminal.ts` | 131 | PI-12 | LOW |
| 313 | `src/utils/terminalPanel.ts` | 191 | PI-12 | LOW |
| 314 | `src/utils/textHighlighting.ts` | 166 | PI-12 | LOW |
| 315 | `src/utils/theme.ts` | 639 |  | MEDIUM |
| 316 | `src/utils/thinking.ts` | 162 | PI-12 | LOW |
| 317 | `src/utils/timeouts.ts` | 39 | PI-12 | LOW |
| 318 | `src/utils/tmuxSocket.ts` | 427 | PI-12 | MEDIUM |
| 319 | `src/utils/todo/types.ts` | 18 | PI-12 | LOW |
| 320 | `src/utils/tokenBudget.ts` | 73 | PI-12 | LOW |
| 321 | `src/utils/toolErrors.ts` | 132 | PI-12 | LOW |
| 322 | `src/utils/toolPool.ts` | 79 | PI-12 | LOW |
| 323 | `src/utils/toolSchemaCache.ts` | 26 | PI-12 | LOW |
| 324 | `src/utils/transcriptSearch.ts` | 202 | PI-12 | MEDIUM |
| 325 | `src/utils/treeify.ts` | 170 | PI-12 | LOW |
| 326 | `src/utils/truncate.ts` | 179 | PI-12 | LOW |
| 327 | `src/utils/ultraplan/ccrSession.ts` | 349 | PI-12 | MEDIUM |
| 328 | `src/utils/ultraplan/keyword.ts` | 127 | PI-12 | LOW |
| 329 | `src/utils/unaryLogging.ts` | 39 | PI-12 | LOW |
| 330 | `src/utils/undercover.ts` | 89 | PI-12 | LOW |
| 331 | `src/utils/user.ts` | 194 | PI-12 | LOW |
| 332 | `src/utils/userPromptKeywords.ts` | 27 | PI-12 | LOW |
| 333 | `src/utils/uuid.ts` | 27 | PI-12 | LOW |
| 334 | `src/utils/which.ts` | 82 | PI-12 | LOW |
| 335 | `src/utils/windowsPaths.ts` | 173 | PI-12 | LOW |
| 336 | `src/utils/words.ts` | 800 |  | MEDIUM |
| 337 | `src/utils/workloadContext.ts` | 57 | PI-12 | LOW |
| 338 | `src/utils/worktree.ts` | 1519 |  | HIGH |
| 339 | `src/utils/xdg.ts` | 65 | PI-12 | LOW |
| 340 | `src/utils/xml.ts` | 16 | PI-12 | LOW |
| 341 | `src/utils/yaml.ts` | 15 | PI-12 | LOW |
| 342 | `src/utils/zodToJsonSchema.ts` | 23 | PI-12 | LOW |

## ML-02-1 (3 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/QueryEngine.ts` | 1295 |  | HIGH |
| 2 | `src/utils/processUserInput/processUserInput.ts` | 605 |  | MEDIUM |
| 3 | `src/utils/queryContext.ts` | 179 |  | LOW |

## ML-02-2 (8 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/query.ts` | 1729 |  | HIGH |
| 2 | `src/query/config.ts` | 46 |  | LOW |
| 3 | `src/query/deps.ts` | 40 |  | LOW |
| 4 | `src/query/stopHooks.ts` | 473 |  | MEDIUM |
| 5 | `src/query/transitions.ts` | 3 |  | LOW |
| 6 | `src/services/compact/autoCompact.ts` | 351 |  | MEDIUM |
| 7 | `src/services/compact/compact.ts` | 1705 |  | HIGH |
| 8 | `src/utils/tokens.ts` | 261 |  | MEDIUM |

## ML-02-3 (8 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/Tool.ts` | 792 |  | MEDIUM |
| 2 | `src/services/api/claude.ts` | 3419 |  | HIGH |
| 3 | `src/services/api/client.ts` | 389 |  | MEDIUM |
| 4 | `src/services/api/errors.ts` | 1207 |  | HIGH |
| 5 | `src/services/api/logging.ts` | 788 |  | MEDIUM |
| 6 | `src/services/api/withRetry.ts` | 822 |  | MEDIUM |
| 7 | `src/services/tools/StreamingToolExecutor.ts` | 530 |  | MEDIUM |
| 8 | `src/services/tools/toolOrchestration.ts` | 188 |  | LOW |

## ML-02-4 (3 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/utils/api.ts` | 718 |  | MEDIUM |
| 2 | `src/utils/messages.ts` | 5512 |  | HIGH |
| 3 | `src/utils/queryHelpers.ts` | 552 |  | MEDIUM |

## ML-03 (21 files)

📋 **Summary**: [summary-ML-03-tool-system-dispatch](/branches/main/report/summary-ML-03-tool-system-dispatch)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/utils/computerUse/appNames.ts` | 196 |  | LOW |
| 2 | `src/utils/computerUse/cleanup.ts` | 86 |  | LOW |
| 3 | `src/utils/computerUse/common.ts` | 61 |  | LOW |
| 4 | `src/utils/computerUse/computerUseLock.ts` | 215 |  | MEDIUM |
| 5 | `src/utils/computerUse/drainRunLoop.ts` | 79 |  | LOW |
| 6 | `src/utils/computerUse/escHotkey.ts` | 54 |  | LOW |
| 7 | `src/utils/computerUse/executor.ts` | 658 |  | MEDIUM |
| 8 | `src/utils/computerUse/gates.ts` | 72 |  | LOW |
| 9 | `src/utils/computerUse/hostAdapter.ts` | 69 |  | LOW |
| 10 | `src/utils/computerUse/inputLoader.ts` | 45 | PI-18 | LOW |
| 11 | `src/utils/computerUse/mcpServer.ts` | 106 |  | LOW |
| 12 | `src/utils/computerUse/setup.ts` | 53 |  | LOW |
| 13 | `src/utils/computerUse/swiftLoader.ts` | 39 | PI-18 | LOW |
| 14 | `src/utils/computerUse/toolRendering.tsx` | 124 |  | LOW |
| 15 | `src/utils/computerUse/wrapper.tsx` | 335 |  | MEDIUM |
| 16 | `src/utils/file.ts` | 584 |  | MEDIUM |
| 17 | `src/utils/fileHistory.ts` | 1115 |  | HIGH |
| 18 | `src/utils/git.ts` | 926 |  | MEDIUM |
| 19 | `src/utils/git/gitFilesystem.ts` | 699 |  | MEDIUM |
| 20 | `src/utils/gitDiff.ts` | 532 |  | MEDIUM |
| 21 | `src/utils/ripgrep.ts` | 679 |  | MEDIUM |

## ML-03-1 (5 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/constants/tools.ts` | 112 |  | LOW |
| 2 | `src/hooks/useCanUseTool.tsx` | 203 |  | MEDIUM |
| 3 | `src/types/tools.ts` | 15 |  | LOW |
| 4 | `src/utils/embeddedTools.ts` | 29 |  | LOW |
| 5 | `src/utils/toolSearch.ts` | 756 |  | MEDIUM |

## ML-03-2 (201 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/tools/toolExecution.ts` | 1745 |  | HIGH |
| 2 | `src/tools/AgentTool/AgentTool.tsx` | 1397 |  | HIGH |
| 3 | `src/tools/AgentTool/UI.tsx` | 871 |  | MEDIUM |
| 4 | `src/tools/AgentTool/agentColorManager.ts` | 66 |  | LOW |
| 5 | `src/tools/AgentTool/agentDisplay.ts` | 104 |  | LOW |
| 6 | `src/tools/AgentTool/agentMemory.ts` | 177 |  | LOW |
| 7 | `src/tools/AgentTool/agentMemorySnapshot.ts` | 197 |  | LOW |
| 8 | `src/tools/AgentTool/agentToolUtils.ts` | 686 |  | MEDIUM |
| 9 | `src/tools/AgentTool/built-in/claudeCodeGuideAgent.ts` | 205 |  | MEDIUM |
| 10 | `src/tools/AgentTool/built-in/exploreAgent.ts` | 83 |  | LOW |
| 11 | `src/tools/AgentTool/built-in/generalPurposeAgent.ts` | 34 |  | LOW |
| 12 | `src/tools/AgentTool/built-in/planAgent.ts` | 92 |  | LOW |
| 13 | `src/tools/AgentTool/built-in/statuslineSetup.ts` | 144 |  | LOW |
| 14 | `src/tools/AgentTool/built-in/verificationAgent.ts` | 152 |  | LOW |
| 15 | `src/tools/AgentTool/builtInAgents.ts` | 72 |  | LOW |
| 16 | `src/tools/AgentTool/constants.ts` | 12 | PI-01 | LOW |
| 17 | `src/tools/AgentTool/forkSubagent.ts` | 210 |  | MEDIUM |
| 18 | `src/tools/AgentTool/loadAgentsDir.ts` | 755 |  | MEDIUM |
| 19 | `src/tools/AgentTool/prompt.ts` | 287 |  | MEDIUM |
| 20 | `src/tools/AgentTool/resumeAgent.ts` | 265 |  | MEDIUM |
| 21 | `src/tools/AgentTool/runAgent.ts` | 973 |  | MEDIUM |
| 22 | `src/tools/AskUserQuestionTool/AskUserQuestionTool.tsx` | 265 |  | MEDIUM |
| 23 | `src/tools/AskUserQuestionTool/prompt.ts` | 44 | PI-01 | LOW |
| 24 | `src/tools/BashTool/BashTool.tsx` | 1143 |  | HIGH |
| 25 | `src/tools/BashTool/BashToolResultMessage.tsx` | 190 |  | LOW |
| 26 | `src/tools/BashTool/UI.tsx` | 184 |  | LOW |
| 27 | `src/tools/BashTool/bashCommandHelpers.ts` | 265 |  | MEDIUM |
| 28 | `src/tools/BashTool/bashPermissions.ts` | 2621 |  | HIGH |
| 29 | `src/tools/BashTool/bashSecurity.ts` | 2592 |  | HIGH |
| 30 | `src/tools/BashTool/commandSemantics.ts` | 140 |  | LOW |
| 31 | `src/tools/BashTool/commentLabel.ts` | 13 | PI-01 | LOW |
| 32 | `src/tools/BashTool/destructiveCommandWarning.ts` | 102 |  | LOW |
| 33 | `src/tools/BashTool/modeValidation.ts` | 115 |  | LOW |
| 34 | `src/tools/BashTool/pathValidation.ts` | 1303 |  | HIGH |
| 35 | `src/tools/BashTool/prompt.ts` | 369 |  | MEDIUM |
| 36 | `src/tools/BashTool/readOnlyValidation.ts` | 1990 |  | HIGH |
| 37 | `src/tools/BashTool/sedEditParser.ts` | 322 |  | MEDIUM |
| 38 | `src/tools/BashTool/sedValidation.ts` | 684 |  | MEDIUM |
| 39 | `src/tools/BashTool/shouldUseSandbox.ts` | 153 |  | LOW |
| 40 | `src/tools/BashTool/toolName.ts` | 2 | PI-01 | LOW |
| 41 | `src/tools/BashTool/utils.ts` | 223 |  | MEDIUM |
| 42 | `src/tools/BriefTool/BriefTool.ts` | 204 |  | MEDIUM |
| 43 | `src/tools/BriefTool/UI.tsx` | 100 |  | LOW |
| 44 | `src/tools/BriefTool/attachments.ts` | 110 |  | LOW |
| 45 | `src/tools/BriefTool/prompt.ts` | 22 | PI-01 | LOW |
| 46 | `src/tools/BriefTool/upload.ts` | 174 |  | LOW |
| 47 | `src/tools/ConfigTool/ConfigTool.ts` | 467 |  | MEDIUM |
| 48 | `src/tools/ConfigTool/UI.tsx` | 37 | PI-01 | LOW |
| 49 | `src/tools/ConfigTool/constants.ts` | 1 | PI-01 | LOW |
| 50 | `src/tools/ConfigTool/prompt.ts` | 93 |  | LOW |
| 51 | `src/tools/ConfigTool/supportedSettings.ts` | 211 |  | MEDIUM |
| 52 | `src/tools/DiscoverSkillsTool/prompt.ts` | 1 | PI-01 | LOW |
| 53 | `src/tools/EnterPlanModeTool/EnterPlanModeTool.ts` | 126 |  | LOW |
| 54 | `src/tools/EnterPlanModeTool/UI.tsx` | 32 | PI-01 | LOW |
| 55 | `src/tools/EnterPlanModeTool/constants.ts` | 1 | PI-01 | LOW |
| 56 | `src/tools/EnterPlanModeTool/prompt.ts` | 170 |  | LOW |
| 57 | `src/tools/EnterWorktreeTool/EnterWorktreeTool.ts` | 127 |  | LOW |
| 58 | `src/tools/EnterWorktreeTool/UI.tsx` | 19 | PI-01 | LOW |
| 59 | `src/tools/EnterWorktreeTool/constants.ts` | 1 | PI-01 | LOW |
| 60 | `src/tools/EnterWorktreeTool/prompt.ts` | 30 | PI-01 | LOW |
| 61 | `src/tools/ExitPlanModeTool/ExitPlanModeV2Tool.ts` | 493 |  | MEDIUM |
| 62 | `src/tools/ExitPlanModeTool/UI.tsx` | 81 |  | LOW |
| 63 | `src/tools/ExitPlanModeTool/constants.ts` | 2 | PI-01 | LOW |
| 64 | `src/tools/ExitPlanModeTool/prompt.ts` | 29 | PI-01 | LOW |
| 65 | `src/tools/ExitWorktreeTool/ExitWorktreeTool.ts` | 329 |  | MEDIUM |
| 66 | `src/tools/ExitWorktreeTool/UI.tsx` | 24 | PI-01 | LOW |
| 67 | `src/tools/ExitWorktreeTool/constants.ts` | 1 | PI-01 | LOW |
| 68 | `src/tools/ExitWorktreeTool/prompt.ts` | 32 | PI-01 | LOW |
| 69 | `src/tools/FileEditTool/FileEditTool.ts` | 625 |  | MEDIUM |
| 70 | `src/tools/FileEditTool/UI.tsx` | 288 |  | MEDIUM |
| 71 | `src/tools/FileEditTool/constants.ts` | 11 | PI-01 | LOW |
| 72 | `src/tools/FileEditTool/prompt.ts` | 28 | PI-01 | LOW |
| 73 | `src/tools/FileEditTool/types.ts` | 85 |  | LOW |
| 74 | `src/tools/FileEditTool/utils.ts` | 775 |  | MEDIUM |
| 75 | `src/tools/FileReadTool/FileReadTool.ts` | 1183 |  | HIGH |
| 76 | `src/tools/FileReadTool/UI.tsx` | 184 |  | LOW |
| 77 | `src/tools/FileReadTool/imageProcessor.ts` | 94 |  | LOW |
| 78 | `src/tools/FileReadTool/limits.ts` | 92 |  | LOW |
| 79 | `src/tools/FileReadTool/prompt.ts` | 49 | PI-01 | LOW |
| 80 | `src/tools/FileWriteTool/FileWriteTool.ts` | 434 |  | MEDIUM |
| 81 | `src/tools/FileWriteTool/UI.tsx` | 404 |  | MEDIUM |
| 82 | `src/tools/FileWriteTool/prompt.ts` | 18 | PI-01 | LOW |
| 83 | `src/tools/GlobTool/GlobTool.ts` | 198 |  | LOW |
| 84 | `src/tools/GlobTool/UI.tsx` | 62 |  | LOW |
| 85 | `src/tools/GlobTool/prompt.ts` | 7 | PI-01 | LOW |
| 86 | `src/tools/GrepTool/GrepTool.ts` | 577 |  | MEDIUM |
| 87 | `src/tools/GrepTool/UI.tsx` | 200 |  | LOW |
| 88 | `src/tools/GrepTool/prompt.ts` | 18 | PI-01 | LOW |
| 89 | `src/tools/LSPTool/LSPTool.ts` | 860 |  | MEDIUM |
| 90 | `src/tools/LSPTool/UI.tsx` | 227 |  | MEDIUM |
| 91 | `src/tools/LSPTool/formatters.ts` | 592 |  | MEDIUM |
| 92 | `src/tools/LSPTool/prompt.ts` | 21 | PI-01 | LOW |
| 93 | `src/tools/LSPTool/schemas.ts` | 215 |  | MEDIUM |
| 94 | `src/tools/LSPTool/symbolContext.ts` | 90 |  | LOW |
| 95 | `src/tools/ListMcpResourcesTool/ListMcpResourcesTool.ts` | 123 |  | LOW |
| 96 | `src/tools/ListMcpResourcesTool/UI.tsx` | 28 | PI-01 | LOW |
| 97 | `src/tools/ListMcpResourcesTool/prompt.ts` | 20 | PI-01 | LOW |
| 98 | `src/tools/MCPTool/MCPTool.ts` | 77 |  | LOW |
| 99 | `src/tools/MCPTool/UI.tsx` | 402 |  | MEDIUM |
| 100 | `src/tools/MCPTool/classifyForCollapse.ts` | 604 |  | MEDIUM |
| 101 | `src/tools/MCPTool/prompt.ts` | 3 | PI-01 | LOW |
| 102 | `src/tools/McpAuthTool/McpAuthTool.ts` | 215 |  | MEDIUM |
| 103 | `src/tools/MonitorTool/MonitorTool.ts` | 1 | PI-01 | LOW |
| 104 | `src/tools/NotebookEditTool/NotebookEditTool.ts` | 490 |  | MEDIUM |
| 105 | `src/tools/NotebookEditTool/UI.tsx` | 92 |  | LOW |
| 106 | `src/tools/NotebookEditTool/constants.ts` | 2 | PI-01 | LOW |
| 107 | `src/tools/NotebookEditTool/prompt.ts` | 3 | PI-01 | LOW |
| 108 | `src/tools/OverflowTestTool/OverflowTestTool.ts` | 1 | PI-01 | LOW |
| 109 | `src/tools/PowerShellTool/PowerShellTool.tsx` | 1000 |  | MEDIUM |
| 110 | `src/tools/PowerShellTool/UI.tsx` | 130 |  | LOW |
| 111 | `src/tools/PowerShellTool/clmTypes.ts` | 211 |  | MEDIUM |
| 112 | `src/tools/PowerShellTool/commandSemantics.ts` | 142 |  | LOW |
| 113 | `src/tools/PowerShellTool/commonParameters.ts` | 30 | PI-01 | LOW |
| 114 | `src/tools/PowerShellTool/destructiveCommandWarning.ts` | 109 |  | LOW |
| 115 | `src/tools/PowerShellTool/gitSafety.ts` | 176 |  | LOW |
| 116 | `src/tools/PowerShellTool/modeValidation.ts` | 404 |  | MEDIUM |
| 117 | `src/tools/PowerShellTool/pathValidation.ts` | 2049 |  | HIGH |
| 118 | `src/tools/PowerShellTool/powershellPermissions.ts` | 1648 |  | HIGH |
| 119 | `src/tools/PowerShellTool/powershellSecurity.ts` | 1090 |  | HIGH |
| 120 | `src/tools/PowerShellTool/prompt.ts` | 145 |  | LOW |
| 121 | `src/tools/PowerShellTool/readOnlyValidation.ts` | 1823 |  | HIGH |
| 122 | `src/tools/PowerShellTool/toolName.ts` | 2 | PI-01 | LOW |
| 123 | `src/tools/REPLTool/constants.ts` | 46 | PI-01 | LOW |
| 124 | `src/tools/REPLTool/primitiveTools.ts` | 39 | PI-01 | LOW |
| 125 | `src/tools/ReadMcpResourceTool/ReadMcpResourceTool.ts` | 158 |  | LOW |
| 126 | `src/tools/ReadMcpResourceTool/UI.tsx` | 36 | PI-01 | LOW |
| 127 | `src/tools/ReadMcpResourceTool/prompt.ts` | 16 | PI-01 | LOW |
| 128 | `src/tools/RemoteTriggerTool/RemoteTriggerTool.ts` | 161 |  | LOW |
| 129 | `src/tools/RemoteTriggerTool/UI.tsx` | 16 | PI-01 | LOW |
| 130 | `src/tools/RemoteTriggerTool/prompt.ts` | 15 | PI-01 | LOW |
| 131 | `src/tools/ReviewArtifactTool/ReviewArtifactTool.ts` | 1 | PI-01 | LOW |
| 132 | `src/tools/ScheduleCronTool/CronCreateTool.ts` | 157 |  | LOW |
| 133 | `src/tools/ScheduleCronTool/CronDeleteTool.ts` | 95 |  | LOW |
| 134 | `src/tools/ScheduleCronTool/CronListTool.ts` | 97 |  | LOW |
| 135 | `src/tools/ScheduleCronTool/UI.tsx` | 59 |  | LOW |
| 136 | `src/tools/ScheduleCronTool/prompt.ts` | 135 |  | LOW |
| 137 | `src/tools/SendMessageTool/SendMessageTool.ts` | 917 |  | MEDIUM |
| 138 | `src/tools/SendMessageTool/UI.tsx` | 30 | PI-01 | LOW |
| 139 | `src/tools/SendMessageTool/constants.ts` | 1 | PI-01 | LOW |
| 140 | `src/tools/SendMessageTool/prompt.ts` | 49 | PI-01 | LOW |
| 141 | `src/tools/SendUserFileTool/prompt.ts` | 1 | PI-01 | LOW |
| 142 | `src/tools/SkillTool/SkillTool.ts` | 1108 |  | HIGH |
| 143 | `src/tools/SkillTool/UI.tsx` | 127 |  | LOW |
| 144 | `src/tools/SkillTool/constants.ts` | 1 | PI-01 | LOW |
| 145 | `src/tools/SkillTool/prompt.ts` | 241 |  | MEDIUM |
| 146 | `src/tools/SleepTool/prompt.ts` | 17 | PI-01 | LOW |
| 147 | `src/tools/SnipTool/prompt.ts` | 1 | PI-01 | LOW |
| 148 | `src/tools/SyntheticOutputTool/SyntheticOutputTool.ts` | 163 |  | LOW |
| 149 | `src/tools/TaskCreateTool/TaskCreateTool.ts` | 138 |  | LOW |
| 150 | `src/tools/TaskCreateTool/constants.ts` | 1 | PI-01 | LOW |
| 151 | `src/tools/TaskCreateTool/prompt.ts` | 56 |  | LOW |
| 152 | `src/tools/TaskGetTool/TaskGetTool.ts` | 128 |  | LOW |
| 153 | `src/tools/TaskGetTool/constants.ts` | 1 | PI-01 | LOW |
| 154 | `src/tools/TaskGetTool/prompt.ts` | 24 | PI-01 | LOW |
| 155 | `src/tools/TaskListTool/TaskListTool.ts` | 116 |  | LOW |
| 156 | `src/tools/TaskListTool/constants.ts` | 1 | PI-01 | LOW |
| 157 | `src/tools/TaskListTool/prompt.ts` | 49 | PI-01 | LOW |
| 158 | `src/tools/TaskOutputTool/TaskOutputTool.tsx` | 583 |  | MEDIUM |
| 159 | `src/tools/TaskOutputTool/constants.ts` | 1 | PI-01 | LOW |
| 160 | `src/tools/TaskStopTool/TaskStopTool.ts` | 131 |  | LOW |
| 161 | `src/tools/TaskStopTool/UI.tsx` | 40 | PI-01 | LOW |
| 162 | `src/tools/TaskStopTool/prompt.ts` | 8 | PI-01 | LOW |
| 163 | `src/tools/TaskUpdateTool/TaskUpdateTool.ts` | 406 |  | MEDIUM |
| 164 | `src/tools/TaskUpdateTool/constants.ts` | 1 | PI-01 | LOW |
| 165 | `src/tools/TaskUpdateTool/prompt.ts` | 77 |  | LOW |
| 166 | `src/tools/TeamCreateTool/TeamCreateTool.ts` | 240 |  | MEDIUM |
| 167 | `src/tools/TeamCreateTool/UI.tsx` | 5 | PI-01 | LOW |
| 168 | `src/tools/TeamCreateTool/constants.ts` | 1 | PI-01 | LOW |
| 169 | `src/tools/TeamCreateTool/prompt.ts` | 113 |  | LOW |
| 170 | `src/tools/TeamDeleteTool/TeamDeleteTool.ts` | 139 |  | LOW |
| 171 | `src/tools/TeamDeleteTool/UI.tsx` | 19 | PI-01 | LOW |
| 172 | `src/tools/TeamDeleteTool/constants.ts` | 1 | PI-01 | LOW |
| 173 | `src/tools/TeamDeleteTool/prompt.ts` | 16 | PI-01 | LOW |
| 174 | `src/tools/TerminalCaptureTool/prompt.ts` | 1 | PI-01 | LOW |
| 175 | `src/tools/TodoWriteTool/TodoWriteTool.ts` | 115 |  | LOW |
| 176 | `src/tools/TodoWriteTool/constants.ts` | 1 | PI-01 | LOW |
| 177 | `src/tools/TodoWriteTool/prompt.ts` | 184 |  | LOW |
| 178 | `src/tools/ToolSearchTool/ToolSearchTool.ts` | 471 |  | MEDIUM |
| 179 | `src/tools/ToolSearchTool/constants.ts` | 1 | PI-01 | LOW |
| 180 | `src/tools/ToolSearchTool/prompt.ts` | 121 |  | LOW |
| 181 | `src/tools/TungstenTool/TungstenLiveMonitor.tsx` | 3 | PI-01 | LOW |
| 182 | `src/tools/TungstenTool/TungstenTool.ts` | 50 | PI-01 | LOW |
| 183 | `src/tools/VerifyPlanExecutionTool/constants.ts` | 1 | PI-01 | LOW |
| 184 | `src/tools/WebBrowserTool/WebBrowserPanel.tsx` | 3 | PI-01 | LOW |
| 185 | `src/tools/WebFetchTool/UI.tsx` | 71 |  | LOW |
| 186 | `src/tools/WebFetchTool/WebFetchTool.ts` | 318 |  | MEDIUM |
| 187 | `src/tools/WebFetchTool/preapproved.ts` | 166 |  | LOW |
| 188 | `src/tools/WebFetchTool/prompt.ts` | 46 | PI-01 | LOW |
| 189 | `src/tools/WebFetchTool/utils.ts` | 530 |  | MEDIUM |
| 190 | `src/tools/WebSearchTool/UI.tsx` | 100 |  | LOW |
| 191 | `src/tools/WebSearchTool/WebSearchTool.ts` | 435 |  | MEDIUM |
| 192 | `src/tools/WebSearchTool/prompt.ts` | 34 | PI-01 | LOW |
| 193 | `src/tools/WorkflowTool/WorkflowPermissionRequest.tsx` | 3 | PI-01 | LOW |
| 194 | `src/tools/WorkflowTool/WorkflowTool.ts` | 1 | PI-01 | LOW |
| 195 | `src/tools/WorkflowTool/constants.ts` | 1 | PI-01 | LOW |
| 196 | `src/tools/WorkflowTool/createWorkflowCommand.ts` | 3 | PI-01 | LOW |
| 197 | `src/tools/shared/gitOperationTracking.ts` | 277 |  | MEDIUM |
| 198 | `src/tools/shared/spawnMultiAgent.ts` | 1093 |  | HIGH |
| 199 | `src/tools/testing/TestingPermissionTool.tsx` | 73 |  | LOW |
| 200 | `src/tools/utils.ts` | 40 |  | LOW |
| 201 | `src/utils/toolResultStorage.ts` | 1040 |  | HIGH |

## ML-04-1 (22 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/migrations/migrateBypassPermissionsAcceptedToSettings.ts` | 40 |  | LOW |
| 2 | `src/remote/remotePermissionBridge.ts` | 78 |  | LOW |
| 3 | `src/services/mcp/channelPermissions.ts` | 240 |  | MEDIUM |
| 4 | `src/services/tools/toolHooks.ts` | 650 |  | MEDIUM |
| 5 | `src/utils/permissions/PermissionMode.ts` | 141 |  | LOW |
| 6 | `src/utils/permissions/PermissionPromptToolResultSchema.ts` | 127 |  | LOW |
| 7 | `src/utils/permissions/PermissionResult.ts` | 35 |  | LOW |
| 8 | `src/utils/permissions/PermissionRule.ts` | 40 |  | LOW |
| 9 | `src/utils/permissions/PermissionUpdate.ts` | 389 |  | MEDIUM |
| 10 | `src/utils/permissions/PermissionUpdateSchema.ts` | 78 |  | LOW |
| 11 | `src/utils/permissions/autoModeState.ts` | 39 |  | LOW |
| 12 | `src/utils/permissions/bypassPermissionsKillswitch.ts` | 155 |  | LOW |
| 13 | `src/utils/permissions/classifierDecision.ts` | 98 |  | LOW |
| 14 | `src/utils/permissions/denialTracking.ts` | 45 |  | LOW |
| 15 | `src/utils/permissions/getNextPermissionMode.ts` | 101 |  | LOW |
| 16 | `src/utils/permissions/pathValidation.ts` | 485 |  | MEDIUM |
| 17 | `src/utils/permissions/permissionExplainer.ts` | 250 |  | MEDIUM |
| 18 | `src/utils/permissions/permissionRuleParser.ts` | 198 |  | LOW |
| 19 | `src/utils/permissions/permissions.ts` | 1486 |  | HIGH |
| 20 | `src/utils/permissions/permissionsLoader.ts` | 296 |  | MEDIUM |
| 21 | `src/utils/permissions/shadowedRuleDetection.ts` | 234 |  | MEDIUM |
| 22 | `src/utils/permissions/shellRuleMatching.ts` | 228 |  | MEDIUM |

## ML-04-2 (62 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/components/permissions/AskUserQuestionPermissionRequest/AskUserQuestionPermissionRequest.tsx` | 644 |  | MEDIUM |
| 2 | `src/components/permissions/AskUserQuestionPermissionRequest/PreviewBox.tsx` | 228 |  | MEDIUM |
| 3 | `src/components/permissions/AskUserQuestionPermissionRequest/PreviewQuestionView.tsx` | 327 |  | MEDIUM |
| 4 | `src/components/permissions/AskUserQuestionPermissionRequest/QuestionNavigationBar.tsx` | 177 |  | LOW |
| 5 | `src/components/permissions/AskUserQuestionPermissionRequest/QuestionView.tsx` | 464 |  | MEDIUM |
| 6 | `src/components/permissions/AskUserQuestionPermissionRequest/SubmitQuestionsView.tsx` | 143 |  | LOW |
| 7 | `src/components/permissions/AskUserQuestionPermissionRequest/use-multiple-choice-state.ts` | 179 |  | LOW |
| 8 | `src/components/permissions/BashPermissionRequest/BashPermissionRequest.tsx` | 481 |  | MEDIUM |
| 9 | `src/components/permissions/BashPermissionRequest/bashToolUseOptions.tsx` | 146 |  | LOW |
| 10 | `src/components/permissions/ComputerUseApproval/ComputerUseApproval.tsx` | 440 |  | MEDIUM |
| 11 | `src/components/permissions/EnterPlanModePermissionRequest/EnterPlanModePermissionRequest.tsx` | 121 |  | LOW |
| 12 | `src/components/permissions/ExitPlanModePermissionRequest/ExitPlanModePermissionRequest.tsx` | 767 |  | MEDIUM |
| 13 | `src/components/permissions/FallbackPermissionRequest.tsx` | 332 |  | MEDIUM |
| 14 | `src/components/permissions/FileEditPermissionRequest/FileEditPermissionRequest.tsx` | 181 |  | LOW |
| 15 | `src/components/permissions/FilePermissionDialog/FilePermissionDialog.tsx` | 203 |  | MEDIUM |
| 16 | `src/components/permissions/FilePermissionDialog/ideDiffConfig.ts` | 42 | PI-06 | LOW |
| 17 | `src/components/permissions/FilePermissionDialog/permissionOptions.tsx` | 176 |  | LOW |
| 18 | `src/components/permissions/FilePermissionDialog/useFilePermissionDialog.ts` | 212 |  | MEDIUM |
| 19 | `src/components/permissions/FilePermissionDialog/usePermissionHandler.ts` | 185 |  | LOW |
| 20 | `src/components/permissions/FileWritePermissionRequest/FileWritePermissionRequest.tsx` | 160 |  | LOW |
| 21 | `src/components/permissions/FileWritePermissionRequest/FileWriteToolDiff.tsx` | 88 |  | LOW |
| 22 | `src/components/permissions/FilesystemPermissionRequest/FilesystemPermissionRequest.tsx` | 114 |  | LOW |
| 23 | `src/components/permissions/MonitorPermissionRequest/MonitorPermissionRequest.tsx` | 3 | PI-06 | LOW |
| 24 | `src/components/permissions/NotebookEditPermissionRequest/NotebookEditPermissionRequest.tsx` | 165 |  | LOW |
| 25 | `src/components/permissions/NotebookEditPermissionRequest/NotebookEditToolDiff.tsx` | 234 |  | MEDIUM |
| 26 | `src/components/permissions/PermissionDecisionDebugInfo.tsx` | 459 |  | MEDIUM |
| 27 | `src/components/permissions/PermissionDialog.tsx` | 71 |  | LOW |
| 28 | `src/components/permissions/PermissionExplanation.tsx` | 271 |  | MEDIUM |
| 29 | `src/components/permissions/PermissionPrompt.tsx` | 335 |  | MEDIUM |
| 30 | `src/components/permissions/PermissionRequest.tsx` | 216 |  | MEDIUM |
| 31 | `src/components/permissions/PermissionRequestTitle.tsx` | 65 |  | LOW |
| 32 | `src/components/permissions/PermissionRuleExplanation.tsx` | 120 |  | LOW |
| 33 | `src/components/permissions/PowerShellPermissionRequest/PowerShellPermissionRequest.tsx` | 234 |  | MEDIUM |
| 34 | `src/components/permissions/PowerShellPermissionRequest/powershellToolUseOptions.tsx` | 90 |  | LOW |
| 35 | `src/components/permissions/ReviewArtifactPermissionRequest/ReviewArtifactPermissionRequest.tsx` | 3 | PI-06 | LOW |
| 36 | `src/components/permissions/SandboxPermissionRequest.tsx` | 162 |  | LOW |
| 37 | `src/components/permissions/SedEditPermissionRequest/SedEditPermissionRequest.tsx` | 229 |  | MEDIUM |
| 38 | `src/components/permissions/SkillPermissionRequest/SkillPermissionRequest.tsx` | 368 |  | MEDIUM |
| 39 | `src/components/permissions/WebFetchPermissionRequest/WebFetchPermissionRequest.tsx` | 257 |  | MEDIUM |
| 40 | `src/components/permissions/WorkerBadge.tsx` | 48 | PI-06 | LOW |
| 41 | `src/components/permissions/WorkerPendingPermission.tsx` | 104 |  | LOW |
| 42 | `src/components/permissions/hooks.ts` | 209 |  | MEDIUM |
| 43 | `src/components/permissions/rules/AddPermissionRules.tsx` | 179 |  | LOW |
| 44 | `src/components/permissions/rules/AddWorkspaceDirectory.tsx` | 339 |  | MEDIUM |
| 45 | `src/components/permissions/rules/PermissionRuleDescription.tsx` | 75 |  | LOW |
| 46 | `src/components/permissions/rules/PermissionRuleInput.tsx` | 137 |  | LOW |
| 47 | `src/components/permissions/rules/PermissionRuleList.tsx` | 1178 |  | HIGH |
| 48 | `src/components/permissions/rules/RecentDenialsTab.tsx` | 206 |  | MEDIUM |
| 49 | `src/components/permissions/rules/RemoveWorkspaceDirectory.tsx` | 109 |  | LOW |
| 50 | `src/components/permissions/rules/WorkspaceTab.tsx` | 149 |  | LOW |
| 51 | `src/components/permissions/shellPermissionHelpers.tsx` | 163 |  | LOW |
| 52 | `src/components/permissions/useShellPermissionFeedback.ts` | 148 |  | LOW |
| 53 | `src/components/permissions/utils.ts` | 25 | PI-06 | LOW |
| 54 | `src/utils/permissions/bashClassifier.ts` | 61 |  | LOW |
| 55 | `src/utils/permissions/classifierShared.ts` | 39 |  | LOW |
| 56 | `src/utils/permissions/dangerousPatterns.ts` | 80 |  | LOW |
| 57 | `src/utils/permissions/filesystem.ts` | 1777 |  | HIGH |
| 58 | `src/utils/permissions/permissionSetup.ts` | 1532 |  | HIGH |
| 59 | `src/utils/permissions/yolo-classifier-prompts/auto_mode_system_prompt.txt` | 33 |  | LOW |
| 60 | `src/utils/permissions/yolo-classifier-prompts/permissions_anthropic.txt` | 19 |  | LOW |
| 61 | `src/utils/permissions/yolo-classifier-prompts/permissions_external.txt` | 22 |  | LOW |
| 62 | `src/utils/permissions/yoloClassifier.ts` | 1495 |  | HIGH |

## ML-05 (73 files)

📋 **Summary**: [summary-ML-05-mcp-service-integration](/branches/main/report/summary-ML-05-mcp-service-integration)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/components/mcp/CapabilitiesSection.tsx` | 60 |  | LOW |
| 2 | `src/components/mcp/MCPAgentServerMenu.tsx` | 182 |  | LOW |
| 3 | `src/components/mcp/MCPListPanel.tsx` | 503 |  | MEDIUM |
| 4 | `src/components/mcp/MCPReconnect.tsx` | 166 |  | LOW |
| 5 | `src/components/mcp/MCPRemoteServerMenu.tsx` | 648 |  | MEDIUM |
| 6 | `src/components/mcp/MCPSettings.tsx` | 397 |  | MEDIUM |
| 7 | `src/components/mcp/MCPStdioServerMenu.tsx` | 176 |  | LOW |
| 8 | `src/components/mcp/MCPToolDetailView.tsx` | 211 |  | MEDIUM |
| 9 | `src/components/mcp/MCPToolListView.tsx` | 140 |  | LOW |
| 10 | `src/components/mcp/McpParsingWarnings.tsx` | 212 |  | MEDIUM |
| 11 | `src/components/mcp/index.ts` | 9 | PI-20 | LOW |
| 12 | `src/components/mcp/types.ts` | 7 | PI-20 | LOW |
| 13 | `src/components/mcp/utils/reconnectHelpers.tsx` | 48 | PI-20 | LOW |
| 14 | `src/services/AgentSummary/agentSummary.ts` | 179 | PI-05 | LOW |
| 15 | `src/services/MagicDocs/magicDocs.ts` | 254 | PI-05 | MEDIUM |
| 16 | `src/services/MagicDocs/prompts.ts` | 127 | PI-05 | LOW |
| 17 | `src/services/PromptSuggestion/promptSuggestion.ts` | 523 | PI-05 | MEDIUM |
| 18 | `src/services/PromptSuggestion/speculation.ts` | 991 | PI-05 | MEDIUM |
| 19 | `src/services/analytics/config.ts` | 38 | PI-05 | LOW |
| 20 | `src/services/analytics/datadog.ts` | 307 | PI-05 | MEDIUM |
| 21 | `src/services/analytics/firstPartyEventLogger.ts` | 449 | PI-05 | MEDIUM |
| 22 | `src/services/analytics/firstPartyEventLoggingExporter.ts` | 806 | PI-05 | MEDIUM |
| 23 | `src/services/analytics/index.ts` | 173 | PI-05 | LOW |
| 24 | `src/services/analytics/metadata.ts` | 973 | PI-05 | MEDIUM |
| 25 | `src/services/analytics/sink.ts` | 114 | PI-05 | LOW |
| 26 | `src/services/analytics/sinkKillswitch.ts` | 25 | PI-05 | LOW |
| 27 | `src/services/autoDream/autoDream.ts` | 324 | PI-05 | MEDIUM |
| 28 | `src/services/autoDream/config.ts` | 21 | PI-05 | LOW |
| 29 | `src/services/autoDream/consolidationLock.ts` | 140 | PI-05 | LOW |
| 30 | `src/services/autoDream/consolidationPrompt.ts` | 65 | PI-05 | LOW |
| 31 | `src/services/awaySummary.ts` | 74 | PI-05 | LOW |
| 32 | `src/services/claudeAiLimitsHook.ts` | 23 | PI-05 | LOW |
| 33 | `src/services/diagnosticTracking.ts` | 397 | PI-05 | MEDIUM |
| 34 | `src/services/extractMemories/extractMemories.ts` | 615 | PI-05 | MEDIUM |
| 35 | `src/services/extractMemories/prompts.ts` | 154 | PI-05 | LOW |
| 36 | `src/services/internalLogging.ts` | 90 | PI-05 | LOW |
| 37 | `src/services/lsp/LSPClient.ts` | 447 | PI-05 | MEDIUM |
| 38 | `src/services/lsp/LSPDiagnosticRegistry.ts` | 386 | PI-05 | MEDIUM |
| 39 | `src/services/lsp/LSPServerInstance.ts` | 511 | PI-05 | MEDIUM |
| 40 | `src/services/lsp/LSPServerManager.ts` | 420 | PI-05 | MEDIUM |
| 41 | `src/services/lsp/config.ts` | 79 | PI-05 | LOW |
| 42 | `src/services/lsp/manager.ts` | 289 | PI-05 | MEDIUM |
| 43 | `src/services/lsp/passiveFeedback.ts` | 328 | PI-05 | MEDIUM |
| 44 | `src/services/lsp/types.ts` | 2 | PI-05 | LOW |
| 45 | `src/services/mcpServerApproval.tsx` | 40 | PI-05 | LOW |
| 46 | `src/services/notifier.ts` | 156 | PI-05 | LOW |
| 47 | `src/services/preventSleep.ts` | 165 | PI-05 | LOW |
| 48 | `src/services/rateLimitMessages.ts` | 344 | PI-05 | MEDIUM |
| 49 | `src/services/rateLimitMocking.ts` | 144 | PI-05 | LOW |
| 50 | `src/services/remoteManagedSettings/securityCheck.tsx` | 73 | PI-05 | LOW |
| 51 | `src/services/settingsSync/index.ts` | 581 | PI-05 | MEDIUM |
| 52 | `src/services/settingsSync/types.ts` | 67 | PI-05 | LOW |
| 53 | `src/services/skillSearch/featureCheck.ts` | 3 | PI-05 | LOW |
| 54 | `src/services/skillSearch/localSearch.ts` | 3 | PI-05 | LOW |
| 55 | `src/services/skillSearch/prefetch.ts` | 1 | PI-05 | LOW |
| 56 | `src/services/skillSearch/remoteSkillLoader.ts` | 3 | PI-05 | LOW |
| 57 | `src/services/skillSearch/remoteSkillState.ts` | 3 | PI-05 | LOW |
| 58 | `src/services/skillSearch/signals.ts` | 3 | PI-05 | LOW |
| 59 | `src/services/skillSearch/telemetry.ts` | 1 | PI-05 | LOW |
| 60 | `src/services/teamMemorySync/index.ts` | 1256 | PI-05 | HIGH |
| 61 | `src/services/teamMemorySync/secretScanner.ts` | 324 | PI-05 | MEDIUM |
| 62 | `src/services/teamMemorySync/teamMemSecretGuard.ts` | 44 | PI-05 | LOW |
| 63 | `src/services/teamMemorySync/types.ts` | 156 | PI-05 | LOW |
| 64 | `src/services/teamMemorySync/watcher.ts` | 387 | PI-05 | MEDIUM |
| 65 | `src/services/tips/tipHistory.ts` | 17 | PI-05 | LOW |
| 66 | `src/services/tips/tipRegistry.ts` | 686 | PI-05 | MEDIUM |
| 67 | `src/services/tips/tipScheduler.ts` | 58 | PI-05 | LOW |
| 68 | `src/services/tips/types.ts` | 2 | PI-05 | LOW |
| 69 | `src/services/toolUseSummary/toolUseSummaryGenerator.ts` | 112 | PI-05 | LOW |
| 70 | `src/services/vcr.ts` | 406 | PI-05 | MEDIUM |
| 71 | `src/services/voice.ts` | 525 |  | MEDIUM |
| 72 | `src/services/voiceKeyterms.ts` | 106 | PI-05 | LOW |
| 73 | `src/services/voiceStreamSTT.ts` | 544 |  | MEDIUM |

## ML-05-1 (9 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/mcp/MCPConnectionManager.tsx` | 72 |  | LOW |
| 2 | `src/services/mcp/claudeai.ts` | 164 |  | LOW |
| 3 | `src/services/mcp/config.ts` | 1578 |  | HIGH |
| 4 | `src/services/mcp/envExpansion.ts` | 38 |  | LOW |
| 5 | `src/services/mcp/mcpStringUtils.ts` | 106 |  | LOW |
| 6 | `src/services/mcp/normalization.ts` | 23 |  | LOW |
| 7 | `src/services/mcp/officialRegistry.ts` | 72 |  | LOW |
| 8 | `src/services/mcp/types.ts` | 258 |  | MEDIUM |
| 9 | `src/services/mcp/useManageMCPConnections.ts` | 1141 |  | HIGH |

## ML-05-2 (10 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/mcp/InProcessTransport.ts` | 63 |  | LOW |
| 2 | `src/services/mcp/SdkControlTransport.ts` | 136 |  | LOW |
| 3 | `src/services/mcp/auth.ts` | 2465 |  | HIGH |
| 4 | `src/services/mcp/client.ts` | 3348 |  | HIGH |
| 5 | `src/services/mcp/elicitationHandler.ts` | 313 |  | MEDIUM |
| 6 | `src/services/mcp/headersHelper.ts` | 138 |  | LOW |
| 7 | `src/services/mcp/oauthPort.ts` | 78 |  | LOW |
| 8 | `src/services/mcp/utils.ts` | 575 |  | MEDIUM |
| 9 | `src/services/mcp/xaa.ts` | 511 |  | MEDIUM |
| 10 | `src/services/mcp/xaaIdpLogin.ts` | 487 |  | MEDIUM |

## ML-05-3 (3 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/mcp/channelAllowlist.ts` | 76 |  | LOW |
| 2 | `src/services/mcp/channelNotification.ts` | 316 |  | MEDIUM |
| 3 | `src/services/mcp/vscodeSdkMcp.ts` | 112 |  | LOW |

## ML-06 (40 files)

📋 **Summary**: [summary-ML-06-auth-session-management](/branches/main/report/summary-ML-06-auth-session-management)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/cli/handlers/auth.ts` | 330 |  | MEDIUM |
| 2 | `src/components/ConsoleOAuthFlow.tsx` | 630 |  | MEDIUM |
| 3 | `src/constants/oauth.ts` | 234 |  | MEDIUM |
| 4 | `src/services/analytics/growthbook.ts` | 1155 |  | HIGH |
| 5 | `src/services/api/bootstrap.ts` | 141 |  | LOW |
| 6 | `src/services/mockRateLimits.ts` | 882 |  | MEDIUM |
| 7 | `src/services/oauth/auth-code-listener.ts` | 211 |  | MEDIUM |
| 8 | `src/services/oauth/client.ts` | 577 |  | MEDIUM |
| 9 | `src/services/oauth/crypto.ts` | 23 |  | LOW |
| 10 | `src/services/oauth/getOauthProfile.ts` | 53 |  | LOW |
| 11 | `src/services/oauth/index.ts` | 198 |  | LOW |
| 12 | `src/services/oauth/types.ts` | 13 |  | LOW |
| 13 | `src/services/policyLimits/index.ts` | 663 |  | MEDIUM |
| 14 | `src/services/policyLimits/types.ts` | 27 |  | LOW |
| 15 | `src/services/remoteManagedSettings/index.ts` | 638 |  | MEDIUM |
| 16 | `src/services/remoteManagedSettings/syncCache.ts` | 112 |  | LOW |
| 17 | `src/services/remoteManagedSettings/syncCacheState.ts` | 96 |  | LOW |
| 18 | `src/services/remoteManagedSettings/types.ts` | 31 |  | LOW |
| 19 | `src/utils/auth.ts` | 2002 |  | HIGH |
| 20 | `src/utils/aws.ts` | 74 |  | LOW |
| 21 | `src/utils/awsAuthStatusManager.ts` | 81 |  | LOW |
| 22 | `src/utils/execFileNoThrow.ts` | 150 |  | LOW |
| 23 | `src/utils/http.ts` | 136 |  | LOW |
| 24 | `src/utils/secureStorage/fallbackStorage.ts` | 70 |  | LOW |
| 25 | `src/utils/secureStorage/index.ts` | 17 |  | LOW |
| 26 | `src/utils/secureStorage/keychainPrefetch.ts` | 116 |  | LOW |
| 27 | `src/utils/secureStorage/macOsKeychainHelpers.ts` | 111 |  | LOW |
| 28 | `src/utils/secureStorage/macOsKeychainStorage.ts` | 231 |  | MEDIUM |
| 29 | `src/utils/secureStorage/plainTextStorage.ts` | 84 |  | LOW |
| 30 | `src/utils/secureStorage/types.ts` | 7 |  | LOW |
| 31 | `src/utils/telemetry/betaSessionTracing.ts` | 491 |  | MEDIUM |
| 32 | `src/utils/telemetry/bigqueryExporter.ts` | 252 |  | MEDIUM |
| 33 | `src/utils/telemetry/events.ts` | 75 |  | LOW |
| 34 | `src/utils/telemetry/instrumentation.ts` | 825 |  | MEDIUM |
| 35 | `src/utils/telemetry/logger.ts` | 26 | PI-24 | LOW |
| 36 | `src/utils/telemetry/perfettoTracing.ts` | 1120 |  | HIGH |
| 37 | `src/utils/telemetry/pluginTelemetry.ts` | 289 |  | MEDIUM |
| 38 | `src/utils/telemetry/sessionTracing.ts` | 927 |  | MEDIUM |
| 39 | `src/utils/telemetry/skillLoadedEvent.ts` | 39 | PI-24 | LOW |
| 40 | `src/utils/telemetryAttributes.ts` | 71 |  | LOW |

## ML-07 (285 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/buddy/sprites.ts` | 514 |  | MEDIUM |
| 2 | `src/components/AgentProgressLine.tsx` | 135 | PI-13 | LOW |
| 3 | `src/components/App.tsx` | 96 | PI-13 | LOW |
| 4 | `src/components/ApproveApiKey.tsx` | 122 | PI-13 | LOW |
| 5 | `src/components/AutoModeOptInDialog.tsx` | 141 | PI-13 | LOW |
| 6 | `src/components/AutoUpdater.tsx` | 197 | PI-13 | LOW |
| 7 | `src/components/AutoUpdaterWrapper.tsx` | 90 | PI-13 | LOW |
| 8 | `src/components/BaseTextInput.tsx` | 135 | PI-13 | LOW |
| 9 | `src/components/BashModeProgress.tsx` | 55 | PI-13 | LOW |
| 10 | `src/components/BridgeDialog.tsx` | 400 | PI-13 | MEDIUM |
| 11 | `src/components/BypassPermissionsModeDialog.tsx` | 86 | PI-13 | LOW |
| 12 | `src/components/ChannelDowngradeDialog.tsx` | 101 | PI-13 | LOW |
| 13 | `src/components/ClaudeCodeHint/PluginHintMenu.tsx` | 77 | PI-13 | LOW |
| 14 | `src/components/ClaudeInChromeOnboarding.tsx` | 120 | PI-13 | LOW |
| 15 | `src/components/ClaudeMdExternalIncludesDialog.tsx` | 136 | PI-13 | LOW |
| 16 | `src/components/ClickableImageRef.tsx` | 72 | PI-13 | LOW |
| 17 | `src/components/CompactSummary.tsx` | 117 | PI-13 | LOW |
| 18 | `src/components/ConfigurableShortcutHint.tsx` | 56 | PI-13 | LOW |
| 19 | `src/components/ContextSuggestions.tsx` | 46 | PI-13 | LOW |
| 20 | `src/components/ContextVisualization.tsx` | 488 | PI-13 | MEDIUM |
| 21 | `src/components/CoordinatorAgentStatus.tsx` | 272 | PI-13 | MEDIUM |
| 22 | `src/components/CtrlOToExpand.tsx` | 50 | PI-13 | LOW |
| 23 | `src/components/CustomSelect/SelectMulti.tsx` | 212 | PI-13 | MEDIUM |
| 24 | `src/components/CustomSelect/index.ts` | 3 | PI-13 | LOW |
| 25 | `src/components/CustomSelect/option-map.ts` | 50 | PI-13 | LOW |
| 26 | `src/components/CustomSelect/select-input-option.tsx` | 487 | PI-13 | MEDIUM |
| 27 | `src/components/CustomSelect/select-option.tsx` | 67 | PI-13 | LOW |
| 28 | `src/components/CustomSelect/select.tsx` | 689 | PI-13 | MEDIUM |
| 29 | `src/components/CustomSelect/use-multi-select-state.ts` | 414 | PI-13 | MEDIUM |
| 30 | `src/components/CustomSelect/use-select-input.ts` | 287 | PI-13 | MEDIUM |
| 31 | `src/components/CustomSelect/use-select-navigation.ts` | 653 | PI-13 | MEDIUM |
| 32 | `src/components/CustomSelect/use-select-state.ts` | 157 | PI-13 | LOW |
| 33 | `src/components/DesktopHandoff.tsx` | 192 | PI-13 | LOW |
| 34 | `src/components/DesktopUpsell/DesktopUpsellStartup.tsx` | 170 | PI-13 | LOW |
| 35 | `src/components/DevChannelsDialog.tsx` | 104 | PI-13 | LOW |
| 36 | `src/components/DiagnosticsDisplay.tsx` | 94 | PI-13 | LOW |
| 37 | `src/components/EffortIndicator.ts` | 42 | PI-13 | LOW |
| 38 | `src/components/ExportDialog.tsx` | 127 | PI-13 | LOW |
| 39 | `src/components/FallbackToolUseErrorMessage.tsx` | 115 | PI-13 | LOW |
| 40 | `src/components/FallbackToolUseRejectedMessage.tsx` | 15 | PI-13 | LOW |
| 41 | `src/components/FastIcon.tsx` | 45 | PI-13 | LOW |
| 42 | `src/components/Feedback.tsx` | 591 |  | MEDIUM |
| 43 | `src/components/FeedbackSurvey/FeedbackSurveyView.tsx` | 107 | PI-13 | LOW |
| 44 | `src/components/FeedbackSurvey/TranscriptSharePrompt.tsx` | 87 | PI-13 | LOW |
| 45 | `src/components/FeedbackSurvey/submitTranscriptShare.ts` | 112 | PI-13 | LOW |
| 46 | `src/components/FeedbackSurvey/useDebouncedDigitInput.ts` | 82 | PI-13 | LOW |
| 47 | `src/components/FeedbackSurvey/useFeedbackSurvey.tsx` | 295 | PI-13 | MEDIUM |
| 48 | `src/components/FeedbackSurvey/useFrustrationDetection.ts` | 3 | PI-13 | LOW |
| 49 | `src/components/FeedbackSurvey/useMemorySurvey.tsx` | 212 | PI-13 | MEDIUM |
| 50 | `src/components/FeedbackSurvey/usePostCompactSurvey.tsx` | 205 | PI-13 | MEDIUM |
| 51 | `src/components/FeedbackSurvey/useSurveyState.tsx` | 99 | PI-13 | LOW |
| 52 | `src/components/FeedbackSurvey/utils.ts` | 8 | PI-13 | LOW |
| 53 | `src/components/FileEditToolDiff.tsx` | 180 | PI-13 | LOW |
| 54 | `src/components/FileEditToolUpdatedMessage.tsx` | 123 | PI-13 | LOW |
| 55 | `src/components/FileEditToolUseRejectedMessage.tsx` | 169 | PI-13 | LOW |
| 56 | `src/components/FilePathLink.tsx` | 42 | PI-13 | LOW |
| 57 | `src/components/GlobalSearchDialog.tsx` | 342 | PI-13 | MEDIUM |
| 58 | `src/components/HelpV2/Commands.tsx` | 81 | PI-13 | LOW |
| 59 | `src/components/HelpV2/General.tsx` | 22 | PI-13 | LOW |
| 60 | `src/components/HelpV2/HelpV2.tsx` | 183 | PI-13 | LOW |
| 61 | `src/components/HighlightedCode.tsx` | 189 | PI-13 | LOW |
| 62 | `src/components/HighlightedCode/Fallback.tsx` | 192 | PI-13 | LOW |
| 63 | `src/components/HistorySearchDialog.tsx` | 117 | PI-13 | LOW |
| 64 | `src/components/IdeAutoConnectDialog.tsx` | 153 | PI-13 | LOW |
| 65 | `src/components/IdeStatusIndicator.tsx` | 57 | PI-13 | LOW |
| 66 | `src/components/InvalidConfigDialog.tsx` | 155 | PI-13 | LOW |
| 67 | `src/components/InvalidSettingsDialog.tsx` | 88 | PI-13 | LOW |
| 68 | `src/components/KeybindingWarnings.tsx` | 54 | PI-13 | LOW |
| 69 | `src/components/LanguagePicker.tsx` | 85 | PI-13 | LOW |
| 70 | `src/components/LogSelector.tsx` | 1574 |  | HIGH |
| 71 | `src/components/LogoV2/AnimatedAsterisk.tsx` | 49 | PI-13 | LOW |
| 72 | `src/components/LogoV2/AnimatedClawd.tsx` | 123 | PI-13 | LOW |
| 73 | `src/components/LogoV2/ChannelsNotice.tsx` | 265 | PI-13 | MEDIUM |
| 74 | `src/components/LogoV2/Clawd.tsx` | 239 | PI-13 | MEDIUM |
| 75 | `src/components/LogoV2/CondensedLogo.tsx` | 160 | PI-13 | LOW |
| 76 | `src/components/LogoV2/EmergencyTip.tsx` | 57 | PI-13 | LOW |
| 77 | `src/components/LogoV2/Feed.tsx` | 111 | PI-13 | LOW |
| 78 | `src/components/LogoV2/FeedColumn.tsx` | 58 | PI-13 | LOW |
| 79 | `src/components/LogoV2/GuestPassesUpsell.tsx` | 69 | PI-13 | LOW |
| 80 | `src/components/LogoV2/LogoV2.tsx` | 542 | PI-13 | MEDIUM |
| 81 | `src/components/LogoV2/Opus1mMergeNotice.tsx` | 54 | PI-13 | LOW |
| 82 | `src/components/LogoV2/OverageCreditUpsell.tsx` | 165 | PI-13 | LOW |
| 83 | `src/components/LogoV2/VoiceModeNotice.tsx` | 67 | PI-13 | LOW |
| 84 | `src/components/LogoV2/WelcomeV2.tsx` | 432 | PI-13 | MEDIUM |
| 85 | `src/components/LogoV2/feedConfigs.tsx` | 91 | PI-13 | LOW |
| 86 | `src/components/LspRecommendation/LspRecommendationMenu.tsx` | 87 | PI-13 | LOW |
| 87 | `src/components/MCPServerApprovalDialog.tsx` | 114 | PI-13 | LOW |
| 88 | `src/components/MCPServerDesktopImportDialog.tsx` | 202 | PI-13 | MEDIUM |
| 89 | `src/components/MCPServerMultiselectDialog.tsx` | 132 | PI-13 | LOW |
| 90 | `src/components/ManagedSettingsSecurityDialog/ManagedSettingsSecurityDialog.tsx` | 148 | PI-13 | LOW |
| 91 | `src/components/ManagedSettingsSecurityDialog/utils.ts` | 144 | PI-13 | LOW |
| 92 | `src/components/Markdown.tsx` | 235 | PI-13 | MEDIUM |
| 93 | `src/components/MarkdownTable.tsx` | 321 | PI-13 | MEDIUM |
| 94 | `src/components/MemoryUsageIndicator.tsx` | 36 | PI-13 | LOW |
| 95 | `src/components/Message.tsx` | 626 |  | MEDIUM |
| 96 | `src/components/MessageModel.tsx` | 42 | PI-13 | LOW |
| 97 | `src/components/MessageResponse.tsx` | 77 | PI-13 | LOW |
| 98 | `src/components/MessageRow.tsx` | 382 | PI-13 | MEDIUM |
| 99 | `src/components/MessageTimestamp.tsx` | 62 | PI-13 | LOW |
| 100 | `src/components/ModelPicker.tsx` | 447 | PI-13 | MEDIUM |
| 101 | `src/components/NativeAutoUpdater.tsx` | 192 | PI-13 | LOW |
| 102 | `src/components/NotebookEditToolUseRejectedMessage.tsx` | 91 | PI-13 | LOW |
| 103 | `src/components/OffscreenFreeze.tsx` | 43 | PI-13 | LOW |
| 104 | `src/components/Onboarding.tsx` | 243 | PI-13 | MEDIUM |
| 105 | `src/components/OutputStylePicker.tsx` | 111 | PI-13 | LOW |
| 106 | `src/components/PackageManagerAutoUpdater.tsx` | 103 | PI-13 | LOW |
| 107 | `src/components/Passes/Passes.tsx` | 183 | PI-13 | LOW |
| 108 | `src/components/PrBadge.tsx` | 96 | PI-13 | LOW |
| 109 | `src/components/PromptInput/HistorySearchInput.tsx` | 50 | PI-13 | LOW |
| 110 | `src/components/PromptInput/IssueFlagBanner.tsx` | 11 | PI-13 | LOW |
| 111 | `src/components/PromptInput/Notifications.tsx` | 331 | PI-13 | MEDIUM |
| 112 | `src/components/PromptInput/PromptInputFooter.tsx` | 190 | PI-13 | LOW |
| 113 | `src/components/PromptInput/PromptInputFooterLeftSide.tsx` | 516 | PI-13 | MEDIUM |
| 114 | `src/components/PromptInput/PromptInputFooterSuggestions.tsx` | 292 | PI-13 | MEDIUM |
| 115 | `src/components/PromptInput/PromptInputHelpMenu.tsx` | 357 | PI-13 | MEDIUM |
| 116 | `src/components/PromptInput/PromptInputModeIndicator.tsx` | 92 | PI-13 | LOW |
| 117 | `src/components/PromptInput/PromptInputQueuedCommands.tsx` | 116 | PI-13 | LOW |
| 118 | `src/components/PromptInput/PromptInputStashNotice.tsx` | 24 | PI-13 | LOW |
| 119 | `src/components/PromptInput/SandboxPromptFooterHint.tsx` | 63 | PI-13 | LOW |
| 120 | `src/components/PromptInput/ShimmeredInput.tsx` | 142 | PI-13 | LOW |
| 121 | `src/components/PromptInput/VoiceIndicator.tsx` | 136 | PI-13 | LOW |
| 122 | `src/components/PromptInput/inputModes.ts` | 33 | PI-13 | LOW |
| 123 | `src/components/PromptInput/inputPaste.ts` | 90 | PI-13 | LOW |
| 124 | `src/components/PromptInput/useMaybeTruncateInput.ts` | 58 | PI-13 | LOW |
| 125 | `src/components/PromptInput/usePromptInputPlaceholder.ts` | 76 | PI-13 | LOW |
| 126 | `src/components/PromptInput/useShowFastIconHint.ts` | 31 | PI-13 | LOW |
| 127 | `src/components/PromptInput/useSwarmBanner.ts` | 155 | PI-13 | LOW |
| 128 | `src/components/PromptInput/utils.ts` | 60 | PI-13 | LOW |
| 129 | `src/components/QuickOpenDialog.tsx` | 243 | PI-13 | MEDIUM |
| 130 | `src/components/RemoteEnvironmentDialog.tsx` | 339 | PI-13 | MEDIUM |
| 131 | `src/components/ResumeTask.tsx` | 267 | PI-13 | MEDIUM |
| 132 | `src/components/SandboxViolationExpandedView.tsx` | 98 | PI-13 | LOW |
| 133 | `src/components/SearchBox.tsx` | 71 | PI-13 | LOW |
| 134 | `src/components/SentryErrorBoundary.ts` | 28 | PI-13 | LOW |
| 135 | `src/components/SessionPreview.tsx` | 193 | PI-13 | LOW |
| 136 | `src/components/Settings/Config.tsx` | 1821 | PI-13 | HIGH |
| 137 | `src/components/Settings/Settings.tsx` | 136 | PI-13 | LOW |
| 138 | `src/components/Settings/Status.tsx` | 240 | PI-13 | MEDIUM |
| 139 | `src/components/Settings/Usage.tsx` | 376 | PI-13 | MEDIUM |
| 140 | `src/components/ShowInIDEPrompt.tsx` | 169 | PI-13 | LOW |
| 141 | `src/components/Spinner/FlashingChar.tsx` | 60 | PI-13 | LOW |
| 142 | `src/components/Spinner/GlimmerMessage.tsx` | 327 | PI-13 | MEDIUM |
| 143 | `src/components/Spinner/ShimmerChar.tsx` | 35 | PI-13 | LOW |
| 144 | `src/components/Spinner/SpinnerAnimationRow.tsx` | 264 | PI-13 | MEDIUM |
| 145 | `src/components/Spinner/SpinnerGlyph.tsx` | 79 | PI-13 | LOW |
| 146 | `src/components/Spinner/TeammateSpinnerLine.tsx` | 232 | PI-13 | MEDIUM |
| 147 | `src/components/Spinner/TeammateSpinnerTree.tsx` | 271 | PI-13 | MEDIUM |
| 148 | `src/components/Spinner/index.ts` | 10 | PI-13 | LOW |
| 149 | `src/components/Spinner/teammateSelectHint.ts` | 1 | PI-13 | LOW |
| 150 | `src/components/Spinner/types.ts` | 6 | PI-13 | LOW |
| 151 | `src/components/Spinner/useShimmerAnimation.ts` | 31 | PI-13 | LOW |
| 152 | `src/components/Spinner/useStalledAnimation.ts` | 75 | PI-13 | LOW |
| 153 | `src/components/Spinner/utils.ts` | 84 | PI-13 | LOW |
| 154 | `src/components/Stats.tsx` | 1227 |  | HIGH |
| 155 | `src/components/StatusLine.tsx` | 323 | PI-13 | MEDIUM |
| 156 | `src/components/StatusNotices.tsx` | 54 | PI-13 | LOW |
| 157 | `src/components/StructuredDiff.tsx` | 189 | PI-13 | LOW |
| 158 | `src/components/StructuredDiff/Fallback.tsx` | 486 | PI-13 | MEDIUM |
| 159 | `src/components/StructuredDiff/colorDiff.ts` | 37 | PI-13 | LOW |
| 160 | `src/components/StructuredDiffList.tsx` | 29 | PI-13 | LOW |
| 161 | `src/components/TagTabs.tsx` | 138 | PI-13 | LOW |
| 162 | `src/components/TeleportError.tsx` | 188 | PI-13 | LOW |
| 163 | `src/components/TeleportProgress.tsx` | 139 | PI-13 | LOW |
| 164 | `src/components/TeleportRepoMismatchDialog.tsx` | 103 | PI-13 | LOW |
| 165 | `src/components/TeleportResumeWrapper.tsx` | 166 | PI-13 | LOW |
| 166 | `src/components/TeleportStash.tsx` | 115 | PI-13 | LOW |
| 167 | `src/components/TextInput.tsx` | 123 | PI-13 | LOW |
| 168 | `src/components/ThemePicker.tsx` | 332 | PI-13 | MEDIUM |
| 169 | `src/components/ThinkingToggle.tsx` | 152 | PI-13 | LOW |
| 170 | `src/components/TokenWarning.tsx` | 178 | PI-13 | LOW |
| 171 | `src/components/ToolUseLoader.tsx` | 41 | PI-13 | LOW |
| 172 | `src/components/TrustDialog/TrustDialog.tsx` | 289 | PI-13 | MEDIUM |
| 173 | `src/components/TrustDialog/utils.ts` | 245 | PI-13 | MEDIUM |
| 174 | `src/components/ValidationErrorsList.tsx` | 147 | PI-13 | LOW |
| 175 | `src/components/VimTextInput.tsx` | 139 | PI-13 | LOW |
| 176 | `src/components/WorkflowMultiselectDialog.tsx` | 127 | PI-13 | LOW |
| 177 | `src/components/WorktreeExitDialog.tsx` | 230 | PI-13 | MEDIUM |
| 178 | `src/components/agents/AgentDetail.tsx` | 219 |  | MEDIUM |
| 179 | `src/components/agents/AgentEditor.tsx` | 177 |  | LOW |
| 180 | `src/components/agents/AgentNavigationFooter.tsx` | 25 | PI-09 | LOW |
| 181 | `src/components/agents/AgentsList.tsx` | 439 |  | MEDIUM |
| 182 | `src/components/agents/AgentsMenu.tsx` | 799 |  | MEDIUM |
| 183 | `src/components/agents/ColorPicker.tsx` | 111 |  | LOW |
| 184 | `src/components/agents/ModelSelector.tsx` | 67 |  | LOW |
| 185 | `src/components/agents/ToolSelector.tsx` | 561 |  | MEDIUM |
| 186 | `src/components/agents/agentFileUtils.ts` | 272 |  | MEDIUM |
| 187 | `src/components/agents/generateAgent.ts` | 197 |  | LOW |
| 188 | `src/components/agents/new-agent-creation/CreateAgentWizard.tsx` | 96 |  | LOW |
| 189 | `src/components/agents/new-agent-creation/types.ts` | 1 | PI-09 | LOW |
| 190 | `src/components/agents/new-agent-creation/wizard-steps/ColorStep.tsx` | 83 |  | LOW |
| 191 | `src/components/agents/new-agent-creation/wizard-steps/ConfirmStep.tsx` | 377 |  | MEDIUM |
| 192 | `src/components/agents/new-agent-creation/wizard-steps/ConfirmStepWrapper.tsx` | 73 |  | LOW |
| 193 | `src/components/agents/new-agent-creation/wizard-steps/DescriptionStep.tsx` | 122 |  | LOW |
| 194 | `src/components/agents/new-agent-creation/wizard-steps/GenerateStep.tsx` | 142 |  | LOW |
| 195 | `src/components/agents/new-agent-creation/wizard-steps/LocationStep.tsx` | 79 |  | LOW |
| 196 | `src/components/agents/new-agent-creation/wizard-steps/MemoryStep.tsx` | 112 |  | LOW |
| 197 | `src/components/agents/new-agent-creation/wizard-steps/MethodStep.tsx` | 79 |  | LOW |
| 198 | `src/components/agents/new-agent-creation/wizard-steps/ModelStep.tsx` | 51 |  | LOW |
| 199 | `src/components/agents/new-agent-creation/wizard-steps/PromptStep.tsx` | 127 |  | LOW |
| 200 | `src/components/agents/new-agent-creation/wizard-steps/ToolsStep.tsx` | 60 |  | LOW |
| 201 | `src/components/agents/new-agent-creation/wizard-steps/TypeStep.tsx` | 102 |  | LOW |
| 202 | `src/components/agents/types.ts` | 6 | PI-09 | LOW |
| 203 | `src/components/agents/utils.ts` | 18 | PI-09 | LOW |
| 204 | `src/components/agents/validateAgent.ts` | 109 |  | LOW |
| 205 | `src/components/design-system/Byline.tsx` | 76 |  | LOW |
| 206 | `src/components/design-system/Dialog.tsx` | 137 |  | LOW |
| 207 | `src/components/design-system/Divider.tsx` | 148 |  | LOW |
| 208 | `src/components/design-system/FuzzyPicker.tsx` | 311 |  | MEDIUM |
| 209 | `src/components/design-system/KeyboardShortcutHint.tsx` | 80 |  | LOW |
| 210 | `src/components/design-system/ListItem.tsx` | 243 |  | MEDIUM |
| 211 | `src/components/design-system/LoadingState.tsx` | 93 |  | LOW |
| 212 | `src/components/design-system/Pane.tsx` | 76 |  | LOW |
| 213 | `src/components/design-system/ProgressBar.tsx` | 85 |  | LOW |
| 214 | `src/components/design-system/Ratchet.tsx` | 79 |  | LOW |
| 215 | `src/components/design-system/StatusIcon.tsx` | 94 |  | LOW |
| 216 | `src/components/design-system/Tabs.tsx` | 339 |  | MEDIUM |
| 217 | `src/components/design-system/ThemeProvider.tsx` | 169 |  | LOW |
| 218 | `src/components/design-system/ThemedBox.tsx` | 155 |  | LOW |
| 219 | `src/components/design-system/ThemedText.tsx` | 123 |  | LOW |
| 220 | `src/components/design-system/color.ts` | 30 | PI-15 | LOW |
| 221 | `src/components/diff/DiffDetailView.tsx` | 280 | PI-13 | MEDIUM |
| 222 | `src/components/diff/DiffDialog.tsx` | 382 | PI-13 | MEDIUM |
| 223 | `src/components/diff/DiffFileList.tsx` | 291 | PI-13 | MEDIUM |
| 224 | `src/components/grove/Grove.tsx` | 462 | PI-13 | MEDIUM |
| 225 | `src/components/hooks/HooksConfigMenu.tsx` | 577 |  | MEDIUM |
| 226 | `src/components/hooks/SelectEventMode.tsx` | 126 | PI-13 | LOW |
| 227 | `src/components/hooks/SelectHookMode.tsx` | 111 | PI-13 | LOW |
| 228 | `src/components/hooks/SelectMatcherMode.tsx` | 143 | PI-13 | LOW |
| 229 | `src/components/hooks/ViewHookMode.tsx` | 198 | PI-13 | LOW |
| 230 | `src/components/memory/MemoryFileSelector.tsx` | 437 | PI-13 | MEDIUM |
| 231 | `src/components/memory/MemoryUpdateNotification.tsx` | 44 | PI-13 | LOW |
| 232 | `src/components/sandbox/SandboxConfigTab.tsx` | 44 | PI-13 | LOW |
| 233 | `src/components/sandbox/SandboxDependenciesTab.tsx` | 119 | PI-13 | LOW |
| 234 | `src/components/sandbox/SandboxDoctorSection.tsx` | 45 | PI-13 | LOW |
| 235 | `src/components/sandbox/SandboxOverridesTab.tsx` | 192 | PI-13 | LOW |
| 236 | `src/components/sandbox/SandboxSettings.tsx` | 295 | PI-13 | MEDIUM |
| 237 | `src/components/shell/ExpandShellOutputContext.tsx` | 35 | PI-13 | LOW |
| 238 | `src/components/shell/OutputLine.tsx` | 117 | PI-13 | LOW |
| 239 | `src/components/shell/ShellProgressMessage.tsx` | 149 | PI-13 | LOW |
| 240 | `src/components/shell/ShellTimeDisplay.tsx` | 73 | PI-13 | LOW |
| 241 | `src/components/skills/SkillsMenu.tsx` | 236 | PI-13 | MEDIUM |
| 242 | `src/components/tasks/AsyncAgentDetailDialog.tsx` | 228 | PI-13 | MEDIUM |
| 243 | `src/components/tasks/BackgroundTask.tsx` | 344 | PI-13 | MEDIUM |
| 244 | `src/components/tasks/BackgroundTaskStatus.tsx` | 428 | PI-13 | MEDIUM |
| 245 | `src/components/tasks/BackgroundTasksDialog.tsx` | 651 | PI-13 | MEDIUM |
| 246 | `src/components/tasks/DreamDetailDialog.tsx` | 250 | PI-13 | MEDIUM |
| 247 | `src/components/tasks/InProcessTeammateDetailDialog.tsx` | 265 | PI-13 | MEDIUM |
| 248 | `src/components/tasks/MonitorMcpDetailDialog.tsx` | 3 | PI-13 | LOW |
| 249 | `src/components/tasks/RemoteSessionDetailDialog.tsx` | 903 | PI-13 | MEDIUM |
| 250 | `src/components/tasks/RemoteSessionProgress.tsx` | 242 | PI-13 | MEDIUM |
| 251 | `src/components/tasks/ShellDetailDialog.tsx` | 403 | PI-13 | MEDIUM |
| 252 | `src/components/tasks/ShellProgress.tsx` | 86 | PI-13 | LOW |
| 253 | `src/components/tasks/WorkflowDetailDialog.tsx` | 3 | PI-13 | LOW |
| 254 | `src/components/tasks/renderToolActivity.tsx` | 32 | PI-13 | LOW |
| 255 | `src/components/tasks/taskStatusUtils.tsx` | 106 | PI-13 | LOW |
| 256 | `src/components/teams/TeamStatus.tsx` | 79 | PI-13 | LOW |
| 257 | `src/components/teams/TeamsDialog.tsx` | 714 |  | MEDIUM |
| 258 | `src/components/ui/OrderedList.tsx` | 70 | PI-13 | LOW |
| 259 | `src/components/ui/OrderedListItem.tsx` | 44 | PI-13 | LOW |
| 260 | `src/components/ui/TreeSelect.tsx` | 396 | PI-13 | MEDIUM |
| 261 | `src/components/wizard/WizardDialogLayout.tsx` | 64 | PI-13 | LOW |
| 262 | `src/components/wizard/WizardNavigationFooter.tsx` | 23 | PI-13 | LOW |
| 263 | `src/components/wizard/WizardProvider.tsx` | 212 | PI-13 | MEDIUM |
| 264 | `src/hooks/fileSuggestions.ts` | 811 |  | MEDIUM |
| 265 | `src/hooks/notifs/useAntOrgWarningNotification.ts` | 1 | PI-16 | LOW |
| 266 | `src/hooks/notifs/useAutoModeUnavailableNotification.ts` | 56 |  | LOW |
| 267 | `src/hooks/notifs/useCanSwitchToExistingSubscription.tsx` | 59 |  | LOW |
| 268 | `src/hooks/notifs/useDeprecationWarningNotification.tsx` | 43 | PI-16 | LOW |
| 269 | `src/hooks/notifs/useFastModeNotification.tsx` | 161 |  | LOW |
| 270 | `src/hooks/notifs/useIDEStatusIndicator.tsx` | 185 |  | LOW |
| 271 | `src/hooks/notifs/useInstallMessages.tsx` | 25 | PI-16 | LOW |
| 272 | `src/hooks/notifs/useLspInitializationNotification.tsx` | 142 |  | LOW |
| 273 | `src/hooks/notifs/useMcpConnectivityStatus.tsx` | 87 |  | LOW |
| 274 | `src/hooks/notifs/useModelMigrationNotifications.tsx` | 51 |  | LOW |
| 275 | `src/hooks/notifs/useNpmDeprecationNotification.tsx` | 24 | PI-16 | LOW |
| 276 | `src/hooks/notifs/usePluginAutoupdateNotification.tsx` | 82 |  | LOW |
| 277 | `src/hooks/notifs/usePluginInstallationStatus.tsx` | 127 |  | LOW |
| 278 | `src/hooks/notifs/useRateLimitWarningNotification.tsx` | 113 |  | LOW |
| 279 | `src/hooks/notifs/useSettingsErrors.tsx` | 68 |  | LOW |
| 280 | `src/hooks/notifs/useStartupNotification.ts` | 41 | PI-16 | LOW |
| 281 | `src/hooks/notifs/useTeammateShutdownNotification.ts` | 78 |  | LOW |
| 282 | `src/native-ts/color-diff/index.ts` | 999 |  | MEDIUM |
| 283 | `src/native-ts/yoga-layout/index.ts` | 2578 |  | HIGH |
| 284 | `src/screens/Doctor.tsx` | 574 |  | MEDIUM |
| 285 | `src/vim/operators.ts` | 556 |  | MEDIUM |

## ML-07-1 (104 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/context/fpsMetrics.tsx` | 30 |  | LOW |
| 2 | `src/context/notifications.tsx` | 240 |  | MEDIUM |
| 3 | `src/ink/Ansi.tsx` | 291 |  | MEDIUM |
| 4 | `src/ink/bidi.ts` | 139 |  | LOW |
| 5 | `src/ink/clearTerminal.ts` | 74 |  | LOW |
| 6 | `src/ink/colorize.ts` | 231 |  | MEDIUM |
| 7 | `src/ink/components/AlternateScreen.tsx` | 80 |  | LOW |
| 8 | `src/ink/components/App.tsx` | 685 |  | MEDIUM |
| 9 | `src/ink/components/AppContext.ts` | 21 | PI-07 | LOW |
| 10 | `src/ink/components/Box.tsx` | 213 |  | MEDIUM |
| 11 | `src/ink/components/Button.tsx` | 191 |  | LOW |
| 12 | `src/ink/components/ClockContext.tsx` | 111 |  | LOW |
| 13 | `src/ink/components/CursorDeclarationContext.ts` | 32 | PI-07 | LOW |
| 14 | `src/ink/components/ErrorOverview.tsx` | 108 |  | LOW |
| 15 | `src/ink/components/Link.tsx` | 41 | PI-07 | LOW |
| 16 | `src/ink/components/Newline.tsx` | 38 | PI-07 | LOW |
| 17 | `src/ink/components/NoSelect.tsx` | 67 |  | LOW |
| 18 | `src/ink/components/RawAnsi.tsx` | 56 |  | LOW |
| 19 | `src/ink/components/ScrollBox.tsx` | 237 |  | MEDIUM |
| 20 | `src/ink/components/Spacer.tsx` | 19 | PI-07 | LOW |
| 21 | `src/ink/components/StdinContext.ts` | 49 | PI-07 | LOW |
| 22 | `src/ink/components/TerminalFocusContext.tsx` | 51 |  | LOW |
| 23 | `src/ink/components/TerminalSizeContext.tsx` | 6 | PI-07 | LOW |
| 24 | `src/ink/components/Text.tsx` | 253 |  | MEDIUM |
| 25 | `src/ink/constants.ts` | 2 | PI-07 | LOW |
| 26 | `src/ink/cursor.ts` | 7 | PI-07 | LOW |
| 27 | `src/ink/dom.ts` | 484 |  | MEDIUM |
| 28 | `src/ink/events/click-event.ts` | 38 | PI-07 | LOW |
| 29 | `src/ink/events/dispatcher.ts` | 233 |  | MEDIUM |
| 30 | `src/ink/events/emitter.ts` | 39 | PI-07 | LOW |
| 31 | `src/ink/events/event-handlers.ts` | 73 |  | LOW |
| 32 | `src/ink/events/event.ts` | 11 | PI-07 | LOW |
| 33 | `src/ink/events/focus-event.ts` | 21 | PI-07 | LOW |
| 34 | `src/ink/events/input-event.ts` | 205 |  | MEDIUM |
| 35 | `src/ink/events/keyboard-event.ts` | 51 |  | LOW |
| 36 | `src/ink/events/paste-event.ts` | 1 | PI-07 | LOW |
| 37 | `src/ink/events/resize-event.ts` | 1 | PI-07 | LOW |
| 38 | `src/ink/events/terminal-event.ts` | 107 |  | LOW |
| 39 | `src/ink/events/terminal-focus-event.ts` | 19 | PI-07 | LOW |
| 40 | `src/ink/focus.ts` | 181 |  | LOW |
| 41 | `src/ink/frame.ts` | 124 |  | LOW |
| 42 | `src/ink/get-max-width.ts` | 27 | PI-07 | LOW |
| 43 | `src/ink/global.d.ts` | 1 | PI-07 | LOW |
| 44 | `src/ink/hit-test.ts` | 130 |  | LOW |
| 45 | `src/ink/hooks/use-animation-frame.ts` | 57 |  | LOW |
| 46 | `src/ink/hooks/use-app.ts` | 8 | PI-07 | LOW |
| 47 | `src/ink/hooks/use-declared-cursor.ts` | 73 |  | LOW |
| 48 | `src/ink/hooks/use-input.ts` | 92 |  | LOW |
| 49 | `src/ink/hooks/use-interval.ts` | 67 |  | LOW |
| 50 | `src/ink/hooks/use-search-highlight.ts` | 53 |  | LOW |
| 51 | `src/ink/hooks/use-selection.ts` | 104 |  | LOW |
| 52 | `src/ink/hooks/use-stdin.ts` | 8 | PI-07 | LOW |
| 53 | `src/ink/hooks/use-tab-status.ts` | 72 |  | LOW |
| 54 | `src/ink/hooks/use-terminal-focus.ts` | 16 | PI-07 | LOW |
| 55 | `src/ink/hooks/use-terminal-title.ts` | 31 | PI-07 | LOW |
| 56 | `src/ink/hooks/use-terminal-viewport.ts` | 96 |  | LOW |
| 57 | `src/ink/instances.ts` | 10 | PI-07 | LOW |
| 58 | `src/ink/layout/engine.ts` | 6 | PI-07 | LOW |
| 59 | `src/ink/layout/geometry.ts` | 97 |  | LOW |
| 60 | `src/ink/layout/node.ts` | 152 |  | LOW |
| 61 | `src/ink/layout/yoga.ts` | 308 |  | MEDIUM |
| 62 | `src/ink/line-width-cache.ts` | 24 | PI-07 | LOW |
| 63 | `src/ink/log-update.ts` | 773 |  | MEDIUM |
| 64 | `src/ink/measure-element.ts` | 23 | PI-07 | LOW |
| 65 | `src/ink/measure-text.ts` | 47 | PI-07 | LOW |
| 66 | `src/ink/node-cache.ts` | 54 |  | LOW |
| 67 | `src/ink/optimizer.ts` | 93 |  | LOW |
| 68 | `src/ink/output.ts` | 797 |  | MEDIUM |
| 69 | `src/ink/parse-keypress.ts` | 801 |  | MEDIUM |
| 70 | `src/ink/reconciler.ts` | 512 |  | MEDIUM |
| 71 | `src/ink/render-border.ts` | 231 |  | MEDIUM |
| 72 | `src/ink/render-to-screen.ts` | 231 |  | MEDIUM |
| 73 | `src/ink/renderer.ts` | 178 |  | LOW |
| 74 | `src/ink/root.ts` | 184 |  | LOW |
| 75 | `src/ink/searchHighlight.ts` | 93 |  | LOW |
| 76 | `src/ink/selection.ts` | 917 |  | MEDIUM |
| 77 | `src/ink/squash-text-nodes.ts` | 92 |  | LOW |
| 78 | `src/ink/stringWidth.ts` | 222 |  | MEDIUM |
| 79 | `src/ink/styles.ts` | 771 |  | MEDIUM |
| 80 | `src/ink/supports-hyperlinks.ts` | 57 |  | LOW |
| 81 | `src/ink/tabstops.ts` | 46 | PI-07 | LOW |
| 82 | `src/ink/terminal-focus-state.ts` | 47 | PI-07 | LOW |
| 83 | `src/ink/terminal-querier.ts` | 212 |  | MEDIUM |
| 84 | `src/ink/terminal.ts` | 248 |  | MEDIUM |
| 85 | `src/ink/termio.ts` | 42 | PI-07 | LOW |
| 86 | `src/ink/termio/ansi.ts` | 75 |  | LOW |
| 87 | `src/ink/termio/csi.ts` | 319 |  | MEDIUM |
| 88 | `src/ink/termio/dec.ts` | 60 |  | LOW |
| 89 | `src/ink/termio/esc.ts` | 67 |  | LOW |
| 90 | `src/ink/termio/osc.ts` | 493 |  | MEDIUM |
| 91 | `src/ink/termio/parser.ts` | 394 |  | MEDIUM |
| 92 | `src/ink/termio/sgr.ts` | 308 |  | MEDIUM |
| 93 | `src/ink/termio/tokenize.ts` | 319 |  | MEDIUM |
| 94 | `src/ink/termio/types.ts` | 236 |  | MEDIUM |
| 95 | `src/ink/useTerminalNotification.ts` | 126 |  | LOW |
| 96 | `src/ink/warn.ts` | 9 | PI-07 | LOW |
| 97 | `src/ink/widest-line.ts` | 19 | PI-07 | LOW |
| 98 | `src/ink/wrap-text.ts` | 74 |  | LOW |
| 99 | `src/ink/wrapAnsi.ts` | 20 | PI-07 | LOW |
| 100 | `src/keybindings/KeybindingProviderSetup.tsx` | 308 |  | MEDIUM |
| 101 | `src/keybindings/shortcutFormat.ts` | 63 |  | LOW |
| 102 | `src/keybindings/useShortcutDisplay.ts` | 59 |  | LOW |
| 103 | `src/screens/REPL.tsx` | 5061 |  | HIGH |
| 104 | `src/state/AppState.tsx` | 200 |  | LOW |

## ML-07-2 (7 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/components/FullscreenLayout.tsx` | 637 |  | MEDIUM |
| 2 | `src/components/Messages.tsx` | 834 |  | MEDIUM |
| 3 | `src/components/PromptInput/PromptInput.tsx` | 2339 |  | HIGH |
| 4 | `src/components/ScrollKeybindingHandler.tsx` | 1012 |  | HIGH |
| 5 | `src/components/Spinner.tsx` | 562 |  | MEDIUM |
| 6 | `src/components/VirtualMessageList.tsx` | 1082 |  | HIGH |
| 7 | `src/components/mcp/ElicitationDialog.tsx` | 1169 |  | HIGH |

## ML-07-3 (61 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/components/AwsAuthStatusBox.tsx` | 82 |  | LOW |
| 2 | `src/components/CostThresholdDialog.tsx` | 50 |  | LOW |
| 3 | `src/components/DevBar.tsx` | 49 |  | LOW |
| 4 | `src/components/EffortCallout.tsx` | 265 |  | MEDIUM |
| 5 | `src/components/ExitFlow.tsx` | 48 |  | LOW |
| 6 | `src/components/FeedbackSurvey/FeedbackSurvey.tsx` | 174 |  | LOW |
| 7 | `src/components/IdeOnboardingDialog.tsx` | 167 |  | LOW |
| 8 | `src/components/IdleReturnDialog.tsx` | 118 |  | LOW |
| 9 | `src/components/MessageSelector.tsx` | 831 |  | MEDIUM |
| 10 | `src/components/RemoteCallout.tsx` | 76 |  | LOW |
| 11 | `src/components/SessionBackgroundHint.tsx` | 108 |  | LOW |
| 12 | `src/components/SkillImprovementSurvey.tsx` | 152 |  | LOW |
| 13 | `src/components/TaskListV2.tsx` | 378 |  | MEDIUM |
| 14 | `src/components/TeammateViewHeader.tsx` | 82 |  | LOW |
| 15 | `src/components/hooks/PromptDialog.tsx` | 90 |  | LOW |
| 16 | `src/components/messageActions.tsx` | 450 |  | MEDIUM |
| 17 | `src/components/messages/AdvisorMessage.tsx` | 157 |  | LOW |
| 18 | `src/components/messages/AssistantRedactedThinkingMessage.tsx` | 30 | PI-08 | LOW |
| 19 | `src/components/messages/AssistantTextMessage.tsx` | 269 |  | MEDIUM |
| 20 | `src/components/messages/AssistantThinkingMessage.tsx` | 85 |  | LOW |
| 21 | `src/components/messages/AssistantToolUseMessage.tsx` | 367 |  | MEDIUM |
| 22 | `src/components/messages/AttachmentMessage.tsx` | 535 |  | MEDIUM |
| 23 | `src/components/messages/CollapsedReadSearchContent.tsx` | 483 |  | MEDIUM |
| 24 | `src/components/messages/CompactBoundaryMessage.tsx` | 17 | PI-08 | LOW |
| 25 | `src/components/messages/GroupedToolUseContent.tsx` | 57 |  | LOW |
| 26 | `src/components/messages/HighlightedThinkingText.tsx` | 161 |  | LOW |
| 27 | `src/components/messages/HookProgressMessage.tsx` | 115 |  | LOW |
| 28 | `src/components/messages/PlanApprovalMessage.tsx` | 221 |  | MEDIUM |
| 29 | `src/components/messages/RateLimitMessage.tsx` | 160 |  | LOW |
| 30 | `src/components/messages/ShutdownMessage.tsx` | 131 |  | LOW |
| 31 | `src/components/messages/SnipBoundaryMessage.tsx` | 3 | PI-08 | LOW |
| 32 | `src/components/messages/SystemAPIErrorMessage.tsx` | 140 |  | LOW |
| 33 | `src/components/messages/SystemTextMessage.tsx` | 826 |  | MEDIUM |
| 34 | `src/components/messages/TaskAssignmentMessage.tsx` | 75 |  | LOW |
| 35 | `src/components/messages/UserAgentNotificationMessage.tsx` | 82 |  | LOW |
| 36 | `src/components/messages/UserBashInputMessage.tsx` | 57 |  | LOW |
| 37 | `src/components/messages/UserBashOutputMessage.tsx` | 53 |  | LOW |
| 38 | `src/components/messages/UserChannelMessage.tsx` | 136 |  | LOW |
| 39 | `src/components/messages/UserCommandMessage.tsx` | 107 |  | LOW |
| 40 | `src/components/messages/UserCrossSessionMessage.tsx` | 3 | PI-08 | LOW |
| 41 | `src/components/messages/UserForkBoilerplateMessage.tsx` | 3 | PI-08 | LOW |
| 42 | `src/components/messages/UserGitHubWebhookMessage.tsx` | 3 | PI-08 | LOW |
| 43 | `src/components/messages/UserImageMessage.tsx` | 58 |  | LOW |
| 44 | `src/components/messages/UserLocalCommandOutputMessage.tsx` | 166 |  | LOW |
| 45 | `src/components/messages/UserMemoryInputMessage.tsx` | 74 |  | LOW |
| 46 | `src/components/messages/UserPlanMessage.tsx` | 41 | PI-08 | LOW |
| 47 | `src/components/messages/UserPromptMessage.tsx` | 79 |  | LOW |
| 48 | `src/components/messages/UserResourceUpdateMessage.tsx` | 120 |  | LOW |
| 49 | `src/components/messages/UserTeammateMessage.tsx` | 205 |  | MEDIUM |
| 50 | `src/components/messages/UserTextMessage.tsx` | 275 |  | MEDIUM |
| 51 | `src/components/messages/UserToolResultMessage/RejectedPlanMessage.tsx` | 30 | PI-08 | LOW |
| 52 | `src/components/messages/UserToolResultMessage/RejectedToolUseMessage.tsx` | 15 | PI-08 | LOW |
| 53 | `src/components/messages/UserToolResultMessage/UserToolCanceledMessage.tsx` | 15 | PI-08 | LOW |
| 54 | `src/components/messages/UserToolResultMessage/UserToolErrorMessage.tsx` | 102 |  | LOW |
| 55 | `src/components/messages/UserToolResultMessage/UserToolRejectMessage.tsx` | 94 |  | LOW |
| 56 | `src/components/messages/UserToolResultMessage/UserToolResultMessage.tsx` | 105 |  | LOW |
| 57 | `src/components/messages/UserToolResultMessage/UserToolSuccessMessage.tsx` | 103 |  | LOW |
| 58 | `src/components/messages/UserToolResultMessage/utils.tsx` | 43 | PI-08 | LOW |
| 59 | `src/components/messages/nullRenderingAttachments.ts` | 70 |  | LOW |
| 60 | `src/components/messages/teamMemCollapsed.tsx` | 139 |  | LOW |
| 61 | `src/components/messages/teamMemSaved.ts` | 19 | PI-08 | LOW |

## ML-07-4 (77 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/hooks/useAfterFirstRender.ts` | 17 |  | LOW |
| 2 | `src/hooks/useApiKeyVerification.ts` | 84 |  | LOW |
| 3 | `src/hooks/useArrowKeyHistory.tsx` | 228 |  | MEDIUM |
| 4 | `src/hooks/useAssistantHistory.ts` | 250 |  | MEDIUM |
| 5 | `src/hooks/useAwaySummary.ts` | 125 |  | LOW |
| 6 | `src/hooks/useBackgroundTaskNavigation.ts` | 251 |  | MEDIUM |
| 7 | `src/hooks/useBlink.ts` | 34 | PI-03 | LOW |
| 8 | `src/hooks/useCancelRequest.ts` | 276 |  | MEDIUM |
| 9 | `src/hooks/useChromeExtensionNotification.tsx` | 49 | PI-03 | LOW |
| 10 | `src/hooks/useClaudeCodeHintRecommendation.tsx` | 128 |  | LOW |
| 11 | `src/hooks/useClipboardImageHint.ts` | 77 |  | LOW |
| 12 | `src/hooks/useCommandKeybindings.tsx` | 107 |  | LOW |
| 13 | `src/hooks/useCommandQueue.ts` | 15 |  | LOW |
| 14 | `src/hooks/useCopyOnSelect.ts` | 98 |  | LOW |
| 15 | `src/hooks/useDeferredHookMessages.ts` | 46 |  | LOW |
| 16 | `src/hooks/useDiffData.ts` | 110 |  | LOW |
| 17 | `src/hooks/useDiffInIDE.ts` | 379 |  | MEDIUM |
| 18 | `src/hooks/useDirectConnect.ts` | 229 |  | MEDIUM |
| 19 | `src/hooks/useDoublePress.ts` | 62 |  | LOW |
| 20 | `src/hooks/useDynamicConfig.ts` | 22 | PI-03 | LOW |
| 21 | `src/hooks/useElapsedTime.ts` | 37 | PI-03 | LOW |
| 22 | `src/hooks/useExitOnCtrlCD.ts` | 95 |  | LOW |
| 23 | `src/hooks/useExitOnCtrlCDWithKeybindings.ts` | 24 | PI-03 | LOW |
| 24 | `src/hooks/useFileHistorySnapshotInit.ts` | 25 |  | LOW |
| 25 | `src/hooks/useGlobalKeybindings.tsx` | 248 |  | MEDIUM |
| 26 | `src/hooks/useHistorySearch.ts` | 303 |  | MEDIUM |
| 27 | `src/hooks/useIDEIntegration.tsx` | 69 |  | LOW |
| 28 | `src/hooks/useIdeAtMentioned.ts` | 76 |  | LOW |
| 29 | `src/hooks/useIdeConnectionStatus.ts` | 33 | PI-03 | LOW |
| 30 | `src/hooks/useIdeLogging.ts` | 41 |  | LOW |
| 31 | `src/hooks/useIdeSelection.ts` | 150 |  | LOW |
| 32 | `src/hooks/useInboxPoller.ts` | 969 |  | MEDIUM |
| 33 | `src/hooks/useInputBuffer.ts` | 132 |  | LOW |
| 34 | `src/hooks/useIssueFlagBanner.ts` | 133 |  | LOW |
| 35 | `src/hooks/useLogMessages.ts` | 119 |  | LOW |
| 36 | `src/hooks/useLspPluginRecommendation.tsx` | 193 |  | LOW |
| 37 | `src/hooks/useMailboxBridge.ts` | 21 |  | LOW |
| 38 | `src/hooks/useMainLoopModel.ts` | 34 |  | LOW |
| 39 | `src/hooks/useManagePlugins.ts` | 304 |  | MEDIUM |
| 40 | `src/hooks/useMemoryUsage.ts` | 39 | PI-03 | LOW |
| 41 | `src/hooks/useMergedClients.ts` | 23 |  | LOW |
| 42 | `src/hooks/useMergedCommands.ts` | 15 |  | LOW |
| 43 | `src/hooks/useMergedTools.ts` | 44 |  | LOW |
| 44 | `src/hooks/useMinDisplayTime.ts` | 35 | PI-03 | LOW |
| 45 | `src/hooks/useNotifyAfterTimeout.ts` | 65 |  | LOW |
| 46 | `src/hooks/useOfficialMarketplaceNotification.tsx` | 47 | PI-03 | LOW |
| 47 | `src/hooks/usePasteHandler.ts` | 285 |  | MEDIUM |
| 48 | `src/hooks/usePluginRecommendationBase.tsx` | 104 |  | LOW |
| 49 | `src/hooks/usePrStatus.ts` | 106 |  | LOW |
| 50 | `src/hooks/usePromptSuggestion.ts` | 177 |  | LOW |
| 51 | `src/hooks/usePromptsFromClaudeInChrome.tsx` | 70 |  | LOW |
| 52 | `src/hooks/useQueueProcessor.ts` | 68 |  | LOW |
| 53 | `src/hooks/useRemoteSession.ts` | 605 |  | MEDIUM |
| 54 | `src/hooks/useReplBridge.tsx` | 723 |  | MEDIUM |
| 55 | `src/hooks/useSSHSession.ts` | 241 |  | MEDIUM |
| 56 | `src/hooks/useScheduledTasks.ts` | 139 |  | LOW |
| 57 | `src/hooks/useSearchInput.ts` | 364 |  | MEDIUM |
| 58 | `src/hooks/useSessionBackgrounding.ts` | 158 |  | LOW |
| 59 | `src/hooks/useSettings.ts` | 17 | PI-03 | LOW |
| 60 | `src/hooks/useSettingsChange.ts` | 25 | PI-03 | LOW |
| 61 | `src/hooks/useSkillImprovementSurvey.ts` | 105 |  | LOW |
| 62 | `src/hooks/useSkillsChange.ts` | 62 |  | LOW |
| 63 | `src/hooks/useSwarmInitialization.ts` | 81 |  | LOW |
| 64 | `src/hooks/useSwarmPermissionPoller.ts` | 330 |  | MEDIUM |
| 65 | `src/hooks/useTaskListWatcher.ts` | 221 |  | MEDIUM |
| 66 | `src/hooks/useTasksV2.ts` | 250 |  | MEDIUM |
| 67 | `src/hooks/useTeammateViewAutoExit.ts` | 63 |  | LOW |
| 68 | `src/hooks/useTeleportResume.tsx` | 84 |  | LOW |
| 69 | `src/hooks/useTerminalSize.ts` | 15 |  | LOW |
| 70 | `src/hooks/useTextInput.ts` | 529 |  | MEDIUM |
| 71 | `src/hooks/useTimeout.ts` | 14 | PI-03 | LOW |
| 72 | `src/hooks/useTurnDiffs.ts` | 213 |  | MEDIUM |
| 73 | `src/hooks/useUpdateNotification.ts` | 34 | PI-03 | LOW |
| 74 | `src/hooks/useVimInput.ts` | 316 |  | MEDIUM |
| 75 | `src/hooks/useVirtualScroll.ts` | 721 |  | MEDIUM |
| 76 | `src/hooks/useVoiceEnabled.ts` | 25 | PI-03 | LOW |
| 77 | `src/hooks/useVoiceIntegration.tsx` | 676 |  | MEDIUM |

## ML-07-5 (5 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/hooks/useTypeahead.tsx` | 1385 |  | HIGH |
| 2 | `src/hooks/useVoice.ts` | 1144 |  | HIGH |
| 3 | `src/ink/ink.tsx` | 1723 |  | HIGH |
| 4 | `src/ink/render-node-to-output.ts` | 1462 |  | HIGH |
| 5 | `src/ink/screen.ts` | 1486 |  | HIGH |

## ML-08 (21 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/Task.ts` | 125 |  | LOW |
| 2 | `src/tasks.ts` | 39 |  | LOW |
| 3 | `src/tasks/DreamTask/DreamTask.ts` | 157 |  | LOW |
| 4 | `src/tasks/InProcessTeammateTask/InProcessTeammateTask.tsx` | 125 |  | LOW |
| 5 | `src/tasks/InProcessTeammateTask/types.ts` | 121 |  | LOW |
| 6 | `src/tasks/LocalAgentTask/LocalAgentTask.tsx` | 682 |  | MEDIUM |
| 7 | `src/tasks/LocalMainSessionTask.ts` | 479 |  | MEDIUM |
| 8 | `src/tasks/LocalShellTask/LocalShellTask.tsx` | 522 |  | MEDIUM |
| 9 | `src/tasks/LocalShellTask/guards.ts` | 41 |  | LOW |
| 10 | `src/tasks/LocalShellTask/killShellTasks.ts` | 76 |  | LOW |
| 11 | `src/tasks/LocalWorkflowTask/LocalWorkflowTask.ts` | 5 |  | LOW |
| 12 | `src/tasks/MonitorMcpTask/MonitorMcpTask.ts` | 5 |  | LOW |
| 13 | `src/tasks/RemoteAgentTask/RemoteAgentTask.tsx` | 855 |  | MEDIUM |
| 14 | `src/tasks/pillLabel.ts` | 82 |  | LOW |
| 15 | `src/tasks/stopTask.ts` | 100 |  | LOW |
| 16 | `src/tasks/types.ts` | 46 |  | LOW |
| 17 | `src/utils/task/TaskOutput.ts` | 390 |  | MEDIUM |
| 18 | `src/utils/task/diskOutput.ts` | 451 |  | MEDIUM |
| 19 | `src/utils/task/framework.ts` | 308 |  | MEDIUM |
| 20 | `src/utils/task/outputFormatting.ts` | 38 |  | LOW |
| 21 | `src/utils/task/sdkProgress.ts` | 36 |  | LOW |

## ML-09 (17 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/cli/exit.ts` | 31 | PI-23 | LOW |
| 2 | `src/cli/handlers/agents.ts` | 70 |  | LOW |
| 3 | `src/cli/handlers/autoMode.ts` | 170 |  | LOW |
| 4 | `src/cli/handlers/mcp.tsx` | 361 |  | MEDIUM |
| 5 | `src/cli/handlers/plugins.ts` | 878 |  | MEDIUM |
| 6 | `src/cli/handlers/util.tsx` | 109 |  | LOW |
| 7 | `src/cli/ndjsonSafeStringify.ts` | 32 | PI-23 | LOW |
| 8 | `src/cli/remoteIO.ts` | 255 |  | MEDIUM |
| 9 | `src/cli/transports/HybridTransport.ts` | 282 |  | MEDIUM |
| 10 | `src/cli/transports/SSETransport.ts` | 711 |  | MEDIUM |
| 11 | `src/cli/transports/SerialBatchEventUploader.ts` | 275 |  | MEDIUM |
| 12 | `src/cli/transports/Transport.ts` | 7 | PI-23 | LOW |
| 13 | `src/cli/transports/WebSocketTransport.ts` | 800 |  | MEDIUM |
| 14 | `src/cli/transports/WorkerStateUploader.ts` | 131 |  | LOW |
| 15 | `src/cli/transports/ccrClient.ts` | 998 |  | MEDIUM |
| 16 | `src/cli/transports/transportUtils.ts` | 45 | PI-23 | LOW |
| 17 | `src/cli/update.ts` | 422 |  | MEDIUM |

## ML-09-1 (18 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/bridge/bridgeApi.ts` | 539 |  | MEDIUM |
| 2 | `src/bridge/bridgeConfig.ts` | 48 |  | LOW |
| 3 | `src/bridge/bridgeDebug.ts` | 135 |  | LOW |
| 4 | `src/bridge/bridgeEnabled.ts` | 202 |  | MEDIUM |
| 5 | `src/bridge/capacityWake.ts` | 56 |  | LOW |
| 6 | `src/bridge/debugUtils.ts` | 141 |  | LOW |
| 7 | `src/bridge/envLessBridgeConfig.ts` | 165 |  | LOW |
| 8 | `src/bridge/flushGate.ts` | 71 |  | LOW |
| 9 | `src/bridge/initReplBridge.ts` | 569 |  | MEDIUM |
| 10 | `src/bridge/jwtUtils.ts` | 256 |  | MEDIUM |
| 11 | `src/bridge/pollConfig.ts` | 110 |  | LOW |
| 12 | `src/bridge/pollConfigDefaults.ts` | 82 |  | LOW |
| 13 | `src/bridge/replBridge.ts` | 2406 |  | HIGH |
| 14 | `src/bridge/replBridgeHandle.ts` | 36 |  | LOW |
| 15 | `src/bridge/sessionIdCompat.ts` | 57 |  | LOW |
| 16 | `src/bridge/trustedDevice.ts` | 210 |  | MEDIUM |
| 17 | `src/bridge/types.ts` | 262 |  | MEDIUM |
| 18 | `src/bridge/workSecret.ts` | 127 |  | LOW |

## ML-09-2 (15 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/bridge/bridgeMain.ts` | 2999 |  | HIGH |
| 2 | `src/bridge/bridgeMessaging.ts` | 461 |  | MEDIUM |
| 3 | `src/bridge/bridgePermissionCallbacks.ts` | 43 |  | LOW |
| 4 | `src/bridge/bridgePointer.ts` | 210 |  | MEDIUM |
| 5 | `src/bridge/bridgeStatusUtil.ts` | 163 |  | LOW |
| 6 | `src/bridge/bridgeUI.ts` | 530 |  | MEDIUM |
| 7 | `src/bridge/codeSessionApi.ts` | 168 |  | LOW |
| 8 | `src/bridge/createSession.ts` | 384 |  | MEDIUM |
| 9 | `src/bridge/inboundAttachments.ts` | 175 |  | LOW |
| 10 | `src/bridge/inboundMessages.ts` | 80 |  | LOW |
| 11 | `src/bridge/peerSessions.ts` | 3 |  | LOW |
| 12 | `src/bridge/remoteBridgeCore.ts` | 1008 |  | HIGH |
| 13 | `src/bridge/replBridgeTransport.ts` | 370 |  | MEDIUM |
| 14 | `src/bridge/sessionRunner.ts` | 550 |  | MEDIUM |
| 15 | `src/bridge/webhookSanitizer.ts` | 3 |  | LOW |

## ML-10 (1 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/claudeAiLimits.ts` | 515 |  | MEDIUM |

## ML-10-1 (14 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/services/api/adminRequests.ts` | 119 |  | LOW |
| 2 | `src/services/api/dumpPrompts.ts` | 226 |  | MEDIUM |
| 3 | `src/services/api/emptyUsage.ts` | 22 |  | LOW |
| 4 | `src/services/api/errorUtils.ts` | 260 |  | MEDIUM |
| 5 | `src/services/api/filesApi.ts` | 748 |  | MEDIUM |
| 6 | `src/services/api/firstTokenDate.ts` | 60 |  | LOW |
| 7 | `src/services/api/grove.ts` | 357 |  | MEDIUM |
| 8 | `src/services/api/metricsOptOut.ts` | 159 |  | LOW |
| 9 | `src/services/api/overageCreditGrant.ts` | 137 |  | LOW |
| 10 | `src/services/api/promptCacheBreakDetection.ts` | 727 |  | MEDIUM |
| 11 | `src/services/api/referral.ts` | 281 |  | MEDIUM |
| 12 | `src/services/api/sessionIngress.ts` | 514 |  | MEDIUM |
| 13 | `src/services/api/ultrareviewQuota.ts` | 38 |  | LOW |
| 14 | `src/services/api/usage.ts` | 63 |  | LOW |

## ML-11 (3 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/utils/sessionRestore.ts` | 551 |  | MEDIUM |
| 2 | `src/utils/sessionStorage.ts` | 5105 |  | HIGH |
| 3 | `src/utils/sessionStoragePortable.ts` | 793 |  | MEDIUM |

## ML-11-1 (31 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/memdir/findRelevantMemories.ts` | 141 |  | LOW |
| 2 | `src/memdir/memdir.ts` | 507 |  | MEDIUM |
| 3 | `src/memdir/memoryAge.ts` | 53 |  | LOW |
| 4 | `src/memdir/memoryScan.ts` | 94 |  | LOW |
| 5 | `src/memdir/memoryShapeTelemetry.ts` | 1 |  | LOW |
| 6 | `src/memdir/memoryTypes.ts` | 271 |  | MEDIUM |
| 7 | `src/memdir/paths.ts` | 278 |  | MEDIUM |
| 8 | `src/memdir/teamMemPaths.ts` | 292 |  | MEDIUM |
| 9 | `src/memdir/teamMemPrompts.ts` | 100 |  | LOW |
| 10 | `src/services/SessionMemory/prompts.ts` | 324 |  | MEDIUM |
| 11 | `src/services/SessionMemory/sessionMemory.ts` | 495 |  | MEDIUM |
| 12 | `src/services/SessionMemory/sessionMemoryUtils.ts` | 207 |  | MEDIUM |
| 13 | `src/services/compact/apiMicrocompact.ts` | 153 |  | LOW |
| 14 | `src/services/compact/cachedMCConfig.ts` | 3 |  | LOW |
| 15 | `src/services/compact/compactWarningHook.ts` | 16 |  | LOW |
| 16 | `src/services/compact/compactWarningState.ts` | 18 |  | LOW |
| 17 | `src/services/compact/grouping.ts` | 63 |  | LOW |
| 18 | `src/services/compact/microCompact.ts` | 530 |  | MEDIUM |
| 19 | `src/services/compact/postCompactCleanup.ts` | 77 |  | LOW |
| 20 | `src/services/compact/prompt.ts` | 374 |  | MEDIUM |
| 21 | `src/services/compact/reactiveCompact.ts` | 3 |  | LOW |
| 22 | `src/services/compact/sessionMemoryCompact.ts` | 630 |  | MEDIUM |
| 23 | `src/services/compact/snipCompact.ts` | 10 |  | LOW |
| 24 | `src/services/compact/snipProjection.ts` | 7 |  | LOW |
| 25 | `src/services/compact/timeBasedMCConfig.ts` | 43 |  | LOW |
| 26 | `src/services/contextCollapse/index.ts` | 51 |  | LOW |
| 27 | `src/services/contextCollapse/operations.ts` | 7 |  | LOW |
| 28 | `src/services/contextCollapse/persist.ts` | 1 |  | LOW |
| 29 | `src/services/tokenEstimation.ts` | 495 |  | MEDIUM |
| 30 | `src/utils/contextAnalysis.ts` | 272 |  | MEDIUM |
| 31 | `src/utils/forkedAgent.ts` | 689 |  | MEDIUM |

## ML-12 (72 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/commands/plugin/ManagePlugins.tsx` | 2214 |  | HIGH |
| 2 | `src/commands/plugin/PluginSettings.tsx` | 1071 |  | HIGH |
| 3 | `src/services/plugins/PluginInstallationManager.ts` | 184 |  | LOW |
| 4 | `src/services/plugins/pluginCliCommands.ts` | 344 |  | MEDIUM |
| 5 | `src/services/plugins/pluginOperations.ts` | 1088 |  | HIGH |
| 6 | `src/skills/bundled/batch.ts` | 124 |  | LOW |
| 7 | `src/skills/bundled/claudeApi.ts` | 196 |  | LOW |
| 8 | `src/skills/bundled/claudeApiContent.ts` | 75 |  | LOW |
| 9 | `src/skills/bundled/claudeInChrome.ts` | 34 | PI-10 | LOW |
| 10 | `src/skills/bundled/debug.ts` | 103 |  | LOW |
| 11 | `src/skills/bundled/dream.ts` | 1 | PI-10 | LOW |
| 12 | `src/skills/bundled/hunter.ts` | 1 | PI-10 | LOW |
| 13 | `src/skills/bundled/index.ts` | 79 |  | LOW |
| 14 | `src/skills/bundled/keybindings.ts` | 339 |  | MEDIUM |
| 15 | `src/skills/bundled/loop.ts` | 92 |  | LOW |
| 16 | `src/skills/bundled/loremIpsum.ts` | 282 |  | MEDIUM |
| 17 | `src/skills/bundled/remember.ts` | 82 |  | LOW |
| 18 | `src/skills/bundled/runSkillGenerator.ts` | 1 | PI-10 | LOW |
| 19 | `src/skills/bundled/scheduleRemoteAgents.ts` | 447 |  | MEDIUM |
| 20 | `src/skills/bundled/simplify.ts` | 69 |  | LOW |
| 21 | `src/skills/bundled/skillify.ts` | 197 |  | LOW |
| 22 | `src/skills/bundled/stuck.ts` | 79 |  | LOW |
| 23 | `src/skills/bundled/updateConfig.ts` | 475 |  | MEDIUM |
| 24 | `src/skills/bundled/verify.ts` | 30 | PI-10 | LOW |
| 25 | `src/skills/bundled/verifyContent.ts` | 13 | PI-10 | LOW |
| 26 | `src/skills/bundledSkills.ts` | 220 |  | MEDIUM |
| 27 | `src/skills/loadSkillsDir.ts` | 1086 |  | HIGH |
| 28 | `src/skills/mcpSkillBuilders.ts` | 44 | PI-10 | LOW |
| 29 | `src/utils/plugins/addDirPluginSettings.ts` | 71 |  | LOW |
| 30 | `src/utils/plugins/cacheUtils.ts` | 196 |  | LOW |
| 31 | `src/utils/plugins/dependencyResolver.ts` | 305 |  | MEDIUM |
| 32 | `src/utils/plugins/fetchTelemetry.ts` | 135 |  | LOW |
| 33 | `src/utils/plugins/gitAvailability.ts` | 69 |  | LOW |
| 34 | `src/utils/plugins/headlessPluginInstall.ts` | 174 |  | LOW |
| 35 | `src/utils/plugins/hintRecommendation.ts` | 164 |  | LOW |
| 36 | `src/utils/plugins/installCounts.ts` | 292 |  | MEDIUM |
| 37 | `src/utils/plugins/installedPluginsManager.ts` | 1268 |  | HIGH |
| 38 | `src/utils/plugins/loadPluginAgents.ts` | 348 |  | MEDIUM |
| 39 | `src/utils/plugins/loadPluginCommands.ts` | 946 |  | MEDIUM |
| 40 | `src/utils/plugins/loadPluginHooks.ts` | 287 |  | MEDIUM |
| 41 | `src/utils/plugins/loadPluginOutputStyles.ts` | 178 |  | LOW |
| 42 | `src/utils/plugins/lspPluginIntegration.ts` | 387 |  | MEDIUM |
| 43 | `src/utils/plugins/lspRecommendation.ts` | 374 |  | MEDIUM |
| 44 | `src/utils/plugins/managedPlugins.ts` | 27 |  | LOW |
| 45 | `src/utils/plugins/marketplaceHelpers.ts` | 592 |  | MEDIUM |
| 46 | `src/utils/plugins/marketplaceManager.ts` | 2643 |  | HIGH |
| 47 | `src/utils/plugins/mcpPluginIntegration.ts` | 634 |  | MEDIUM |
| 48 | `src/utils/plugins/mcpbHandler.ts` | 968 |  | MEDIUM |
| 49 | `src/utils/plugins/officialMarketplace.ts` | 25 |  | LOW |
| 50 | `src/utils/plugins/officialMarketplaceGcs.ts` | 216 |  | MEDIUM |
| 51 | `src/utils/plugins/officialMarketplaceStartupCheck.ts` | 439 |  | MEDIUM |
| 52 | `src/utils/plugins/orphanedPluginFilter.ts` | 114 |  | LOW |
| 53 | `src/utils/plugins/parseMarketplaceInput.ts` | 162 |  | LOW |
| 54 | `src/utils/plugins/performStartupChecks.tsx` | 69 |  | LOW |
| 55 | `src/utils/plugins/pluginAutoupdate.ts` | 284 |  | MEDIUM |
| 56 | `src/utils/plugins/pluginBlocklist.ts` | 127 |  | LOW |
| 57 | `src/utils/plugins/pluginDirectories.ts` | 178 |  | LOW |
| 58 | `src/utils/plugins/pluginFlagging.ts` | 208 |  | MEDIUM |
| 59 | `src/utils/plugins/pluginIdentifier.ts` | 123 |  | LOW |
| 60 | `src/utils/plugins/pluginInstallationHelpers.ts` | 595 |  | MEDIUM |
| 61 | `src/utils/plugins/pluginLoader.ts` | 3302 |  | HIGH |
| 62 | `src/utils/plugins/pluginOptionsStorage.ts` | 400 |  | MEDIUM |
| 63 | `src/utils/plugins/pluginPolicy.ts` | 20 |  | LOW |
| 64 | `src/utils/plugins/pluginStartupCheck.ts` | 341 |  | MEDIUM |
| 65 | `src/utils/plugins/pluginVersioning.ts` | 157 |  | LOW |
| 66 | `src/utils/plugins/reconciler.ts` | 265 |  | MEDIUM |
| 67 | `src/utils/plugins/refresh.ts` | 215 |  | MEDIUM |
| 68 | `src/utils/plugins/schemas.ts` | 1681 |  | HIGH |
| 69 | `src/utils/plugins/validatePlugin.ts` | 903 |  | MEDIUM |
| 70 | `src/utils/plugins/walkPluginMarkdown.ts` | 69 |  | LOW |
| 71 | `src/utils/plugins/zipCache.ts` | 406 |  | MEDIUM |
| 72 | `src/utils/plugins/zipCacheAdapters.ts` | 164 |  | LOW |

## ML-13 (37 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/utils/bash/ParsedCommand.ts` | 318 |  | MEDIUM |
| 2 | `src/utils/bash/ShellSnapshot.ts` | 582 |  | MEDIUM |
| 3 | `src/utils/bash/ast.ts` | 2679 |  | HIGH |
| 4 | `src/utils/bash/bashParser.ts` | 4436 |  | HIGH |
| 5 | `src/utils/bash/bashPipeCommand.ts` | 294 |  | MEDIUM |
| 6 | `src/utils/bash/commands.ts` | 1339 |  | HIGH |
| 7 | `src/utils/bash/heredoc.ts` | 733 |  | MEDIUM |
| 8 | `src/utils/bash/parser.ts` | 230 |  | MEDIUM |
| 9 | `src/utils/bash/prefix.ts` | 204 |  | MEDIUM |
| 10 | `src/utils/bash/registry.ts` | 53 |  | LOW |
| 11 | `src/utils/bash/shellCompletion.ts` | 259 |  | MEDIUM |
| 12 | `src/utils/bash/shellPrefix.ts` | 28 |  | LOW |
| 13 | `src/utils/bash/shellQuote.ts` | 304 |  | MEDIUM |
| 14 | `src/utils/bash/shellQuoting.ts` | 128 |  | LOW |
| 15 | `src/utils/bash/specs/alias.ts` | 14 |  | LOW |
| 16 | `src/utils/bash/specs/index.ts` | 18 |  | LOW |
| 17 | `src/utils/bash/specs/nohup.ts` | 13 |  | LOW |
| 18 | `src/utils/bash/specs/pyright.ts` | 91 |  | LOW |
| 19 | `src/utils/bash/specs/sleep.ts` | 13 |  | LOW |
| 20 | `src/utils/bash/specs/srun.ts` | 31 |  | LOW |
| 21 | `src/utils/bash/specs/time.ts` | 13 |  | LOW |
| 22 | `src/utils/bash/specs/timeout.ts` | 20 |  | LOW |
| 23 | `src/utils/bash/treeSitterAnalysis.ts` | 506 |  | MEDIUM |
| 24 | `src/utils/powershell/dangerousCmdlets.ts` | 185 |  | LOW |
| 25 | `src/utils/powershell/parser.ts` | 1804 |  | HIGH |
| 26 | `src/utils/powershell/staticPrefix.ts` | 316 |  | MEDIUM |
| 27 | `src/utils/sandbox/sandbox-adapter.ts` | 985 |  | MEDIUM |
| 28 | `src/utils/shell/bashProvider.ts` | 255 |  | MEDIUM |
| 29 | `src/utils/shell/outputLimits.ts` | 14 |  | LOW |
| 30 | `src/utils/shell/powershellDetection.ts` | 107 |  | LOW |
| 31 | `src/utils/shell/powershellProvider.ts` | 123 |  | LOW |
| 32 | `src/utils/shell/prefix.ts` | 367 |  | MEDIUM |
| 33 | `src/utils/shell/readOnlyCommandValidation.ts` | 1893 |  | HIGH |
| 34 | `src/utils/shell/resolveDefaultShell.ts` | 14 |  | LOW |
| 35 | `src/utils/shell/shellProvider.ts` | 33 |  | LOW |
| 36 | `src/utils/shell/shellToolUtils.ts` | 22 |  | LOW |
| 37 | `src/utils/shell/specPrefix.ts` | 241 |  | MEDIUM |

## ML-14 (22 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/utils/swarm/It2SetupPrompt.tsx` | 379 |  | MEDIUM |
| 2 | `src/utils/swarm/backends/ITermBackend.ts` | 370 |  | MEDIUM |
| 3 | `src/utils/swarm/backends/InProcessBackend.ts` | 339 |  | MEDIUM |
| 4 | `src/utils/swarm/backends/PaneBackendExecutor.ts` | 354 |  | MEDIUM |
| 5 | `src/utils/swarm/backends/TmuxBackend.ts` | 764 |  | MEDIUM |
| 6 | `src/utils/swarm/backends/detection.ts` | 128 |  | LOW |
| 7 | `src/utils/swarm/backends/it2Setup.ts` | 245 |  | MEDIUM |
| 8 | `src/utils/swarm/backends/registry.ts` | 464 |  | MEDIUM |
| 9 | `src/utils/swarm/backends/teammateModeSnapshot.ts` | 87 |  | LOW |
| 10 | `src/utils/swarm/backends/types.ts` | 311 |  | MEDIUM |
| 11 | `src/utils/swarm/constants.ts` | 33 |  | LOW |
| 12 | `src/utils/swarm/inProcessRunner.ts` | 1552 |  | HIGH |
| 13 | `src/utils/swarm/leaderPermissionBridge.ts` | 54 |  | LOW |
| 14 | `src/utils/swarm/permissionSync.ts` | 928 |  | MEDIUM |
| 15 | `src/utils/swarm/reconnection.ts` | 119 |  | LOW |
| 16 | `src/utils/swarm/spawnInProcess.ts` | 328 |  | MEDIUM |
| 17 | `src/utils/swarm/spawnUtils.ts` | 146 |  | LOW |
| 18 | `src/utils/swarm/teamHelpers.ts` | 683 |  | MEDIUM |
| 19 | `src/utils/swarm/teammateInit.ts` | 129 |  | LOW |
| 20 | `src/utils/swarm/teammateLayoutManager.ts` | 107 |  | LOW |
| 21 | `src/utils/swarm/teammateModel.ts` | 10 |  | LOW |
| 22 | `src/utils/swarm/teammatePromptAddendum.ts` | 18 |  | LOW |

## ML-15 (9 files)

| # | File | Lines | Pattern | Risk |
|---|------|-------|---------|------|
| 1 | `src/entrypoints/sdk/controlSchemas.ts` | 663 |  | MEDIUM |
| 2 | `src/entrypoints/sdk/controlTypes.ts` | 62 |  | LOW |
| 3 | `src/entrypoints/sdk/coreSchemas.ts` | 1889 |  | HIGH |
| 4 | `src/entrypoints/sdk/coreTypes.generated.ts` | 10 |  | LOW |
| 5 | `src/entrypoints/sdk/coreTypes.ts` | 62 |  | LOW |
| 6 | `src/entrypoints/sdk/runtimeTypes.ts` | 22 |  | LOW |
| 7 | `src/entrypoints/sdk/sdkUtilityTypes.ts` | 6 |  | LOW |
| 8 | `src/entrypoints/sdk/settingsTypes.generated.ts` | 1 |  | LOW |
| 9 | `src/entrypoints/sdk/toolTypes.ts` | 1 |  | LOW |
