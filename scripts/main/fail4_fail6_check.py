#!/usr/bin/env python3
"""FAIL_4 v2 + FAIL_6 v2: Proper orphan check + section reference check"""
import os, re, json

task_dir = '.code_analysis/branches/main/task-analyses'
tasks_file = '.code_analysis/branches/main/analysis/03-analysis-tasks.md'
manifest_file = '.code_analysis/map/instance-manifest.jsonl'
mapped_file = '.code_analysis/map/mapped-files.jsonl'

# ============ FAIL_4 v2: Use File Roles union ============
print("=" * 60)
print("FAIL_4 v2: ORPHAN FILES CHECK (using File Roles union)")
print("=" * 60)

# Load all mapped files
mapped = {}
with open(mapped_file) as f:
    for line in f:
        line = line.strip()
        if line:
            entry = json.loads(line)
            mapped[entry['file']] = entry

print(f"Total mapped files: {len(mapped)}")

# Build union of all files in File Roles tables
all_in_file_roles = set()
# Also build per-task File Roles mapping for FAIL_6
task_file_roles = {}

for fname in sorted(os.listdir(task_dir)):
    if not fname.startswith('T-') or not fname.endswith('.md'):
        continue
    
    tid_match = re.match(r'(T-\d+)', fname)
    if not tid_match:
        continue
    tid = tid_match.group(1)
    
    fpath = os.path.join(task_dir, fname)
    with open(fpath) as f:
        fcontent = f.read()
    
    fr_section = re.search(r'^## File Roles\b[^\n]*\n(.*?)(?=^##[^#]|\Z)', fcontent, re.MULTILINE | re.DOTALL)
    if fr_section:
        section_text = fr_section.group(1)
        files_in_task = set()
        where_analyzed = {}
        for line in section_text.split('\n'):
            line = line.strip()
            if not line.startswith('|'):
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 4:
                continue
            file_col = parts[1]
            where_col = parts[4] if len(parts) > 4 else parts[-1]
            
            if not file_col or 'File' in file_col or re.match(r'^[-:| ]+$', file_col):
                continue
            
            all_in_file_roles.add(file_col)
            files_in_task.add(file_col)
            where_analyzed[file_col] = where_col
        
        task_file_roles[tid] = {
            'files': files_in_task,
            'where': where_analyzed,
            'fname': fname
        }

print(f"Files in File Roles union: {len(all_in_file_roles)}")

# Also get scope files from 03-analysis-tasks.md
with open(tasks_file) as f:
    content = f.read()

all_scope_files = set()
task_pattern = re.compile(r'^### (T-\d+):', re.MULTILINE)
positions = [(m.group(1), m.start()) for m in task_pattern.finditer(content)]
for i, (tid, start) in enumerate(positions):
    end = positions[i+1][1] if i+1 < len(positions) else len(content)
    block = content[start:end]
    scope = [m.strip().strip('`"') for m in re.findall(r'^  - [`"]?([^`"\n]+)[`"]?', block, re.MULTILINE)]
    all_scope_files.update(scope)

combined = all_in_file_roles | all_scope_files
print(f"Combined (File Roles + scope_files): {len(combined)}")

orphan = set(mapped.keys()) - combined
print(f"Orphan files: {len(orphan)}")

if orphan:
    # Categorize orphans
    by_dir = {}
    for f in sorted(orphan):
        d = os.path.dirname(f)
        if d not in by_dir:
            by_dir[d] = []
        by_dir[d].append(f)
    
    print(f"\nOrphan by directory:")
    for d in sorted(by_dir.keys()):
        print(f"  {d}: {len(by_dir[d])} files")

# ============ FAIL_6 v2: Where Analyzed section reference ============
print()
print("=" * 60)
print("FAIL_6 v2: WHERE ANALYZED SECTION REFERENCE CHECK")
print("=" * 60)

fail6 = []
fail6_count = 0
pass6_count = 0
skip6_count = 0

for tid, info in task_file_roles.items():
    fname = info['fname']
    fpath = os.path.join(task_dir, fname)
    with open(fpath) as f:
        fcontent = f.read()
    
    # Get ALL section headers (H2, H3, H4+)
    all_sections = set()
    for m in re.finditer(r'^#{2,}\s+[^\n]+', fcontent, re.MULTILINE):
        section_name = re.sub(r'^#{2,}\s+', '', m.group(0)).strip()
        # Clean markdown formatting
        section_name = re.sub(r'\*\*.*?\*\*', '', section_name).strip()
        all_sections.add(section_name)
    
    for file_path, where in info['where'].items():
        if 'enumerated only' in where.lower() or where == 'OVERVIEW (enumerated only)':
            skip6_count += 1
            continue
        
        # Split Where Analyzed by §, +, |, comma
        refs = re.split(r'[§|+,]', where)
        
        for ref in refs:
            ref = ref.strip()
            # Remove prefixes
            ref = re.sub(r'^(DEEP|STANDARD|OVERVIEW|STANDARD 概要):\s*', '', ref)
            ref = ref.strip()
            if not ref:
                continue
            
            # Check partial match (case-insensitive)
            found = any(ref.lower() in s.lower() or s.lower() in ref.lower() for s in all_sections)
            if not found:
                fail6.append((fname, file_path, ref, where))
                fail6_count += 1
            else:
                pass6_count += 1

print(f"References checked: {fail6_count + pass6_count + skip6_count}")
print(f"PASS: {pass6_count}, FAIL: {fail6_count}, SKIP (enumerated): {skip6_count}")

if fail6:
    print(f"\nFAIL_6: {len(fail6)} invalid references (showing first 30):")
    for fn, fc, ref, full_where in fail6[:30]:
        print(f"  {fn}: {fc}")
        print(f"    ref='{ref}' in where='{full_where}'")
else:
    print("FAIL_6: ALL PASS")
