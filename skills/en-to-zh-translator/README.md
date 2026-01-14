# English to Chinese Translator Skill

一个专业的英文到中文翻译skill，支持技术文档、学术论文、新闻文章等多种内容类型的高质量翻译。

## 功能特点

### ✨ 核心能力
- 🎯 **智能内容识别** - 自动识别技术文档、学术内容、新闻等类型，应用相应翻译风格
- 📝 **格式完整保留** - 保留Markdown格式、代码块、链接等结构元素
- 💻 **代码友好** - 代码块保持不翻译，技术术语标准化处理
- 📄 **多种输入方式** - 支持文件路径和直接文本输入
- 💾 **自动输出** - 生成带`-zh`后缀的新文件（如：`README.md` → `README-zh.md`）

### 📚 内容类型支持
- **技术文档** - 保留技术术语，平衡专业性和可读性
- **学术论文** - 严谨正式，保持学术规范
- **新闻资讯** - 流畅自然，符合中文表达习惯
- **混合内容** - 自动识别并采用合适风格

### 🎨 翻译质量保证
- ✅ 准确性：精确传达原文含义
- ✅ 流畅性：符合中文语言习惯，避免"翻译腔"
- ✅ 一致性：术语翻译统一，风格保持一致
- ✅ 可读性：优先考虑中文读者的理解

## 安装方法

### 方法1：直接解压（推荐）
```bash
# 解压到Claude skills目录
unzip en-to-zh-translator.zip -d ~/.claude/skills/
```

### 方法2：通过Claude Code安装
1. 将 `en-to-zh-translator.zip` 放到任意位置
2. 在Claude Code中执行：
```
安装skill：en-to-zh-translator.zip
```

## 使用方法

### 基本用法

#### 1. 翻译文件
```
翻译这个文件：D:\docs\README.md
```

```
帮我把 D:\projects\guide.md 翻译成中文
```

#### 2. 翻译直接文本
```
翻译这段话：

React is a JavaScript library for building user interfaces.
It makes it easy to create interactive UIs.
```

#### 3. 批量翻译
```
翻译以下文件：
- D:\docs\introduction.md
- D:\docs\installation.md
- D:\docs\usage.md
```

### 高级用法

#### 指定内容类型（可选）
```
翻译这个技术文档：D:\docs\api-reference.md
```

```
这是学术论文，请翻译：D:\research\paper.md
```

#### 指定翻译风格（可选）
```
翻译这个文件，使用更口语化的风格：D:\blog\article.md
```

```
翻译时保持正式语气：D:\docs\policy.md
```

## 输出示例

### 技术文档翻译

**原文 (README.md):**
```markdown
# Getting Started

To install the package, run:

```bash
npm install react-toolkit
```

This library provides hooks and utilities for React development.
```

**译文 (README-zh.md):**
```markdown
# 快速开始

要安装这个包，请运行：

```bash
npm install react-toolkit
```

这个库为React开发提供了hooks和工具函数。
```

### 混合内容翻译

**原文包含:**
- Markdown格式 ✓ 保留
- 代码块 ✓ 不翻译
- 技术术语 ✓ 标准化处理
- 链接 ✓ 保持功能

## 技术特性

### 格式处理规则

