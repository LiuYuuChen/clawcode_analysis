#!/usr/bin/env python3
"""FAIL_2: Check File Roles row count vs effective_scope_files"""
import os, re, json

task_dir = '.code_analysis/branches/main/task-analyses'
tasks_file = '.code_analysis/branches/main/analysis/03-analysis-tasks.md'
manifest_file = '.code_analysis/map/instance-manifest.jsonl'

# Load manifest
manifest = {}
with open(manifest_file) as f:
    for line in f:
        line = line.strip()
        if line:
            entry = json.loads(line)
            pid = entry['pattern_id']
            if pid not in manifest:
                manifest[pid] = []
            manifest[pid].append(entry)

# Parse task definitions from 03-analysis-tasks.md
with open(tasks_file) as f:
    content = f.read()

task_defs = {}
task_pattern = re.compile(r'^### (T-\d+):', re.MULTILINE)
positions = [(m.group(1), m.start()) for m in task_pattern.finditer(content)]

for i, (tid, start) in enumerate(positions):
    end = positions[i+1][1] if i+1 < len(positions) else len(content)
    block = content[start:end]
    
    # Extract scope_files list
    scope_matches = re.findall(r'^  - [`"]?([^`"\n]+)[`"]?', block, re.MULTILINE)
    
    # Extract pattern_coverage
    pc_match = re.search(r'pattern_coverage:\s*[`"]*([A-Za-z][\w-]*)', block)
    pattern_id = pc_match.group(1) if pc_match else None
    
    effective = len(scope_matches)
    cat_count = 0
    if pattern_id and pattern_id in manifest:
        cat_count = len(manifest[pattern_id])
        effective += cat_count
    
    task_defs[tid] = {
        'scope_count': len(scope_matches),
        'pattern_id': pattern_id,
        'catalog_count': cat_count,
        'effective': effective
    }

# Count File Roles rows in each task file
fail2 = []
print('Task | FileRoles | Effective | Scope | Catalog | Pattern | Status')
print('-----|-----------|-----------|-------|---------|---------|-------')

# Get unique task IDs from file names (handle duplicates like T-12)
seen_tids = set()
for fname in sorted(os.listdir(task_dir)):
    if not fname.startswith('T-') or not fname.endswith('.md'):
        continue
    
    tid_match = re.match(r'(T-\d+)', fname)
    if not tid_match:
        continue
    tid = tid_match.group(1)
    
    # For tasks with multiple files (e.g. T-12), take the latest
    if tid in seen_tids:
        continue
    seen_tids.add(tid)
    
    fpath = os.path.join(task_dir, fname)
    with open(fpath) as f:
        fcontent = f.read()
    
    # Count File Roles table rows
    fr_section = re.search(r'^## File Roles\s*\n(.*?)(?=^##[^#]|\Z)', fcontent, re.MULTILINE | re.DOTALL)
    if fr_section:
        rows = re.findall(r'^\|[^|]+\|[^|]+\|', fr_section.group(1), re.MULTILINE)
        data_rows = [r for r in rows if not re.match(r'^\|[-:| ]+\|', r) and not re.match(r'^\|.*File.*Role.*Where', r, re.IGNORECASE)]
        fr_count = len(data_rows)
    else:
        fr_count = 0
    
    td = task_defs.get(tid, {'effective': 0, 'scope_count': 0, 'catalog_count': 0, 'pattern_id': None})
    
    status = 'PASS' if fr_count >= td['effective'] else 'FAIL_2'
    if status == 'FAIL_2':
        fail2.append(tid)
    
    pid_str = td['pattern_id'] or '-'
    print(f'{tid} | {fr_count} | {td["effective"]} | {td["scope_count"]} | {td["catalog_count"]} | {pid_str} | {status}')

print()
if fail2:
    print(f'FAIL_2: {len(fail2)} failures: {fail2}')
else:
    print('FAIL_2: ALL PASS')
