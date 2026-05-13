# catalog-supplement Goal

## Status: ✅ ALL COMPLETE

- [x] 读取 uncovered-files.jsonl，分离 pattern-supplement (850) 和 ml-expand (59) 条目
- [x] 按 category 分组 850 个 pattern-supplement 文件到 36 个原始 category
- [x] 映射 36 个 category → 13 个 pattern (1 个扩展 PI-05 + 12 个新建 PI-09/10/11/12/13/14/15/16/18/20/23/24)
- [x] 为每个 catalog 文件生成 role_one_liner (inferred)
- [x] 59 个 ml-expand 文件按目录路由到 9 条 ML (ML-01/02/03/05/07/10/11/12/13)
- [x] 更新 pattern-categories.jsonl: 8 → 20 patterns
- [x] 更新 instance-manifest.jsonl: 611 → 1461 entries (+850)
- [x] 重建 mapped-files.jsonl: 1048 → 1957 files (+909)
- [x] 更新 mainline-file-map.jsonl: 27 entries (各 ML 追加 cataloged_files/supporting_files)
- [x] 更新 metadata.json: mapped_file_count=1957, mapped_lines=515,166
- [x] 覆盖率验证: 1957/2019 = 96.9% (Tier3 ≥95% PASS)
- [x] mapped ↔ manifest 一致性验证: 0 差异
- [x] 清理临时脚本

## Results Summary

| Metric | Before | After |
|--------|--------|-------|
| mapped_file_count | 1048 (51.9%) | 1957 (96.9%) |
| mapped_lines | 292,121 | 515,166 |
| pattern-categories | 8 | 20 |
| instance-manifest | 611 | 1461 |
| deep files | 359 | 359 |
| standard files | 78 | 137 (+59) |
| catalog files | 611 | 1461 (+850) |
