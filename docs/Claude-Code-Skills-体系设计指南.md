# Claude Code Skills 体系设计指南

**核心结论：** Skills 是为 AI 编程助手提供专业知识的模块化系统，通过合理分工和协作，让 AI 在特定领域表现更专业。

## 为什么需要 Skills

### 传统方式的问题

AI 编程助手面临三大挑战：

1. **知识泛化** - 对所有问题一视同仁，缺乏专业深度
2. **上下文限制** - 无法同时加载所有专业知识
3. **规范不一致** - 不同任务的代码质量标准不统一

### Skills 解决方案

**本质：** Skills = 专业知识 + 工作流程 + 质量标准

```
传统方式: AI + 用户提示 → 通用回答
Skills 方式: AI + 专业 Skill + 用户提示 → 专业回答
```

**优势对比：**

| 维度 | 传统方式 | Skills 方式 |
|------|---------|------------|
| 专业性 | 泛泛而谈 | 领域专家级 |
| 一致性 | 每次不同 | 标准化输出 |
| 可控性 | 难以预测 | 工具权限控制 |
| 可维护性 | 重复教育 | 一次配置 |

## Skills vs 传统文档

### 关键区别

**传统文档（如 README）：**
- 给人类看的静态参考
- 通常只读一次
- 缺乏执行流程

**Skills：**
- 给 AI 执行的工作手册
- 每次任务都激活
- 包含详细工作流程和决策树

### 设计思维转变

```
文档思维: "这个技术是什么"
Skill 思维: "遇到 X 场景，做 Y 步骤，用 Z 工具"
```

**示例对比：**

```markdown
# 文档写法
## React 组件最佳实践
组件应该遵循单一职责原则，保持代码简洁...

# Skill 写法
## 组件设计流程
1. 分析需求 → 判断复杂度
   - 简单组件（<100行）→ 直接创建
   - 复杂组件（>100行）→ 拆分为子组件

2. 选择模板 → 使用 assets/BasicComponent.tsx

3. 质量检查 → 文件行数 ≤ 200 行，否则必须拆分
```

## 何时创建新 Skill

### 判定标准

**需要创建 Skill 的情况：**

1. **专业领域** - 需要深度知识
   - 示例：代码审查、无障碍合规、性能优化
   - 原因：需要系统化的检查清单和标准

2. **重复性任务** - 频繁执行
   - 示例：创建 React 组件、生成 API 接口
   - 原因：标准化流程提高效率和质量

3. **复杂工作流** - 多步骤协作
   - 示例：完整功能开发（UI + 业务逻辑 + API）
   - 原因：需要明确的执行顺序和协调逻辑

4. **质量门槛** - 有明确标准
   - 示例：安全审查、代码规范检查
   - 原因：避免遗漏关键检查项

**不需要创建 Skill 的情况：**

- ❌ 一次性任务
- ❌ 过于简单（3 步以内完成）
- ❌ 没有明确标准或流程
- ❌ 与现有 Skill 高度重叠

### 决策树

```
任务分析
├─ 专业性高？
│  ├─ 是 → 考虑创建
│  └─ 否 → 继续判断
├─ 重复频率高？
│  ├─ 是 → 考虑创建
│  └─ 否 → 继续判断
├─ 有标准流程？
│  ├─ 是 → 创建 Skill
│  └─ 否 → 写入 CLAUDE.md 即可
```

## Skill 设计原则

### 1. 单一职责

**原则：** 每个 Skill 只做一件事，做好一件事。

**示例：**

```
✅ 好的设计：
- react-component-generator: 只生成组件
- code-review: 只审查代码
- feature-builder: 构建完整功能

❌ 坏的设计：
- frontend-helper: 既生成组件又审查又部署（职责不清）
```

**判断方法：**
- Skill 名称能用一个动词描述吗？
- Skill 的 description 超过 50 字了吗？（可能职责过多）

### 2. 明确边界

**原则：** 清楚说明 Skill 做什么、不做什么。

**要素：**

```yaml
name: ui-analyzer
description: 分析 UI 设计截图并生成 React 代码

# 明确职责
做什么:
  - 分析布局和样式
  - 提取设计 token
  - 生成 Tailwind 代码

不做什么:
  - ❌ 不实现业务逻辑
  - ❌ 不添加 API 调用
  - ❌ 不创建状态管理
```

