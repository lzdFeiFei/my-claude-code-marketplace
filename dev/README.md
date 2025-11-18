# Dev Docs Pattern - 使用指南

一种在 Claude Code 会话和上下文重置之间维护项目上下文的方法论。

---

## 问题背景

**上下文重置会丢失一切**：
- 实现决策
- 关键文件及其用途
- 任务进度
- 技术约束
- 为什么选择某些方法

**重置后，Claude 必须重新发现所有内容。**

---

## 解决方案：持久化开发文档

一个三文件结构，捕获恢复工作所需的所有信息：

```
dev/active/[task-name]/
├── [task-name]-plan.md      # 战略计划
├── [task-name]-context.md   # 关键决策和文件
└── [task-name]-tasks.md     # 清单格式
```

**这些文件在上下文重置后保留** - Claude 读取它们即可立即恢复状态。

---

## 三文件结构

### 1. [task-name]-plan.md

**目的**：实施的战略计划

**包含**：
- 执行摘要
- 当前状态分析
- 未来目标状态
- 实施阶段
- 带验收标准的详细任务
- 风险评估
- 成功指标
- 时间估算

**何时创建**：复杂任务开始时

**何时更新**：范围变更或发现新阶段时

**示例**：
```markdown
# 功能名称 - 实施计划

## 执行摘要
我们正在构建什么以及为什么

## 当前状态
我们现在处于什么位置

## 实施阶段

### 阶段 1：基础设施（2小时）
- 任务 1.1：设置数据库架构
  - 验收：架构编译通过，关系正确
- 任务 1.2：创建服务结构
  - 验收：所有目录已创建

### 阶段 2：核心功能（3小时）
...
```

---

### 2. [task-name]-context.md

**目的**：恢复工作的关键信息

**包含**：
- SESSION PROGRESS 部分（频繁更新！）
- 已完成 vs 进行中的内容
- 关键文件及其用途
- 做出的重要决策
- 发现的技术约束
- 相关文件链接
- 快速恢复说明

**何时创建**：任务开始时

**何时更新**：**频繁** - 在重大决策、完成或发现后

**示例**：
```markdown
# 功能名称 - 上下文

## SESSION PROGRESS (2025-11-18)

### ✅ 已完成
- 数据库架构已创建（User、Post、Comment 模型）
- PostController 使用 BaseController 模式实现
- Sentry 集成正常工作

### 🟡 进行中
- 创建包含业务逻辑的 PostService
- 文件：src/services/postService.ts

### ⚠️ 阻塞点
- 需要决定缓存策略

## 关键文件

**src/controllers/PostController.ts**
- 继承 BaseController
- 处理 posts 的 HTTP 请求
- 委托给 PostService

**src/services/postService.ts**（进行中）
- posts 操作的业务逻辑
- 下一步：添加缓存

## 快速恢复
继续工作：
1. 阅读此文件
2. 继续实现 PostService.createPost()
3. 查看 tasks 文件了解剩余工作
```

**关键**：每次完成重要工作时更新 SESSION PROGRESS 部分！

---

### 3. [task-name]-tasks.md

**目的**：追踪进度的清单

**包含**：
- 按逻辑部分分解的阶段
- 复选框格式的任务
- 状态指示器（✅/🟡/⏳）
- 验收标准
- 快速恢复部分

**何时创建**：任务开始时

**何时更新**：完成每个任务或发现新任务后

**示例**：
```markdown
# 功能名称 - 任务清单

## 阶段 1：设置 ✅ 完成
- [x] 创建数据库架构
- [x] 设置控制器
- [x] 配置 Sentry

## 阶段 2：实现 🟡 进行中
- [x] 创建 PostController
- [ ] 创建 PostService（进行中）
- [ ] 创建 PostRepository
- [ ] 使用 Zod 添加验证

## 阶段 3：测试 ⏳ 未开始
- [ ] 服务单元测试
- [ ] 集成测试
- [ ] 手动 API 测试
```

---

## 何时使用 Dev Docs

**使用场景**：
- ✅ 复杂的多天任务
- ✅ 有许多相关部分的功能
- ✅ 可能跨多个会话的任务
- ✅ 需要仔细规划的工作
- ✅ 重构大型系统

**跳过场景**：
- ❌ 简单的 bug 修复
- ❌ 单文件更改
- ❌ 快速更新
- ❌ 琐碎的修改

**经验法则**：如果超过 2 小时或跨多个会话，使用 dev docs。

---

## Dev Docs 工作流程

### 开始新任务

1. **使用 /dev-docs 斜杠命令**：
   ```
   /dev-docs 重构认证系统
   ```

2. **Claude 创建三个文件**：
   - 分析需求
   - 检查代码库
   - 创建综合计划
   - 生成 context 和 tasks 文件

3. **审查和调整**：
   - 检查计划是否合理
   - 添加任何遗漏的考虑
   - 调整时间估算

### 实施期间

1. **参考 plan** 了解整体策略
2. **频繁更新 context.md**：
   - 标记已完成的工作
   - 记录做出的决策
   - 添加阻塞点
3. **勾选 tasks.md 中的任务**（完成时）

### 上下文重置后

1. **Claude 读取所有三个文件**
2. **在几秒内理解完整状态**
3. **从离开的地方精确恢复**

无需解释你在做什么 - 一切都已记录！

---

## 斜杠命令集成

### /dev-docs
**创建**：为任务创建新的 dev docs

**用法**：
```
/dev-docs 实现实时通知
```

