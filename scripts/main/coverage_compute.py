#!/usr/bin/env python3
"""Compute task coverage for code-deep-analysis-workflow tasks step."""
import json, sys, os

BASE = ".code_analysis"

def load_jsonl(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

# Load data
file_lines_data = load_jsonl(f"{BASE}/map/mapped-files.jsonl")
file_lines = {r['file']: r['lines'] for r in file_lines_data}

ml_segments = {}
for r in load_jsonl(f"{BASE}/map/mainline-file-map.jsonl"):
    ml_segments[r['mainline']] = r

patterns = {}
for r in load_jsonl(f"{BASE}/map/pattern-categories.jsonl"):
    patterns[r['pattern_id']] = r

instance_files = {}
for r in load_jsonl(f"{BASE}/map/instance-manifest.jsonl"):
    instance_files.setdefault(r['pattern_id'], []).append(r['file'])

# Shared file ownership
shared_ownership = {
    "src/Tool.ts": ("ML-03-1", ["ML-02-3"]),
    "src/tools.ts": ("ML-03-1", ["ML-01"]),
    "src/context.ts": ("ML-01", ["ML-07-1"]),
    "src/services/tools/StreamingToolExecutor.ts": ("ML-02-3", ["ML-03-1"]),
    "src/services/tools/toolOrchestration.ts": ("ML-02-3", ["ML-03-1"]),
    "src/services/api/client.ts": ("ML-10-1", ["ML-02-3"]),
    "src/services/api/errors.ts": ("ML-10-1", ["ML-02-3"]),
    "src/services/api/logging.ts": ("ML-10-1", ["ML-02-3"]),
    "src/services/api/withRetry.ts": ("ML-10-1", ["ML-02-3"]),
    "src/services/api/bootstrap.ts": ("ML-06", ["ML-10-1"]),
    "src/services/compact/autoCompact.ts": ("ML-02-2", ["ML-11-1"]),
    "src/services/compact/compact.ts": ("ML-11-1", ["ML-02-2"]),
    "src/hooks/useCanUseTool.tsx": ("ML-04-1", ["ML-03-1", "ML-07-4"]),
    "src/utils/tokens.ts": ("ML-02-2", []),
    "src/ink.ts": ("ML-07-1", ["ML-01"]),
    "src/services/mcp/channelPermissions.ts": ("ML-04-1", ["ML-05-3"]),
    "src/commands/login/login.tsx": ("ML-06", ["ML-01"]),
    "src/commands/session/session.tsx": ("ML-06", ["ML-01"]),
    "src/components/permissions/PermissionRequest.tsx": ("ML-04-2", ["ML-07-3"]),
    "src/components/permissions/SandboxPermissionRequest.tsx": ("ML-04-2", ["ML-07-3"]),
    "src/tools/MCPTool/MCPTool.ts": ("ML-05-3", ["ML-03-2"]),
    "src/tools/MCPTool/UI.tsx": ("ML-05-3", []),
    "src/tools/MCPTool/classifyForCollapse.ts": ("ML-05-3", []),
    "src/tools/MCPTool/prompt.ts": ("ML-05-3", []),
    "src/tools/McpAuthTool/McpAuthTool.ts": ("ML-05-3", []),
    "src/tools/ListMcpResourcesTool/ListMcpResourcesTool.ts": ("ML-05-3", []),
    "src/tools/ReadMcpResourceTool/ReadMcpResourceTool.ts": ("ML-05-3", []),
}

def get_deep_files(ml_ids):
    """Get all deep files for given ML segment IDs, minus shared files owned elsewhere."""
    all_files = set()
    for ml_id in ml_ids:
        if ml_id in ml_segments:
            s = ml_segments[ml_id]
            all_files.update(s.get('core_files', []) + s.get('supporting_files', []))
    remove = set()
    for f in all_files:
        if f in shared_ownership:
            owner = shared_ownership[f][0]
            if owner not in ml_ids:
                remove.add(f)
    return sorted(all_files - remove)

def get_all_files(ml_ids):
    """Get all files (deep + catalog) for given ML segment IDs."""
    files = set()
    for ml_id in ml_ids:
        if ml_id in ml_segments:
            s = ml_segments[ml_id]
            files.update(s.get('core_files', []) + s.get('supporting_files', []) + s.get('cataloged_files', []))
    return files

# Build task scope files
task_scopes = {}

# Main tasks
task_defs = {
    "T-01": {"mls": ["ML-01"], "slug": "cli-startup"},
    "T-02": {"mls": ["ML-01"], "slug": "command-context"},
    "T-03": {"mls": ["ML-01"], "slug": "infra-support"},
    "T-04": {"mls": ["ML-02-1", "ML-02-2", "ML-02-3"], "slug": "query-engine"},
    "T-05": {"mls": ["ML-02-4"], "slug": "message-processing"},
    "T-06": {"mls": ["ML-03-1", "ML-03-2"], "slug": "tool-system"},
    "T-07": {"mls": ["ML-04-1", "ML-04-2"], "slug": "permission-system"},
    "T-08": {"mls": ["ML-05-1", "ML-05-2", "ML-05-3"], "slug": "mcp-integration"},
    "T-09": {"mls": ["ML-06"], "slug": "auth-session"},
    "T-10": {"mls": ["ML-07-1", "ML-07-2", "ML-07-5"], "slug": "tui-framework"},
    "T-11": {"mls": ["ML-07-3", "ML-07-4"], "slug": "tui-components-hooks"},
    "T-12": {"mls": ["ML-08"], "slug": "task-system"},
    "T-13": {"mls": ["ML-09-1", "ML-09-2"], "slug": "bridge-remote"},
    "T-14": {"mls": ["ML-10-1"], "slug": "api-client"},
    "T-15": {"mls": ["ML-11-1"], "slug": "context-memory"},
    "T-16": {"mls": ["ML-12-1"], "slug": "plugin-system"},
    "T-17": {"mls": ["ML-13-1"], "slug": "bash-engine"},
    "T-18": {"mls": ["ML-14-1"], "slug": "swarm-orchestration"},
    "T-19": {"mls": ["ML-15-1"], "slug": "sdk-entrypoints"},
}

# For ML-01 split into 3 tasks manually
ml01_all = sorted(set(ml_segments["ML-01"]["core_files"] + ml_segments["ML-01"]["supporting_files"]))
ml01_remove = set()
for f in ml01_all:
    if f in shared_ownership and shared_ownership[f][0] != "ML-01":
        ml01_remove.add(f)
ml01_available = [f for f in ml01_all if f not in ml01_remove]

t01_files = [
    "src/bootstrap-entry.ts", "src/bootstrap/state.ts", "src/bootstrapMacro.ts",
    "src/main.tsx", "src/dev-entry.ts",
    "src/entrypoints/cli.tsx", "src/entrypoints/init.ts", "src/entrypoints/mcp.ts",
    "src/entrypoints/agentSdkTypes.ts", "src/entrypoints/sandboxTypes.ts",
    "src/setup.ts", "src/replLauncher.tsx", "src/history.ts",
    "src/state/AppStateStore.ts", "src/state/AppState.tsx",
    "src/state/onChangeAppState.ts", "src/state/selectors.ts",
    "src/state/store.ts", "src/state/teammateViewHelpers.ts",
    "src/cost-tracker.ts", "src/costHook.ts",
]
t02_files = [
    "src/commands.ts", "src/commands/help/index.ts", "src/commands/insights.ts",
    "src/context.ts",
    "src/context/QueuedMessageContext.tsx", "src/context/mailbox.tsx",
    "src/context/modalContext.tsx", "src/context/overlayContext.tsx",
    "src/context/promptOverlayContext.tsx", "src/context/stats.tsx", "src/context/voice.tsx",
    "src/dialogLaunchers.tsx", "src/interactiveHelpers.tsx",
    "src/utils/config.ts", "src/outputStyles/loadOutputStylesDir.ts",
    "src/projectOnboardingState.ts", "src/query/tokenBudget.ts",
]
t03_files = [f for f in ml01_available if f not in set(t01_files + t02_files)]

task_scopes["T-01"] = set(t01_files)
task_scopes["T-02"] = set(t02_files)
task_scopes["T-03"] = set(t03_files)

# Other main tasks
for tid in ["T-04","T-05","T-06","T-07","T-08","T-09","T-10","T-11","T-12","T-13","T-14","T-15","T-16","T-17","T-18","T-19"]:
    mls = task_defs[tid]["mls"]
    task_scopes[tid] = set(get_deep_files(mls))

# Pattern Audit tasks
pattern_audits = {
    "T-20": ("ML-03", "PI-01"), "T-21": ("ML-01", "PI-02"), "T-22": ("ML-07", "PI-03"),
    "T-23": ("ML-08", "PI-04"), "T-24": ("ML-04", "PI-06"), "T-25": ("ML-07", "PI-07"),
    "T-26": ("ML-07", "PI-08"), "T-27": ("ML-07", "PI-09"), "T-28": ("ML-12", "PI-10"),
    "T-29": ("ML-01", "PI-11"), "T-30": ("ML-02", "PI-12"), "T-31": ("ML-07", "PI-13"),
    "T-32": ("ML-01", "PI-14"), "T-33": ("ML-07", "PI-15"), "T-34": ("ML-07", "PI-16"),
    "T-35": ("ML-03", "PI-18"), "T-36": ("ML-05", "PI-20"), "T-37": ("ML-09", "PI-23"),
    "T-38": ("ML-06", "PI-24"),
}

for tid, (ml, pid) in pattern_audits.items():
    scope = set()
    if pid in patterns:
        scope.add(patterns[pid]["files"][0])  # representative file
    if pid in instance_files:
        scope.update(instance_files[pid])
    task_scopes[tid] = scope

# ── Compute coverage ──
all_scope_files = set()
for s in task_scopes.values():
    all_scope_files.update(s)

mapped_lines_total = sum(file_lines.values())
global_lines = sum(file_lines.get(f, 0) for f in all_scope_files)
global_cov = global_lines / mapped_lines_total * 100

print(f"Total tasks: {len(task_scopes)}")
print(f"Main tasks: 19, Pattern audit tasks: 19")
print(f"\nGlobal coverage: {global_lines:,}/{mapped_lines_total:,} = {global_cov:.2f}%")
print(f"Scope files: {len(all_scope_files)}/{len(file_lines)}")

# Per-ML coverage
logical_mls = {}
for seg_id in ml_segments:
    parts = seg_id.split('-')
    logical = '-'.join(parts[:2]) if len(parts) > 2 else seg_id
    logical_mls.setdefault(logical, []).append(seg_id)

print(f"\nPer-ML coverage:")
for lm in sorted(logical_mls.keys()):
    segs = logical_mls[lm]
    lm_files = get_all_files(segs)
    lm_lines = sum(file_lines.get(f, 0) for f in lm_files)

    related_task_files = set()
    for tid, scope in task_scopes.items():
        if tid in pattern_audits:
            pml = pattern_audits[tid][0]
        else:
            pml = task_defs[tid]["mls"][0]
        # Normalize to logical ML
        pml_logical = '-'.join(pml.split('-')[:2]) if '-' in pml[3:] else pml
        if pml_logical == lm:
            related_task_files.update(scope)

    covered = lm_files & related_task_files
    covered_lines = sum(file_lines.get(f, 0) for f in covered)
    cov = covered_lines / lm_lines * 100 if lm_lines else 100

    core_files = set()
    for seg_id in segs:
        core_files.update(ml_segments[seg_id].get('core_files', []))
    core_covered = core_files & related_task_files
    core_cov = len(core_covered) / len(core_files) * 100 if core_files else 100

    status = "PASS" if cov >= 95 and core_cov >= 100 else "FAIL"
    print(f"  {lm}: {len(lm_files)}f/{lm_lines:,}L covered={covered_lines:,}L ({cov:.1f}%) core={len(core_covered)}/{len(core_files)} ({core_cov:.0f}%) {status}")

# Duplicate check
all_raw = []
for scope in task_scopes.values():
    all_raw.extend(scope)
dups = [f for f in set(all_raw) if all_raw.count(f) > 1]
print(f"\nRaw: {len(all_raw)}, Union: {len(set(all_raw))}")
if dups:
    print(f"DUPLICATES ({len(dups)}):")
    for d in sorted(dups):
        print(f"  {d}")
else:
    print("No duplicate scope files ✓")

# Print scope file counts per task
print("\nPer-task scope sizes:")
for tid in sorted(task_scopes.keys(), key=lambda x: int(x.split('-')[1])):
    scope = task_scopes[tid]
    lines = sum(file_lines.get(f, 0) for f in scope)
    print(f"  {tid}: {len(scope)} files, {lines:,} lines")
