# 系统架构

## 设计目标

AI PM Project Takeover 把“项目理解”设计成四层系统：认知编排、证据模型、确定性工具链和离线交付。

```text
┌──────────────────────────────────────────────────────────┐
│                    Codex + Skill                         │
│  选择路线 / 审计证据 / 产品重构 / AI 审计 / 指标 / 优先级 │
└───────────────────────────┬──────────────────────────────┘
                            │ structured findings
┌───────────────────────────▼──────────────────────────────┐
│                    Evidence Model                        │
│ inventory / ledger / E0-E3 / drift / unknowns / owners │
└───────────────────────────┬──────────────────────────────┘
                            │ dossier.json + HTML fragments
┌───────────────────────────▼──────────────────────────────┐
│                Deterministic Python Tools                │
│ scaffold_dossier → build_dossier → verify_dossier       │
└───────────────────────────┬──────────────────────────────┘
                            │ static files
┌───────────────────────────▼──────────────────────────────┐
│                  Offline Dossier UI                      │
│ navigation / search / evidence badges / theme / print  │
└──────────────────────────────────────────────────────────┘
```

## 1. 认知编排层

`SKILL.md` 定义九阶段工作流：

1. 接手范围与成功定义。
2. 证据清单与置信度。
3. 产品、用户、旅程和能力重构。
4. AI 运行路径审计。
5. 指标、评测与单位经济性。
6. 风险、产品债和利益相关方缺口。
7. 优先级和 30/60/90 天计划。
8. AI PM Dossier 构建。
9. 事实、安全、浏览器和决策质量验证。

详细方法按需放在 `references/`，避免一次加载全部内容。

## 2. 证据模型层

核心数据结构是 Claim：

```text
Claim
├── statement
├── claim_type: product | behavior | AI | metric | safety | roadmap
├── sources[]
├── confidence: E3 | E2 | E1 | E0
├── decision_impact
├── contradictions[]
├── owner
└── next_validation
```

它解决三个问题：

- 防止把代码行为等同于用户价值。
- 防止把 PRD、TODO 或注释等同于已上线能力。
- 把未知问题转化为访谈、埋点、实验、评测或风险任务。

## 3. AI 产品模型

Skill 使用统一运行链路描述 AI 能力：

```text
用户意图 → 输入与策略 → 上下文 → RAG/Memory → Prompt/Orchestration
→ Model → Agent/Tools → Output validation → Human control
→ Action → Feedback → Evaluation
```

每个能力同时记录用户价值、AI 机制、输出契约、失败模式、Guardrails、评测、成本、延迟、隐私和供应商依赖。

## 4. 指标架构

指标被拆成五层：

```text
Business outcome
      ↓
Product adoption and task outcome
      ↓
AI task quality
      ↓
Safety and trust
      ↓
System cost, latency, reliability
```

这样可以避免“模型分数很好，但用户不使用”或“调用量增长，但单位经济性恶化”的局部优化。

## 5. 确定性工具层

### `scaffold_dossier.py`

- 创建完整 20 页目录。
- 只写缺失文件，不覆盖用户内容。
- 初始结论全部标为 E0，避免模板伪装成事实。

### `build_dossier.py`

- 读取 `dossier.json`。
- 重写 `page:` 和 `asset:` 链接。
- 生成侧边栏、页内目录、上下页和搜索索引。
- 对配置文本执行 HTML 转义。
- 清理失效的生成页面，不删除源内容。

### `verify_dossier.py`

- 检查 20 个 AI PM 必需章节。
- 检查配置、来源/依据、内容片段、生成页面和死链。
- 检查危险 URL、内联事件、远程资产和资产越界。
- 检查常见秘密形态和 Mermaid 本地运行时。

脚本负责确定性，Codex 负责需要判断的产品和 AI 推理。

## 6. 交付层

生成站点完全离线：

- 多页导航、页内目录、上一页/下一页。
- 全文搜索、明暗主题、阅读进度、响应式和打印。
- E0–E3 证据标签、决策块和 AI 能力卡片。
- 无 Node.js、无 Python 第三方依赖、无 CDN。

## 安全边界

- HTML 内容被视为受信任的本地作者输入；验证器不是完整沙箱。
- 秘密检测是启发式，不代替专业扫描和人工审查。
- Skill 默认只读目标项目，不自动运行生产或破坏性命令。
- 内部档案与公开案例必须物理分离。

## 兼容性

- Python 3.9+。
- 现代 Chromium、Safari 或 Firefox。
- `file://` 直接打开。
- Mermaid 可选，需单独提供本地运行时或预渲染 SVG。
