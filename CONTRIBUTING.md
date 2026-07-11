# Contributing

## Issue

请提供 Python、操作系统和浏览器版本、准确命令、最小配置、期望与实际行为。提交前删除秘密、内部地址和个人数据。安全问题按 `SECURITY.md` 私下报告。

## 变更流程

1. 从最新主分支创建功能分支。
2. 保持改动聚焦。
3. 为脚本行为变化增加测试。
4. 同步更新 README、USAGE、ARCHITECTURE 或 MAINTAINING。
5. 运行测试和 Skill 校验。

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/build-project-handbook
```

## 要求

- Python 3.9+，优先标准库。
- UTF-8、LF 换行。
- 路径使用 `pathlib.Path` 并规范化公开输入。
- 错误信息不输出秘密值。
- 脚手架默认不覆盖用户文件。
- JavaScript 不引入远程运行依赖。
- 新配置字段必须记录类型、默认行为与兼容性。
- 第三方资产必须记录版本、来源和许可证。

提交标题使用祈使句，例如 `Reject asset paths outside the handbook root`。PR 描述包含动机、测试结果、兼容性影响和必要截图。
