# 输出规范

## A. `takeover-notes/`

### `00-brief.md`

- 接手角色、范围、时间、受众和决策。
- 保密级别和允许公开的边界。
- 已知利益相关方、系统和资料位置。
- 选择的证据路线及原因。

### `01-inventory.md`

| Source | Type | Owner | Date | Freshness | Confidentiality | Supports |
|---|---|---|---|---|---|---|

必须覆盖产品、研究、设计、指标、代码、AI、数据、评测、测试、部署、事件、路线图和支持材料。

### `02-evidence-ledger.md`

| ID | Claim | Type | Evidence | Confidence | Decision impact | Next validation |
|---|---|---|---|---|---|---|

重要结论必须可追踪；不要求给每句话编号。

### `03-drift-register.md`

| Narrative | Current evidence | Impact | Provisional authority | Owner/action |
|---|---|---|---|---|

### `04-unknowns.md`

| Question | Why it matters | Decision blocked | Who can answer | Validation | Priority |
|---|---|---|---|---|---|

## B. `ai-pm-dossier/`

### 必需章节

| Slug | 核心内容 |
|---|---|
| `index` | 项目身份、证据路线、当前置信度、下一决策 |
| `executive-brief` | 产品、AI 价值、状态、风险、优先事项 |
| `reading-guide` | 管理层、AI 产品经理、工程/算法和跨职能评审路线 |
| `product-context` | 用户、买方、角色、问题、价值、阶段、边界 |
| `user-journeys` | Happy path、失败恢复、人机交接、可观测事件 |
| `capability-map` | 用户结果、能力、AI 贡献、上线状态、缺口 |
| `ai-system` | 模型、Prompt、上下文、RAG、Agent、工具、Fallback |
| `data-knowledge` | 来源、血缘、检索、Memory、隐私、反馈 |
| `evaluation-guardrails` | 数据集、Rubric、基线、发布门槛、安全、人审 |
| `metrics-scorecard` | 业务、产品、AI、安全、系统五层指标 |
| `economics-performance` | 单任务成本、延迟、可靠性、容量和价值假设 |
| `architecture-integrations` | 运行边界、外部依赖、契约和所有权 |
| `operations-dependencies` | 部署、监控、事件、供应商和人工运营 |
| `current-state-roadmap` | Live、limited、partial、planned、deprecated、unknown |
| `product-debt` | 证据、指标、流程、评测和决策债务 |
| `risks-unknowns` | 风险、未知、影响、置信度、缓解和负责人 |
| `stakeholder-agenda` | 各角色问题、证据请求和会议目标 |
| `takeover-plan` | 30/60/90 天结果、行动、依赖和退出标准 |
| `drift-register` | 叙事、文档、代码、配置和运行事实冲突 |
| `glossary-sources` | 术语、定义、来源、负责人、新鲜度和置信度 |

### 页面验收

每个证据敏感页面至少回答：

1. 已知什么。
2. 仍不确定什么。
3. 为什么影响产品决策。
4. 下一步如何验证或决策。

### 风险格式

| Risk | Scenario | User/outcome | Impact | Likelihood | Detectability | Confidence | Mitigation | Owner |
|---|---|---|---|---|---|---|---|---|

### 计划格式

| Horizon | Outcome | Actions | Evidence | Dependencies | Owner | Exit criteria |
|---|---|---|---|---|---|---|

禁止使用“熟悉项目”“推进优化”这类不可验收描述。

## C. 自动验收

- 20 个必需 slug 全部存在。
- 每页有来源或明确编写依据。
- `page:` 与 `asset:` 引用有效。
- 生成页面和内部链接完整。
- 无危险 HTML、远程资产、资产越界和明显秘密。
- Mermaid 使用时存在合法本地运行时。

## D. 人工验收

- 抽查产品、AI、指标、架构、风险和计划事实。
- 检查 E0–E3 使用是否一致。
- 检查建议是否有证据、负责人、依赖和退出标准。
- 检查内部和公开边界。
- 检查浏览器、窄屏、搜索、明暗主题、键盘和打印。
