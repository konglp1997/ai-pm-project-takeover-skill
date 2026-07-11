# 使用说明

## 安装

从仓库根目录执行：

```bash
mkdir -p ~/.codex/skills
cp -R skill/build-project-handbook ~/.codex/skills/build-project-handbook
```

目录名必须与 `SKILL.md` 中的 `name: build-project-handbook` 一致。安装后刷新 Codex 的 Skill 列表。

## 推荐提示词

完整项目：

```text
使用 $build-project-handbook 审计这个仓库的有效文档和当前代码，
在 docs-site/ 生成离线项目手册。必须包含完整阅读路线、30 分钟速览、
按角色路线、职责边界、运行流程、数据与集成、部署运维、术语表和漂移清单。
构建后运行验证，并明确报告没有执行的浏览器检查。
```

无文档项目：

```text
使用 $build-project-handbook 按 code-first 路线梳理这个仓库。
先从入口、模块、数据、配置、部署、外部集成和测试建立证据台账，
再生成可离线打开的接手手册。不要把推断写成事实。
```

只整理文档：

```text
使用 $build-project-handbook 按 docs-first 路线重组 docs/，
用代码抽查命令、配置名和关键流程。不要执行应用或部署命令。
```

## 手工使用

### 1. 创建站点源目录

```bash
python3 skill/build-project-handbook/scripts/scaffold_handbook.py ./docs-site
```

脚手架只创建缺失文件，不覆盖已有配置、内容或资产。再次运行可以补齐误删的基础文件。

### 2. 编辑 `handbook.json`

```json
{
  "language": "zh-CN",
  "title": "示例项目手册",
  "subtitle": "面向维护者的项目全景",
  "description": "离线、可搜索的项目手册。",
  "version": "0.1.0",
  "repository": "",
  "sections": [
    {
      "title": "从这里开始",
      "pages": [
        {
          "slug": "index",
          "title": "示例项目手册",
          "summary": "项目定位与阅读入口。",
          "minutes": 5,
          "home": true,
          "sources": ["README.md"]
        }
      ]
    }
  ]
}
```

规则：

| 字段 | 要求 |
|---|---|
| `language` | HTML 语言，例如 `zh-CN` |
| `sections` | 非空；顺序就是推荐阅读顺序 |
| `slug` | 小写字母、数字、连字符；全站唯一 |
| `home` | 全站必须且只能有一个 `true` |
| `minutes` | 大于零的整数 |
| `sources` | 证据路径数组，可以为空 |
| `rationale` | `sources` 为空时必须填写页面依据 |

### 3. 编写页面

每页对应 `content/<slug>.html`。只写正文片段，不写 `html`、`head`、`body`、`script` 或页面级 `h1`。

使用规范链接：

```html
<a href="page:architecture">阅读架构说明</a>
<a href="page:operations#recovery">进入恢复章节</a>
<img src="asset:diagrams/system.svg" alt="系统边界图">
```

构建器会计算正确的相对路径。`asset:` 不允许绝对路径、反斜杠或 `..`。

### 4. 构建和验证

```bash
python3 skill/build-project-handbook/scripts/build_handbook.py ./docs-site
python3 skill/build-project-handbook/scripts/verify_handbook.py ./docs-site
```

生成：

```text
docs-site/
├── index.html
├── pages/*.html
├── assets/style.css
├── assets/app.js
├── assets/search-index.js
├── handbook.json
└── content/*.html
```

验证器检查配置、内容片段、来源、生成页面、内部链接、重复 ID、危险 HTML、远程资产、常见秘密和 Mermaid 本地运行时。

## Mermaid

本仓库不附带 Mermaid，避免未经确认复制第三方代码。需要时：

1. 从 Mermaid 官方发行包取得 `mermaid.min.js`。
2. 遵守其许可证。
3. 放到站点 `assets/mermaid.min.js`。
4. 使用 `<pre class="mermaid">...</pre>`。
5. 在真实浏览器确认生成 SVG 且控制台无错误。

无法捆绑运行时时，优先预渲染 SVG 并用 `asset:` 引用。

## 离线边界

- 样式、交互和搜索索引本地加载。
- 普通外部超链接允许存在，但验证器会警告。
- 远程脚本、样式、图片和媒体会导致失败。
- 主要运行方式是直接打开 `file://.../index.html`。