| 元素 | 处理方式 |
|------|---------|
| 标题 `#` | 翻译文本，保留标记 |
| 列表 `-`, `*`, `1.` | 翻译内容，保留结构 |
| 代码块 ` ``` ` | 完全不翻译 |
| 行内代码 `` `code` `` | 保持不变 |
| 链接 `[text](url)` | 翻译text，保留url |
| 图片 `![alt](url)` | 翻译alt，保留url |
| 表格 | 翻译内容，保留结构 |
| 加粗/斜体 | 保留格式，翻译文本 |

### 标点符号转换

自动转换为中文标点：
- 句号 `.` → `。`
- 逗号 `,` → `，`
- 问号 `?` → `？`
- 感叹号 `!` → `！`
- 冒号 `:` → `：`

代码和URL中保持不变。

### 技术术语处理

参考 `references/tech-terms.md`，包含：
- React/Vue/TypeScript 等框架术语
- API/HTTP/数据库 等后端术语
- Git/npm/Docker 等工具术语
- 前端开发、性能优化等概念术语

**处理策略：**
1. **保持原文** - 广泛认可的英文术语（如 `useState`, `API`）
2. **翻译+括号** - 重要概念首次出现（如：组件 (Component)）
3. **纯中文翻译** - 已有标准中文术语（如：函数、数组、对象）

## 质量保证

每次翻译后自动检查：
- ✓ Markdown格式完整保留
- ✓ 代码块完全未翻译
- ✓ 链接功能正常（URL未改变）
- ✓ 技术术语翻译一致
- ✓ 中文标点正确应用
- ✓ 表达自然流畅，无"翻译腔"
- ✓ 风格符合内容类型
- ✓ 原文含义和语气完整保留

## 常见问题

### Q: 如何处理专业术语？
A: skill会根据内置的术语表（tech-terms.md）自动处理。常见技术术语保持英文或使用标准中文翻译。

### Q: 代码注释会被翻译吗？
A: 代码块内的所有内容（包括注释）都保持不翻译，确保代码可直接运行。

### Q: 可以自定义翻译风格吗？
A: 可以在请求时说明偏好（如"使用更正式的语气"），skill会相应调整。

### Q: 翻译后的文件会覆盖原文件吗？
A: 不会。默认生成新文件，文件名为`原文件名-zh.扩展名`，原文件保持不变。

### Q: 支持哪些文件格式？
A: 主要支持Markdown (.md)和纯文本 (.txt)。其他格式可以尝试，但最佳体验是Markdown。

### Q: 如何保证翻译质量？
A: skill遵循"信达雅"原则，使用标准术语表，避免"翻译腔"，并进行多重质量检查。

## 示例场景

### 场景1：开源项目README翻译
```
我需要为开源项目创建中文README，请翻译：
D:\project\README.md
```

**结果:** 生成 `README-zh.md`，保留所有Badge、链接、代码示例

### 场景2：技术博客文章翻译
```
翻译这篇关于React的博客文章：
D:\blog\react-best-practices.md
```

**结果:** 自动识别为技术内容，使用专业但易读的翻译风格

### 场景3：API文档翻译
```
这是API文档，需要翻译为中文：
D:\docs\api-reference.md
```

**结果:** 保留所有API端点、参数名称，翻译说明文字

### 场景4：学术论文摘要翻译
```
请翻译这个学术论文的摘要部分（使用正式语气）：
[直接粘贴文本]
```

**结果:** 使用严谨的学术语言翻译

## 参考资源

skill内置参考文档：

### 📖 references/tech-terms.md
- 前端开发术语（React, TypeScript, Tailwind等）
- 后端和API术语
- 开发工具术语（Git, npm, Docker等）
- 软件工程概念
- 性能优化术语

### 📖 references/translation-guidelines.md
- 翻译原则（信达雅）
- 避免"翻译腔"技巧
- 不同内容类型的翻译策略
- 标点符号规则
- 质量保证清单

## 技术实现

- **引擎**: Claude Sonnet 4.5
- **格式解析**: Markdown结构识别
- **术语管理**: 标准化术语对照表
- **质量控制**: 多层次检查机制

## 反馈与改进

使用中如果遇到：
- 术语翻译不准确
- 翻译风格需要调整
- 特定领域术语需要补充

可以直接在对话中提出，skill会记住并应用到后续翻译中。

## 更新日志

### v1.0.0 (2026-01-14)
- ✨ 初始版本发布
- ✅ 支持技术文档、学术、新闻等多种内容类型
- ✅ 完整的Markdown格式保留
- ✅ 代码块智能识别不翻译
- ✅ 标准化技术术语处理
- ✅ 自动文件输出功能

---

## 许可证

MIT License

## 作者

Created for Claude Code Plugin Marketplace

---

**开始使用**: 直接在Claude Code中说"翻译这个文件：[文件路径]"即可！