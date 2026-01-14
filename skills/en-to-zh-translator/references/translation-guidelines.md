# Translation Guidelines

This document provides detailed guidelines for producing high-quality English-to-Chinese translations with natural fluency and professional accuracy.

## Core Principles

### 1. 信达雅 (Faithfulness, Expressiveness, Elegance)

**信 (Faithfulness) - Accuracy**
- Preserve the original meaning precisely
- Don't add or omit information
- Maintain technical accuracy
- Keep the author's intended message

**达 (Expressiveness) - Clarity**
- Use natural Chinese expressions
- Ensure readability and comprehension
- Adapt to Chinese linguistic patterns
- Make complex ideas accessible

**雅 (Elegance) - Style**
- Use appropriate register and tone
- Employ elegant but not archaic language
- Match the sophistication of the original
- Avoid awkward or stilted phrasing

### 2. Avoid "翻译腔" (Translation Tone)

Translation tone refers to awkward Chinese that sounds like a direct word-for-word translation from English. It's grammatically correct but unnatural to native speakers.

**Common Issues & Solutions:**

#### Issue 1: Passive Voice Overuse
English uses passive voice frequently; Chinese prefers active voice.

❌ **Translation Tone**
```
这个功能被广泛地使用在现代应用程序中。
```

✅ **Natural Chinese**
```
现代应用程序广泛使用这个功能。
```

#### Issue 2: Literal Translation of English Phrases
English idioms and phrases often don't translate literally.

❌ **Translation Tone**
```
在一天结束时，性能是最重要的。
(At the end of the day, performance is what matters.)
```

✅ **Natural Chinese**
```
归根结底，性能才是关键。
or: 最终，性能才是最重要的。
```

#### Issue 3: Over-using "的"
English uses many adjectives; Chinese can be more concise.

❌ **Translation Tone**
```
一个高度可配置的和非常灵活的框架
```

✅ **Natural Chinese**
```
高度可配置且灵活的框架
or: 可高度配置的灵活框架
```

#### Issue 4: Subject-Heavy Sentences
English emphasizes subjects; Chinese can omit them when clear from context.

❌ **Translation Tone**
```
开发者可以使用这个API。这个API提供了强大的功能。开发者会发现它很有用。
```

✅ **Natural Chinese**
```
开发者可以使用这个API，它提供了强大的功能，非常实用。
```

#### Issue 5: Literal Word Order
English and Chinese have different natural word orders.

❌ **Translation Tone**
```
我们需要认真地和仔细地考虑这个问题。
```

✅ **Natural Chinese**
```
我们需要认真仔细地考虑这个问题。
or: 这个问题需要认真考虑。
```

---

## Content-Type Specific Guidelines

### Technical Documentation

**Characteristics:**
- Clear, precise language
- Step-by-step instructions
- Mix of prose and code
- Heavy use of technical terms

**Translation Approach:**

1. **Imperative Mood for Instructions**
   ```
   Run the following command:
   → 运行以下命令：

   Make sure to install dependencies:
   → 确保安装依赖项：
   ```

2. **Keep Technical Accuracy**
   - Verify term consistency with tech-terms.md
   - Don't translate code examples
   - Preserve command-line syntax exactly

3. **Simplify Long Sentences**
   English tech docs often have complex sentences. Break them down:

   ❌ **Too Complex**
   ```
   在开始之前，确保你已经安装了Node.js版本16或更高版本，并且配置好了npm或yarn包管理器，同时确认你的系统满足所有必要的依赖要求。
   ```

   ✅ **Clear and Organized**
   ```
   开始之前，请确保：
   - 已安装Node.js 16或更高版本
   - 已配置npm或yarn包管理器
   - 系统满足所有依赖要求
   ```

4. **Version/Number Formatting**
   Keep numbers and versions in Western format:
   ```
   version 2.0 → 版本2.0
   3 parameters → 3个参数
   between 1 and 10 → 介于1到10之间
   ```

