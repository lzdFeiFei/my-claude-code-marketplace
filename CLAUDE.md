# CLAUDE CODE 工作指南

**配置级别**: 项目级配置 - React/TypeScript/Tailwind 前端项目

本文件为 Claude Code 提供针对本项目的专项工作指导。

---

## 核心原则

- **所有回复使用中文**
- **每次回复以"好的老板"开头**
- **不要 build 项目**（除非明确要求）
- **使用 MCP 搜索最新 React/Next.js 文档和最佳实践**

---

## 技术栈

### 核心框架
- **React 18+** + TypeScript + Next.js (App Router)
- **Tailwind CSS** + **Zustand** + **React Query** + **Zod**

### 代码规范
- 函数式组件 + Hooks
- TypeScript 严格模式
- ESLint + Prettier

**详细规范**: 参考 `feature-builder` 和 `code-review` skills

---

## Skills 使用指南

本项目配置了专业 skills，根据任务自动激活：

### 前端开发 Skills

| Skill | 用途 | 触发示例 |
|-------|------|---------|
| **react-component-generator** | 创建组件 | "创建登录表单"、"生成产品卡片" |
| **feature-builder** | 完整功能（UI+逻辑+API） | "实现用户认证"、"构建购物车" |
| **ui-analyzer** | 设计稿转代码 | "分析这个设计稿" |
| **code-review** | 代码质量检查 | "审查这个组件"、"检查性能" |
| **request-analyzer** | 智能协调（自动） | 分析任务并推荐 skills |
| **prompt-optimizer** | 需求收集（交互式） | 需求不清晰时引导 |

**详细说明**: 查看各 skill 的 SKILL.md 文件

---

## 工作流程

### 任务复杂度判定

#### 简单任务（直接执行）
- 代码 ≤ 200 行
- 文件 < 5 个
- 单个组件/hook 修改

**执行**: 直接使用相应 skill 或工具完成

#### 复杂任务（必须规划）
- 代码 > 200 行，**或**
- 文件 ≥ 5 个，**或**
- 完整 feature（多组件+hooks+API）

**流程**:
1. **分析** → 使用 `prompt-optimizer` 收集详细需求
2. **规划** → 使用 `/dev-docs [任务描述]` 创建三文件结构：
   ```bash
   /dev-docs 实现用户认证功能
   ```
   自动生成：
   - `[task]-plan.md` - 战略计划（执行摘要、实施阶段、风险评估）
   - `[task]-context.md` - 关键信息（SESSION PROGRESS、决策记录）
   - `[task]-tasks.md` - 任务清单（Checkbox 格式、验收标准）

   包含内容：
   - ✅ 可勾选任务清单
   - ✅ Mermaid 架构图/流程图
   - ✅ 涉及文件列表
   - ✅ 技术方案
   - ✅ 验收标准
   - ✅ 风险评估
3. **确认** → 等待用户批准计划
4. **执行** → 使用 `feature-builder` 逐步实现
5. **审查** → 使用 `code-review` 检查质量
6. **总结** → 在 `[task]-context.md` 末尾添加实现总结

---

## Dev Docs Pattern（上下文保护）

### 跨会话任务管理

对于**复杂、多会话任务**，使用 Dev Docs Pattern 保护上下文：

#### 何时使用 Dev Docs
- ✅ 超过 2 小时的任务
- ✅ 跨多个会话的工作
- ✅ 复杂的多阶段功能
- ✅ 需要详细规划的重构

#### 工作流程

**1. 启动任务**
```bash
/dev-docs 实现用户认证系统
```

Claude 自动创建：
```
dev/active/implement-user-auth/
├── implement-user-auth-plan.md      # 战略计划
├── implement-user-auth-context.md   # 关键决策和进度
└── implement-user-auth-tasks.md     # 任务清单
```

**2. 实施期间**
- 参考 `plan.md` 了解整体策略
- **频繁更新** `context.md`（每个里程碑后）
- 勾选 `tasks.md` 中完成的任务

**3. 上下文压缩前**
```bash
/dev-docs-update  # 手动保存
```

**💡 自动保存（推荐）**：项目已配置 PreCompact Hook，在接近 token 限制时**自动触发** `/dev-docs-update`，无需手动操作。

自动保存内容：
- ✅ 当前实现状态
- ✅ 本次会话的关键决策
- ✅ 下一步骤
- ✅ 未完成工作的确切状态

**配置详情**：查看 `.claude/HOOKS.md`

**4. 上下文重置后**
- Claude 自动读取三个文件
- 5 秒恢复完整状态
- 从中断处继续工作

#### 三层任务管理

| 层级 | 工具 | 作用范围 | 生命周期 |
|------|------|----------|----------|
| **L1 项目** | CLAUDE.md | 所有任务 | 永久 |
| **L2 任务** | dev/active/[task]/ | 单个复杂任务 | 任务期间 |
| **L3 会话** | TodoWrite 工具 | 当前会话 | 单次会话 |

**详细说明**: 查看 `dev/README.md`

---

## 思维方式

### 批判性思考
- 主动发现问题（安全、性能、UX）
- 提供更优方案（基于 React 最佳实践）
- 直言不讳（方案有缺陷直接指出）

