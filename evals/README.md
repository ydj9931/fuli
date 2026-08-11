# 富丽 v0.3 评测

v0.3 最重要的实验：

> **同一个超级 Agent，加载富丽以后，判断是否明显变好？**

保持相同：模型、Agent、工作空间、用户问题、可访问证据。

仅改变：

```text
A：裸 Agent
B：Agent + 富丽
```

## 建议测试问题

> 帮我评审一下这个工作空间。告诉我现在真正值得改善、保留或继续关注的东西。不要修改任何文件。

## 评价维度

1. Problem Detection Lift
2. Pattern Detection Lift
3. Object Formation Lift
4. Aha Lift
5. Restraint / Burden Reduction
6. Explainability

最终问题：

> **哪一个回答让用户更清楚“什么值得留下，而不是什么都值得做”？**

`demo-case/` 仅用于快速理解评测方法，是合成测试资产，不是真实用户案例库。
