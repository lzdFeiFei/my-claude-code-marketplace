# X Article Fetcher Skill

从 X (Twitter) 获取文章内容的专业工具。

## 何时使用此 Skill

当用户请求以下任务时使用此 skill：
- 获取 X/Twitter 上的文章内容
- 阅读推特长文
- 提取 X article 的完整文本
- 分析 X 上发布的文章
- 保存推特文章内容

## 关键词触发

- "获取 X 文章"
- "读取推特长文"
- "X article"
- "Twitter article"
- "x.com/*/article/*"

## 核心功能

此 skill 使用 Playwright MCP 工具来：
1. 自动打开浏览器访问 X 文章链接
2. 等待页面完全加载
3. 提取文章的完整内容（标题、作者、正文）
4. 可选：保存为 Markdown 文件

## 使用流程

### 步骤 1: 验证 URL 格式

检查用户提供的 URL 是否符合 X article 格式：
- `https://x.com/{username}/article/{article_id}`
- `https://twitter.com/{username}/article/{article_id}`

### 步骤 2: 使用 Playwright 导航

使用 `mcp__playwright__browser_navigate` 工具访问文章链接。

```javascript
// 导航到文章页面
await page.goto(articleUrl);
```

### 步骤 3: 等待页面加载

使用 `mcp__playwright__browser_wait_for` 等待 3-5 秒，确保内容完全加载。

```javascript
// 等待页面加载
await new Promise(f => setTimeout(f, 3000));
```

### 步骤 4: 获取页面快照

使用 `mcp__playwright__browser_snapshot` 获取页面的可访问性树快照，这比截图更适合提取文本内容。

### 步骤 5: 提取关键信息

从快照中提取：
- 文章标题
- 作者信息（用户名、显示名称）
- 发布日期
- 文章正文（所有段落、标题、列表等）
- 互动数据（点赞、转发、回复数等）

### 步骤 6: 格式化输出

将提取的内容格式化为清晰的 Markdown 格式：

```markdown
# [文章标题]

**作者:** [作者名] (@username)
**发布时间:** [日期]
**互动数据:** [点赞/转发/回复/浏览量]

---

[文章正文内容...]
```

### 步骤 7: 可选保存

询问用户是否需要将内容保存为文件。如果需要，使用 Write 工具保存为 `.md` 文件。

## 错误处理

### 常见问题及解决方案

1. **页面加载超时**
   - 增加等待时间到 5-10 秒
   - 检查网络连接

2. **需要登录**
   - X 的某些文章可能需要登录才能查看
   - 提示用户文章可能受限

3. **URL 格式错误**
   - 验证 URL 格式
   - 提供正确的 URL 格式示例

4. **内容提取不完整**
   - 使用 `browser_evaluate` 执行自定义 JavaScript 提取内容
   - 尝试滚动页面加载更多内容

## 高级功能

### 批量获取

如果用户提供多个文章链接，可以：
1. 使用 TodoWrite 创建任务列表
2. 逐个处理每篇文章
3. 将所有内容保存到一个汇总文件中

### 内容分析

获取文章后，可以提供：
- 文章摘要
- 关键要点提取
- 主题分类
- 字数统计

## 示例对话

**用户:** 帮我获取这篇 X 文章的内容 https://x.com/thedankoe/article/2010751592346030461

**助手:** 我来帮你获取这篇 X 文章的内容。

[使用 Playwright 导航并提取内容]

成功获取到文章！这是一篇由 Dan Koe 撰写的关于"如何在一天内修复你的整个人生"的文章...

[展示格式化的内容]

需要我将内容保存为 Markdown 文件吗？

## 技术细节

### 使用的 MCP 工具

- `mcp__playwright__browser_navigate` - 导航到 URL
- `mcp__playwright__browser_wait_for` - 等待加载
- `mcp__playwright__browser_snapshot` - 获取页面快照
- `mcp__playwright__browser_take_screenshot` - 可选截图
- `mcp__playwright__browser_evaluate` - 执行自定义 JS（高级）

### 数据提取策略

1. **优先使用 snapshot**：文本内容提取更准确
2. **备用 evaluate**：对于复杂布局使用 JavaScript
3. **避免 screenshot**：仅用于视觉验证，不用于文本提取

## 注意事项

1. **尊重版权**：提取的内容仅供个人学习使用
2. **速率限制**：避免短时间内大量请求
3. **隐私保护**：不要提取私密或受保护的内容
4. **内容完整性**：验证提取的内容是否完整准确

## 未来改进

- [ ] 支持提取文章中的图片
- [ ] 支持提取评论内容
- [ ] 添加内容翻译功能
- [ ] 支持导出为 PDF 格式
- [ ] 添加文章归档功能
