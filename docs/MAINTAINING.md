# 维护说明

## 兼容性

- Python 3.9+。
- 不引入必需第三方 Python 包。
- 生成站点可通过 `file://` 打开。
- 同一主版本内保持 `handbook.json` 兼容。
- 不轻易更改已发布页面 slug。

## 修改 Skill

1. 把触发场景写在 frontmatter 的 `description`。
2. 保持 `SKILL.md` 为流程骨架，细节放一层 `references/`。
3. 新 reference 必须从 `SKILL.md` 直接链接并说明何时读取。
4. 不在真正的 Skill 目录加入 README、变更日志或仓库文档。
5. 确认 `agents/openai.yaml` 与 Skill 一致。

## 修改构建器

- `handbook.json` 继续作为导航与元数据事实来源。
- `content/` 继续作为正文来源。
- 新字段必须有校验、默认行为和文档。
- 路径必须规范化并阻止越出站点根目录。
- 配置文本写入 HTML 前必须转义。
- 引入远程依赖前评估离线承诺、许可、体积和失败模式。

## 修改验证器

- 错误表示不应交付；警告表示需要人工判断。
- 尽量同时覆盖源和生成结果。
- 秘密检测只报告文件和类别，不输出匹配值。
- 添加安全检查时增加失败测试。
- 不把启发式扫描描述成安全证明。

## 测试与发布

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/build-project-handbook
```

视觉回归至少检查桌面/窄屏、长标题、长代码、宽表格、明暗主题、搜索、键盘焦点和打印。修改 Mermaid 时必须验证真实 SVG。

版本策略：

- Patch：修复脚本、样式、文档或误报。
- Minor：新增向后兼容的工作流、组件或字段。
- Major：修改配置、目录、链接语义或最低环境。
