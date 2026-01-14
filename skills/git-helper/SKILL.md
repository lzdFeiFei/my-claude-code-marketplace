---
name: git-helper
description: 智能 Git 操作助手，自动处理代码提交、生成符合 Conventional Commits 规范的 commit message。当用户请求提交代码、commit、保存修改、创建提交等操作时使用此 skill。支持自动分析变更、生成规范 message、安全检查。
allowed-tools: Bash, Read, Grep, Glob
---

# Git Helper - 智能 Git 操作助手

专业的 Git 工作流助手，帮助用户高效、规范地完成 Git 操作。

## 核心功能

### 1. 智能代码提交 (主要功能)
- 自动分析代码变更
- 生成符合 Conventional Commits 规范的 commit message
- 执行安全检查
- 处理 pre-commit hooks

### 2. 未来扩展 (规划中)
- 智能 push 操作
- PR 创建和管理
- 分支管理
- Rebase 辅助

---

## 何时激活此 Skill

### 触发关键词

用户说以下任何内容时，应该激活此 skill：

**直接命令**：
- "提交代码"
- "commit"
- "git commit"
- "保存修改"
- "提交修改"
- "创建 commit"

**含蓄表达**：
- "保存一下"（在代码修改后）
- "记录这些变更"
- "帮我提交"
- "把改动提交了"

**明确不触发**：
- 仅讨论 Git 概念（不执行操作）
- 查看 Git 历史（使用 git log 即可）

---

## 执行流程

### 步骤 1: 分析当前状态

**并行执行以下命令**（提高效率）：

```bash
# 命令 1: 查看工作区状态
git status

# 命令 2: 查看未暂存的变更
git diff

# 命令 3: 查看已暂存的变更
git diff --staged

# 命令 4: 学习项目提交风格
git log -5 --oneline
```

**输出分析**：
- 识别修改/新增/删除的文件
- 了解变更的代码内容
- 学习历史 commit message 风格

---

### 步骤 2: 变更内容分析

基于 `git diff` 输出，分析：

1. **变更性质**：
   - 新功能（feat）
   - Bug 修复（fix）
   - 代码重构（refactor）
   - 样式调整（style）
   - 性能优化（perf）
   - 测试相关（test）
   - 文档更新（docs）
   - 构建/配置（chore）

2. **影响范围**：
   - 哪些模块/组件被修改
   - 是否跨多个功能域
   - 是否影响公共 API

3. **变更目的**：
   - 为什么做这个改动
   - 解决了什么问题
   - 带来了什么价值

---

### 步骤 3: 确定 Commit Type 和 Scope

#### Type（必选）

| Type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | 添加用户登录功能 |
| `fix` | Bug 修复 | 修复登录页面 404 错误 |
| `refactor` | 重构（不改功能） | 重构认证模块代码结构 |
| `style` | 代码格式 | 格式化代码、调整缩进 |
| `perf` | 性能优化 | 优化列表渲染性能 |
| `test` | 测试 | 添加登录功能单元测试 |
| `docs` | 文档 | 更新 README 使用说明 |
| `chore` | 构建/工具 | 升级依赖、更新配置 |
| `ci` | CI/CD | 修改 GitHub Actions 配置 |
| `build` | 构建系统 | 修改 Vite 配置 |
| `revert` | 回滚 | 回滚登录功能提交 |

#### Scope（可选）

影响的模块或组件名称：
- `auth` - 认证模块
- `ui` - UI 组件
- `api` - API 接口
- `router` - 路由
- `[component-name]` - 具体组件名

**示例**：
- `feat(auth): 添加 JWT 认证`
- `fix(ui): 修复按钮样式问题`
- `refactor(api): 重构用户接口`

---

### 步骤 4: 生成 Commit Message

#### 格式规范

```
<type>(<scope>): <subject>

<body>
```

#### Subject（必须）

**要求**：
- ✅ 简洁明了（不超过 50 字符）
- ✅ 使用祈使句（"添加"而非"添加了"）
- ✅ 首字母小写
- ✅ 末尾不加句号
- ✅ 聚焦"为什么"而非"是什么"
- ✅ **使用中文**（符合项目团队习惯）

**好的示例**：
```
feat(auth): 添加用户登录功能
fix(ui): 修复按钮在移动端的样式问题
refactor(api): 优化用户数据获取逻辑
```

