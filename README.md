# AI PM Project Takeover Skill

把一个陌生 AI 项目的文档、代码、Prompt、模型、RAG、Agent、数据、评测、指标和路线图，转化为 AI 产品经理可以直接使用的“项目接手操作系统”。

这不是一个仓库摘要器，也不只是文档网站生成器。它解决的是更困难的问题：AI 产品经理接手项目时，如何从碎片化资料中建立可信的产品认知，分清事实、推断和未知，找到影响决策的风险与缺口，并形成可执行的 30/60/90 天计划。

## 为什么需要它

AI 产品接手通常同时面对四种断层：

- **产品断层：** PRD、路线图、销售说法和真实用户行为不一致。
- **AI 断层：** 只知道模型名称，不知道 Prompt、上下文、RAG、Agent、工具和人工审核如何共同工作。
- **指标断层：** 有模型指标或调用量，却无法解释用户价值、质量、安全、成本和商业结果。
- **组织断层：** 关键知识分散在工程、算法、数据、设计、运营、销售和支持人员之间。

本 Skill 使用证据分级、产品重构、AI 系统审计、指标评测设计、风险治理和接手计划，把这些断层组织成一个可验证的交付物。

## 核心输出

### 1. `takeover-notes/`：接手过程资料

```text
takeover-notes/
├── 00-brief.md
├── 01-inventory.md
├── 02-evidence-ledger.md
├── 03-drift-register.md
└── 04-unknowns.md
```

- 资料清单、负责人、时间和可信度。
- 关键结论与证据映射。
- 产品叙事、文档、代码、配置和运行事实之间的冲突。
- 待确认问题、影响决策和验证方式。

### 2. `ai-pm-dossier/`：项目接手档案

默认包含 20 个章节：

- Executive Brief 与阅读路线。
- 产品背景、用户、价值主张、旅程和能力地图。
- AI 系统、Prompt/RAG/Agent/工具、数据与知识架构。
- 评测、Guardrails、人工审核和反馈闭环。
- 业务、产品、AI 质量、安全、系统指标与单位经济性。
- 技术架构、集成、运维、依赖和隐藏人工成本。
- 当前状态、路线图、产品债、风险和未知问题。
- 利益相关方访谈议程与 30/60/90 天计划。
- 漂移清单、术语表和来源地图。

档案是可搜索、响应式、支持明暗主题和打印的离线站点，直接打开 `index.html` 即可使用。

## 证据分级

| 等级 | 含义 | 写法 |
|---|---|---|
| E3 · Verified | 多个当前来源，或运行/指标直接验证 | “产品当前会……” |
| E2 · Supported | 一个强当前来源 | “当前证据表明……” |
| E1 · Inferred | 间接或不完整证据 | “推测……，需与……确认” |
| E0 · Unknown | 缺失或互相矛盾 | “未知；在……前必须确认” |

未知不是失败。高影响的 E0/E1 会被转化为访谈问题、实验、埋点任务、评测任务或路线图风险。

## 工作流架构

```text
项目资料与代码
      │
      ▼
证据审计 ──→ E0–E3 置信度 ──→ 漂移与未知问题
      │
      ├─→ 产品重构：用户 / 价值 / 旅程 / 能力 / 范围
      ├─→ AI 审计：模型 / Prompt / RAG / Agent / 工具 / 人审
      ├─→ 评测指标：业务 / 产品 / AI / 安全 / 系统 / 经济性
      └─→ 交付治理：风险 / 产品债 / 利益相关方 / 优先级
                                  │
                                  ▼
                         30 / 60 / 90 天计划
                                  │
                                  ▼
                 离线 AI PM Dossier + 自动验证报告
```

详细设计见 [架构说明](docs/ARCHITECTURE.md) 和 [设计决策](docs/DESIGN-DECISIONS.md)。

## 安装

```bash
mkdir -p ~/.codex/skills
cp -R skill/ai-pm-project-takeover ~/.codex/skills/ai-pm-project-takeover
```

刷新 Codex 后调用：

```text
使用 $ai-pm-project-takeover 接手当前 AI 项目。
从产品经理视角审计文档、代码、Prompt、模型、RAG、Agent、数据、评测、指标、
架构、运维和路线图，建立 E0–E3 证据台账，生成 takeover-notes/ 和 ai-pm-dossier/。
不要把推断写成事实，最后输出风险、待确认问题和 30/60/90 天计划。
```

完整用法见 [USAGE.md](docs/USAGE.md)。

## 手工运行确定性工具

```bash
python3 skill/ai-pm-project-takeover/scripts/scaffold_dossier.py ./ai-pm-dossier
python3 skill/ai-pm-project-takeover/scripts/build_dossier.py ./ai-pm-dossier
python3 skill/ai-pm-project-takeover/scripts/verify_dossier.py ./ai-pm-dossier
```

脚手架只创建缺失文件，不覆盖已有内容；构建器和验证器仅使用 Python 标准库。

## 演示

打开 [`examples/ai-pm-dossier-demo/index.html`](examples/ai-pm-dossier-demo/index.html) 查看完整 20 页档案结构。

## 作品集与面试

这个项目可以从三个层面讲解：

1. **产品层：** 发现 AI PM 项目接手不是“读文档”，而是建立可信决策模型。
2. **AI 层：** 把模型、Prompt、RAG、Agent、数据、评测、Guardrails 和人机协作放进同一产品框架。
3. **工程层：** 用 Skill 负责编排与判断，用 Python 负责确定性构建和验证，用离线站点负责交付。

面试讲解脚本、常见追问和演示顺序见 [INTERVIEW-GUIDE.md](docs/INTERVIEW-GUIDE.md)。

## 项目结构

```text
ai-pm-project-takeover-skill/
├── skill/ai-pm-project-takeover/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   ├── scripts/
│   └── assets/site/
├── examples/ai-pm-dossier-demo/
├── tests/
├── docs/
├── .github/workflows/ci.yml
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## 文档

- [完整使用说明](docs/USAGE.md)
- [系统架构](docs/ARCHITECTURE.md)
- [设计决策](docs/DESIGN-DECISIONS.md)
- [输出规范](docs/OUTPUT-SPEC.md)
- [面试讲解指南](docs/INTERVIEW-GUIDE.md)
- [产品路线图](docs/ROADMAP.md)
- [维护与版本](docs/MAINTAINING.md)
- [发布到 GitHub](docs/PUBLISHING.md)
- [安全政策](SECURITY.md) 与 [贡献指南](CONTRIBUTING.md)

## 验证

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/ai-pm-project-takeover
```

## License

[MIT License](LICENSE) © 2026 konglp1997