### Academic Content

**Characteristics:**
- Formal, rigorous language
- Complex sentence structures
- Citations and references
- Specialized terminology

**Translation Approach:**

1. **Maintain Formal Register**
   Use formal Chinese expressions appropriate for academic writing:
   ```
   shows → 表明、显示
   demonstrates → 证明、论证
   indicates → 指出、表示
   suggests → 暗示、提示
   ```

2. **Preserve Academic Phrasing**
   ```
   Previous research has shown that...
   → 先前的研究表明...

   This study aims to investigate...
   → 本研究旨在探讨...

   The findings suggest that...
   → 研究结果表明...
   ```

3. **Handle Citations Carefully**
   ```
   According to Smith (2020), the method is effective.
   → 根据Smith（2020）的研究，该方法是有效的。

   Note: Keep author names and years in original format
   ```

4. **Technical Terms**
   For specialized academic terms:
   - First mention: 中文 (English)
   - Subsequent mentions: 中文 only
   - Keep Latin terms: in vitro, de facto, etc.

### News and General Articles

**Characteristics:**
- Engaging, conversational tone
- Cultural references
- Idioms and metaphors
- Varied sentence structures

**Translation Approach:**

1. **Adapt Cultural References**
   Don't translate literally; find Chinese equivalents or explain:

   ```
   The project is a home run.
   ❌ 这个项目是一个本垒打。
   ✅ 这个项目大获成功。

   It's not rocket science.
   ❌ 这不是火箭科学。
   ✅ 这并不复杂。/ 这很简单。
   ```

2. **Localize Idioms**
   ```
   A blessing in disguise
   → 塞翁失马，焉知非福

   Kill two birds with one stone
   → 一举两得

   The ball is in your court
   → 现在轮到你做决定了
   ```

3. **Maintain Engagement**
   Keep the conversational and engaging tone:

   ```
   Let's dive into the details.
   → 让我们深入了解一下细节。

   Here's the thing...
   → 关键在于... / 问题是...

   You might be wondering...
   → 你可能想知道... / 也许你会疑惑...
   ```

4. **Rhetorical Questions**
   These work well in both languages:
   ```
   Why does this matter?
   → 这为什么重要？

   What can we learn from this?
   → 我们能从中学到什么？
   ```

---

## Structural Elements

### Headings and Titles

**Guidelines:**
- Keep concise and informative
- Remove articles (a, an, the) if not needed
- Use parallel structure in lists

```markdown
## Getting Started with React
→ ## React入门 / 开始使用React

### Understanding the Basics
→ ### 理解基础知识 / 基础概念

#### Common Pitfalls to Avoid
→ #### 常见陷阱 / 需要避免的常见问题
```

### Lists and Bullets

**Maintain parallel structure in Chinese:**

✅ **Good - Parallel Structure**
```
- 安装依赖
- 配置环境
- 启动服务器
```

❌ **Bad - Inconsistent**
```
- 安装依赖
- 需要配置环境
- 然后启动服务器
```

### Tables

Translate headers and content, but keep structure intact:

```markdown
| Feature | Description | Status |
|---------|-------------|--------|
| Dark Mode | Theme support | Active |

→

| 功能 | 描述 | 状态 |
|---------|-------------|--------|
| 深色模式 | 主题支持 | 启用 |
```

### Code Comments

**Decision Matrix:**

| Type | Translate? | Example |
|------|-----------|---------|
| Inline code comments | Optional* | `// 获取用户数据` vs `// Get user data` |
| Documentation comments | Yes | JSDoc → Chinese |
| TODO comments | Yes | `// TODO: 修复此bug` |
| Code itself | Never | Variable names stay English |

*For inline comments: Translate if it helps Chinese readers understand the code logic; keep English if it's obvious or part of standard practice.

---

## Punctuation Rules

