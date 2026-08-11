---
project: AI Cognitive OS / Creator Advisor
version: v0.1
updated_at: 2026-08-09 23:03 +08:00
document_type: Product Specification / Current Truth
status: active
intended_reader:
  - future AI agents
  - project creator
  - future contributors
---

# AI Cognitive OS / Creator Advisor v0.1
## 产品方案书 / Current Truth

> 本文是当前版本的“产品真相源”。后续 AI 在继续设计、开发和评审前，应优先读取本文；除非有新的真实测试证据，否则不要重新推翻已经确认的基本边界。

---

# 1. 项目使命

建设一个面向 AI 时代的个人工作与创作系统。

它不以“让人完成更多任务”为最终目标，而是试图突破当前 AI 主要停留在任务执行和局部效率提升的使用方式，从底层改变创作者如何：

- 理解自己的工作；
- 组织工作和创作；
- 发现 AI 增强机会；
- 从真实实践中发现问题；
- 把重复活动转化为 Workflow / Skill；
- 把长期问题转化为 Project / Exploration / Work；
- 把日常工作中形成的可迁移认知逐渐积累成个人长期资产；
- 最终与 AI 形成长期认知伙伴关系。

长期产品路径：

**Advisor → Workbench → Cognitive Partner**

当前只做第一阶段：**Advisor**。

---

# 2. 大背景与产品前提

目标用户已经拥有并使用强大模型和 Codex / WorkBuddy / Claude Code 等超级 Agent。

因此本产品明确：

- 不做新的基础模型；
- 不做另一个通用 Agent；
- 不做另一个聊天框；
- 不与超级 Agent 竞争执行能力；
- 不重新发明 Agent Runtime。

产品建立在“强模型 + 强 Agent 已经成为基础设施”的背景上。

基本关系：

**Human governs → Advisor recommends → Existing Agent executes**

Advisor 负责判断与组织，Agent 负责执行。

---

# 3. 产品定位

建议定位：

## AI Work & Creation Control Layer
### AI 工作与创作控制层

Advisor 的三个核心动作：

**Observe → Advise → Route**

- Observe：理解工作与创作环境；
- Advise：判断哪里值得改善、升级、停止、自动化或继续探索；
- Route：用户确认后，将动作交给已有超级 Agent。

产品不是工作内容的 System of Record。

核心原则：

> **Connect, don't centralize. Understand, don't merely collect.**
>
> 不搬家，只建立认知。

---

# 4. 目标用户

核心用户不是泛化“知识工作者”，而是：

## AI-native Creator
尤其是：

## Practitioner-Creator / 实践型创作者

典型特征：

- 已经使用强 AI；
- 有真实职业、项目或产业现场；
- 同时把自己视为创作者；
- 不满足于只完成岗位任务；
- 会把工作中的真实问题、矛盾、经验和反馈转化为自己的研究、方法、作品或产品；
- 希望 AI 使用产生长期复利，而不是只节省时间。

职业不是关键分类。

判断标准：

> **这个人是否试图把现实经验变成自己能够长期积累的东西？**

---

# 5. 非目标用户

当前版本不主要服务：

- 只把自己定位为岗位执行者的人；
- 只希望 AI 帮助写邮件、做 PPT、报表、会议纪要的人；
- 只追求 Todo 完成率和单位时间产出的人；
- 希望 AI 自动接管全部工作，而不希望形成个人长期作品或能力的人。

这些需求可以被超级 Agent 直接满足。

本产品关心的是 AI 是否进入人的长期创造与认知复利循环。

---

# 6. 核心价值判断

存在两条 AI 使用路径。

## Efficiency Loop

Task → AI Execution → Time Saved → More Tasks → More Automation

价值存在，但容易把 AI 锁死在效率函数内。

## Creation Loop

Real Work → Problem → AI-assisted Understanding → Model / Method → Work → External Feedback → New Capability / Cognition → Better Problem

本产品选择第二条作为长期方向。

AI 使用阶梯：

1. Task
2. Workflow
3. Skill
4. Capability
5. Creation
6. Cognitive Compounding

Advisor 应帮助用户发现：
- 当前活动在哪一层；
- 哪些东西值得向上升级；
- 哪些东西根本不值得升级。

---

# 7. 第一阶段：Creator Advisor

Advisor 是持续观察真实工作与创作环境的 AI 协作顾问。

它不是先问：

“你今天要我做什么？”

而是先尝试回答：

“你现在到底在做什么？哪些工作结构合理？哪些值得升级？哪些应该停止？哪些正在产生长期作品或研究问题？”

