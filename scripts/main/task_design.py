#!/usr/bin/env python3
"""
Task decomposition design script for code-deep-analysis-workflow.
Reads all data sources, computes coverage gaps, and designs sweep tasks.
Outputs coverage verification report.
"""
import json, os, re
from collections import defaultdict

BASE = '/Users/liuyuchen/ai/open-resources/claude-code'
MAP = f'{BASE}/.code_analysis/map'
ANALYSIS = f'{BASE}/.code_analysis/branches/main/analysis'

# ─── 1. Load data sources ───

file_lines = {}
file_mainlines = {}
with open(f'{MAP}/mapped-files.jsonl') as f:
    for line in f:
        r = json.loads(line.strip())
        file_lines[r['file']] = r['lines']
        file_mainlines[r['file']] = r.get('mainlines', [])

segs = {}
with open(f'{MAP}/mainline-file-map.jsonl') as f:
    for line in f:
        r = json.loads(line.strip())
        segs[r['mainline']] = r

patterns = {}
with open(f'{MAP}/pattern-categories.jsonl') as f:
    for line in f:
        r = json.loads(line.strip())
        patterns[r['pattern_id']] = r

instance_manifest = defaultdict(list)
with open(f'{MAP}/instance-manifest.jsonl') as f:
    for line in f:
        r = json.loads(line.strip())
        instance_manifest[r['pattern_id']].append(r['file'])

# ─── 2. Build file→ML mapping ───

file_to_ml = {}
file_source = {}

for seg_id, s in segs.items():
    parts = seg_id.split('-')
    logical = '-'.join(parts[:2]) if len(parts) > 2 else seg_id
    for f in s.get('core_files', []):
        if f not in file_to_ml:
            file_to_ml[f] = logical
            file_source[f] = 'segment_core'
    for f in s.get('supporting_files', []):
        if f not in file_to_ml:
            file_to_ml[f] = logical
            file_source[f] = 'segment_supp'
    for f in s.get('cataloged_files', []):
        if f not in file_to_ml:
            file_to_ml[f] = logical
            file_source[f] = 'segment_cat'

for f in file_lines:
    if f not in file_to_ml:
        mls = file_mainlines.get(f, [])
        if mls:
            ml = mls[0]
            parts = ml.split('-')
            logical = '-'.join(parts[:2]) if len(parts) > 2 else ml
            file_to_ml[f] = logical
            file_source[f] = 'orphan'

ml_files = defaultdict(set)
for f, ml in file_to_ml.items():
    ml_files[ml].add(f)

# ─── 3. Parse existing tasks ───

with open(f'{ANALYSIS}/03-analysis-tasks.md') as f:
    existing = f.read()

task_pattern = re.compile(r'### (T-\d+): (.+?)\n(.*?)(?=\n### T-|\n## (?!Task)|\Z)', re.DOTALL)
existing_tasks = {}
for m in task_pattern.finditer(existing):
    tid = m.group(1)
    title = m.group(2).strip()
    body = m.group(3)
    pm = re.search(r'\*\*Primary Mainline\*\*:\s*(ML-[\d-]+)', body)
    primary_ml = pm.group(1) if pm else None
    sf_match = re.search(r'\*\*Scope Files\*\*.*?:\n((?:  - .+\n)*)', body)
    scope_files = []
    if sf_match:
        scope_files = [l.strip().lstrip('- ') for l in sf_match.group(1).strip().split('\n') if l.strip().startswith('- ')]
    pri = re.search(r'\*\*Priority\*\*:\s*(P\d)', body)
    priority = pri.group(1) if pri else 'P3'
    pc = re.search(r'\*\*Pattern Coverage\*\*:\s*(PI-\d+)', body)
    pattern_cov = pc.group(1) if pc else None
    existing_tasks[tid] = {'title': title, 'primary_ml': primary_ml, 'scope_files': scope_files, 'priority': priority, 'pattern_coverage': pattern_cov}

# ─── 4. Categorize ───

deep_tasks = {k: v for k, v in existing_tasks.items() if v['pattern_coverage'] is None and v['scope_files']}
pattern_tasks = {k: v for k, v in existing_tasks.items() if v['pattern_coverage'] is not None}

print(f"Existing: {len(existing_tasks)} tasks")
print(f"  Deep: {len(deep_tasks)}, Pattern: {len(pattern_tasks)}")

# ─── 5. Coverage analysis ───

covered_files = set()
for task in deep_tasks.values():
    covered_files.update(task['scope_files'])

pattern_covered = set()
for pid, files in instance_manifest.items():
    pattern_covered.update(files)

uncovered = set(file_lines.keys()) - covered_files - pattern_covered
total_lines = sum(file_lines.values())
uncovered_lines = sum(file_lines.get(f, 0) for f in uncovered)

print(f"\nTotal mapped: {len(file_lines)} files / {total_lines:,} lines")
print(f"Deep scope: {len(covered_files)} files")
print(f"Pattern audit: {len(pattern_covered)} files")
print(f"Uncovered: {len(uncovered)} files / {uncovered_lines:,} lines ({uncovered_lines*100/total_lines:.1f}%)")

# ─── 6. Group uncovered by ML ───

