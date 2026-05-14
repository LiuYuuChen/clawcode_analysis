#!/usr/bin/env python3
"""Find T-17 missing File Roles files and FAIL_4 orphan files"""
import os, re, json

task_dir = '.code_analysis/branches/main/task-analyses'
tasks_file = '.code_analysis/branches/main/analysis/03-analysis-tasks.md'
manifest_file = '.code_analysis/map/instance-manifest.jsonl'
mapped_file = '.code_analysis/map/mapped-files.jsonl'

# ============ T-17 Missing Files ============
print("=" * 60)
print("T-17 MISSING FILE ROLES")
print("=" * 60)

# Get T-17 scope files
with open(tasks_file) as f:
    content = f.read()

t17_match = re.search(r'^### T-17:(.*?)(?=^### T-|\Z)', content, re.MULTILINE | re.DOTALL)
if t17_match:
    block = t17_match.group(1)
    scope_files = [m.strip().strip('`"') for m in re.findall(r'^  - [`"]?([^`"\n]+)[`"]?', block, re.MULTILINE)]
    print(f"T-17 scope files: {len(scope_files)}")

# Get T-17 File Roles entries
t17_file = os.path.join(task_dir, 'T-17-plugin-system.md')
with open(t17_file) as f:
    fcontent = f.read()

fr_section = re.search(r'^## File Roles\b[^\n]*\n(.*?)(?=^##[^#]|\Z)', fcontent, re.MULTILINE | re.DOTALL)
fr_files = set()
if fr_section:
    for line in fr_section.group(1).split('\n'):
        line = line.strip()
        if line.startswith('|') and 'File' not in line.split('|')[1]:
            # Extract file path from first data column
            parts = line.split('|')
            if len(parts) > 1:
                file_path = parts[1].strip()
                if file_path and not re.match(r'^[-:| ]+$', file_path):
                    fr_files.add(file_path)

print(f"T-17 File Roles entries: {len(fr_files)}")
missing = [sf for sf in scope_files if sf not in fr_files]
print(f"Missing ({len(missing)}):")
for m in missing:
    print(f"  - {m}")

# ============ FAIL_4: Orphan Files ============
print()
print("=" * 60)
print("FAIL_4: ORPHAN FILES CHECK")
print("=" * 60)

# Load all mapped files
mapped = set()
with open(mapped_file) as f:
    for line in f:
        line = line.strip()
        if line:
            entry = json.loads(line)
            mapped.add(entry['file'])

print(f"Total mapped files: {len(mapped)}")

# Load manifest
manifest_entries = {}
with open(manifest_file) as f:
    for line in f:
        line = line.strip()
        if line:
            entry = json.loads(line)
            manifest_entries[entry['file']] = entry

# Build union of all task scopes
all_in_scope = set()
task_pattern = re.compile(r'^### (T-\d+):', re.MULTILINE)
positions = [(m.group(1), m.start()) for m in task_pattern.finditer(content)]

for i, (tid, start) in enumerate(positions):
    end = positions[i+1][1] if i+1 < len(positions) else len(content)
    block = content[start:end]
    
    scope = [m.strip().strip('`"') for m in re.findall(r'^  - [`"]?([^`"\n]+)[`"]?', block, re.MULTILINE)]
    all_in_scope.update(scope)
    
    pc_match = re.search(r'pattern_coverage:\s*[`"]*([A-Za-z][\w-]*)', block)
    if pc_match:
        pid = pc_match.group(1)
        for entry in manifest_entries.values():
            if entry['pattern_id'] == pid:
                all_in_scope.add(entry['file'])

print(f"Files in any task scope: {len(all_in_scope)}")

orphan = mapped - all_in_scope
print(f"Orphan files: {len(orphan)}")
if orphan:
    for o in sorted(orphan):
        print(f"  - {o}")

# ============ FAIL_6: Where Analyzed Check ============
print()
print("=" * 60)
print("FAIL_6: WHERE ANALYZED SECTION REFERENCE CHECK")
print("=" * 60)

fail6 = []
for fname in sorted(os.listdir(task_dir)):
    if not fname.startswith('T-') or not fname.endswith('.md'):
        continue
    
    fpath = os.path.join(task_dir, fname)
    with open(fpath) as f:
        fcontent = f.read()
    
    # Find File Roles section
    fr_section = re.search(r'^## File Roles\b[^\n]*\n(.*?)(?=^##[^#]|\Z)', fcontent, re.MULTILINE | re.DOTALL)
    if not fr_section:
        continue
    
    # Get actual section headers in the file
    actual_sections = set()
    for m in re.finditer(r'^##[^#][^\n]*', fcontent, re.MULTILINE):
        section_name = m.group(0).strip()
        actual_sections.add(section_name)
    
    # Parse Where Analyzed column
    section_text = fr_section.group(1)
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
        
        # Skip OVERVIEW enumerated
        if 'enumerated only' in where_col.lower() or 'OVERVIEW' in where_col:
            continue
        
        # Extract section references from Where Analyzed
        refs = re.findall(r'[§]\s*([^,;|]+?)(?:\s*[,;|]|\s*$)', where_col)
        if not refs:
            refs = re.findall(r'§\s*(.+?)$', where_col, re.MULTILINE)
        
        for ref in refs:
            ref = ref.strip()
            if not ref:
                continue
            # Check if this section name exists (case-insensitive partial match)
            found = any(ref.lower() in s.lower() for s in actual_sections)
            if not found:
                fail6.append((fname, file_col, ref))

if fail6:
    print(f"FAIL_6: {len(fail6)} invalid references:")
    for fn, fc, ref in fail6[:20]:
        print(f"  {fn}: {fc} -> '{ref}' not found")
else:
    print("FAIL_6: ALL PASS")