Advisor 的长期目标：

> 从“看见文件”逐渐进化到“看见工作”，再进化到“看见创作者自己尚未命名的问题”。

---

# 8. 检测分层

检测必须从低争议事实逐步走向高不确定认知判断。

## L0 — Fact / Risk
客观事实与硬性风险。

例如：
- 重复文件；
- 版本冲突；
- 明显数据丢失风险；
- 密钥 / 敏感信息暴露；
- 重要未跟踪变更。

## L1 — Workspace Hygiene
环境卫生。

例如：
- 命名混乱；
- Working / Final 混放；
- 无入口；
- 归档失控。

## L2 — Structure
工作结构。

例如：
- 多个文件实际上属于同一项目；
- 输入、过程、输出混合；
- 多个事实源并存；
- 项目边界不清。

## L3 — AI Readiness
AI 就绪度。

例如：
- 上下文只存在文件名；
- 重要判断只存在聊天；
- 重复操作没有写成可复用说明；
- 工作流缺少明确输入 / 输出。

## L4 — Workflow / Skill
AI 原生工作模式。

识别：
- Template 候选；
- Workflow 候选；
- Skill 候选；
- Agent 自动化候选。

原则：

> 自动化低价值摩擦，保留高价值认知摩擦。

## L5 — Project / Work / Creation
判断活动是否值得：
- 保持 Task；
- 升级 Project；
- 建立 Exploration；
- 进入 Work；
- 版本化；
- 发布；
- 停止 / 归档。

## L6 — Cognitive / Research Insight
发现：
- 重复矛盾；
- 跨项目的共同模式；
- 尚未命名的问题；
- 潜在作品母题；
- 潜在研究主题。

高阶建议必须明确标记不确定性。

---

# 9. 建议类型

每条建议必须区分其知识性质：

- **HARD_FINDING**：客观 / 近客观事实；
- **BEST_PRACTICE**：通用最佳实践；
- **CREATOR_PRINCIPLE**：Creator Doctrine 产生的方法论建议；
- **INSIGHT_HYPOTHESIS**：高阶认知假设。

每条建议尽量包含：

- Evidence；
- Why it matters；
- Recommendation；
- Confidence；
- Action。

核心原则：

> Advisor 必须知道什么时候在陈述事实，什么时候在引用最佳实践，什么时候在表达一种工作哲学。

---

# 10. Creator Doctrine v0.1

当前默认 Doctrine 具有明确创作者倾向，但不得冒充普适真理。

已确认原则：

1. Creation over throughput。
2. 真实工作是认知传感器。
3. 组织资产留在组织。
4. 个人可以沉淀经过抽象、脱敏后的可迁移认知。
5. 长期个人创作优先考虑版本化。
6. Git / GitHub / Issue 驱动 / 开放协作是强推荐范式，但不是普遍强制规则。
7. 结构应当从真实使用中长出来，而不是提前强制 taxonomy。
8. 自动化低价值摩擦，保留高价值认知摩擦。
9. 作品不是单纯输出，而是认知实验。
10. 开放应当由对象成熟度推动，而不是作为意识形态强推。

---

# 11. 最小对象与演化原则

核心产品原则：

## Minimum Cognitive Primitive

不要要求用户一开始理解完整认知对象模型。

历史上曾讨论：
- Folder
- File
- Project
- Workflow
- Exploration
- Work
- Superproject

但当前版本不应把这些全部强加给用户。

对象应当从真实工作中 emergent：

File → Related Files → Workspace → Project → Exploration / Work → Open Collaboration

Workbench 不能先设计出来。

> **Workbench 应该由 Advisor 运行一段时间以后，从真实建议和真实工作模式中“长出来”。**

---

# 12. 当前 MVP 产品形态

已经确认最小产品形式：

## Creator Advisor Skill v0.1

不是独立 App。

不是本地桌面软件。

不是 Web SaaS。

而是：

> **一个安装 / 下载到用户已有超级 Agent 中即可工作的 Skill 包。**

用户操作：

安装 Skill → 指定当前工作空间 / 仓库 → 使用 Advisor。

Skill 内部可以包含：
- Markdown 规则；
- Creator Doctrine；
- scripts；
- detector modules；
- templates。

对非技术用户不暴露内部工程复杂度。

---

# 13. 已实现 Skill 结构

当前已生成并成功测试：

```text
creator-advisor-skill-v0.1/
├── SKILL.md
├── DOCTRINE.md
├── README.md
├── scripts/
│   └── scan_workspace.py
├── templates/
│   ├── advisor-report.md
│   ├── state.md
│   ├── inbox.md
│   └── history.md
└── detectors/
    └── README.md
```