uncovered_by_ml = defaultdict(set)
for f in uncovered:
    ml = file_to_ml.get(f)
    if ml:
        uncovered_by_ml[ml].add(f)

print(f"\nUncovered by ML:")
for ml in sorted(uncovered_by_ml.keys()):
    files = uncovered_by_ml[ml]
    lines = sum(file_lines.get(f, 0) for f in files)
    print(f"  {ml}: {len(files)} files / {lines:,} lines")

# ─── 7. Design sweep tasks ───

sweep_tasks = []
next_id = 41

for ml in sorted(uncovered_by_ml.keys()):
    files = uncovered_by_ml[ml]
    lines = sum(file_lines.get(f, 0) for f in files)
    pri_map = {f'ML-{i:02d}': ('P1' if i <= 6 else ('P2' if i <= 13 else 'P3')) for i in range(1, 16)}
    ml_pri = pri_map.get(ml, 'P3')

    dir_groups = defaultdict(list)
    for f in files:
        d = os.path.dirname(f)
        dir_groups[d].append(f)

    sorted_dirs = sorted(dir_groups.keys(), key=lambda d: sum(file_lines.get(f,0) for f in dir_groups[d]), reverse=True)

    if lines <= 12000:
        sweep_tasks.append({'id': f'T-{next_id:02d}', 'ml': ml, 'files': sorted(files), 'lines': lines, 'priority': ml_pri, 'depth': 'OVERVIEW', 'description': f'{ml} 未覆盖文件'})
        next_id += 1
    else:
        chunks = []
        current_chunk = []
        current_lines = 0
        for d in sorted_dirs:
            dfiles = dir_groups[d]
            dlines = sum(file_lines.get(f,0) for f in dfiles)
            if current_lines + dlines > 25000 and current_chunk:
                chunks.append(current_chunk)
                current_chunk = list(dfiles)
                current_lines = dlines
            else:
                current_chunk.extend(dfiles)
                current_lines += dlines
        if current_chunk:
            chunks.append(current_chunk)
        for i, chunk in enumerate(chunks):
            clines = sum(file_lines.get(f,0) for f in chunk)
            sweep_tasks.append({'id': f'T-{next_id:02d}', 'ml': ml, 'files': sorted(chunk), 'lines': clines, 'priority': ml_pri, 'depth': 'OVERVIEW', 'description': f'{ml} 未覆盖文件 (part-{i+1}/{len(chunks)})'})
            next_id += 1

print(f"\nNew sweep tasks: {len(sweep_tasks)}")
for st in sweep_tasks:
    print(f"  {st['id']}: {st['ml']} | {len(st['files'])}f / {st['lines']:,}L | {st['priority']} | {st['description']}")

# ─── 8. Final coverage ───

all_covered = set(covered_files) | set(pattern_covered)
for st in sweep_tasks:
    all_covered.update(st['files'])

final_lines = sum(file_lines.get(f, 0) for f in all_covered if f in file_lines)
final_uncovered = set(file_lines.keys()) - all_covered
final_uncovered_lines = sum(file_lines.get(f, 0) for f in final_uncovered)

print(f"\n{'='*60}")
print(f"FINAL: {final_lines*100/total_lines:.1f}% coverage ({final_lines:,}/{total_lines:,})")
if final_uncovered:
    print(f"Still uncovered: {len(final_uncovered)} files / {final_uncovered_lines:,} lines")
print(f"{'='*60}")

print(f"\nPer-ML coverage:")
for ml in sorted(ml_files.keys()):
    ml_line_total = sum(file_lines.get(f,0) for f in ml_files[ml])
    ml_cov = ml_files[ml] & all_covered
    ml_cov_lines = sum(file_lines.get(f,0) for f in ml_cov)
    status = "PASS" if ml_cov_lines * 100 / ml_line_total >= 95 else "FAIL"
    print(f"  {ml}: {ml_cov_lines:,}/{ml_line_total:,} ({ml_cov_lines*100/ml_line_total:.1f}%) | {status}")

# Save sweep task data as JSON for 03-analysis-tasks.md generation
output = {
    'sweep_tasks': sweep_tasks,
    'existing_deep_tasks': {k: {'title': v['title'], 'primary_ml': v['primary_ml'], 'file_count': len(v['scope_files']), 'priority': v['priority']} for k, v in deep_tasks.items()},
    'existing_pattern_tasks': {k: {'title': v['title'], 'primary_ml': v['primary_ml'], 'pattern_coverage': v['pattern_coverage'], 'priority': v['priority']} for k, v in pattern_tasks.items()},
    'coverage': {
        'total_lines': total_lines,
        'final_covered_lines': final_lines,
        'global_pct': final_lines*100/total_lines,
        'uncovered_files': len(final_uncovered),
        'uncovered_lines': final_uncovered_lines,
        'per_ml': {ml: {'total': sum(file_lines.get(f,0) for f in ml_files[ml]), 'covered': sum(file_lines.get(f,0) for f in ml_files[ml] & all_covered)} for ml in sorted(ml_files.keys())}
    }
}

with open(f'{ANALYSIS}/task_design_data.json', 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved design data to {ANALYSIS}/task_design_data.json")
