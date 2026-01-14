# 贡献指南

感谢您对 My Claude Code Marketplace 的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 报告问题

如果您发现 bug 或有功能建议，请：

1. 在 [Issues](https://github.com/lzdFeiFei/my-claude-code-marketplace/issues) 中搜索是否已有相关问题
2. 如果没有，创建新 Issue，并提供：
   - 清晰的标题和描述
   - 复现步骤（如果是 bug）
   - 预期行为和实际行为
   - 环境信息（Claude Code 版本、操作系统等）

### 贡献新 Skill

#### 1. Fork 仓库

```bash
git clone https://github.com/lzdFeiFei/my-claude-code-marketplace.git
cd my-claude-code-marketplace
```

#### 2. 创建新分支

```bash
git checkout -b feature/your-skill-name
```

#### 3. 创建 Skill 目录结构

```
skills/your-skill-name/
├── SKILL.md           # Skill 定义（必需）
├── references/        # 参考文档（可选）
├── assets/            # 资源文件（可选）
└── README.md          # 详细说明（可选）
```

#### 4. 编写 SKILL.md

SKILL.md 必须包含 frontmatter：

```markdown
---
name: your-skill-name
description: 简短描述（1-2 句话）
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Your Skill Name

详细的 skill 说明...

## 何时使用此 Skill

- 触发条件 1
- 触发条件 2

## 核心功能

...
```

#### 5. 更新 plugin.json

在 `.claude-plugin/plugin.json` 的 `skills` 数组中添加：

```json
{
  "id": "your-skill-name",
  "name": "Your Skill Name",
  "version": "1.0.0",
  "description": "简短描述",
  "path": "skills/your-skill-name",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "dependencies": []
}
```

#### 6. 测试 Skill

确保您的 skill：
- [ ] SKILL.md 格式正确
- [ ] Frontmatter 包含所有必需字段
- [ ] Description 清晰准确
- [ ] 功能正常工作
- [ ] 没有破坏现有 skills

#### 7. 提交 Pull Request

```bash
git add .
git commit -m "feat: add your-skill-name skill"
git push origin feature/your-skill-name
```

然后在 GitHub 上创建 Pull Request。

## Skill 开发规范

### 命名规范

- **Skill ID**: 小写字母，用连字符分隔（如 `react-component-generator`）
- **Skill Name**: 标题格式（如 `React Component Generator`）
- **文件名**: 大写（如 `SKILL.md`）

### 描述规范

- **简短描述**: 1-2 句话，说明 skill 的核心功能
- **详细说明**: 包含使用场景、触发条件、核心功能、示例等

### Keywords 规范

- 3-6 个关键词
- 使用小写字母
- 包含技术栈关键词（如 `react`, `typescript`）
- 包含功能关键词（如 `generator`, `analyzer`）

### 依赖关系

如果您的 skill 依赖其他 skills，在 `dependencies` 数组中声明：

```json
"dependencies": ["react-component-generator"]
```

## 代码规范

### TypeScript

- 使用严格模式
- 明确的类型定义
- 避免使用 `any`

### React

- 函数式组件 + Hooks
- 合理使用 `useMemo`/`useCallback`/`memo`
- 遵循 React 最佳实践

### Tailwind CSS

- Mobile-first 响应式设计
- 使用 Tailwind 变量复用样式
- 避免内联样式

## 文档规范

### SKILL.md 结构

```markdown
---
frontmatter
---

# Skill Name

## 概述

简短介绍

## 何时使用此 Skill

- 触发条件列表

## 核心功能

详细功能说明

## 使用示例

代码示例或对话示例

## 注意事项

重要提示
```

### 参考文档

如果您的 skill 包含参考文档，放在 `references/` 目录：

```
references/
├── best-practices.md
├── examples.md
└── troubleshooting.md
```

## Pull Request 流程

1. **创建 PR**: 提供清晰的标题和描述
2. **代码审查**: 维护者会审查您的代码
3. **修改反馈**: 根据反馈进行修改
4. **合并**: 审查通过后合并到主分支

## 版本管理

我们遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **MAJOR**: 破坏性变更
- **MINOR**: 新增功能（向后兼容）
- **PATCH**: Bug 修复

## 行为准则

- 尊重他人
- 建设性反馈
- 专注于技术讨论
- 保持友好和专业

## 许可证

贡献的代码将采用 MIT 许可证。

## 联系方式

如有问题，请：
- 创建 [Issue](https://github.com/lzdFeiFei/my-claude-code-marketplace/issues)
- 发送邮件至维护者

---

再次感谢您的贡献！🎉