当前用户测试结果：

> **可以正常运行。**

这验证了：

**Skill + 内置脚本 + 现有超级 Agent**

作为 V0 产品形态在技术交互上是成立的。

这不等于验证了 Advisor Intelligence。

下一阶段核心风险是判断质量。

---

# 14. 三个核心操作

当前版本只支持三个核心认知动作：

## SCAN
看当前状态。

目标：
- 建立基线；
- 优先发现硬性问题；
- 给出少量高价值建议。

## REVIEW
看时间变化。

目标：
- 与历史状态比较；
- 发现变化、重复、停滞和升级阈值。

## REFLECT
看高阶模式。

目标：
- 发现 Workflow / Skill 候选；
- 项目 / 作品升格；
- 重复矛盾；
- 潜在创作和研究主题。

概念上：

**Scan = 当前状态**

**Review = 时间变化**

**Reflect = 高阶模式发现**

---

# 15. State 是关键

Advisor 的价值不是来自扫描次数，而来自比较。

必须逐步保留：

```text
.advisor/
├── state.md
├── inbox.md
├── history.md
└── snapshots/
```

记录：

- 上次看到什么；
- 给过什么建议；
- 用户接受 / 拒绝 / 延后；
- 后来实际结果；
- 正在观察的弱信号。

没有 State，只是一次性扫描器。

有 State，才开始进入持续 Advisor。

---

# 16. 召回机制

不采用“只靠固定周期”的单一模型。

已确认：

## 三层召回

### 1. User Invocation
用户主动：
- Scan
- Review
- Reflect

### 2. Event / Session Trigger
更自然的 V0 触发方式：

用户打开 Codex / WorkBuddy 并进入 Workspace 时，Advisor 可以进行轻量检查。

- 无重要变化 → 静默；
- 有重要变化 → 在当前 Agent 对话中显示 Advisor Card。

任务完成后，也可以记录简短 Advisor Note。

### 3. Periodic Review
高阶模式需要时间序列。

可形成：
- Weekly Advisor Review；
- Monthly Creator Review。

早期不要求真正后台定时器，可在“用户下次打开 Agent”时召回。

---

# 17. Attention Budget

检测可以高频，打扰必须低频。

## Silent
只记录。

## Inbox
下次自然交互时呈现。

## Interrupt
极少数：
- 数据丢失风险；
- 秘密暴露；
- 破坏性版本冲突；
- 证据极强的高价值阈值事件。

核心原则：

> **持续观察，克制打扰，只在值得改变的时候出现。**

---

# 18. 消息出现在哪里

V0 不做新消息中心。

## 前台
现有 Agent 对话。

例如：
- Codex
- WorkBuddy
- 其他支持 Skill 的超级 Agent

Advisor Card 出现在“工作发生的地方”。

## 后台
`.advisor/`

逻辑 Inbox 和历史状态保存在 Workspace 内。

核心交互原则：

> **寄生在工作发生的地方，而不是要求用户去一个新的地方管理工作。**

理想体验：

> 用户照常打开超级 Agent 工作，Advisor 偶尔说一句真正值得用户停下来想一想的话。

---

# 19. 工作空间与未来连接对象

长期 Advisor 需要连接：

## Personal Space
- 本地文件
- Markdown
- PDF
- Office
- 素材

## Collaboration Space
- GitHub
- Repository
- Issue
- PR
- Commit
- Release

## Publication Space
- 微信公众号
- 知乎
- 网站
- 其他发布渠道

## Organization Space
经授权：
- 企业微信文档
- 微盘
- 智能表格
- 日历
- 会议
- 邮件
- 其他组织协作系统

## AI Space
- AI 对话
- Agent 操作记录
- Prompt
- Tool calls
- AI 文件修改
- 接受 / 拒绝建议记录

特别判断：

> AI 操作日志可能比 AI 对话更重要，因为它告诉系统“实际上做了什么”。

当前 v0.1 不做这些连接器。

---

# 20. 工作资产与认知资产边界

核心原则不能简单写成法律意义上的“工作资产归组织、认知资产归个人”。

更严谨的产品原则：

> **组织事实与受保护资产留在组织；个人可以持续沉淀从实践中形成的、经过抽象和脱敏的可迁移认知。**

Advisor 未来可以帮助做 Cognitive Extraction：

组织具体经验
→ 权限 / 边界识别
→ 脱敏
→ 抽象
→ 可迁移认知
→ 个人长期研究 / 创作。

