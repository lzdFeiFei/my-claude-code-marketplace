# X to WeChat Agent Launcher

---
name: x-to-wechat-agent
description: Lightweight launcher that spawns a dedicated subagent to convert X (Twitter) articles to WeChat official account articles. When user provides X article URL and wants WeChat content, this skill launches an independent agent that autonomously handles fetching, translation, formatting, and HTML generation without consuming main agent context. Use when user mentions converting X articles to WeChat, provides X URLs with publishing intent, or says "X文章转公众号".
---

## Purpose

This is a lightweight launcher skill that delegates X-to-WeChat conversion work to an independent subagent. The main agent only handles task recognition and subagent spawning - all heavy processing (fetching, translation, formatting, HTML generation) runs in the subagent's isolated context.

## When to Use This Skill

Trigger when user:
- Provides X article URL + mentions WeChat/公众号
- Says "把这个X文章转成公众号"
- Asks to convert/publish X content to WeChat
- Pattern: X URL + any WeChat-related keyword

## How It Works

```
User Request → This Skill (Launcher) → Spawn Subagent → Independent Processing
                 ↓ (lightweight)              ↓
            Task recognition           Full workflow execution
            Prompt construction       (fetch → translate → format → HTML)
            Subagent spawn                    ↓
                 ↓                      Return results
            Wait for completion ←───────────────┘
```

**Key Benefit**: Main agent only loads ~1KB of launcher logic. The subagent handles all ~50KB of workflow instructions and processing.

## Workflow

### Step 1: Detect User Intent

