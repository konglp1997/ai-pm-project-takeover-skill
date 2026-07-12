# 维护说明

## 兼容性承诺

- Python 3.9+，不引入必需第三方 Python 包。
- 生成 dossier 可通过 `file://` 打开。
- 同一主版本内保持 `dossier.json` 字段和必需 slug 兼容。
- 已发布 slug 不随意更改，避免破坏书签和引用。

## 修改 Skill

1. 把触发场景写在 frontmatter `description`。
2. `SKILL.md` 只保留流程、路由和硬规则。
3. 详细方法放一层 `references/`，从 `SKILL.md` 直接链接。
4. 仓库 README 和维护资料不放进 Skill 目录。
5. 更新后检查 `agents/openai.yaml` 与 Skill 名和提示一致。

## 修改 AI PM 框架

- 新增决策领域时更新 `REQUIRED_SLUGS`、脚手架、输出规范、示例和测试。
- 调整 E0–E3 时同时更新 source audit、authoring、README 和 demo。
- 指标框架必须保持业务→产品→AI→安全→系统的可追踪性。
- 不把技术可观察性误写成产品价值证据。
- 建议和优先级必须保留 evidence、owner、dependency、exit criteria。

## 修改脚本

- `dossier.json` 是导航和页面元数据事实来源。
- `content/` 是正文来源；生成 HTML 不作为编辑入口。
- 路径必须规范化并阻止越出 dossier 根目录。
- 配置文本写入 HTML 前必须转义。
- 脚手架默认不得覆盖用户内容。
- 秘密检测只报告类型和文件，不输出匹配值。

## 测试

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/ai-pm-project-takeover
```

测试至少覆盖：

- 20 页完整 pipeline。
- 非覆盖脚手架。
- 缺少必需章节。
- 坏 `page:` 链接和资产越界。
- 危险 URL 和远程 CSS。
- 来源/依据缺失。
- 秘密形态不回显。

## 视觉回归

检查管理摘要、AI 系统、指标、风险和接手计划页面；覆盖桌面、窄屏、明暗主题、搜索、长表格、键盘焦点和打印。Mermaid 必须真实渲染验证。

## 发布

1. 更新 CHANGELOG 和 ROADMAP。
2. 运行测试、Skill 校验、示例构建和全局残留扫描。
3. 检查 README、USAGE、ARCHITECTURE、OUTPUT-SPEC 和 PROJECT-OVERVIEW。
4. 检查 demo 不含公司或个人敏感信息。
5. 提交、推送、确认 CI，按需发布版本标签。
