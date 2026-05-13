# catalog-to-standard-upgrade Goal

## Iteration 3 补救目标

- [x] 识别 eligible 文件：PI-12/13/14 中 lines>20 + PI-05 中 lines>30
- [x] 升级 660 文件从 catalog → standard（PI-05:45, PI-12:302, PI-13:203, PI-14:110）
- [x] mapped-files.jsonl: deep=359, standard=797, catalog=801 (total=1957)
- [x] mainline-file-map.jsonl: 110 文件从 ML-01 catalog → supporting
- [x] instance-manifest.jsonl: 移除 660 条升级条目，剩余 801
- [x] pattern-categories.jsonl: PI-05 189→109, PI-12 314→12, PI-13 213→10, PI-14 112→2
- [x] metadata.json: mapped_file_count=1957, mapped_lines=515166 不变
- [x] 数据一致性验证：mapped count PASS, manifest/catalog match PASS

## 覆盖率结果

| Tier | 升级前 | 升级后 | 阈值 |
|------|--------|--------|------|
| Tier 1 (deep) | 17.8% | 17.8% | ≥10% ✅ |
| Tier 2 (deep+standard) | 24.6% | **57.3%** | ≥80% ❌ |
| Tier 3 (all) | 96.9% | 96.9% | ≥95% ✅ |

## 已知预存不一致

- mainline-file-map.jsonl unique files = 1192 (vs mapped-files 1957)
  - 原因：catalog-supplement 步骤添加文件到 mapped-files/instance-manifest 但未更新 mainline-file-map
  - 不影响覆盖率计算（以 mapped-files.jsonl 为准）