Check if user provided:
- ✓ X article URL (https://x.com/.../article/...)
- ✓ WeChat publishing intent (keywords: 公众号, wechat, 转换, 发布)

### Step 2: Confirm and Prepare

Brief confirmation:
```
收到！我将启动专门的agent来处理X文章转公众号的完整流程：
📥 爬取文章
🌐 翻译为中文
📱 优化排版
📄 生成HTML

预计2-3分钟完成。
```

### Step 3: Spawn Subagent

Use Task tool to launch general-purpose subagent with complete workflow instructions:

```typescript
Task tool parameters:
- subagent_type: "general-purpose"
- description: "X文章转公众号完整流程"
- prompt: [Complete workflow instructions - see below]
```

### Step 4: Return Results

When subagent completes:
```
✅ Agent任务完成！

生成的文件：
📂 ./x-pipeline-temp/
   └── wechat-final.html ⭐ (可直接复制到公众号编辑器)

[显示subagent返回的摘要信息]
```

## Subagent Prompt Template

When spawning subagent, provide this complete workflow prompt:

```
你是一个专门的X文章转公众号处理agent。用户提供了X文章链接，你需要完成完整的转换流程。

## 任务目标

将以下X文章转换为微信公众号文章：
[USER_PROVIDED_URL]

## 工作流程

你需要依次完成4个步骤，每步完成后保存中间文件。

### 步骤1：获取X文章内容

使用 `x-article-fetcher` skill 获取文章内容。

**执行**：
"使用 x-article-fetcher 获取这个X文章：[URL]"

**输出**：保存为 `./x-pipeline-temp/original-en.md`

**验证**：
- 文件存在且大小 > 1KB
- 包含标题和正文
- 内容是有意义的英文文本

如果失败：报告错误并终止

### 步骤2：翻译为中文

使用 `en-to-zh-translator` skill 翻译内容。

**执行**：
"翻译这个文件：./x-pipeline-temp/original-en.md
这是[技术/新闻/一般]类文章，请保持自然流畅"

**输出**：保存为 `./x-pipeline-temp/translated-zh.md`

**验证**：
- 文件存在
- 主要是中文内容
- Markdown格式保留完整

如果失败：重试一次，仍失败则报告错误

### 步骤3：优化公众号排版

使用 `wechat-md-formatter` skill 优化格式。

**执行**：
"优化这个译文为公众号格式：./x-pipeline-temp/translated-zh.md
针对移动端阅读优化"

**输出**：保存为 `./x-pipeline-temp/formatted-zh.md`

**验证**：
- 文件存在
- 段落长度适中
- 标题层级合理

如果失败：使用 translated-zh.md 继续（跳过此步）

### 步骤4：生成公众号HTML

使用 `md-to-wechat` skill 生成HTML。

**执行**：
"将这个Markdown转换为公众号HTML：./x-pipeline-temp/formatted-zh.md
使用简约清新的样式"

**输出**：保存为 `./x-pipeline-temp/wechat-final.html`

**验证**：
- 文件存在
- 包含完整HTML结构
- 样式正确应用

如果失败：报告错误

## 进度报告

每完成一步，向用户报告：
```
✅ 步骤 N/4 完成：[步骤名称]
```

## 最终交付

全部完成后，总结：
```
🎉 X文章转公众号完成！

📊 处理统计：
- 原文：[字数] 词
- 译文：[字数] 字
- 处理时间：[时长]

📂 生成文件位置：./x-pipeline-temp/
主要文件：wechat-final.html ⭐

💡 使用方法：
1. 打开 wechat-final.html
2. 复制内容到微信公众号编辑器
3. 预览、发布
```

## 错误处理

如果任何步骤失败：
1. 报告具体错误
2. 说明已完成的步骤
3. 提供中间文件路径（供手动继续）

## 依赖Skills

确保以下skills可用：
- x-article-fetcher
- en-to-zh-translator
- wechat-md-formatter
- md-to-wechat

如果缺少任何skill，报告并提供安装指导。

## 自定义选项

用户可能指定：
- 翻译风格：正式/轻松/技术
- 排版样式：极简/现代/科技
- 其他偏好

注意识别并应用这些偏好。

---

现在开始执行任务！
```

## Custom Options Support

If user specifies preferences, inject into subagent prompt:

**Translation style**:
```
用户要求：使用[正式/轻松/技术]的翻译风格
在步骤2翻译时应用此风格
```

**Formatting style**:
```
用户要求：使用[极简/现代/科技]排版样式
在步骤4生成HTML时应用此样式
```

## Example Usage

### Example 1: Basic

**User**:
```
把这个X文章转成公众号：
https://x.com/dan_abramov/article/1234567890
```

**Launcher (This Skill)**:
```
收到！启动专门的agent处理...
[Spawns subagent with workflow prompt]
```

**Subagent** (runs independently):
```
步骤1：获取文章... ✅
步骤2：翻译... ✅
步骤3：优化排版... ✅
步骤4：生成HTML... ✅
完成！
```

**Launcher reports back**:
```
✅ 转换完成！文件已生成...
```

### Example 2: With Custom Style

**User**:
```
转换这个X技术文章，用轻松的翻译风格：
https://x.com/example/article/123
```

**Launcher**:
```
收到！翻译风格：轻松
[Spawns subagent with custom style instruction]
```

## Benefits of Subagent Approach

### Main Agent
- ✅ Only loads ~1KB launcher logic
- ✅ Remains responsive
- ✅ Can handle other tasks
- ✅ Minimal context consumption

### Subagent
- ✅ Isolated context (doesn't affect main)
- ✅ Full access to all skills
- ✅ Can handle complex multi-step workflow
- ✅ Automatic cleanup after completion

### User Experience
- ✅ Same one-command simplicity
- ✅ Clear progress updates
- ✅ Clean final deliverable
- ✅ Better performance (parallel execution possible)

## Technical Notes

**Subagent Type**: `general-purpose`
- Has access to all tools
- Can invoke skills
- Can read/write files
- Autonomous multi-step execution

**Communication**:
- Main agent → Subagent: Via Task tool prompt
- Subagent → Main agent: Via Task tool result
- User sees: Progress from subagent, summary from main

**File Persistence**:
- Subagent creates files in `./x-pipeline-temp/`
- Files persist after subagent completes
- Main agent can access these files
- User can access final outputs

## Limitations

- Requires all 4 dependent skills installed
- Subagent runs time limited by Task tool constraints
- No direct real-time streaming (progress shown at checkpoints)

## Future Enhancements

- Batch processing (spawn multiple subagents)
- Resume from checkpoint (if subagent interrupted)
- Quality scoring and retry logic
- Direct WeChat API publishing

---

**Note**: This skill is extremely lightweight (~1KB). All heavy processing happens in the spawned subagent's isolated context.