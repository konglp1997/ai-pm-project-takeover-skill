# GitHub 发布说明

建议仓库名：`ai-pm-project-takeover-skill`。

## 发布前检查

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/ai-pm-project-takeover
git status
```

确认：

- README 和示例使用新品牌。
- 没有真实公司、客户、Prompt、指标、内部路径、Token 或私有架构。
- Demo 是虚构/匿名化案例。
- CI、License、Security、Contributing、Roadmap 和 Interview Guide 齐全。

## 新仓库推送

```bash
git init
git add .
git status
git commit -m "Initial release of AI PM Project Takeover Skill"
git branch -M main
git remote add origin git@github.com:<你的用户名>/ai-pm-project-takeover-skill.git
git push -u origin main
```

## 已有仓库改名

GitHub 仓库设置中把名称改为 `ai-pm-project-takeover-skill`，然后更新本地远程：

```bash
git remote set-url origin https://github.com/<你的用户名>/ai-pm-project-takeover-skill.git
git push
```

GitHub 通常会保留旧 URL 重定向，但 README、Clone 命令和作品集链接应使用新地址。

## Release

```bash
git tag -a v0.2.0 -m "AI PM Project Takeover v0.2.0"
git push origin v0.2.0
```

Release 页面重点说明用户问题、九阶段工作流、20 章输出、E0–E3 模型、Demo、测试结果和当前限制。
