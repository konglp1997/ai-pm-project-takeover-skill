# SupportLens AI 项目接手档案演示

这是一个完全虚构的案例，用于展示 `ai-pm-project-takeover` 的输出。
产品名称、组织、证据、数据、指标、阈值和结果均为合成内容，不代表任何真实公司或生产系统。

## 维护方式

1. 在 `dossier.json` 中编辑导航、元数据、来源和置信度。
2. 在 `content/<slug>.html` 中编辑正文片段。
3. 使用 `python3 /path/to/build_dossier.py .` 重新构建。
4. 使用 `python3 /path/to/verify_dossier.py .` 执行验证。

不要直接编辑生成的 `index.html`、`pages/` 或 `assets/search-index.js`。
包含机密信息的内部档案必须与可对外共享的材料分开保存并独立审查。
