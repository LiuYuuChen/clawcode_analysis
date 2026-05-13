# map-repo-supplement Goal (Remediation Iteration 1)

## Mode: supplement — Add ML-12~ML-15

- [x] Read existing 01-repo-map.md (ML-01~ML-11 present and verified)
- [x] Read uncovered-files.jsonl, filter remediation_type=ml-supplement (116 files in 4 groups)
- [x] Verify entry files exist for all 4 new MLs
- [x] Add ML-12 (Plugin System, 49 files, entry: src/utils/plugins/pluginLoader.ts)
- [x] Add ML-13 (Bash/Shell Engine, 36 files, entry: src/utils/bash/bashParser.ts)
- [x] Add ML-14 (Swarm Orchestration, 22 files, entry: src/utils/swarm/inProcessRunner.ts)
- [x] Add ML-15 (SDK Entry Points, 9 files, entry: src/entrypoints/sdk/coreSchemas.ts)
- [x] Update metadata.json mainline_count: 11 → 15
- [x] Update metadata.json version_history with SUPPLEMENT entry
- [x] Write sub-map-repo-summary-remediation.md
- [x] Verify existing ML-01~ML-11 content untouched

## Constraints Verified

- ML-01~ML-11 content in 01-repo-map.md: unchanged
- Each new ML has: id (ML-12~ML-15), name, priority (P2), entry file, scope_dirs, estimated_files
- No existing analysis files (sub-maps, mapped-files, call-graph) modified — trace-mainline will handle those
