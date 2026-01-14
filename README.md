# My Claude Code Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/lzdFeiFei/my-claude-code-marketplace)
[![Skills](https://img.shields.io/badge/skills-15-green.svg)](https://github.com/lzdFeiFei/my-claude-code-marketplace)

个人 Claude Code Skills Marketplace - 包含 15 个专业前端开发和内容创作 Skills，支持标准 marketplace 安装流程。

## 快速开始

### 方式 1: Marketplace 安装（推荐）

```bash
# 1. 添加 marketplace
/plugin marketplace add lzdFeiFei/my-claude-code-marketplace

# 2. 浏览可用 skills
/plugin marketplace list

# 3. 安装特定 skill
/plugin install react-component-generator

# 4. 或安装多个 skills
/plugin install feature-builder code-review ui-analyzer
```

### 方式 2: 手动安装

将整个仓库克隆到本地，然后将 `skills/`、`commands/`、`hooks/` 目录复制到你的项目中。

## 包含的 Skills (15 个)

### 前端开发类 (5 个)

#### 1. **react-component-generator**
生成遵循最佳实践的 React 组件，支持 TypeScript、Tailwind CSS 和 Zustand 状态管理。

**关键词**: `react`, `typescript`, `tailwind`, `component`, `zustand`

#### 2. **feature-builder**
构建完整的 React 功能，包含 UI 组件、业务逻辑、API 集成和状态管理的分层架构。

**关键词**: `react`, `feature`, `architecture`, `api`, `state-management`
**依赖**: `react-component-generator`

#### 3. **code-review**
前端代码审查工具，分析代码质量、安全漏洞、性能问题、无障碍性和最佳实践。

**关键词**: `code-review`, `security`, `performance`, `accessibility`, `react`

#### 4. **ui-analyzer**
分析 UI 设计截图并生成 React 组件（TypeScript + Tailwind CSS）。

**关键词**: `ui`, `design`, `screenshot`, `analysis`, `react`
**依赖**: `react-component-generator`

#### 5. **figma-ui-analyzer**
专业的 Figma 设计稿分析工具，通过 Figma MCP 获取设计信息，提供详细的 UI 还原开发思路。

**关键词**: `figma`, `ui`, `design`, `mcp`, `react`
**依赖**: `react-component-generator`

### 辅助工具类 (3 个)

#### 6. **request-analyzer**
主动分析用户请求，确定任务类型，评估提示词质量，智能推荐激活哪些 skills。

**关键词**: `analyzer`, `coordinator`, `prompt`, `workflow`, `automation`

#### 7. **prompt-optimizer**
使用交互式问卷或直接分析来优化用户提示词的清晰度、具体性和完整性。

**关键词**: `prompt`, `optimization`, `clarity`, `interactive`, `questionnaire`

#### 8. **skill-creator**
创建有效 skills 的指南，扩展 Claude 的能力，支持专业知识、工作流程或工具集成。

**关键词**: `skill`, `creator`, `guide`, `development`, `tools`

### 内容创作类 (5 个)

#### 9. **tech-article-writer**
技术干货文章创作专家，擅长用简练语言传递核心知识点，不遗漏关键信息。

**关键词**: `article`, `writing`, `technical`, `content`, `documentation`

#### 10. **wechat-article-writer**
专业的微信公众号文章创作助手，支持通过搜索工具丰富内容、优化标题、调整语气为官方文案风格。

**关键词**: `wechat`, `article`, `writing`, `content`, `social-media`

#### 11. **md-to-wechat**
将 Markdown 文档转换为适合微信公众号的美观 HTML 格式，支持标题、代码块、引用块、列表、表格等。

**关键词**: `markdown`, `wechat`, `html`, `converter`, `formatting`

#### 12. **wechat-md-formatter**
微信公众号 Markdown 智能排版专家，将各种格式的文本内容优化为适合公众号阅读的 Markdown 格式。

**关键词**: `wechat`, `markdown`, `formatting`, `optimization`, `typography`

#### 13. **product-manager**
资深产品经理助手，提供专业的 PRD 文档评审和创作服务，涵盖需求分析、用户价值、技术可行性、商业目标等。

**关键词**: `product`, `prd`, `requirements`, `analysis`, `documentation`

### 其他工具类 (2 个)

#### 14. **git-helper**
智能 Git 操作助手，自动处理代码提交、生成符合 Conventional Commits 规范的 commit message。

**关键词**: `git`, `commit`, `conventional-commits`, `automation`, `version-control`

#### 15. **x-article-fetcher**
从 X (Twitter) 获取文章内容的专业工具，使用 Playwright MCP 自动访问 X 文章链接，提取完整内容。

**关键词**: `x`, `twitter`, `article`, `fetcher`, `mcp`, `playwright`

## 技术栈

### 核心框架
- **React 18+** + TypeScript + Next.js (App Router)
- **Tailwind CSS** + **Zustand** + **React Query** + **Zod**

### 代码规范
- 函数式组件 + Hooks
- TypeScript 严格模式
- ESLint + Prettier

## 额外功能

### Commands (斜杠命令)
- `/dev-docs` - 创建包含结构化任务分解的综合战略计划
- `/dev-docs-update` - 在上下文压缩前更新开发文档

### Hooks
- **PreCompact Hook** - 上下文压缩前自动保存开发文档

## 文档

- **CLAUDE.md** - 项目级配置和工作指南
- **CONTRIBUTING.md** - 贡献指南
- **CHANGELOG.md** - 版本历史

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 作者

**lzdFeiFei** - [GitHub](https://github.com/lzdFeiFei)

## 问题反馈

如有问题或建议，请在 [Issues](https://github.com/lzdFeiFei/my-claude-code-marketplace/issues) 中提出。

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。