### 3. 工具权限最小化

**原则：** 只授权必要的工具。

**工具分类：**

```typescript
// 只读 Skills
allowed-tools: Read, Grep, Glob
// 示例: code-review, request-analyzer

// 写入 Skills
allowed-tools: Read, Write, Edit, Glob, Grep
// 示例: react-component-generator, feature-builder

// 交互 Skills
allowed-tools: AskUserQuestion
// 示例: prompt-optimizer

// 网络 Skills
allowed-tools: WebSearch, WebFetch
// 示例: tech-article-writer, product-manager
```

**安全考虑：**

| 工具 | 风险级别 | 使用场景 |
|------|---------|---------|
| Read/Grep/Glob | 低 | 所有 Skills |
| Write/Edit | 中 | 需要生成/修改代码 |
| Bash | 高 | 需要执行命令（慎用） |
| WebSearch | 低 | 需要最新信息 |

### 4. 分层设计

**三层架构：**

```
Skill 结构
├── SKILL.md              # 核心工作流程
├── references/           # 详细规范和标准
│   ├── checklist.md      # 检查清单
│   ├── best-practices.md # 最佳实践
│   └── examples.md       # 示例代码
└── assets/               # 模板和资源
    ├── template1.tsx
    └── template2.tsx
```

**职责划分：**