### Chinese Punctuation Standards

#### Full-Width vs Half-Width

**Use Full-Width (全角) for:**
- Period: 。
- Comma: ，
- Question mark: ？
- Exclamation: ！
- Colon: ：
- Semicolon: ；
- Quotes: ""「」
- Parentheses in Chinese text: （）
- Em dash: ——

**Use Half-Width (半角) for:**
- Numbers: 123 (not 123)
- English letters: ABC (not ABC)
- Code and technical terms: `useState`
- URLs and paths: `/api/users`
- Parentheses around English: (example)
- In code blocks: everything

#### Specific Rules

**Periods**
```
The function returns a value.
→ 该函数返回一个值。
(Chinese period, not English period)
```

**Commas in Lists**
```
red, blue, and green
→ 红色、蓝色和绿色
(Chinese 、 for lists, not comma)
```

**Quotes**
```
The "Hello World" program
→ "Hello World"程序
or: 「Hello World」程序
(Full-width quotes)
```

**Colons**
```
Example: This is an example.
→ 示例：这是一个示例。
(Chinese colon followed by no space)
```

**Numbers and Units**
```
It costs $100.
→ 它的价格是100美元。
(Half-width number, no space before unit)

Version 2.0
→ 版本2.0
(Half-width numbers)
```

**Mixed Chinese-English**
```
使用React框架
(No space between Chinese and English)

React框架很流行
(No space)

但是，当English phrase较长时，可以考虑添加空格以提高可读性：
使用 React Server Components 可以提高性能
```

---

## Advanced Techniques

### 1. Sentence Restructuring

Sometimes Chinese requires different sentence structure for naturalness:

**Example 1: Subject Change**
```
English: The framework makes building apps easy.
Direct: 框架使构建应用变得容易。
Better: 使用这个框架，构建应用变得容易。
Best: 这个框架让应用构建变得简单。
```

**Example 2: Emphasis Shift**
```
English: Performance is critical for user experience.
Direct: 性能对用户体验是关键的。
Better: 对于用户体验来说，性能至关重要。
```

**Example 3: Topic-Comment Structure**
Chinese often uses topic-comment structure:
```
English: We need to consider security carefully.
Natural Chinese: 安全问题，我们需要仔细考虑。
(Topic first: 安全问题)
```

### 2. Handling Ambiguity

When English terms are ambiguous:

**Strategy A: Context-Based Translation**
```
"state" in React context → state (keep English)
"state" in general explanation → 状态
"the component's state" → 组件的state / 组件状态
```

**Strategy B: Provide Both**
```
First mention: 状态 (state)
Later: Use whichever feels more natural in context
```

**Strategy C: Ask for Clarification**
If critical and unclear, note: "译者注：此处'state'可能指..."

### 3. Preserving Tone and Voice

**Formal vs Informal:**

| English | Formal Chinese | Informal Chinese |
|---------|---------------|------------------|
| You can... | 您可以... / 可以... | 你可以... |
| Let's start | 让我们开始 | 咱们开始吧 |
| This is great | 这很出色 | 这太棒了 |

**Technical vs Conversational:**

Maintain the original tone level:
```
Formal doc: "Execute the command"
→ 执行命令

Tutorial: "Let's run the command"
→ 让我们运行这个命令
```

### 4. Handling Nested Structures

English often uses nested clauses; Chinese prefers shorter sentences:

❌ **Too Nested**
```
这个在2020年发布的、用于构建用户界面的、基于组件的框架已经被全世界数百万开发者采用。
```

✅ **Broken Down**
```
这个基于组件的框架用于构建用户界面，于2020年发布。目前，全球已有数百万开发者采用。
```

Or:
```
这个框架于2020年发布，用于构建基于组件的用户界面，已被全球数百万开发者采用。
```

---

## Quality Assurance

### Self-Review Checklist

Before submitting translation, ask:

