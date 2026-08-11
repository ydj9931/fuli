# FULI v0.2 Release Notes

## 为什么升级到 v0.2

v0.1 已验证：

> **Skill + 内置脚本 + 现有超级 Agent**

可以正常运行。

随后讨论进一步明确：FULI 的核心不是“检查本地文件”，因为超级 Agent 本身已经具备这些能力。

因此 v0.2 是一次**产品定位与判断框架升级**，而不是功能堆叠。

## 主要变化

1. **品牌升级**
   - Creator Advisor → **富丽 FULI**
   - 核心承诺：**发现工作中值得复利的东西**

2. **重新定义与超级 Agent 的边界**
   - 不提供重复基础能力
   - 提供判断协议与长期评价函数

3. **Native-first**
   - 宿主 Agent 原生检查能力优先
   - 内置脚本退居 deterministic helper / fallback

4. **复利价值成为核心评价函数**
   - Task → Workflow → Skill → Capability → Work → Feedback → Better Questions

5. **强化 Longitudinal Memory**
   - `.advisor/` → `.fuli/`
   - REVIEW 明确聚焦时间变化与历史结果

6. **强化注意力治理**
   - Silent / Inbox / Interrupt
   - 持续观察，克制打扰

7. **加入 Archive Signal**
   - 重要 AI 共创产生版本变化时可建议“归档本轮”
   - 附 Session Close Protocol 模板

8. **人格明确**
   - 富丽更像编辑 + 研究伙伴 + 长期顾问
   - 不是秘书

## 本版本刻意不增加

- 独立 App
- 新聊天 UI
- 企业微信连接器
- 发布渠道连接器
- 复杂 Workbench
- 新 Agent Runtime

## v0.2 继续验证的唯一主问题

> **富丽能否持续形成值得信赖的工作与创作判断？**