- **SKILL.md**: 执行流程（如何做）
- **references/**: 知识库（为什么这样做）
- **assets/**: 可复用资源（直接使用的模板）

### 5. 可组合性

**原则：** Skills 之间可以协作，但不强依赖。

**协作模式：**

```
request-analyzer (协调者)
├─→ prompt-optimizer (需求澄清)
├─→ feature-builder (功能开发)
│   └─→ react-component-generator (组件生成)
└─→ code-review (质量检查)
```

**设计要点：**

- ✅ Skill A 可以推荐激活 Skill B
- ✅ 但 Skill A 单独使用也能完成基本任务
- ❌ 避免循环依赖

## CLAUDE.md 的角色定位

### 核心原则

**CLAUDE.md = 快速参考卡片 + Skills 导航**

- 长度：≤ 300 行
- 作用：高层指导，详细规范交给 Skills
- 更新频率：低（项目级配置）

### 内容分层

**CLAUDE.md 应该包含：**

```markdown
✅ 保留在 CLAUDE.md:
- 核心原则（回复格式、工作态度）
- 技术栈（一句话说明）
- Skills 导航表（触发场景）
- 架构规则（3 层架构速查）
- 禁止行为（红线清单）
- 最终检查清单

❌ 移到 Skills:
- 详细代码规范 → feature-builder/references/
- 安全检查清单 → code-review/references/
- 组件设计流程 → react-component-generator
- 性能优化手册 → code-review skill
```

### 引用关系

**设计模式：**

```markdown
# CLAUDE.md 中
## 代码规范速查
- TypeScript: 禁用 any
- React: 使用 Hooks
- 详细规范 → `feature-builder/references/coding-standards.md`

# feature-builder/references/coding-standards.md 中
## TypeScript 规范
### 类型定义
[200+ 行详细说明和代码示例]
```

**优势：**
- CLAUDE.md 保持简洁
- 需要时查看详细规范
- 单一来源真理（避免重复）

## 前端项目 Skills 设计实例

### 完整体系设计

**需求分析：** React/TypeScript 前端项目需要什么？

```
任务类型分析
├── 组件创建（高频、标准化） → react-component-generator
├── 功能开发（复杂、多层次） → feature-builder
├── UI 实现（设计稿转代码） → ui-analyzer
├── 代码审查（质量、安全） → code-review
├── 需求澄清（模糊需求） → prompt-optimizer
└── 任务协调（智能分发） → request-analyzer
```

### Skill 职责划分

#### 1. react-component-generator

**定位：** 标准组件快速生成

```yaml
触发场景: "创建登录表单"、"生成产品卡片"
职责:
  - 提供 7 种组件模板
  - 应用 TypeScript + Tailwind 规范
  - 生成符合项目规范的代码
不负责:
  - ❌ 业务逻辑（交给 feature-builder）
  - ❌ API 集成（交给 feature-builder）
allowed-tools: Read, Write, Edit, Glob, Grep
```

**设计要点：**
- 模板驱动（assets/ 目录存放模板）
- 快速生成（减少重复工作）
- 规范约束（自动应用最佳实践）

#### 2. feature-builder

**定位：** 完整功能开发

```yaml
触发场景: "实现用户认证"、"构建购物车"
职责:
  - 3 层架构（UI + 业务逻辑 + API）
  - 集成 Zustand、React Query、Zod
  - 创建完整 feature 目录结构
协作关系:
  - 调用 react-component-generator 生成 UI 组件
  - 调用 code-review 进行质量检查
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
```

**设计要点：**
- 分层架构强制执行
- 交互式需求收集（AskUserQuestion）
- 完整性保证（UI + 逻辑 + 数据）

#### 3. code-review

**定位：** 前端代码质量检查

```yaml
触发场景: "审查这个组件"、"检查性能问题"
审查维度:
  - 前端安全（XSS、CSRF）
  - React 性能（re-render、memoization）
  - 无障碍（WCAG 2.1 AA）
  - TypeScript 类型安全
references:
  - frontend-security.md
  - accessibility-guide.md
  - react-patterns.md
allowed-tools: Read, Grep, Glob, Bash
```

**设计要点：**
- 只读权限（审查不修改）
- 分级反馈（Critical、High、Medium、Low）
- 可执行建议（提供修复代码）

#### 4. prompt-optimizer

**定位：** 需求澄清

```yaml
触发场景: 用户需求模糊时
工作模式:
  - 交互式问卷（AskUserQuestion）
  - 渐进式收集信息
  - 结构化输出
示例:
  用户: "做个东西"
  Skill:
    1. 识别需求不清晰
    2. 提供多选问题
    3. 收集完整需求
    4. 推荐合适的 Skill
allowed-tools: AskUserQuestion
```

**设计要点：**
- 最小权限（只需交互）
- 问题库设计（覆盖常见缺失信息）
- 输出格式化（便于后续 Skills 使用）

#### 5. request-analyzer

**定位：** 智能协调器

```yaml
触发时机: 每次用户请求（自动）
职责:
  - 分析任务类型
  - 评估提示质量（0-100%）
  - 推荐激活哪些 Skills
决策逻辑:
  需求清晰度 < 60% → 激活 prompt-optimizer
  提到 "设计稿" → 激活 ui-analyzer
  提到 "审查" → 激活 code-review
  涉及完整功能 → 激活 feature-builder
allowed-tools: Read, Glob, Grep, Skill
```

**设计要点：**
- 全局视角（了解所有 Skills）
- 决策矩阵（明确的激活规则）
- 可激活其他 Skills（Skill 工具权限）

### Skills 协作流程

**场景：用户请求 "实现一个用户登录功能"**

```
request-analyzer (分析)
├─ 识别: 完整功能需求
├─ 评估: 需求清晰度 80%（可直接执行）
└─ 推荐: 激活 feature-builder

feature-builder (执行)
├─ Step 1: 使用 AskUserQuestion 收集详细需求
│   - 认证方式？(邮箱/手机)
│   - 需要记住登录状态吗？
│   - 是否需要社交登录？
├─ Step 2: 创建计划文档 ./plan/plan-login.md
│   - [ ] 创建 LoginForm 组件
│   - [ ] 实现 useAuth hook
│   - [ ] 集成 API（authApi.ts）
│   - [ ] 配置 Zustand store
├─ Step 3: 调用 react-component-generator
│   - 生成 LoginForm.tsx（基于 FormComponent 模板）
├─ Step 4: 实现业务逻辑
│   - hooks/useAuth.ts
│   - stores/authStore.ts
│   - api/authApi.ts
├─ Step 5: 调用 code-review
│   - 检查安全性（密码处理）
│   - 检查无障碍（表单标签）
│   - 检查性能（不必要的 re-render）
└─ Step 6: 生成实现总结

code-review (质量检查)
├─ 安全审查
│   - ✅ 密码字段使用 type="password"
│   - ⚠️ 建议: token 不要存 localStorage
├─ 性能审查
│   - ✅ 表单验证使用 useMemo
│   - 💡 建议: 使用 React.memo 优化 LoginForm
└─ 无障碍审查
    - ✅ 表单 label 正确关联
    - ✅ 错误提示使用 role="alert"
```

## Dev Docs Pattern - 上下文保护机制

### 核心问题

**上下文重置 = 进度归零？**

AI 编程助手面临的致命问题：Token 限制导致上下文压缩，实现决策、任务进度、关键文件全部丢失。

**数据：** 典型场景下，上下文重置后重新理解代码需要 30-60 分钟。

### 解决方案：三文件持久化

**本质：** 将关键信息固化到文件，上下文重置后 5 秒恢复。

```
dev/active/[task-name]/
├── [task-name]-plan.md      # 战略计划
├── [task-name]-context.md   # 关键决策和进度
└── [task-name]-tasks.md     # 任务清单
```

#### 1. plan.md - 战略计划

**包含内容：**
- 执行摘要（1 段话说明目标）
- 当前状态 vs 目标状态
- 实施阶段（Phase 1/2/3）
- 详细任务 + 验收标准
- 风险评估 + 缓解策略
- 时间估算

**何时创建：** 复杂任务开始时（>2 小时或跨会话）

**更新频率：** 低（范围变更时）

#### 2. context.md - 上下文文件（最关键！）

**核心结构：**

```markdown
## SESSION PROGRESS (2025-11-18)

### ✅ 已完成
- 数据库架构创建（User、Post、Comment 模型）
- PostController 使用 BaseController 模式实现

### 🟡 进行中
- 创建 PostService（文件：src/services/postService.ts）
- 当前进度：已完成 CRUD，待添加缓存

### ⚠️ 阻塞点
- 缓存策略待决定（Redis vs 内存缓存）

## 关键文件
**src/controllers/PostController.ts** - 继承 BaseController
**src/services/postService.ts** - 业务逻辑（进行中）

## 快速恢复
继续实现 PostService.createPost()，参考 tasks.md 剩余工作
```

**更新频率：** **高** - 每个重要里程碑后必须更新

**为什么最关键：** 决定能否快速恢复工作状态

#### 3. tasks.md - 任务清单

**格式：** Checkbox + 状态指示器

```markdown
## 阶段 1：设置 ✅ 完成
- [x] 创建数据库架构
- [x] 配置 Sentry

## 阶段 2：实现 🟡 进行中
- [x] 创建 PostController
- [ ] 创建 PostService（进行中）
- [ ] 使用 Zod 添加验证

## 阶段 3：测试 ⏳ 未开始
- [ ] 单元测试
- [ ] 集成测试
```

**更新频率：** 中（完成任务时勾选）

### 自定义命令

#### /dev-docs - 创建任务结构

**用法：**
```bash
/dev-docs 实现用户认证系统
```

**自动执行：**
1. 分析需求 + 检查代码库
2. 创建 `dev/active/implement-user-auth/`
3. 生成 plan.md（700+ 行战略计划）
4. 生成 context.md（SESSION PROGRESS + 关键文件）
5. 生成 tasks.md（Checkbox 清单）

**适用场景：**
- ✅ 代码 > 200 行
- ✅ 文件 ≥ 5 个
- ✅ 跨多个会话
- ✅ 需要详细规划

#### /dev-docs-update - 保存进度

**用法：**
```bash
/dev-docs-update  # 手动保存
```

**自动执行：**
1. 扫描 `dev/active/` 所有任务
2. 更新 context.md（当前状态 + 决策）
3. 更新 tasks.md（标记完成、添加新任务）
4. 添加交接笔记（未完成工作的确切状态）

**何时使用：**
- Token 接近限制（~180K/200K）
- 长时间中断前
- 切换任务前

### PreCompact Hook - 自动保护

**配置文件：** `.claude/hooks.json`

```json
{
  "hooks": {
    "preCompact": {
      "enabled": true,
      "command": "/dev-docs-update",
      "description": "上下文压缩前自动保存进度"
    }
  }
}
```

**工作原理：**

```
Token 使用累积
  ↓ 达到 ~180K/200K
PreCompact Hook 触发
  ↓ 自动执行 /dev-docs-update
进度保存完成
  ↓
上下文压缩
  ↓ 5 秒读取文件
立即恢复工作
```

**关键特性：**
- ✅ **零干预** - 完全自动触发
- ✅ **零丢失** - 每次压缩前保存
- ✅ **零延迟** - 5 秒恢复状态

### 三层任务管理架构

**完整体系：**

| 层级 | 文件/工具 | 作用范围 | 生命周期 | 更新频率 |
|------|----------|----------|----------|----------|
| **L1 项目级** | CLAUDE.md | 所有任务 | 永久 | 低 |
| **L2 任务级** | dev/active/[task]/ | 单个复杂任务 | 任务期间 | 中-高 |
| **L3 会话级** | TodoWrite 工具 | 当前会话 | 单次会话 | 实时 |

**配合方式：**

```
CLAUDE.md（项目规范）
  ↓ 定义"游戏规则"（技术栈、架构、禁止行为）

dev/active/[task]/（任务管理）
  ↓ 记录"当前任务"（计划、进度、决策）
  ↓ PreCompact Hook 自动保护

TodoWrite 工具（实时追踪）
  ↓ 追踪"当前会话"（任务清单、状态）
```

### 实战效果对比

#### 场景：实现用户认证系统（4 小时任务）

**无 Dev Docs：**
```
会话 1（2小时）→ 实现 70% → [上下文重置]
会话 2：
  - 重新阅读代码（30 分钟）
  - 回忆设计决策（15 分钟）
  - 找到中断点（10 分钟）
  - 继续实现（剩余 30%）
总耗时：3.5 小时
```

**有 Dev Docs + Hook：**
```
会话 1（2小时）→ 实现 70% → Hook 自动保存 → [上下文重置]
会话 2：
  - 读取 context.md（5 秒）
  - 从 SESSION PROGRESS 确定进度
  - 继续实现（剩余 30%）
总耗时：2 小时
```

**节省时间：** 1.5 小时（43% 效率提升）

### 最佳实践

#### 1. 频繁更新 context.md

**不好：** 只在会话结束时更新
**好：** 每个重要里程碑后更新

**关键原则：**
- 完成核心功能 → 立即更新
- 做出重要决策 → 立即记录
- 遇到阻塞点 → 立即标注

#### 2. 任务描述可执行

**不好：** "修复认证"
**好：** "在 AuthMiddleware.ts 中实现 JWT 验证（验收：token 验证通过，错误发送 Sentry）"

**必须包含：**
- 具体文件名
- 明确验收标准
- 依赖关系

#### 3. 保持计划最新

**范围变更时：**
- 更新 plan.md 添加新阶段
- 在 context.md 记录变更原因
- 调整 tasks.md 任务优先级

### 与 Skills 的协作

**协作模式：**

```
复杂任务请求
  ↓
request-analyzer 分析
  ↓ 识别为多会话任务
  ↓
/dev-docs 创建任务结构
  ↓
feature-builder 逐步实现
  ↓ 每个里程碑更新 context.md
  ↓
PreCompact Hook 自动保存
  ↓ [上下文重置]
  ↓
读取 dev/active/[task]/
  ↓ 5 秒恢复
  ↓
继续实现 + code-review 检查
```

**关键点：**
- Dev Docs 提供持久化存储
- Skills 提供执行能力
- Hook 提供自动保护
- 三者配合实现零丢失工作流

### 何时使用 Dev Docs

**必须使用：**
- ✅ 任务超过 2 小时
- ✅ 跨多个会话
- ✅ 需要详细规划
- ✅ 多人协作任务

**可以跳过：**
- ❌ 简单 bug 修复（< 30 分钟）
- ❌ 单文件修改
- ❌ 一次性探索任务

**判断标准：** 如果担心中断后忘记进度 → 使用 Dev Docs

### 实施建议

**第 1 步：配置基础设施**
```bash
# 创建目录结构
mkdir -p dev/active dev/archive

# 配置 Hook
echo '{
  "hooks": {
    "preCompact": {
      "enabled": true,
      "command": "/dev-docs-update"
    }
  }
}' > .claude/hooks.json
```

**第 2 步：创建第一个任务**
```bash
/dev-docs 实现第一个功能
```

**第 3 步：养成习惯**
- 重要里程碑后更新 context.md
- 完成任务后勾选 tasks.md
- 信任 Hook 自动保存

**第 4 步：验证效果**
- 模拟上下文重置
- 检查能否快速恢复
- 优化文档结构

### 核心收益

| 维度 | 传统方式 | Dev Docs + Hook |
|------|---------|-----------------|
| **恢复时间** | 30-60 分钟 | 5 秒 |
| **进度丢失** | 高风险 | 零风险 |
| **心智负担** | 需要记住保存 | 完全自动 |
| **长期价值** | 无积累 | 知识沉淀 |

**金句：** "Dev Docs Pattern 让上下文重置从'灾难'变成'无感切换'。"

---

## 最佳实践

### 1. Skill 命名

**原则：** 动词 + 对象

```
✅ 好的命名:
- react-component-generator (生成组件)
- code-review (审查代码)
- feature-builder (构建功能)

❌ 不好的命名:
- frontend-helper (过于宽泛)
- my-skill (无意义)
- generator (不知道生成什么)
```

### 2. Description 撰写

**公式：** 核心能力 + 触发场景 + 关键特性

```yaml
# ✅ 好的 description
description: 分析 UI 设计截图并生成 React 代码。使用时机：
  用户提供设计稿/Figma 截图。功能：布局分析 + design token
  提取 + Tailwind 代码生成。

# ❌ 不好的 description
description: 这个 skill 用于帮助分析 UI
```

**要素：**
- 一句话说明核心能力
- 明确触发场景
- 列出 2-3 个关键特性
- 长度：50-150 字

### 3. References 组织

**原则：** 按使用频率和重要性分层

```
references/
├── quick-reference.md      # 速查表（最常用）
├── detailed-guide.md       # 详细指南（深度学习）
├── checklist.md            # 检查清单（执行时用）
├── examples.md             # 示例代码（参考实现）
└── troubleshooting.md      # 问题排查（遇到问题时）
```

**编写建议：**
- quick-reference: 表格形式，关键点一目了然
- detailed-guide: 结构化说明，包含原理
- checklist: 纯列表，用于逐项核对
- examples: 完整可运行代码

### 4. 渐进式增强

**原则：** 先做最小可用版本，逐步完善

**阶段 1: MVP**
```yaml
基础功能:
  - 核心工作流程（SKILL.md）
  - 1-2 个最常用场景
  - 基础工具权限
```

**阶段 2: 完善**
```yaml
增强功能:
  - 添加 references/（详细规范）
  - 覆盖更多场景
  - 优化错误处理
```

**阶段 3: 协作**
```yaml
系统集成:
  - 与其他 Skills 协作
  - 添加 assets/（模板库）
  - 完善文档和示例
```

### 5. 持续优化

**观察指标：**

```
Skill 质量评估
├── 使用频率
│   └─ 高频 Skill 需要持续优化
├── 出错率
│   └─ 错误多 → 工作流程不清晰
├── 用户反馈
│   └─ 收集实际使用中的痛点
└── 协作效率
    └─ 与其他 Skills 配合是否顺畅
```

**优化方向：**

| 问题 | 解决方案 |
|------|---------|
| 使用率低 | 检查 description 是否准确，场景是否常见 |
| 经常出错 | 简化工作流程，增加决策树 |
| 职责不清 | 拆分为多个 Skill 或合并到现有 Skill |
| 与其他 Skill 冲突 | 明确边界，调整触发条件 |

## 常见问题

### Q1: Skill 太多会不会影响性能？

**A:** 不会。Skills 按需激活。

- request-analyzer 会智能选择相关 Skill
- 用户可以手动指定 Skill（/skill-name）
- 只有激活的 Skill 才加载到上下文

**建议：**
- 保持 Skill 数量在 5-15 个
- 每个 Skill 职责单一
- 避免功能重叠

### Q2: Skill 和 CLAUDE.md 内容重复怎么办？

**A:** 分层设计，避免重复。

```
CLAUDE.md:
  "组件文件大小 ≤ 300 行"

feature-builder/references/coding-standards.md:
  "## 组件大小控制
   ### 推荐: ≤ 200 行
   ### 最大: ≤ 300 行
   ### 超过 300 行: 拆分方案
      1. 按功能拆分
      2. 提取子组件
      3. 抽取 hooks
   [200 行详细说明]"
```

**原则：**
- CLAUDE.md: 核心规则（一句话）
- Skill: 详细说明（如何做、为什么）

### Q3: 什么时候用 Skill，什么时候用 Subagent？

**决策标准：**

| 场景 | 使用 | 原因 |
|------|------|-----|
| 代码审查 | Skill | 需要主对话上下文 |
| 功能开发 | Skill | 需要交互式确认 |
| 全代码库分析 | Subagent | 需要独立上下文 |
| 并行任务 | Subagent | 同时执行多个任务 |
| 长时间运行 | Subagent | 不阻塞主对话 |

**简单判断：**
- 需要与用户交互 → Skill
- 需要独立执行 → Subagent
- 需要访问当前代码 → Skill
- 需要扫描整个项目 → Subagent

### Q4: 如何避免 Skill 之间的职责冲突？

**预防措施：**

1. **明确边界**
```yaml
# react-component-generator
做: 生成 UI 组件（只有 JSX 和样式）
不做: 业务逻辑、API 调用、状态管理

# feature-builder
做: 完整功能（UI + 逻辑 + API）
不做: 单纯的组件生成（交给 react-component-generator）
```

2. **协作而非竞争**
```
feature-builder 调用 react-component-generator
└─ 而不是自己重新实现组件生成逻辑
```

3. **定期审查**
```
每月检查:
- Skills 之间是否有功能重叠
- 是否有未使用的 Skill（考虑删除或合并）
- 是否有新的需求需要新 Skill
```

## 实施建议

### 从零开始构建 Skills 体系

**第 1 周: 基础设施**
```
1. 创建 CLAUDE.md（核心原则 + 技术栈）
2. 创建 request-analyzer（智能协调器）
3. 测试基础流程
```

**第 2-3 周: 核心 Skills**
```
根据项目类型选择:

前端项目:
  - react-component-generator
  - feature-builder
  - code-review

后端项目:
  - api-generator
  - database-schema-designer
  - code-review

全栈项目:
  - 前端 + 后端 Skills 组合
```

**第 4+ 周: 迭代优化**
```
1. 收集实际使用反馈
2. 优化高频 Skill
3. 添加辅助 Skill（如 prompt-optimizer）
4. 完善 references/
```

### 团队协作建议

**角色分工：**

```
架构师: 设计 Skills 体系结构
开发者: 编写 Skill 工作流程
技术写作: 完善 references/ 文档
测试: 验证 Skill 质量和协作
```

**版本管理：**

```
.claude/
├── skills/
│   └── [skill-name]/
│       ├── SKILL.md          # Git 跟踪
│       ├── references/       # Git 跟踪
│       └── assets/           # Git 跟踪
└── CLAUDE.md                 # Git 跟踪

建议:
- 所有 Skills 纳入版本管理
- Pull Request 时审查 Skill 变更
- 使用语义化版本（如 v1.2.0）
```

## 总结

### 核心理念

**Skills = 专业知识的模块化封装**

三个关键点：
1. **单一职责** - 每个 Skill 只做一件事
2. **明确边界** - 清楚说明做什么、不做什么
3. **可组合性** - Skills 之间可以协作

### 设计检查清单

创建新 Skill 前，确认：

- [ ] 有明确的使用场景（不是一次性需求）
- [ ] 职责单一（能用一个动词描述）
- [ ] 不与现有 Skill 重叠
- [ ] 有标准化的工作流程
- [ ] 需要的工具权限已明确
- [ ] description 清晰准确（50-150 字）

完成 Skill 后，确认：

- [ ] SKILL.md 包含完整工作流程
- [ ] references/ 包含必要的详细规范
- [ ] allowed-tools 遵循最小权限原则
- [ ] 与其他 Skills 的协作关系已定义
- [ ] 有实际示例或测试用例

### 持续改进

**观察 → 分析 → 优化**

```
观察使用情况
├─ Skill 使用频率
├─ 常见错误模式
└─ 用户反馈

分析问题根源
├─ 工作流程不清晰？
├─ 职责定义不明确？
└─ 缺少必要工具？

优化改进
├─ 简化流程
├─ 补充文档
└─ 调整工具权限
```

**记住：** Skills 体系不是一次性设计，而是随项目演进持续优化的过程。

---

**扩展阅读：**
- [Claude Code 官方文档](https://code.claude.com/docs)
- [Skills 最佳实践](https://github.com/anthropics/claude-code-skills)
