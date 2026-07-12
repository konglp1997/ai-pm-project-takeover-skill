# 使用说明

## 你实际怎么使用

Skill 不是独立应用。安装后，在 Codex 中打开你要接手的项目目录，通过提示词调用。Codex 会按照 Skill 的流程阅读资料和代码，并调用脚本生成档案。

```text
AI PM Project Takeover Skill
          ↓ 指导 Codex
目标项目的文档、代码、配置、测试和数据定义
          ↓
takeover-notes/ + ai-pm-dossier/
```

## 安装

```bash
mkdir -p ~/.codex/skills
cp -R skill/ai-pm-project-takeover ~/.codex/skills/ai-pm-project-takeover
```

目录必须保持：

```text
~/.codex/skills/ai-pm-project-takeover/SKILL.md
```

刷新或重启 Codex。

## 完整接手提示词

在目标项目根目录调用：

```text
使用 $ai-pm-project-takeover 接手当前 AI 项目。

我的角色是新接手项目的 AI 产品经理。请从产品、用户、业务、AI 系统、数据、
评测、指标、架构、运维和组织协作角度完成系统尽调。

要求：
1. 先选择 Product-led、Hybrid audit 或 Evidence recovery 路线并解释原因。
2. 建立 takeover-notes/，记录资料清单、证据台账、文档漂移和未知问题。
3. 所有重要结论使用 E3/E2/E1/E0 置信度，不要把推断或路线图写成已上线事实。
4. 梳理用户、买方、管理员、运营、审核者和下游消费者。
5. 梳理核心旅程、失败恢复、能力地图、范围和上线状态。
6. 梳理模型、Prompt、上下文、RAG、Memory、Agent、工具调用、Guardrails、
   人工审核、Fallback 和可观测性。
7. 建立业务、产品、AI 质量、安全、系统和单位经济性指标体系。
8. 输出产品债、风险、待确认问题、利益相关方访谈议程和 30/60/90 天计划。
9. 在 ai-pm-dossier/ 生成可搜索离线档案并运行构建与验证。
10. 报告未执行的浏览器、运行时或生产数据检查。
```

## 快速一天接手模式

```text
使用 $ai-pm-project-takeover 对当前项目做一天内可完成的快速接手。
优先输出 Executive Brief、产品与用户、AI 系统图、当前能力状态、指标缺口、
Top 10 风险/未知问题、关键利益相关方问题和前 30 天计划。
深度不足的内容标 E0/E1，不要猜测。
```

## 只有代码、没有产品文档

```text
使用 $ai-pm-project-takeover 按 Evidence recovery 路线接手当前项目。
从入口、前端路由、API、Prompt、模型配置、Agent/RAG、Schema、测试、部署和历史
反推当前产品行为。业务目标、用户价值和路线图无法从仓库确认时，整理为高优先级
利益相关方问题，不要自行补全。
```

## 作品集安全模式

```text
使用 $ai-pm-project-takeover 基于当前项目制作一份公开作品集案例。
保留问题框架、方法、设计决策、架构、验证、权衡和学习；删除或泛化公司名称、
客户数据、真实指标、Prompt、私有模型、内部路径、端点、供应商和商业机密。
任何无法公开的内容不要进入搜索索引和截图。
```

## 你需要参与的检查点

Codex 可以自动继续，但建议你在四个节点确认：

1. **证据路线：** 是否确实需要代码反推。
2. **产品模型：** 用户、问题、范围和上线状态是否符合组织认知。
3. **关键未知：** 哪些问题值得找人、补数据或做实验。
4. **接手计划：** 优先级、负责人和退出标准是否现实。

## 输出目录

```text
target-project/
├── takeover-notes/
│   ├── 00-brief.md
│   ├── 01-inventory.md
│   ├── 02-evidence-ledger.md
│   ├── 03-drift-register.md
│   └── 04-unknowns.md
└── ai-pm-dossier/
    ├── dossier.json
    ├── content/
    ├── assets/
    ├── pages/
    ├── index.html
    └── README.md
```

打开 `ai-pm-dossier/index.html` 阅读。

## 手工构建

通常由 Codex 自动运行。需要手工操作时：

```bash
python3 skill/ai-pm-project-takeover/scripts/scaffold_dossier.py ./ai-pm-dossier
python3 skill/ai-pm-project-takeover/scripts/build_dossier.py ./ai-pm-dossier
python3 skill/ai-pm-project-takeover/scripts/verify_dossier.py ./ai-pm-dossier
```

脚手架只创建缺失文件，不覆盖已有内容。

## `dossier.json`

```json
{
  "language": "zh-CN",
  "title": "AI Product Takeover Dossier",
  "subtitle": "Evidence-backed AI PM operating model",
  "description": "Project takeover dossier",
  "version": "0.1.0",
  "repository": "",
  "sections": [
    {
      "title": "Start",
      "pages": [
        {
          "slug": "index",
          "title": "AI Product Takeover",
          "summary": "Project identity and takeover entry point.",
          "minutes": 4,
          "home": true,
          "sources": ["README.md"],
          "status": "supported"
        }
      ]
    }
  ]
}
```

`status` 可选值：`verified`、`supported`、`inferred`、`unknown`。

页面链接使用：

```html
<a href="page:ai-system">查看 AI 系统</a>
<img src="asset:diagrams/ai-runtime.svg" alt="AI 运行路径">
```

## 安全边界

- 不要把真实 `.env`、Token、客户数据或私有 Prompt 写入档案。
- 内部档案和公开作品集必须分开。
- 自动秘密扫描不是安全证明，公开前人工检查 `content/`、生成页面和搜索索引。
- 不要为了理解项目擅自执行迁移、部署、生产访问或外部写操作。
