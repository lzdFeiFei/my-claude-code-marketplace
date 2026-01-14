# English to Chinese Translator Skill

---
name: en-to-zh-translator
description: Translate English articles and documents to Chinese with high-quality, context-aware translation. Automatically identifies content type (technical, academic, news) and applies appropriate translation style. Preserves Markdown formatting and code blocks. Supports file input and generates translated output files. Use when user requests translating English content to Chinese, mentions "翻译", "translate", or provides English text/files for translation.
---

## Purpose

This skill provides professional English-to-Chinese translation capabilities with intelligent content type recognition, format preservation, and context-aware translation quality. It handles technical documentation, academic papers, news articles, and mixed content while maintaining the original structure and meaning.

## When to Use This Skill

Activate this skill when the user:
- Explicitly requests English-to-Chinese translation
- Mentions keywords: "翻译", "translate", "中文", "Chinese"
- Provides English text or file paths for translation
- Asks to convert English documentation to Chinese
- Requests bilingual content creation

## Core Translation Principles

### 1. Content Type Recognition

Automatically identify and apply appropriate translation style:

**Technical Documentation**
- Preserve technical terms and APIs in English when appropriate
- Use standardized Chinese tech terminology (参考 `references/tech-terms.md`)
- Maintain code examples, commands, and file paths untranslated
- Balance professionalism with readability

**Academic Content**
- Use formal, rigorous language
- Preserve academic terminology and proper nouns
- Maintain citation formats and references
- Keep research methodology terms consistent

**News/General Content**
- Use fluent, natural Chinese expressions
- Prioritize readability over literal translation
- Adapt idioms and cultural references
- Maintain journalistic tone

**Mixed Content**
- Analyze each section independently
- Apply context-appropriate translation style
- Ensure consistent terminology throughout

### 2. Format Preservation

**Markdown Elements (MUST Preserve)**
- Headings: `#`, `##`, `###`, etc.
- Lists: `-`, `*`, `1.`, `2.`, etc.
- Code blocks: ` ``` ` fenced blocks
- Inline code: `` `code` ``
- Links: `[text](url)` - translate text, keep URL
- Images: `![alt](url)` - translate alt text, keep URL
- Tables: preserve structure, translate content
- Bold/Italic: `**bold**`, `*italic*`
- Blockquotes: `>` preserve marker, translate content

**Special Content (DO NOT Translate)**
- Code blocks (entire content)
- Command-line examples
- URLs and file paths
- API names and function names
- Environment variables
- Configuration keys
- Brand names (unless official Chinese name exists)

### 3. Translation Quality Standards

**Accuracy**
- Preserve original meaning and nuance
- Avoid over-translation or under-translation
- Maintain technical precision
- Verify context before translating ambiguous terms

**Fluency**
- Use natural Chinese expressions
- Avoid "翻译腔" (translation tone)
- Follow Chinese grammar and sentence structure
- Use appropriate punctuation (。，！？instead of .,!?)

**Consistency**
- Maintain consistent term translation throughout
- Keep consistent tone and style
- Preserve document hierarchy and structure
- Align with terminology in `references/tech-terms.md`

**Readability**
- Prioritize clarity and comprehension
- Use appropriate technical level for target audience
- Break long sentences when needed for Chinese readability
- Add necessary context for Chinese readers

## Workflow

### Step 1: Input Processing

**File Input (Primary Method)**
1. Read the file using Read tool
2. Detect file encoding and format
3. Parse Markdown structure if applicable
4. Identify content type and sections

**Text Input (Secondary Method)**
1. Accept direct text from user message
2. Detect format (Markdown, plain text)
3. Identify content type

### Step 2: Content Analysis

1. **Detect Content Type**
   - Scan for code blocks, technical terms → Technical
   - Check for academic keywords, citations → Academic
   - Analyze general tone and structure → News/General
   - Identify mixed content sections

2. **Identify Translation Units**
   - Separate translatable text from code/special content
   - Map Markdown structure elements
   - Mark sections requiring different translation styles

3. **Load Reference Resources**
   - If technical content: consult `references/tech-terms.md`
   - If needed: check `references/translation-guidelines.md`

### Step 3: Translation Execution

1. **Translate by Sections**
   - Process headings first (for context)
   - Translate body content paragraph by paragraph
   - Maintain original structure and formatting

2. **Apply Quality Checks**
   - Verify term consistency
   - Check format preservation
   - Ensure code blocks remain untouched
   - Validate Markdown syntax

3. **Post-Processing**
   - Review for fluency and naturalness
   - Adjust punctuation to Chinese standards
   - Verify links and references work
   - Check overall readability

### Step 4: Output Generation

**For File Input (Default)**
1. Generate new filename: `{original-name}-zh.{ext}`
   - Example: `README.md` → `README-zh.md`
   - Example: `guide.txt` → `guide-zh.txt`

2. Write translated content to new file using Write tool

3. Confirm to user:
   - Original file path
   - Translated file path
   - Word count or line count
   - Content type identified

**For Text Input**
- Display translated text directly in response
- Optionally offer to save to file if content is long

**Example Output Message**
```
✅ 翻译完成