**Accuracy**
- [ ] Is the meaning exactly preserved?
- [ ] Are technical terms translated correctly?
- [ ] Are numbers, dates, and names accurate?
- [ ] Have I verified ambiguous terms?

**Fluency**
- [ ] Does it sound natural to a native Chinese speaker?
- [ ] Have I avoided "翻译腔"?
- [ ] Is sentence structure appropriate for Chinese?
- [ ] Would a Chinese developer/reader understand this easily?

**Consistency**
- [ ] Are terms translated consistently throughout?
- [ ] Is the tone consistent with the original?
- [ ] Have I checked against tech-terms.md?
- [ ] Are similar sentences translated similarly?

**Format**
- [ ] Is Markdown structure preserved?
- [ ] Are code blocks untouched?
- [ ] Is punctuation correct (full-width/half-width)?
- [ ] Are links functional?

**Readability**
- [ ] Can the target audience understand this?
- [ ] Have I broken down overly complex sentences?
- [ ] Is the information hierarchy clear?
- [ ] Are there any awkward phrasings?

### Common Pitfalls to Avoid

1. **Over-translating**: Not everything needs translation (code, brands, established terms)
2. **Under-translating**: Don't leave too much English in prose sections
3. **Inconsistency**: Same term translated differently in different places
4. **Cultural blindness**: Missing cultural references that need adaptation
5. **Tone mismatch**: Formal translation of casual content or vice versa
6. **Grammar errors**: Chinese grammar mistakes due to English influence
7. **Punctuation errors**: Mixing full-width and half-width inappropriately

---

## Special Cases

### Abbreviations

**Keep original + explanation when first mentioned:**
```
API (Application Programming Interface)
→ API（应用程序编程接口）

Then use: API in later mentions
```

**Common abbreviations can be kept:**
```
HTML, CSS, JS, SQL, etc. → Keep as-is
```

### Proper Nouns

**Company names**: Keep original
```
Microsoft, Google, Apple → unchanged
```

**Product names**: Keep original
```
iPhone, Windows, Chrome → unchanged
```

**People names**: Keep original in Latin alphabet
```
Linus Torvalds → Linus Torvalds
```

### URLs and File Paths

**Never translate:**
```
/src/components/Button.tsx → unchanged
https://example.com/docs → unchanged
filename.config.js → unchanged
```

**But translate surrounding text:**
```
See the /docs folder for more information.
→ 更多信息请参考/docs文件夹。
```

### Version Numbers and Dates

**Keep Western format:**
```
Version 1.2.3 → 版本1.2.3
Released on Jan 15, 2024 → 发布于2024年1月15日
```

### Mathematical and Scientific Notation

**Keep original notation:**
```
x + y = z → x + y = z
E = mc² → E = mc²
p < 0.05 → p < 0.05
```

---

## Continuous Improvement

### Gathering Feedback

After delivering translations, note:
- Terms that users want translated differently
- Style preferences for future translations
- Domain-specific vocabulary to add to tech-terms.md

### Staying Updated

- Check official Chinese documentation for new terminology
- Monitor Chinese developer communities for emerging terms
- Update tech-terms.md with new conventions
- Adapt to evolving Chinese tech language

---

## Resources

### Official Documentation (Chinese)
- [React 中文文档](https://react.dev/zh-hans)
- [Vue.js 中文文档](https://cn.vuejs.org/)
- [MDN Web 文档](https://developer.mozilla.org/zh-CN/)

### Style Guides
- 《现代汉语词典》for standard usage
- 《中国翻译》journal for translation theory
- Chinese tech company style guides (Alibaba, Tencent)

### Community Resources
- SegmentFault (Chinese Stack Overflow)
- Zhihu tech topics
- Chinese GitHub trending repositories

---

**Remember**: Great translation is invisible. The reader should feel like they're reading original Chinese content, not a translation. Aim for naturalness, clarity, and accuracy in equal measure.