**生成**：
- `dev/active/implement-real-time-notifications/`
  - implement-real-time-notifications-plan.md
  - implement-real-time-notifications-context.md
  - implement-real-time-notifications-tasks.md

### /dev-docs-update
**更新**：上下文重置前更新现有 dev docs

**用法**：
```bash
/dev-docs-update  # 手动触发
```

**💡 自动触发（推荐）**：
本项目已配置 **PreCompact Hook**，在接近 token 限制（~180K/200K）时**自动触发**此命令，无需手动操作！

**工作原理**：
```
Token 使用 → 接近限制 → PreCompact Hook 触发
→ /dev-docs-update 自动执行 → 进度保存 → 上下文压缩
```

**更新内容**：
- 标记已完成的任务
- 添加发现的新任务
- 更新 context 的会话进度
- 捕获当前状态

**何时手动使用**：
- 长时间中断前主动保存
- 切换到其他任务前
- 想要确保进度已记录

**配置详情**：查看 [.claude/HOOKS.md](../.claude/HOOKS.md)

---

## 文件组织

```
dev/
├── README.md              # 本文件
├── active/                # 当前工作
│   ├── task-1/
│   │   ├── task-1-plan.md
│   │   ├── task-1-context.md
│   │   └── task-1-tasks.md
│   └── task-2/
│       └── ...
└── archive/               # 已完成工作（可选）
    └── old-task/
        └── ...
```

**active/**：进行中的工作
**archive/**：已完成的任务（供参考）

---

## 最佳实践

### 频繁更新 Context

**不好**：仅在会话结束时更新
**好**：每个重大里程碑后更新

**SESSION PROGRESS 部分应始终反映现实**：
```markdown
## SESSION PROGRESS (YYYY-MM-DD)

### ✅ 已完成（列出所有已完成的内容）
### 🟡 进行中（你现在正在做的事情）
### ⚠️ 阻塞点（阻止进度的内容）
```

### 使任务可执行

**不好**："修复认证"
**好**："在 AuthMiddleware.ts 中实现 JWT 令牌验证（验收：令牌已验证，错误发送到 Sentry）"

**包含**：
- 具体文件名
- 明确的验收标准
- 对其他任务的依赖

### 保持计划最新

如果范围变更：
- 更新计划
- 添加新阶段
- 调整时间估算
- 记录为什么范围变更

---

## 对 Claude Code 的指导

**当用户要求创建 dev docs 时**：

1. **使用 /dev-docs 斜杠命令**（如果可用）
2. **或手动创建**：
   - 询问任务范围
   - 分析相关代码库文件
   - 创建综合计划
   - 生成 context 和 tasks

3. **构建计划时包含**：
   - 清晰的阶段
   - 可执行的任务
   - 验收标准
   - 风险评估

4. **使 context 文件可恢复**：
   - SESSION PROGRESS 在顶部
   - 快速恢复说明
   - 带解释的关键文件列表

**从 dev docs 恢复时**：

1. **读取所有三个文件**（plan、context、tasks）
2. **从 context.md 开始** - 有当前状态
3. **检查 tasks.md** - 查看已完成和下一步
4. **参考 plan.md** - 理解整体策略

**频繁更新**：
- 立即标记任务完成
- 重要工作后更新 SESSION PROGRESS
- 发现时添加新任务

---

## 手动创建 Dev Docs

如果你没有 /dev-docs 命令：

**1. 创建目录**：
```bash
mkdir -p dev/active/your-task-name
```

**2. 创建 plan.md**：
- 执行摘要
- 实施阶段
- 详细任务
- 时间估算

**3. 创建 context.md**：
- SESSION PROGRESS 部分
- 关键文件
- 重要决策
- 快速恢复说明

**4. 创建 tasks.md**：
- 带复选框的阶段
- [ ] 任务格式
- 验收标准

---

## 收益

**使用 dev docs 前**：
- 上下文重置 = 从头开始
- 忘记为什么做出决策
- 失去进度追踪
- 重复工作

**使用 dev docs 后**：
- 上下文重置 = 读 3 个文件，立即恢复
- 决策已记录
- 进度已追踪
- 无重复工作

**节省时间**：每次上下文重置节省数小时

---

## 与本项目的配合

### 三层架构

| 层级 | 文件 | 作用范围 | 生命周期 |
|------|------|----------|----------|
| **L1 项目级** | CLAUDE.md | 所有任务 | 永久 |
| **L2 任务级** | dev/active/[task]/ | 单个复杂任务 | 任务期间 |
| **L3 会话级** | TodoWrite 工具 | 当前会话 | 单次会话 |

### 配合方式

1. **CLAUDE.md** → 定义"游戏规则"
   - 技术栈（React、TypeScript、Tailwind）
   - 架构原则（3层架构、分层）
   - 代码规范（TypeScript 严格模式、函数式组件）
   - 禁止行为（不使用 any、不直接修改 state）

2. **dev/active/[task]/** → 记录"当前任务"
   - 战略计划（如何实现这个功能）
   - 实施进度（已完成什么、进行中什么）
   - 关键决策（为什么选择这种方案）

3. **TodoWrite 工具** → 追踪"实时进度"
   - 当前会话的任务清单
   - 实时状态更新

---

## 下一步

1. **在下一个复杂任务上尝试这个模式**
2. **使用 /dev-docs 斜杠命令**（如果可用）
3. **频繁更新** - 特别是 context.md
4. **查看实际应用** - 参考原始 showcase 项目中的 dev/active/public-infrastructure-repo/

**问题？** 查看 [CLAUDE.md](../CLAUDE.md) 了解项目级配置
