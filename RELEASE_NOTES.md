RELEASE_NOTES.md

# 富丽 FULI v0.2

## From Creator Advisor to FULI

v0.1 完成了一件非常重要但很基础的事情：

> 验证了“Skill + 内置脚本 + 现有超级 Agent”这种最小产品形态可以正常运行。

但第一次真实测试之后，我们重新追问了一个更重要的问题：

> **如果 Codex、WorkBuddy 等超级 Agent 本身已经能够检查本地文件和仓库，那么这个 Skill 为什么还要存在？**

这个问题推动了 v0.2。

---

# v0.2 的核心变化

## 1. Creator Advisor 正式更名为「富丽 FULI」

`Creator Advisor` 准确，但只是一个功能描述。

v0.2 开始使用人格化名称：

# 富丽 FULI

“富丽”首先是一个人的名字，同时与中文“复利”接近。

它代表这个产品新的核心价值：

> **发现工作中值得复利的东西。**

富丽不只关心：

> 今天帮用户完成了多少事情。

她更关心：

> 今天做的事情，有多少能够在未来继续产生价值。

---

# 2. 从“文件扫描器”升级为“判断层”

v0.1 中，Skill 内置 Workspace Scanner，并把扫描作为主要入口。

这很快暴露出一个问题：

> 超级 Agent 本来就能够读取文件、浏览目录、搜索、查看 Git 和理解代码。

重复建设这些能力没有意义。

因此 v0.2 明确：

> **FULI 的核心不是给 Agent 增加眼睛，而是给它增加判断标准。**

新的能力模型：

```text
Super Agent
=
Read
+ Search
+ Reason
+ Write
+ Execute

FULI
=
Inspection Protocol
+ Judgment Framework
+ Creator Doctrine
+ Longitudinal Memory
+ Attention Policy
```

一句话：

> **Agent 有能力，富丽给它判断标准。**

---

# 3. Native First

v0.2 改变工作空间检查策略。

原来：

```text
FULI
→ 自带扫描脚本
→ Workspace Snapshot
→ 分析
```

现在：

```text
FULI
→ 优先调用宿主 Agent 原生能力
→ 获取必要证据
→ 使用富丽判断框架
→ 必要时才调用确定性脚本
```

原则：

> **Native first, script when useful.**

内置脚本仍然保留，但只负责：

* Hash 重复检测
* 文件时间统计
* Snapshot
* 历史比较
* 其他需要确定性的辅助工作

它不再是产品的核心。

---

# 4. “复利价值”成为新的核心评价函数

v0.1 更强调：

> 工作空间有没有问题？

v0.2 开始进一步问：

> **这里有什么值得未来继续积累？**

FULI 会尝试观察：

```text
Task
→ Workflow
→ Skill
→ Capability
→ Project / Work
→ External Feedback
→ Better Cognition
→ Better Problems
```

并同时判断：

* 什么值得自动化
* 什么不应该自动化
* 什么值得项目化
* 什么正在形成作品
* 什么应该停止
* 什么可能成为长期研究问题

---

# 5. 保留高价值认知摩擦

v0.2 正式加入一个重要原则：

> **自动化低价值摩擦，保留高价值认知摩擦。**

重复并不天然等于应该 Skill 化。

如果一个过程包含大量：

* 阅读
* 比较
* 判断
* 问题定义
* 品味形成
* 模型重构

那么这种摩擦可能正是创作者形成能力的过程。

FULI 应该有能力说：

> **这件事暂时不建议自动化。**

---

# 6. SCAN / REVIEW / REFLECT 被重新定义

三个核心操作仍然保留，但含义进一步清晰。

## SCAN

> **现在最值得注意什么？**

关注当前状态。

---

## REVIEW

> **和上一次相比，什么正在变化？**

重点从静态问题转向时间变化：

* 重复
* 停滞
* 升级
* 历史建议效果

---

## REFLECT

> **这些变化背后有什么更值得长期关注？**

寻找：

* Workflow / Skill
* Project
* Work
* 潜在作品
* 重复矛盾
* 研究主题
* 尚未命名的问题

---

# 7. `.advisor/` 更名为 `.fuli/`

长期状态正式与品牌统一：

```text
.fuli/
├── state.md
├── inbox.md
├── history.md
└── snapshots/
```

这是一个很小但重要的变化。

FULI 的长期价值越来越依赖：

> **比较，而不是单次扫描。**

核心判断：

> **Advisor 的智能增长不是来自扫描次数，而来自比较。**

---

# 8. 加入 Attention Budget

持续观察不能演变成持续骚扰。

v0.2 引入三层注意力机制：

## Silent

知道，但不说。

## Inbox

值得保留，在自然工作节点出现。

## Interrupt

只有严重风险或极高价值事件。

核心原则：

> **持续观察，克制打扰，只在值得改变的时候出现。**

---

# 9. 加入 Archive Signal

本轮产品设计本身暴露了另一个重要问题：

> 高质量 AI 对话如果只留在聊天记录里，很容易失去后续价值。

因此 v0.2 开始内置：

## Session Close Protocol

当一次 AI 共创产生：

* 产品版本变化
* MVP 决策
* 新核心原则
* 重要方向调整
* 新研究母题

FULI 可以建议：

> **“本轮已经形成重要变化，建议归档本轮。”**

标准归档包括：

```text
Conversation Archive
Product Spec / Current Truth
Insight Memo
```

---

# 10. 富丽的人格开始明确

FULI 不应该被设计成传统 AI 秘书。

她更接近：

* 编辑
* 研究伙伴
* 长期顾问

人格原则：

* 观察力强
* 克制
* 敢于反对
* 长期主义
* 尊重创作者自主性
* 有方法论，但知道方法论不是事实

最重要的一句：

> **富丽不急着帮你把事情做完，她更关心这件事最后会留下什么。**

---

# 本版本没有做什么

v0.2 刻意没有增加：

* 独立桌面 App
* Web SaaS
* 新聊天 UI
* 企业微信 Connector
* 微信公众号 Connector
* 复杂知识图谱
* Agent 市场
* 大型 Workbench
* 新 Agent Runtime

原因非常明确：

> 当前最大的产品风险不是工程能力，而是 Advisor Intelligence。

---

# 当前最重要的验证目标

v0.1 已经验证：

> **能运行。**

v0.2 需要验证：

> **是否值得长期使用。**

未来真实测试只重点记录三类结果。

## Valuable

> “对，而且我之前没有意识到。”

## Wrong / Over-advice

* 套话
* 过度结构化
* 错误升级
* 无意义 Skill 化
* 把高价值认知过程自动化掉

## Missed

用户自己能够明显发现，但 FULI 没有发现的重要问题。

---

# 下一版本

v0.3 暂不以“增加功能”为主要目标。

优先基于真实使用积累：

> **10–20 个 Advisor 判断样本。**

然后反向迭代：

* 判断规则
* Workflow 阈值
* 复利信号
* REFLECT 质量
* Attention Policy
* Creator Doctrine

理想的 v0.3 应该主要来自：

> **真实工作纠正产品，而不是继续靠产品脑暴扩张产品。**

---

# v0.2 一句话总结

> **FULI v0.2 从一个帮助超级 Agent 检查工作空间的 Skill，升级为一套让超级 Agent 以“创作者长期复利”为评价函数理解工作世界的判断系统。**