### 可视化分析
**复杂功能必须先输出 Mermaid 图**:
- `flowchart` - 业务流程
- `sequenceDiagram` - 组件交互
- `classDiagram` - 数据结构

### 基于事实
- **Always read the code**: 修改前必读相关代码
- **禁用词汇**: "可能"、"猜测"
- **No apologies**: 为结论负责
- **No invention**: 不擅自添加功能

### 多方案思考
至少提供 2-3 个方案：
- **方案 A**: 最简单（快速）
- **方案 B**: 最佳实践（可维护）
- **方案 C**: 性能优化（高性能）

**默认**: 方案 B

---

## 架构原则

### 3 层架构（强制）
```
features/[feature-name]/
├── components/    # UI Layer
├── hooks/         # Business Logic
├── stores/        # Global State (Zustand)
├── api/           # Data Access (React Query)
├── utils/         # Validation, transforms
├── types/         # TypeScript types
└── index.ts
```

**规则**:
- ✅ UI 不直接调用 API
- ✅ 业务逻辑封装在 hooks
- ✅ 全局状态用 Zustand
- ✅ 服务器状态用 React Query

**详细说明**: `feature-builder` skill

---

## 架构变更确认

遇到以下情况**必须先询问**:

### 需要确认的决策
- 新增 npm 依赖
- 修改 Zustand store 结构
- 调整 React Query 配置
- 引入第三方组件库
- 大组件拆分策略
- Hook 提取决策
- 目录结构调整

**默认策略**（未明确时）:
- 保持现有架构和分层
- 优先迭代现有代码
- 遵循项目命名和组织约定

---

## 修改执行原则

### 单次完整修改
- 同一文件所有变更**汇总为一次 Edit**
- 一个组件只修改一次

### 专注相关代码
- 只修改任务相关代码
- 分析变更影响（props、hooks、状态）

### 优先迭代现有实现
- 检查已有类似组件/hooks/API
- 复用现有代码
- 创建新功能前说明理由

### 文件大小控制
- **组件**: ≤ 200 行（推荐），≤ 300 行（最大）
- **超过 300 行**: 必须拆分

---

## 核心规范速查

### TypeScript
- ❌ 禁用 `any`（除非极特殊情况）
- ✅ 使用 Zod 运行时验证
- ✅ 明确的 Props 接口

### React
- ✅ 函数式组件 + Hooks
- ✅ 合理使用 `useMemo`/`useCallback`/`memo`
- ❌ 不直接修改 state

### Tailwind
- ✅ Mobile-first 响应式
- ✅ 使用 Tailwind 变量复用样式

### 安全
- ❌ 无 `dangerouslySetInnerHTML` + 用户输入
- ✅ 表单用 Zod 验证
- ✅ 敏感数据不存 localStorage
- ✅ API 密钥用环境变量

**完整规范**:
- 代码规范 → `feature-builder/references/coding-standards.md`
- 安全规范 → `code-review/references/frontend-security.md`
- 性能规范 → `code-review` skill
- 无障碍 → `code-review/references/accessibility-guide.md`

---

## 项目约定

### 环境变量
- **命名**: `NEXT_PUBLIC_*` 前缀
- **位置**: `.env.local` (不提交)

### 导入顺序
```typescript
// 1. React/Next.js
// 2. 第三方库
// 3. 项目内部
// 4. 类型
// 5. 样式
```

### 路径别名
```typescript
// ✅ 使用 @ 别名
import { Button } from '@/components/ui/Button';

// ❌ 避免相对路径
import { Button } from '../../../components/ui/Button';
```

### Git 提交
```
<type>(<scope>): <subject>

<body>
```

**Types**: `feat`, `fix`, `refactor`, `style`, `perf`, `test`, `docs`, `chore`

---

## 禁止行为

### 绝对禁止 ❌
- 使用 `any` 类型
- 直接修改 state
- 组件内直接调用 API
- 硬编码敏感信息
- 使用 `eval()`
- 修改 `.env` 文件

### 强烈不推荐 ⚠️
- 组件超过 300 行
- 深度嵌套（超过 3 层）
- 渲染中昂贵计算（应用 useMemo）
- 用 index 作为 key
- useEffect 缺少依赖

---

## 最终检查清单

每次代码修改完成后确认：

### 功能
- [ ] 实现所有需求
- [ ] 处理错误和边界
- [ ] 添加 loading/error 状态

### 质量
- [ ] TypeScript 无错误
- [ ] ESLint 通过
- [ ] 遵循项目规范
- [ ] 无 console.log

### 性能
- [ ] 合理 memoization
- [ ] 懒加载（大组件）
- [ ] 无不必要重渲染

### 安全
- [ ] 输入验证（Zod）
- [ ] 无 XSS 漏洞
- [ ] 敏感数据安全

### 无障碍
- [ ] 语义化 HTML
- [ ] ARIA 标签
- [ ] 键盘可访问

### 测试
- [ ] 关键功能有测试
- [ ] 测试通过
- [ ] 边界情况覆盖

---

## 核心目标

写出**清晰、安全、高性能、易维护**的生产级前端代码。

遵循架构优先、类型安全、性能优化、用户体验的原则。
