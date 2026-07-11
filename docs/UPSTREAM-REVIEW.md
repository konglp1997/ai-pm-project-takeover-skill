# 上游项目审阅

## 来源

- linux.do：<https://linux.do/t/topic/2540331>
- 仓库：<https://github.com/lili-luo/aicoding-cookbook>
- 目录：`skills/claude code/docs-to-book`
- 审阅提交：`f1cf1dbdb6f9d2604fa494927b4eb89c38195168`
- 审阅日期：2026-07-10

## 原项目结构

```text
docs-to-book/
├── SKILL.md
├── references/
│   ├── classification.md
│   ├── codebase-survey.md
│   ├── quality-checks.md
│   ├── reading-path.md
│   └── voice-style.md
└── templates/
    ├── app.js
    ├── book.config.js
    ├── build.js
    ├── content-example.html
    ├── style.css
    └── verify.js
```

原项目先判断文档完备度，再选择文档优先、混合或代码优先路线；随后按认知顺序重排内容，生成带导航、搜索、明暗主题和 Mermaid 的静态站点。

## 保留的高层思想

1. 重叙述而不是搬运原目录。
2. 代码是当前事实基线。
3. 主线、速览和按角色路线降低接手成本。
4. 文档漂移必须显式记录。
5. 静态离线交付适合内部和受限环境。
6. Mermaid 与视觉必须真实渲染验证。

## 发现的问题

### 许可证缺失

审阅提交的仓库根目录和 `docs-to-book` 目录都没有许可证。另一个子目录的许可证不能推定覆盖全仓库。直接复制并公开上游模板存在版权不确定性，因此本项目独立实现并保留概念来源说明。

### Codex 结构不足

上游位于 Claude Code 目录，没有 Codex 推荐的 `agents/openai.yaml`，也不是独立 GitHub Skill 项目结构。

### 构建和验证边界

上游依赖 Node.js/CommonJS，验证重点是页面、链接、HTML、Mermaid 和资产。本项目改为 Python/JSON，并增加规范链接、路径越界、远程资源、危险 URL、图片替代文本、来源依据和常见秘密检查。

### 仓库文档不足

上游作为 Skill 资源已经有用，但独立发布还缺 README、许可证边界、贡献、安全、维护、发布和变更文档。本项目将这些仓库级资料放在 Skill 外部。

## 重写决策

| 决策 | 原因 |
|---|---|
| Skill 名 `build-project-handbook` | 动作式名称，触发意图清晰 |
| 仓库文档与 Skill 分离 | 兼顾 GitHub 维护和 Skill 精简 |
| Python + JSON | 标准库、跨平台、易校验 |
| `page:` / `asset:` | 消除根页与嵌套页的相对路径错误 |
| 证据台账与置信度 | 防止把推断写成事实 |
| 非破坏性脚手架 | 保护用户已有内容 |
| 源与输出双重验证 | 同时定位作者错误与构建错误 |
| 不捆绑 Mermaid | 明确第三方许可和离线依赖 |
