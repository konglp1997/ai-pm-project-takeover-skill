# Build Project Handbook Skill

把散乱、过时或缺失的项目文档，整理成一套以代码证据为基线、支持全文搜索、可离线打开的项目手册。

这是一个可独立安装的 Codex Skill 项目。它参考了 linux.do 主题中 `docs-to-book` 的核心想法，但重新实现了工作流、构建器、验证器和站点资产：不复制上游模板，不依赖 Node.js，仅使用 Python 标准库生成静态站点。

## 解决的问题

- 项目文档按文件类型或时间堆放，新成员不知道从哪里读。
- README、设计文档、配置和实际代码互相矛盾。
- 项目几乎没有文档，需要从入口、模块、数据、配置和测试反推结构。
- 需要双击 `index.html` 即可阅读的交接手册，不想部署文档服务。
- 希望交付包含证据来源、阅读路线、漂移清单与可重复验证。

## 核心能力

- 根据文档完备度选择 docs-first、hybrid 或 code-first 路线。
- 建立资料清单、证据映射、置信度与文档漂移记录。
- 按读者认知路径设计完整、速览和按角色阅读路线。
- 生成离线多页站点：侧边栏、页内目录、全文搜索、上下页、明暗主题、响应式与打印样式。
- 用 `page:<slug>` 和 `asset:<path>` 自动计算相对链接。
- 检查配置、缺页、死链、重复锚点、危险 HTML、远程资源、资产越界和常见秘密形态。

## 与原版的关系

| 方面 | 上游 `docs-to-book` | 本项目 |
|---|---|---|
| 目标平台 | Claude Code 目录 | Codex Skill 标准结构 |
| 构建环境 | Node.js / CommonJS | Python 3 标准库 / JSON |
| 元数据 | 无 `agents/openai.yaml` | 包含 Codex UI 元数据 |
| 链接 | 手写相对链接 | `page:` / `asset:` 规范链接 |
| 验证 | 结构、链接、Mermaid、资产 | 额外检查来源、安全、离线和路径 |
| GitHub 文档 | Skill 内部资料 | README、许可、贡献、安全、维护、发布文档 |
| 测试与 CI | 未提供 | 单元测试与 GitHub Actions |

## 快速安装

```bash
mkdir -p ~/.codex/skills
cp -R skill/build-project-handbook ~/.codex/skills/build-project-handbook
```

刷新 Codex 后调用：

```text
使用 $build-project-handbook，把这个仓库整理成一份离线项目手册。
先审计文档与代码差异，再生成阅读路线、漂移清单和可搜索站点。
```

## 直接运行工具

```bash
python3 skill/build-project-handbook/scripts/scaffold_handbook.py ./my-handbook
python3 skill/build-project-handbook/scripts/build_handbook.py ./my-handbook
python3 skill/build-project-handbook/scripts/verify_handbook.py ./my-handbook
```

打开 `my-handbook/index.html` 即可阅读。编辑 `handbook.json` 和 `content/*.html` 后重新构建；不要直接修改生成文件。

仓库附带已构建示例：打开 [`examples/demo-handbook/index.html`](examples/demo-handbook/index.html)。

## 项目结构

```text
build-project-handbook-skill/
├── skill/build-project-handbook/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── scripts/
│   ├── references/
│   └── assets/site/
├── examples/demo-handbook/
├── tests/
├── docs/
├── .github/workflows/ci.yml
├── README.md
├── LICENSE
└── NOTICE.md
```

## 文档索引

- [完整使用说明](docs/USAGE.md)
- [架构与安全边界](docs/ARCHITECTURE.md)
- [维护与发布版本](docs/MAINTAINING.md)
- [上游审阅和重写决策](docs/UPSTREAM-REVIEW.md)
- [推送到自己的 GitHub](docs/PUBLISHING.md)
- [贡献指南](CONTRIBUTING.md) 与 [安全政策](SECURITY.md)

## 本地验证

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/build-project-handbook
```

## 许可与来源

本项目中新编写的代码和文档使用 [MIT License](LICENSE)。概念来源与上游许可证缺失情况见 [NOTICE.md](NOTICE.md) 和 [上游审阅](docs/UPSTREAM-REVIEW.md)。
