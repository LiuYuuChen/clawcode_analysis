# Uncovered Files Summary

**Total uncovered**: 69 files (3.4% of 2,019 implementation files)
**Decision**: All accept-uncovered — low-priority leaf files that do not warrant analysis resources.

## By Directory

| Directory | Count | Description |
|-----------|-------|-------------|
| src/commands | 20 | Minor/legacy command variants (help topics, admin commands) |
| src/utils | 17 | Isolated utility functions (formatters, validators, helpers) |
| src/components | 9 | Minor UI component leaves (icons, badges, separators) |
| src/types | 6 | Type-only files with no runtime logic |
| src/constants | 4 | Pure constant/enum definitions |
| src/ssh | 2 | SSH utility stubs |
| src/assistant | 2 | Assistant-mode helper functions |
| shims/ant-computer-use-mcp | 1 | Shim for ant-computer-use-mcp |
| src/services | 1 | Minor service helper |
| shims/color-diff-napi | 1 | Native module shim |
| shims/modifiers-napi | 1 | Native module shim |
| src/proactive | 1 | Proactive notification stub |
| src/jobs | 1 | Job scheduler helper |
| src/skills | 1 | Skill definition leaf |
| src/coordinator | 1 | Coordinator utility |

## Characteristics

- **All files are &lt;= 50 lines** — pure boilerplate, type definitions, or simple helpers
- **No architectural significance** — none participate in core data flows or state management
- **No cross-references** — none are imported by mapped deep/standard files
- **No security-sensitive logic** — no auth, permission, or validation code

## Justification for Accept-Uncovered

These 69 files (3.4% of baseline) satisfy the accept-uncovered criteria:
1. Low line count (all &lt;= 50 lines)
2. Isolated (no callers in mapped files)
3. No architectural role (pure leaves)
4. Below the 5% accept-uncovered threshold

For the full file-by-file listing, see `uncovered-files.jsonl`.