---

# 21. Advisor 的核心长期壁垒

不是基础模型。

不是 Token。

不是聊天 UI。

而是：

- Longitudinal Context；
- Work Model；
- Personal Doctrine；
- Feedback History；
- Cognitive Trace；
- 对“哪些活动值得升级”的长期判断能力。

产品应坚持：

- Model-agnostic；
- Agent-agnostic；
- 尽可能 Local-first。

---

# 22. 当前已验证与未验证

## 已验证

1. 目标用户已经收敛。
2. 不替代大模型 / 超级 Agent 的边界已明确。
3. Skill 作为 V0 产品载体可以正常运行。
4. 内置脚本可以由超级 Agent 调用。
5. SCAN / REVIEW / REFLECT 作为第一组三个操作成立。

## 尚未验证

1. Advisor 是否真的能稳定产生高价值判断。
2. 高阶 REFLECT 是否能持续发现“用户之前没有意识到”的问题。
3. 时间比较是否能比单次扫描产生明显新增价值。
4. 用户是否会认为 Advisor Card 值得被召回，而不是干扰。
5. Doctrine 如何从个人偏好扩展为多用户可 Fork 体系。
6. 哪些检测规则真正具有跨用户普适性。
7. 什么条件下应开始长出 Workbench。

---

# 23. v0.2 不应急着增加什么

暂不优先：

- 独立桌面 App；
- Web SaaS；
- 新聊天 UI；
- 企业微信连接器；
- 微信公众号连接器；
- 多 Agent 编排平台；
- 复杂知识图谱；
- Agent 市场；
- Workbench。

原因：

当前最大风险不是工程，而是 Advisor Intelligence。

---

# 24. v0.2 建议优先级

下一阶段只做“真实测试 → 反馈 → 规则迭代”。

建议积累至少 10–20 个真实测试样本。

每次测试只记录：

1. **有价值**
   - 哪条建议让用户产生“对，而且我之前没意识到”的反应？

2. **错误 / 过度建议**
   - 哪些建议看起来像 AI 套话？
   - 哪些自动化建议破坏了高价值认知摩擦？

3. **遗漏**
   - 用户自己明显看见，但 Advisor 完全没有发现什么？

重点测试三类空间：

- 相对混乱的真实工作空间；
- 长期个人创作 / 研究空间；
- 已经成熟的 Git 仓库。

重点测试三个时间尺度：

- SCAN；
- 一段时间后的 REVIEW；
- REFLECT。

---

# 25. 第一阶段成功标准

不是：

- 扫描了多少文件；
- 找到多少重复文件；
- 节约多少分钟；
- 完成多少任务。

而是：

> **Advisor 是否开始形成值得信赖的工作与创作判断。**

更高级的成功信号：

> Advisor 能否持续发现“值得成为 Skill、Project、Work、研究主题”的东西，而其中有一部分是用户此前没有意识到的。

---

# 26. 长期产品路线

当前仍保留：

## Phase 1 — Advisor
看懂工作世界。

## Phase 2 — Workbench
从真实工作模式中自然长出来，承载已被证明确有价值的对象和结构。

## Phase 3 — Cognitive Partner
AI 与用户共同长期发现问题、形成模型、创造作品并接受现实反馈。

长期目标不是“拥有一个更聪明的任务助手”。

而是：

> **建立一个让 AI 使用产生长期认知复利的个人工作与创作系统。**

---

# 27. 给后续 AI 的继续工作指令

后续 AI 在接手本项目时：

1. 不要重新建议先做独立 App。
2. 不要把产品改成通用知识工作效率工具。
3. 不要重新把目标用户泛化成所有知识工作者。
4. 不要把 GitHub Doctrine 伪装成普遍客观真理。
5. 不要急着设计 Workbench；让它从 Advisor 的真实使用中长出来。
6. 优先分析真实 Advisor 输出质量。
7. 每个新增功能都应回答：它是否帮助 Advisor 更好地 Observe / Advise / Route？
8. 继续坚持：
   - 持续观察；
   - 克制打扰；
   - 自动化低价值摩擦；
   - 保留高价值认知摩擦；
   - 工作资产与个人认知之间保持边界；
   - 作品和现实反馈是长期复利的重要闭环。

---

# 28. 当前一句话定义

> **Creator Advisor 是建立在强大模型和超级 Agent 之上的 AI 工作与创作顾问：它持续理解创作者真实的工作环境，发现结构问题、AI 增强机会、作品化机会和潜在研究问题，再把用户确认后的行动交给现有 Agent 执行。**