**不好的示例**：
```
❌ feat: added user login feature  (用了英文、过去式)
❌ fix: 修复了一个 bug。            (太模糊、有句号)
❌ Update some files              (没有 type、太模糊)
```

#### Body（可选）

**何时需要 body**：
- 变更复杂，需要详细说明
- 需要解释"为什么"这样做
- 涉及重大架构调整
- 有 breaking changes

**格式要求**：
- 每行不超过 72 字符
- 可以多段
- 使用列表说明多个要点
- 详细说明变更原因和影响

**示例**：
```
feat(auth): 添加 JWT 认证功能

实现了基于 JWT 的用户认证系统，包含：
- 登录/登出接口
- Token 自动刷新机制
- 路由守卫保护
- 本地 token 存储

这个改动替换了之前的 session 认证，提升了可扩展性
```

---

### 步骤 5: 安全检查

**提交前必须确认**：

#### 禁止操作 ❌
- ❌ 不提交包含敏感信息的文件：
  - `.env`
  - `credentials.json`
  - 包含 API keys、密码的文件
- ❌ 不使用 `--no-verify` 跳过 hooks
- ❌ 不使用 `--amend`（除非用户明确要求）
- ❌ 不提交 build 产物（如 `dist/`, `build/`）
- ❌ 不提交 `node_modules/`

#### 必须检查 ✅
- ✅ 所有暂存的文件都是相关的
- ✅ commit message 准确反映变更
- ✅ 没有调试代码（console.log, debugger）
- ✅ 代码符合项目规范

**如果发现问题**：
1. 立即警告用户
2. 列出具体问题
3. 询问是否继续或修改

---

### 步骤 6: 执行 Commit

#### 情况 A: 有未暂存的修改

```bash
git add . && git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>
EOF
)"
```

#### 情况 B: 所有修改已暂存

```bash
git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>
EOF
)"
```

#### 使用 HEREDOC 的原因

- ✅ 保证多行格式正确
- ✅ 避免引号冲突
- ✅ 支持换行和特殊字符

---

### 步骤 7: 后续操作

提交成功后**必须执行**：

```bash
# 确认提交状态
git status
```

**向用户报告**：
1. ✅ 提交成功的确认
2. 📋 Commit hash（前 7 位）
3. 📝 完整的 commit message
4. 📊 变更统计（文件数、行数）
5. 🔄 分支状态（是否领先 origin）

**示例输出**：
```
✅ 代码已成功提交！

📋 Commit: 85d933d
📝 Message:
   feat(auth): 添加用户登录功能

   实现了基于 JWT 的认证系统

📊 变更: 4 files changed, 433 insertions(+), 46 deletions(-)
🔄 本地分支领先 origin/main 4 个提交
```

**不要自动执行**：
- ❌ 不要自动 `git push`（除非用户明确要求）
- ❌ 不要自动创建 PR

---

### 步骤 8: 处理 Pre-commit Hook 失败

项目配置了以下 hooks：
- **husky** - Git hooks 管理
- **commitlint** - Commit message 规范检查
- **lint-staged** - 暂存文件代码检查（Biome）

#### 情况 A: lint-staged 修改了文件

**现象**：
```
[main 85d933d] feat: 添加功能
→ lint-staged: Biome formatted 3 files
```

**处理流程**：
1. 查看 lint-staged 的修改内容
2. 如果只是格式化（空格、换行），可以 amend：
   ```bash
   git add . && git commit --amend --no-edit
   ```
3. 如果修改了代码逻辑，创建新 commit

#### 情况 B: commitlint 失败

**现象**：
```
⧗   input: update some files
✖   subject may not be empty [subject-empty]
✖   type may not be empty [type-empty]
```

**处理**：
1. 分析 commitlint 错误
2. 调整 commit message 格式
3. 重新提交

#### 情况 C: Biome 检查失败

**现象**：
```
✖ Found 5 errors
```

**处理**：
1. 显示具体错误
2. 询问用户是否修复
3. 如果修复，运行 `pnpm check` 并重新提交

---

## 高级功能

### 智能 Scope 推断

基于文件路径自动推断 scope：

| 文件路径 | 推断 Scope |
|----------|-----------|
| `app/components/ui/*` | `ui` |
| `app/routes/auth/*` | `auth` |
| `app/lib/api/*` | `api` |
| `.github/workflows/*` | `ci` |
| `*.md` | `docs` |
| `package.json`, `vite.config.ts` | 无 scope 或 `deps`/`config` |

