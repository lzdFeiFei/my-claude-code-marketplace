# Conventional Commits 规范参考

## 规范版本
基于 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/)

---

## 格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

---

## Type 类型完整列表

### 主要类型

| Type | 说明 | 何时使用 | 示例 |
|------|------|----------|------|
| `feat` | 新功能 | 添加新的功能特性 | `feat(auth): 添加 OAuth 登录` |
| `fix` | Bug 修复 | 修复代码缺陷 | `fix(ui): 修复按钮样式错误` |
| `docs` | 文档 | 仅文档变更 | `docs: 更新 API 文档` |
| `style` | 代码格式 | 不影响代码含义的变更（空格、格式化、分号等） | `style: 格式化代码` |
| `refactor` | 重构 | 既不修复 bug 也不添加功能的代码变更 | `refactor: 重构用户模块` |
| `perf` | 性能优化 | 提升性能的代码变更 | `perf: 优化列表渲染` |
| `test` | 测试 | 添加或修改测试 | `test: 添加登录测试` |
| `build` | 构建系统 | 影响构建系统或外部依赖的变更 | `build: 升级 Vite 到 v7` |
| `ci` | CI/CD | CI 配置文件和脚本的变更 | `ci: 添加 GitHub Actions` |
| `chore` | 其他变更 | 不修改 src 或 test 的变更 | `chore: 更新依赖` |
| `revert` | 回滚 | 回滚之前的 commit | `revert: 回滚 commit abc123` |

### Angular 额外类型（可选）

这些在某些项目中使用，但不是 Conventional Commits 标准的一部分：

| Type | 说明 |
|------|------|
| `wip` | Work in Progress（进行中的工作，不推荐提交到主分支） |
| `deps` | 依赖更新（有些项目用这个代替 chore） |
| `config` | 配置变更 |
| `release` | 发布新版本 |

---

## Scope（作用域）

### 什么是 Scope？

Scope 是可选的，用于指定变更影响的范围（模块、组件、包等）。

### 项目常见 Scope

**功能模块**：
- `auth` - 认证/授权
- `user` - 用户管理
- `dashboard` - 仪表板
- `settings` - 设置

**技术层**：
- `ui` - UI 组件
- `api` - API 接口
- `router` - 路由
- `store` - 状态管理
- `db` - 数据库

**工具/配置**：
- `deps` - 依赖
- `config` - 配置
- `ci` - CI/CD
- `build` - 构建

**具体组件**：
- `Button` - 按钮组件
- `LoginForm` - 登录表单
- `UserList` - 用户列表

### Scope 规则

- ✅ 小写字母
- ✅ 简短明了
- ✅ 能快速识别影响范围
- ❌ 不要太具体（如文件名）
- ❌ 不要太宽泛（如 "frontend"）

---

## Description（描述）

### 规则

1. **使用祈使句**：
   - ✅ "添加"、"修复"、"更新"
   - ❌ "添加了"、"修复了"、"更新了"

2. **首字母小写**（英文）：
   - ✅ `add feature`
   - ❌ `Add feature`

3. **中文不加句号**：
   - ✅ `添加用户登录功能`
   - ❌ `添加用户登录功能。`

4. **简洁明了**：
   - ✅ 建议 ≤ 50 字符
   - ❌ 最多不超过 72 字符

5. **聚焦"为什么"而非"是什么"**：
   - ✅ `优化登录页面加载速度`（说明目的）
   - ❌ `修改了 Login.tsx 文件`（只说了做了什么）

### 示例

**好的描述**：
```
feat(auth): 添加 JWT 认证功能
fix(ui): 修复按钮在移动端的点击区域过小
refactor(api): 简化用户数据获取逻辑
perf(list): 使用虚拟滚动优化长列表性能
docs(readme): 添加快速开始指南
```

**不好的描述**：
```
❌ feat: 添加了一些功能              (太模糊)
❌ fix: bug修复                     (无意义)
❌ update: 更新代码                 (没有 type)
❌ feat(auth): 修改了 auth.ts 文件   (说"做了什么"而非"为什么")
❌ feat: Add User Login Feature.   (英文、首字母大写、有句号)
```

---

## Body（正文）

### 何时需要 Body

