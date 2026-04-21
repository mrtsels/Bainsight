# 工作流程 / Workflow

## 整体架构

```
仓库 (Git)                      OneDrive
─────────────────────────────────────────────────
├── Case 文件                    └── 最终 PPT (sharedoc)
├── 访谈记录
├── 市场研究资料
├── 数据处理脚本
├── 中间分析结果
├── 草稿文档
└── 报告输出
```

**原则**：
- 仓库存储所有**参考文件**和**中间产物**
- OneDrive 存放最终 PPT，定稿后同步到仓库 `Finals/` 备份

---

## 阶段流程

### Phase 1：Case 接手

1. 将 case PDF 放入 `Drafts/case_original.pdf`
2. 在 `Plans/meeting_notes.md` 记录首次讨论要点
3. 明确任务分工，编辑 `Tasks/current_tasks.md`

### Phase 2：分析框架

1. 在 `Drafts/` 下创建框架文档（如 `framework_v1.md`）
2. 使用 MECE 方法分解问题
3. 识别需要数据支撑的关键假设

### Phase 3：数据收集与处理

1. 将外部数据放入 `Preprocessings/raw/`
2. 脚本处理后存到 `Preprocessings/processed/`
3. 分析结果输出到 `Reports/`

### Phase 4：撰写报告

1. 各部分草稿放入 `Drafts/`
2. 定期合并到 `Reports/draft_integration.md`
3. 交叉审核（至少一名队友）

### Phase 5：Slide 制作

1. 根据 `Reports/` 中的分析结果制作 PPT
2. PPT 初稿保存到 OneDrive sharedoc
3. 每次修改在仓库 `Drafts/slide_drafts/` 留下版本备份
4. 定稿后复制到 `Finals/presentation_final.pptx`

---

## 文件命名规范

- 日期格式：`YYYY-MM-DD`
- 版本号：`v1`, `v2`, `v3`
- 示例：`2026-04-21_analysis_v1.md`

---

## 目录职责

| 目录 | 内容 | 谁负责 |
|------|------|--------|
| `People/` | 队员信息 | 各自维护 |
| `Drafts/` | 所有草稿、case 原件、slide 版本 | 所有人 |
| `Finals/` | 最终定稿（PPT + 报告备份） | 所有人 |
| `Plans/` | 会议记录、时间线、决策 | 队长 |
| `Preprocessings/` | 数据处理脚本与结果 | 数据负责 |
| `Reports/` | 分析报告、图表输出 | 分析负责 |
| `Scripts/` | 可复用代码 | 代码负责 |
| `Tasks/` | 任务分配与进度 | 队长 |

---

## 沟通与同步

- **日常沟通**：微信群
- **文档协作**：OneDrive sharedoc（PPT）
- **代码与文本**：本仓库
- **会议节奏**：每 1-2 天同步一次进展

---

## 状态标记

在 `Tasks/current.md` 中使用状态：

- `[ ]` 待开始
- `[W]` 进行中
- `[D]` 等待审核
- `[✓]` 已完成

---

*最后更新：2026-04-21*