### 多类型变更处理

如果一次提交包含多种类型的变更：

1. **优先原则**：
   - feat > fix > refactor > 其他
   - 选择最重要的变更作为主 type

2. **建议拆分**：
   如果变更差异很大，建议用户拆分为多个 commit：
   ```
   检测到以下变更：
   - 新增用户认证功能（feat）
   - 修复按钮样式 bug（fix）
   - 更新 README（docs）

   建议拆分为 3 个独立的 commit，是否需要帮助拆分？
   ```

### 交互式确认

对于以下情况，询问用户确认：

1. **变更太大**（超过 500 行）
   ```
   检测到大量变更（673 行），建议拆分为多个 commit。
   是否继续单次提交？
   ```

2. **Scope 不明确**
   ```
   变更涉及多个模块：auth, ui, api
   建议的 scope 是 "auth"，是否正确？
   ```

3. **可能的敏感文件**
   ```
   检测到以下文件可能包含敏感信息：
   - .env.local

   确认要提交吗？
   ```

---

## 用户提供的上下文

用户可能提供额外说明，例如：
- "这次主要是优化了性能"
- "修复了登录页面的问题"
- "重构了认证模块"

**使用这些信息**：
- 辅助判断 type 和 scope
- 丰富 commit message 的 body
- 确保 message 符合用户意图

---

## 错误处理

### 常见错误

#### 1. 工作区干净（无变更）

```
On branch main
nothing to commit, working tree clean
```

**处理**：
```
当前没有代码变更需要提交。
工作区是干净的。
```

#### 2. Git 未初始化

```
fatal: not a git repository
```

**处理**：
```
当前目录不是 Git 仓库。
需要先运行 `git init` 初始化 Git 仓库。
```

#### 3. 冲突未解决

```
You have unmerged paths.
```

**处理**：
```
检测到未解决的合并冲突。
请先解决冲突后再提交。
```

---

## 最佳实践

### Commit Message 编写原则

1. **原子性**：每个 commit 只做一件事
2. **可读性**：让别人（和未来的自己）能快速理解
3. **可追溯**：关联 issue、PR（如果有）
4. **规范性**：严格遵循 Conventional Commits

### 项目特定规范

参考 CLAUDE.md 和 README.md：
- ✅ 使用中文 subject 和 body
- ✅ 遵循 Biome 代码规范
- ✅ 通过 commitlint 检查
- ✅ 不跳过 pre-commit hooks

### 提交频率建议

- ✅ 功能完成一个小模块就提交
- ✅ 修复一个 bug 就提交
- ✅ 重构一个文件/模块就提交
- ❌ 避免一天只提交一次大 commit
- ❌ 避免提交未完成的功能（除非有 feature flag）

---

## 输出格式

### 成功提交的输出

```markdown
✅ 代码已成功提交！

## 提交详情

**Commit Hash**: `85d933d`

**提交信息**:
```
<type>(<scope>): <subject>

<body>
```

## 变更统计

- **X 个文件变更**: Y 行新增，Z 行删除
  - `file1.ts` - N 行
  - `file2.tsx` - M 行

## 当前状态

- ✅ 工作区干净
- 📌 本地分支领先 origin/main X 个提交

## 下一步（可选）

如需推送到远程仓库：
`git push origin main`
```

---

## 注意事项

### 强制要求

1. **使用中文**：subject 和 body 必须使用中文
2. **禁用占位符**：不使用 `any`、`TODO` 等占位符
3. **完整分析**：必须先分析 git diff，不能猜测
4. **安全优先**：发现敏感信息立即警告

### 最佳实践

1. **并行执行**：git status/diff/log 并行运行
2. **简洁输出**：向用户展示关键信息，不啰嗦
3. **友好提示**：用 emoji 增强可读性（✅❌📋等）
4. **持续改进**：学习项目的 commit 历史风格

---

## 未来规划

### Phase 2: Push 管理
- 智能判断是否需要 push
- 检查远程分支状态
- 处理 push 冲突

### Phase 3: PR 创建
- 自动生成 PR 描述
- 关联 issue
- 设置 reviewer

### Phase 4: 分支管理
- 创建功能分支
- 合并分支
- 删除已合并分支

### Phase 5: Rebase 辅助
- 交互式 rebase 指导
- 冲突解决建议
- Commit 整理
