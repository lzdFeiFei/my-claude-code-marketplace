# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-14

### Added

#### 🎉 Marketplace 支持
- 添加 `.claude-plugin/` 配置目录
- 创建 `plugin.json` 主配置文件，包含所有 15 个 skills 的完整元数据
- 生成 `marketplace.json` 清单文件
- 支持标准 marketplace 安装流程：`/plugin marketplace add lzdFeiFei/my-claude-code-marketplace`

#### 📁 目录重组
- 将 skills 从 `.claude/skills/` 移动到根目录 `skills/`
- 将 commands 从 `.claude/commands/` 移动到根目录 `commands/`
- 将 hooks 从 `.claude/hooks.json` 重组为 `hooks/pre-compact.json`
- 创建 `.backup/` 目录保存原有结构

#### 📝 Skills 元数据
- 为所有 15 个 skills 定义版本号（1.0.0）
- 为每个 skill 生成 3-6 个关键词
- 定义 skills 之间的依赖关系：
  - `feature-builder` 依赖 `react-component-generator`
  - `ui-analyzer` 依赖 `react-component-generator`
  - `figma-ui-analyzer` 依赖 `react-component-generator`

#### 🔧 Skills 修复
- 为 `x-article-fetcher` 添加完整的 frontmatter
- 为 `wechat-md-formatter` 添加完整的 frontmatter
- 为 `figma-ui-analyzer` 添加完整的 frontmatter
- 统一所有 SKILL.md 文件格式

#### 📚 文档更新
- 更新 `README.md`，添加 marketplace 安装说明和所有 15 个 skills 的完整列表
- 添加徽章（License、Version、Skills 数量）
- 创建 `CONTRIBUTING.md` 贡献指南
- 创建 `CHANGELOG.md` 版本历史
- 添加 `CODEOWNERS` 文件
- 添加 `LICENSE` 文件（MIT）

#### 🎯 Skills 列表（15 个）

**前端开发类 (5 个)**:
1. `react-component-generator` - React 组件生成器
2. `feature-builder` - 完整功能构建器
3. `code-review` - 前端代码审查工具
4. `ui-analyzer` - UI 设计稿分析器
5. `figma-ui-analyzer` - Figma 设计稿分析工具

**辅助工具类 (3 个)**:
6. `request-analyzer` - 智能请求分析器
7. `prompt-optimizer` - 提示词优化器
8. `skill-creator` - Skill 创建工具

**内容创作类 (5 个)**:
9. `tech-article-writer` - 技术文章写作助手
10. `wechat-article-writer` - 微信公众号文章创作助手
11. `md-to-wechat` - Markdown 转微信 HTML
12. `wechat-md-formatter` - 微信 Markdown 排版专家
13. `product-manager` - 产品经理助手

**其他工具类 (2 个)**:
14. `git-helper` - Git 智能提交助手
15. `x-article-fetcher` - X (Twitter) 文章抓取工具

### Changed

- 目录结构从 `.claude/` 迁移到标准 marketplace 结构
- Skills 路径从 `.claude/skills/` 更新为 `skills/`
- Commands 路径从 `.claude/commands/` 更新为 `commands/`
- Hooks 配置从 `.claude/hooks.json` 更新为 `hooks/pre-compact.json`

### Breaking Changes

⚠️ **重要**: 此版本包含破坏性变更

- 旧的安装方式（复制 `.claude/` 目录）不再推荐
- 建议使用新的 marketplace 安装方式
- 如果您已经在使用旧结构，请参考迁移指南

### Migration Guide

#### 从旧结构迁移到新结构

**方式 1: 使用 Marketplace 安装（推荐）**

```bash
# 1. 卸载旧的 skills（如果有）
# 删除项目中的 .claude/skills/ 目录

# 2. 添加 marketplace
/plugin marketplace add lzdFeiFei/my-claude-code-marketplace

# 3. 安装需要的 skills
/plugin install react-component-generator feature-builder code-review
```

**方式 2: 手动迁移**

```bash
# 1. 备份现有配置
cp -r .claude .claude.backup

# 2. 克隆新版本
git clone https://github.com/lzdFeiFei/my-claude-code-marketplace.git

# 3. 复制新结构
cp -r my-claude-code-marketplace/skills ./
cp -r my-claude-code-marketplace/commands ./
cp -r my-claude-code-marketplace/hooks ./

# 4. 删除旧的 .claude/skills/ 和 .claude/commands/
rm -rf .claude/skills
rm -rf .claude/commands
```

## [Unreleased]

### Added

#### 🤖 新增工作流自动化
- **x-to-wechat-agent** - X文章转公众号自动化agent launcher
  - 轻量级launcher (~1KB)，不占用主agent上下文
  - 启动独立subagent完成：爬取 → 翻译 → 排版 → 生成HTML
  - Subagent在隔离上下文中自主执行全流程
  - 支持并行处理多个文章
  - 支持自定义翻译和排版风格
  - 完整的错误处理和质量验证
  - 依赖: x-article-fetcher, en-to-zh-translator, wechat-md-formatter, md-to-wechat

#### 🌐 新增翻译工具
- **en-to-zh-translator** - 专业的英文到中文翻译 skill
  - 智能识别内容类型（技术文档、学术论文、新闻等）
  - 完整保留 Markdown 格式和代码块
  - 自动应用相应翻译风格
  - 支持文件路径和直接文本输入
  - 生成带 `-zh` 后缀的翻译文件
  - 内置技术术语对照表（600+ 术语）
  - 包含详细的翻译指南文档

### Changed

- 更新 README.md，skill 数量从 15 个增加到 17 个
- 新增分类 "工作流自动化类"
- 更新 "其他工具类" 从 2 个增加到 3 个
- 添加 `workflow`, `automation`, `pipeline` 关键词

### Planned

- 添加更多前端开发 skills
- 支持 skill 套件（suites）
- 添加自动化测试
- 改进文档和示例

---

## 版本说明

### 版本号格式

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：`MAJOR.MINOR.PATCH`

- **MAJOR**: 破坏性变更
- **MINOR**: 新增功能（向后兼容）
- **PATCH**: Bug 修复

### 变更类型

- `Added` - 新增功能
- `Changed` - 功能变更
- `Deprecated` - 即将废弃的功能
- `Removed` - 已移除的功能
- `Fixed` - Bug 修复
- `Security` - 安全相关

---

[1.0.0]: https://github.com/lzdFeiFei/my-claude-code-marketplace/releases/tag/v1.0.0
