&lt;!-- analysis-version: 0 | commit: a5179f6588dd03cbe83a8d8b718a61875dba7b24 | updated: 2025-07-18 | mode: full | task: T-07 --&gt;
# T-07 Analysis: Permission AI Classifier & Filesystem

## Scope Confirmation
- Task ID: T-07
- Primary Mainline: ML-04
- ML Priority: P1
- Analysis Depth: DEEP
- Secondary Mainlines: []
- Pattern Coverage: N/A
- Scope Files (confirmed): 55 files, 16,761 lines total
- Scope adjustments: None -- all 55 files verified on disk

## File Roles

| File | Lines | One-liner Role | Where Analyzed |
|------|-------|----------------|---------------|
| src/utils/permissions/yoloClassifier.ts | 1495 | Core AI classifier for auto-mode allow/block decisions using sideQuery LLM calls | DEEP: S Function-Level Analysis |
| src/utils/permissions/permissionSetup.ts | 1532 | Permission context initialization, auto-mode gate verification, dangerous permission detection and stripping | DEEP: S Function-Level Analysis |
| src/utils/permissions/filesystem.ts | 1777 | Filesystem permission checks (read/write), path safety validation, rule matching, suggestion generation | DEEP: S Function-Level Analysis |
| src/components/permissions/rules/PermissionRuleList.tsx | 1179 | UI component displaying all permission rules with add/remove/edit capabilities | DEEP: S Analysis Findings |
| src/utils/permissions/bashClassifier.ts | 61 | External-build stub for Bash command semantic classifier (ANT-only feature) | DEEP: S Analysis Findings |
| src/utils/permissions/classifierShared.ts | 39 | Shared utilities for extracting tool use blocks and parsing classifier responses | DEEP: S Analysis Findings |
| src/utils/permissions/dangerousPatterns.ts | 80 | Pattern lists for dangerous shell allow-rule prefixes (interpreters, package runners) | DEEP: S Analysis Findings |
| src/components/permissions/PermissionRequest.tsx | 216 | Top-level permission request dispatcher routing to tool-specific permission UIs | DEEP: S Analysis Findings |
| src/components/permissions/PermissionPrompt.tsx | 335 | Permission prompt rendering with allow/deny buttons and rule suggestions | DEEP: S Analysis Findings |
| src/components/permissions/PermissionDialog.tsx | 71 | Ink dialog wrapper for permission request modals | DEEP: S Analysis Findings |
| src/components/permissions/PermissionExplanation.tsx | 271 | Risk-level explanation UI with shimmer loading and color-coded risk indicators | DEEP: S Analysis Findings |
| src/components/permissions/PermissionDecisionDebugInfo.tsx | 459 | Debug panel showing decision reason, suggested rules, and classifier details | DEEP: S Analysis Findings |
| src/components/permissions/hooks.ts | 209 | usePermissionRequestLogging hook for analytics event tracking on permission prompts | DEEP: S Analysis Findings |
| src/components/permissions/FallbackPermissionRequest.tsx | 332 | Generic fallback permission UI for tools without specialized request components | DEEP: S Analysis Findings |
| src/components/permissions/SandboxPermissionRequest.tsx | 162 | Permission UI for sandbox-related tool operations | DEEP: S Analysis Findings |
| src/components/permissions/PermissionRequestTitle.tsx | 65 | Renders permission request title with tool name and path information | DEEP: S Analysis Findings |
| src/components/permissions/PermissionRuleExplanation.tsx | 120 | Explains permission rule effects and source (settings/CLI/session) | DEEP: S Analysis Findings |
| src/components/permissions/utils.ts | 25 | Utility for logging unary permission events to analytics | DEEP: S Analysis Findings |
| src/components/permissions/BashPermissionRequest/BashPermissionRequest.tsx | 482 | Bash-specific permission request UI with command preview and allow-rule options | DEEP: S Analysis Findings |
| src/components/permissions/BashPermissionRequest/bashToolUseOptions.tsx | 147 | Tool use option buttons for Bash permission (allow-prefix, allow-all, deny) | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/AskUserQuestionPermissionRequest.tsx | 645 | Multi-question permission request UI with navigation bar and preview | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/PreviewBox.tsx | 229 | Preview box component for question content display | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/PreviewQuestionView.tsx | 328 | Question preview view with answer display | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/QuestionNavigationBar.tsx | 178 | Navigation bar for stepping through multiple permission questions | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/QuestionView.tsx | 465 | Single question view with multiple-choice state management | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/SubmitQuestionsView.tsx | 144 | Submit view for batch question responses | DEEP: S Analysis Findings |
| src/components/permissions/AskUserQuestionPermissionRequest/use-multiple-choice-state.ts | 179 | Hook for managing multiple-choice question state in permission requests | DEEP: S Analysis Findings |
| src/components/permissions/ExitPlanModePermissionRequest/ExitPlanModePermissionRequest.tsx | 768 | UI for exiting plan mode with permission review and auto-mode cleanup | DEEP: S Analysis Findings |
| src/components/permissions/ComputerUseApproval/ComputerUseApproval.tsx | 441 | Approval UI for computer use tool actions (screenshots, mouse, keyboard) | DEEP: S Analysis Findings |
| src/components/permissions/FilePermissionDialog/FilePermissionDialog.tsx | 204 | File permission dialog with diff preview and accept/reject options | DEEP: S Analysis Findings |
| src/components/permissions/FilePermissionDialog/ideDiffConfig.ts | 177 | IDE diff configuration for file permission display | DEEP: S Analysis Findings |
| src/components/permissions/FilePermissionDialog/permissionOptions.tsx | 212 | Permission option buttons (accept, reject, always-allow) for file operations | DEEP: S Analysis Findings |
| src/components/permissions/FilePermissionDialog/useFilePermissionDialog.ts | 185 | Hook managing file permission dialog state and handler logic | DEEP: S Analysis Findings |
| src/components/permissions/FilePermissionDialog/usePermissionHandler.ts | 89 | Hook for handling permission allow/deny/always-allow actions | DEEP: S Analysis Findings |
| src/components/permissions/FileEditPermissionRequest/FileEditPermissionRequest.tsx | 182 | Permission UI for file edit operations with diff display | DEEP: S Analysis Findings |
| src/components/permissions/FileWritePermissionRequest/FileWritePermissionRequest.tsx | 161 | Permission UI for file write/create operations | DEEP: S Analysis Findings |
| src/components/permissions/FileWritePermissionRequest/FileWriteToolDiff.tsx | 89 | Diff display component for file write permission requests | DEEP: S Analysis Findings |
| src/components/permissions/FilesystemPermissionRequest/FilesystemPermissionRequest.tsx | 115 | Permission UI for filesystem listing operations | DEEP: S Analysis Findings |
| src/components/permissions/NotebookEditPermissionRequest/NotebookEditPermissionRequest.tsx | 166 | Permission UI for notebook cell edit operations | DEEP: S Analysis Findings |
| src/components/permissions/NotebookEditPermissionRequest/NotebookEditToolDiff.tsx | 235 | Diff display for notebook edit permission requests | DEEP: S Analysis Findings |
| src/components/permissions/PowerShellPermissionRequest/PowerShellPermissionRequest.tsx | 235 | PowerShell-specific permission request UI with command preview | DEEP: S Analysis Findings |
| src/components/permissions/PowerShellPermissionRequest/powershellToolUseOptions.tsx | 91 | Tool use option buttons for PowerShell permission | DEEP: S Analysis Findings |
| src/components/permissions/SedEditPermissionRequest/SedEditPermissionRequest.tsx | 230 | Permission UI for sed-style edit operations | DEEP: S Analysis Findings |
| src/components/permissions/SkillPermissionRequest/SkillPermissionRequest.tsx | 369 | Permission UI for skill execution requests | DEEP: S Analysis Findings |
| src/components/permissions/WebFetchPermissionRequest/WebFetchPermissionRequest.tsx | 258 | Permission UI for web fetch URL operations | DEEP: S Analysis Findings |
| src/components/permissions/EnterPlanModePermissionRequest/EnterPlanModePermissionRequest.tsx | 121 | UI for entering plan mode with permission mode transition | DEEP: S Analysis Findings |
| src/components/permissions/ReviewArtifactPermissionRequest/ReviewArtifactPermissionRequest.tsx | 3 | Placeholder for artifact review permission (not yet implemented) | DEEP: S Analysis Findings |
| src/components/permissions/MonitorPermissionRequest/MonitorPermissionRequest.tsx | 3 | Placeholder for monitor permission (not yet implemented) | DEEP: S Analysis Findings |
| src/components/permissions/rules/AddPermissionRules.tsx | 425 | UI for adding new permission rules with tool/pattern input | DEEP: S Analysis Findings |
| src/components/permissions/rules/AddWorkspaceDirectory.tsx | 137 | UI for adding workspace directories to permission scope | DEEP: S Analysis Findings |
| src/components/permissions/rules/PermissionRuleDescription.tsx | 120 | Descriptive rendering of individual permission rules | DEEP: S Analysis Findings |
| src/components/permissions/rules/PermissionRuleInput.tsx | 292 | Input component for entering permission rule patterns | DEEP: S Analysis Findings |
| src/components/permissions/rules/RecentDenialsTab.tsx | 221 | Tab showing recently denied permission requests | DEEP: S Analysis Findings |
| src/components/permissions/rules/WorkspaceTab.tsx | 150 | Tab showing workspace directory configuration | DEEP: S Analysis Findings |
| src/components/permissions/rules/RemoveWorkspaceDirectory.tsx | 104 | UI for removing workspace directories from permission scope | DEEP: S Analysis Findings |
| src/components/permissions/shellPermissionHelpers.tsx | 164 | Shared helpers for Bash/PowerShell permission request components | DEEP: S Analysis Findings |
| src/components/permissions/useShellPermissionFeedback.ts | 148 | Hook for shell command permission feedback and suggestion generation | DEEP: S Analysis Findings |
| src/components/permissions/WorkerPendingPermission.tsx | 104 | Swarm worker waiting indicator UI while leader approves permission request — shows Spinner + "Waiting for team lead approval" + WorkerBadge + tool name | DEEP: S Analysis Findings |
| src/utils/permissions/yolo-classifier-prompts/auto_mode_system_prompt.txt | 33 | System prompt template for AI permission classifier — defines decision policy (cautious default, risk categories, block/allow response format) | DEEP: S Analysis Findings |
| src/utils/permissions/yolo-classifier-prompts/permissions_anthropic.txt | 19 | Anthropic-managed allow/deny rule template for AI classifier — placeholder slots for user allow rules, soft-deny guidance, and environment guidance | DEEP: S Analysis Findings |
| src/utils/permissions/yolo-classifier-prompts/permissions_external.txt | 22 | External-user allow/deny rule template for AI classifier — default soft-deny rules and environment guidance with user_allow/deny/environment replaceable sections | DEEP: S Analysis Findings |
