# CHANGELOG

## v0.4 — 2026-08-11

### 版本主题

**体验收敛**

### 产品变化

- 用户入口简化为两个："富丽扫描"和"富丽升级"，去掉 SCAN/REVIEW/REFLECT 概念负担
- 统一扫描流程：宿主 Agent 基础检查 + 富丽创作判断 → 统一 Suggestions
- 建议标注来源：`🤖 来自 [宿主名称]` / `🌿 来自富丽`
- 新增"富丽升级"：一键检查并安全更新，只动系统文件不动 `.fuli/`
- 安装心智转变：富丽安装到 Agent 全局，而非项目本地
- README 重写为：安装 → 扫描 → 升级 → 卸载 四步
- 明确两层空间：富丽系统文件 / 用户 `.fuli/` 资产，升级只碰前者

### 工程变化

- `version` 从 `metadata.version` 回归标准 `version: "0.4.0"`
- 新增 `VERSION` 文件，集中管理版本号
- 新增 `scripts/update_fuli.py`：安全自更新（仅 Git 安装、仅 fast-forward）
- `富丽扫描` 内部自动选择 SCAN/REVIEW/REFLECT，用户无需学习
- 建立标准发布流程：开发 → 升级 VERSION → CHANGELOG → 评测 → tag → Release

---

## v0.3 — 2026-08-11

### 版本主题

**证明判断增益**

### 产品变化

- 中文优先：首次使用“富丽（Fuli）”，后续统一“富丽”。
- 核心目标收敛为：判断增益、Aha Moment、最小行动、渐进式个性化。
- 正式加入“默认复利创作规范”，支持浏览、修改、开源共创。
- 个人偏好文件默认初始化，用户无需手工新建。
- 经过用户确认的个人创作习惯优先于默认规范。
- 个性化采用“观察 → 提出 → 用户确认 → 采用”。
- 高成本创作建议改为高门槛行为。
- 默认行动阶梯：`Ignore → Watch → Capture → Small Action → Invest`。
- Compressed Review 不依赖 Git，Git 只是增强项。
- 正式建立裸 Agent vs Agent + 富丽的判断增益评测。
- Playground 收敛为一个最小 demo-case，不建设正式产品模块。
- 真实工作经验默认属于用户，不建设公开真实案例库。

### 工程变化

- 根目录为唯一发布源，`.claude/skills/fuli/` 为运行时加载副本。
- `SKILL.md` 收敛为运行内核。
- 默认规范下沉到 `references/compounding-creation-guide.md`。
- frontmatter 版本进入 `metadata.version`。
- `.advisor/` 全面废弃，统一 `.fuli/`。
- snapshot 脚本默认不自动创建 `.fuli/`。
- `preferences.md` 与 `state.md` 使用 `assets/` 模板初始化。