原文件: D:\docs\README.md
译文件: D:\docs\README-zh.md
内容类型: 技术文档
原文行数: 245行
译文行数: 198行

已保留所有Markdown格式和代码块。
```

## Special Handling Rules

### Code Blocks
```python
# DO NOT translate code content
def example_function():
    return "Keep this English"
```

Translate only:
- Comments if they explain the code: `# 这是注释` (if translating comments helps Chinese readers)
- Surrounding explanation text

### Technical Terms

**Keep in English:**
- API names: `useState`, `useEffect`
- Programming languages: `JavaScript`, `Python`
- Frameworks: `React`, `Vue`
- Tools: `Git`, `npm`, `Docker`
- File formats: `JSON`, `YAML`

**Translate with Original in Parentheses (First Occurrence):**
- Component (组件)
- State Management (状态管理)
- Dependency (依赖)

**Use Standard Chinese Terms:**
- Function → 函数
- Variable → 变量
- Array → 数组
- Object → 对象

See `references/tech-terms.md` for comprehensive terminology.

### Links and References

```markdown
Original:
Read more in [Getting Started](./guide.md) section.

Translated:
更多信息请参考[快速开始](./guide.md)部分。
```

- Translate link text: "Getting Started" → "快速开始"
- Keep URL unchanged: `./guide.md`
- Translate surrounding text naturally

### Punctuation Conversion

Automatically convert:
- Period: `.` → `。`
- Comma: `,` → `，`
- Question: `?` → `？`
- Exclamation: `!` → `！`
- Colon: `:` → `：` (except in URLs, code)
- Quotes: `"text"` → `"文本"` or `「文本」`

Keep unchanged:
- In code blocks and inline code
- In URLs and file paths
- In mathematical expressions

## Error Handling

### Missing or Inaccessible Files
- Inform user clearly
- Suggest checking file path
- Offer to translate direct text input instead

### Ambiguous Content
- Note uncertainty in translation
- Provide alternative translations if applicable
- Ask user for clarification if critical

### Large Files
- Process in chunks if needed
- Maintain context across chunks
- Ensure consistency throughout

### Encoding Issues
- Detect and handle different encodings (UTF-8, GB2312, etc.)
- Convert to UTF-8 for output
- Preserve special characters

## Quality Assurance Checklist

Before delivering translation, verify:

- [ ] All Markdown formatting preserved
- [ ] Code blocks completely untranslated
- [ ] Links functional (URLs unchanged)
- [ ] Technical terms consistent
- [ ] Chinese punctuation applied correctly
- [ ] Natural and fluent Chinese expression
- [ ] No "翻译腔" (literal translation tone)
- [ ] Appropriate style for content type
- [ ] Output file correctly named and saved
- [ ] Original meaning and nuance preserved

## Examples

### Example 1: Technical Documentation

**Input (file: installation.md)**
```markdown
# Installation Guide

To install the package, run:

```bash
npm install my-package
```

This command will download dependencies and configure your environment.
```

**Output (file: installation-zh.md)**
```markdown
# 安装指南

要安装这个包，请运行：

```bash
npm install my-package
```

此命令将下载依赖项并配置您的环境。
```

### Example 2: Academic Content

**Input**
```
The research demonstrates significant correlation between variables A and B (p < 0.05).
This finding suggests that further investigation is warranted.
```

**Output**
```
研究表明变量A和变量B之间存在显著相关性（p < 0.05）。
这一发现表明有必要进行进一步调查。
```

### Example 3: Mixed Content with Code

**Input**
```markdown
## User Authentication

Implement authentication using the `useAuth` hook:

```typescript
const { user, login, logout } = useAuth();
```

The hook returns user state and authentication methods.
```

**Output**
```markdown
## 用户认证

使用`useAuth` hook实现认证：

```typescript
const { user, login, logout } = useAuth();
```

该hook返回用户状态和认证方法。
```

## Tips for Best Results

1. **Provide Context**: If translating specialized content, mention the domain (e.g., "这是关于机器学习的技术文档")

2. **Specify Style Preference**: If you prefer specific terminology or tone, mention it upfront

3. **Batch Translation**: For multiple files, provide all file paths together for consistent terminology

4. **Review Suggestions**: After translation, review critical sections and request adjustments if needed

5. **Terminology Feedback**: If certain terms should be translated differently, let me know for future consistency

## Bundled Resources

### references/tech-terms.md
Comprehensive technical terminology reference for consistent translation of programming, framework, and tool names.

### references/translation-guidelines.md
Detailed style guidelines for different content types and advanced translation techniques.

---

**Note**: This skill prioritizes quality over speed. For long documents, translation may take time to ensure accuracy, fluency, and format preservation.