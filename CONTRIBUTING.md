# 贡献指南

## 提交问题

请提供 Python、系统、浏览器、目标项目类型、运行命令、最小 `dossier.json`、期望与实际行为。删除真实公司、客户、凭据和内部信息。安全问题按 `SECURITY.md` 私下报告。

## 提交合并请求

1. 保持改动聚焦。
2. 为脚本、必需章节或验证规则变化增加测试。
3. 同步更新 README、USAGE、ARCHITECTURE、OUTPUT-SPEC 或 ROADMAP。
4. 运行：

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/ai-pm-project-takeover
```

## 原则

- Python 3.9+，优先标准库。
- 脚手架默认不覆盖用户内容。
- 错误信息不回显秘密。
- 新 AI PM 框架必须解释支持的决策和证据要求。
- 不把代码测试称为 AI 质量评测。
- 不把演示结果称为业务价值证据。
- 第三方资产必须记录来源、版本和许可证。