- ✅ 变更复杂，需要详细说明
- ✅ 需要解释动机和背景
- ✅ 有 breaking changes
- ✅ 涉及架构调整

### 格式规则

1. **与 description 空一行**
2. **每行不超过 72 字符**
3. **可以多段**
4. **使用列表说明多个要点**

### 示例

```
feat(auth): 添加 JWT 认证功能

实现了基于 JWT 的用户认证系统，替代之前的 session 方案。

主要变更：
- 添加 JWT token 生成和验证逻辑
- 实现 token 自动刷新机制
- 添加路由守卫保护敏感页面
- 支持 remember me 功能

这个改动提升了系统的可扩展性，便于未来支持多端登录。
```

---

## Footer（页脚）

### Breaking Changes

如果有破坏性变更，必须在 footer 中说明：

```
feat(api): 重构用户 API 接口

将 /api/user 重构为 RESTful 风格

BREAKING CHANGE:
- GET /api/user 改为 GET /api/users/:id
- POST /api/user/create 改为 POST /api/users
- 移除了 /api/user/list 接口，使用 GET /api/users 替代
```

或使用 `!` 标记：

```
feat(api)!: 重构用户 API 接口
```

### 关联 Issue

```
fix(ui): 修复登录按钮无响应

修复了点击登录按钮时偶尔无响应的问题，
原因是事件监听器重复绑定。

Closes #123
```

支持的关键词：
- `Closes` / `Fixes` / `Resolves` - 关闭 issue
- `Refs` / `See also` - 引用相关 issue

---

## 完整示例

### 示例 1: 简单功能

```
feat(auth): 添加用户登录功能
```

### 示例 2: 带 Body

```
feat(auth): 添加 OAuth 第三方登录

支持通过 Google 和 GitHub 账号登录系统。

实现内容：
- OAuth 2.0 授权流程
- 第三方账号与本地账号绑定
- 登录按钮 UI 组件
```

### 示例 3: Breaking Change

```
feat(api)!: 重构用户 API 为 RESTful 风格

BREAKING CHANGE:
- GET /user 改为 GET /users/:id
- POST /user/create 改为 POST /users
- 响应数据结构从 { data, code, msg } 改为 { data, error }
```

### 示例 4: Bug 修复

```
fix(ui): 修复移动端菜单无法关闭

修复了在 iOS Safari 上点击遮罩层无法关闭菜单的问题。
原因是 touch 事件和 click 事件冲突。

Fixes #456
```

---

## 验证工具

### Commitlint

项目使用 `@commitlint/config-conventional` 配置。

**检查规则**：
- ✅ Type 必须是允许的类型之一
- ✅ Subject 不能为空
- ✅ Subject 不能以句号结尾
- ✅ Subject 应使用祈使句

**配置文件**：`commitlint.config.js`

### Husky Hook

Git hooks 配置在 `.husky/commit-msg`，每次 commit 时自动运行 commitlint。

---

## 常见问题

### Q1: 一次提交包含多种变更怎么办？

**建议拆分**：
```bash
# 不推荐
git commit -m "feat: 添加登录功能 + 修复样式 bug + 更新文档"

# 推荐
git add app/auth/
git commit -m "feat(auth): 添加登录功能"

git add app/styles/
git commit -m "fix(ui): 修复样式问题"

git add README.md
git commit -m "docs: 更新使用文档"
```

### Q2: Scope 应该多细？

**原则**：能快速识别影响范围即可

```
✅ feat(auth): 添加登录      - 合适
✅ feat(LoginForm): 添加登录  - 也可以
❌ feat(src/app/auth/components/LoginForm.tsx): 添加登录  - 太细
❌ feat(frontend): 添加登录   - 太宽
```

### Q3: 重构代码算 refactor 还是 feat？

**判断标准**：
- 如果改变了外部行为 → `feat` 或 `fix`
- 如果只改变内部实现 → `refactor`

```
refactor: 重构认证模块代码结构    - 内部重构，功能不变
feat: 添加认证缓存机制           - 新增功能
```

### Q4: 更新依赖用什么 type？

**推荐**：
```
chore(deps): 升级 React 到 v19
build(deps): 更新 Vite 到 v7
```

---

## 参考资源

- [Conventional Commits 官方规范](https://www.conventionalcommits.org/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
- [Commitlint](https://commitlint.js.org/)
