# 发布到自己的 GitHub

本项目不会替你创建远程仓库或执行 GitHub 写操作。

## 发布前

1. 把 `LICENSE` 的版权主体改成你的姓名或组织，也可以保留 contributors。
2. 保留 `NOTICE.md` 与上游许可边界。
3. 更新 README 中的项目名、安装路径或截图。
4. 运行测试与 Skill 校验。
5. 检查个人路径、内部地址、令牌和临时产物。

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/build-project-handbook
```

## 初始化和推送

先在 GitHub 创建空仓库，例如 `build-project-handbook-skill`，不要自动生成 README 或 LICENSE。然后在本项目根目录执行：

```bash
git init
git add .
git status
git commit -m "Initial release of build-project-handbook skill"
git branch -M main
git remote add origin git@github.com:<你的用户名>/build-project-handbook-skill.git
git push -u origin main
```

推送前阅读 `git status`，不要把上游下载目录、真实项目代码或秘密文件加入提交。不要把访问令牌写进远程 URL。

## 首次发布后

- 确认 GitHub Actions 通过。
- 添加 `codex-skill`、`documentation`、`offline-first` 等主题。
- 创建 `v0.1.0` 标签与 Release。
- 明确真正的 Skill 位于 `skill/build-project-handbook/`。

```bash
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```
