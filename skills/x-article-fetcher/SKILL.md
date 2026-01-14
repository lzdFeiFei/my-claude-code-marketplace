---
name: x-article-fetcher
description: 从 X (Twitter) 获取文章内容的专业工具。使用 Playwright MCP 自动访问 X 文章链接，提取完整内容（标题、作者、正文），并可选保存为 Markdown 文件。适用于获取推特长文、分析 X 文章、保存文章内容等场景。
allowed-tools: mcp__playwright__browser_navigate, mcp__playwright__browser_wait_for, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_evaluate, Write, AskUserQuestion
---

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

### 步骤 4: 提取文章内容（优化版）⚡

**推荐方式**：使用 `mcp__playwright__browser_evaluate` 精确提取内容，避免内存溢出。

```javascript
const articleData = await browser_evaluate({
  function: `() => {
    // 提取文章主体
    const article = document.querySelector('article');

    // 提取标题
    const title = document.querySelector('h1')?.innerText ||
                  document.querySelector('[data-testid="tweetText"] h2')?.innerText ||
                  '无标题';

    // 提取作者信息
    const authorName = document.querySelector('[data-testid="User-Name"]')?.innerText || '';
    const authorHandle = document.querySelector('[data-testid="User-ScreenName"]')?.innerText || '';

    // 提取发布时间
    const publishDate = document.querySelector('time')?.getAttribute('datetime') || '';

    // 提取文章正文（所有段落）
    const contentElements = article?.querySelectorAll('p, h1, h2, h3, ul, ol') || [];
    const content = Array.from(contentElements)
      .map(el => el.innerText)
      .filter(text => text.trim().length > 0)
      .join('\n\n');

    // 提取互动数据
    const getMetric = (ariaLabel) => {
      const element = document.querySelector(\`[aria-label*="\${ariaLabel}"]\`);
      return element?.getAttribute('aria-label') || '0';
    };

    return {
      title,
      author: {
        name: authorName,
        handle: authorHandle
      },
      publishDate,
      content,
      metrics: {
        likes: getMetric('Like'),
        retweets: getMetric('Repost'),
        replies: getMetric('Reply'),
        views: getMetric('View')
      }
    };
  }`
});
```

**备用方式**：如果 evaluate 提取不完整，可以使用 `browser_snapshot`，但要注意内存使用。

### 步骤 5: 验证提取结果

检查提取的数据是否完整：
- 标题不为空
- 正文内容长度 > 100 字符
- 作者信息存在

如果数据不完整，可以：
1. 增加等待时间（步骤 3）
2. 调整 CSS 选择器
3. 使用 `browser_snapshot` 作为备用方案

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

### 步骤 8: 关闭浏览器 ⚠️ 必须执行

**关键步骤**：无论成功或失败，都必须关闭浏览器释放内存。

使用 `mcp__playwright__browser_close` 工具：

```javascript
// 在所有操作完成后
await browser_close();
```

**最佳实践**：使用 try-finally 模式确保浏览器一定会被关闭：

```
1. 开始处理
2. try {
     - 导航到文章
     - 等待加载
     - 提取内容
     - 格式化输出
   }
3. finally {
     - 关闭浏览器（无论成功或失败）
   }
```

如果不关闭浏览器，会导致：
- 内存持续占用（每个实例 500MB-2GB）
- 多次调用后内存溢出
- 系统性能下降

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

### 批量获取（内存优化版）⚡

如果用户提供多个文章链接，**必须**按以下方式处理以避免内存溢出：

#### 正确的批量处理流程

```
1. 使用 TodoWrite 创建任务列表
2. 逐个处理每篇文章（不要并发）
3. 每篇文章处理完后立即关闭浏览器
4. 可选：添加延迟避免速率限制
5. 将所有内容保存到一个汇总文件中
```

#### 实现示例

```javascript
// ✅ 正确：串行处理
const articles = [];

for (let i = 0; i < articleUrls.length; i++) {
  const url = articleUrls[i];

  try {
    // 1. 导航到文章
    await browser_navigate({ url });

    // 2. 等待加载
    await browser_wait_for({ time: 3 });

    // 3. 提取内容
    const content = await browser_evaluate({ ... });

    // 4. 保存结果
    articles.push(content);

    // 5. 更新进度
    console.log(`已完成 ${i + 1}/${articleUrls.length}`);

  } catch (error) {
    console.error(`获取失败: ${url}`, error);
  } finally {
    // 6. ⚠️ 关键：每次都关闭浏览器
    await browser_close();
  }

  // 7. 可选：添加延迟（避免速率限制）
  if (i < articleUrls.length - 1) {
    await new Promise(r => setTimeout(r, 2000)); // 等待 2 秒
  }
}

// 8. 保存汇总文件
await saveAllArticles(articles);
```

#### ❌ 错误做法

```javascript
// 错误 1：并发处理（会导致内存溢出）
const articles = await Promise.all(
  articleUrls.map(url => fetchArticle(url))
);

// 错误 2：不关闭浏览器
for (const url of articleUrls) {
  await browser_navigate({ url });
  const content = await browser_evaluate({ ... });
  // 忘记关闭浏览器！
}

// 错误 3：在循环外关闭（只关闭最后一个）
for (const url of articleUrls) {
  await browser_navigate({ url });
  const content = await browser_evaluate({ ... });
}
await browser_close(); // 太晚了！
```

#### 批量处理建议

- **小批量**（1-5 篇）：直接串行处理
- **中批量**（6-20 篇）：添加进度提示和延迟
- **大批量**（20+ 篇）：
  - 分批处理（每批 10 篇）
  - 每批之间暂停 10 秒
  - 监控内存使用
  - 考虑让用户分多次执行

### 内容分析

获取文章后，可以提供：
- 文章摘要
- 关键要点提取
- 主题分类
- 字数统计

## 示例对话

### 示例 1：单篇文章获取（优化版）

**用户:** 帮我获取这篇 X 文章的内容 https://x.com/thedankoe/article/2010751592346030461

**助手:** 我来帮你获取这篇 X 文章的内容。

```
步骤 1: 导航到文章页面
步骤 2: 等待页面加载（3秒）
步骤 3: 使用 browser_evaluate 提取内容
步骤 4: 格式化为 Markdown
步骤 5: 关闭浏览器释放内存 ✓
```

成功获取到文章！这是一篇由 Dan Koe 撰写的关于"如何在一天内修复你的整个人生"的文章...

[展示格式化的内容]

需要我将内容保存为 Markdown 文件吗？

### 示例 2：批量文章获取（内存优化）

**用户:** 帮我获取这 5 篇文章的内容：
- https://x.com/user1/article/123
- https://x.com/user2/article/456
- https://x.com/user3/article/789
- https://x.com/user4/article/101
- https://x.com/user5/article/112

**助手:** 我来帮你批量获取这 5 篇文章。为了避免内存问题，我会逐个处理并在每次完成后关闭浏览器。

```
[1/5] 正在获取第 1 篇文章...
      ✓ 提取完成，浏览器已关闭
[2/5] 正在获取第 2 篇文章...
      ✓ 提取完成，浏览器已关闭
[3/5] 正在获取第 3 篇文章...
      ✓ 提取完成，浏览器已关闭
[4/5] 正在获取第 4 篇文章...
      ✓ 提取完成，浏览器已关闭
[5/5] 正在获取第 5 篇文章...
      ✓ 提取完成，浏览器已关闭

全部完成！共获取 5 篇文章。
```

需要我将所有内容保存到一个汇总文件吗？

## 完整实现示例（生产级代码）

以下是一个完整的、内存优化的实现示例：

```javascript
// 单篇文章获取（内存优化版）
async function fetchSingleArticle(url) {
  try {
    // 1. 验证 URL
    if (!url.includes('x.com/') && !url.includes('twitter.com/')) {
      throw new Error('无效的 X 文章链接');
    }

    // 2. 导航到文章
    await browser_navigate({ url });

    // 3. 等待加载
    await browser_wait_for({ time: 3 });

    // 4. 提取内容（使用 evaluate 而非 snapshot）
    const articleData = await browser_evaluate({
      function: `() => {
        const article = document.querySelector('article');

        const title = document.querySelector('h1')?.innerText || '无标题';
        const authorName = document.querySelector('[data-testid="User-Name"]')?.innerText || '';
        const authorHandle = document.querySelector('[data-testid="User-ScreenName"]')?.innerText || '';
        const publishDate = document.querySelector('time')?.getAttribute('datetime') || '';

        const contentElements = article?.querySelectorAll('p, h1, h2, h3, ul, ol') || [];
        const content = Array.from(contentElements)
          .map(el => el.innerText)
          .filter(text => text.trim().length > 0)
          .join('\\n\\n');

        return {
          title,
          author: { name: authorName, handle: authorHandle },
          publishDate,
          content
        };
      }`
    });

    // 5. 验证数据
    if (!articleData.content || articleData.content.length < 100) {
      throw new Error('文章内容提取不完整');
    }

    // 6. 格式化为 Markdown
    const markdown = `# ${articleData.title}

**作者:** ${articleData.author.name} (${articleData.author.handle})
**发布时间:** ${articleData.publishDate}

---

${articleData.content}
`;

    return { success: true, data: markdown };

  } catch (error) {
    return { success: false, error: error.message };
  } finally {
    // ⚠️ 关键：无论成功或失败都关闭浏览器
    await browser_close();
  }
}

// 批量文章获取（内存优化版）
async function fetchMultipleArticles(urls) {
  const results = [];

  for (let i = 0; i < urls.length; i++) {
    const url = urls[i];

    console.log(`[${i + 1}/${urls.length}] 正在获取: ${url}`);

    // 获取单篇文章（内部会自动关闭浏览器）
    const result = await fetchSingleArticle(url);

    if (result.success) {
      results.push({
        url,
        content: result.data,
        status: 'success'
      });
      console.log(`✓ 第 ${i + 1} 篇完成，浏览器已关闭`);
    } else {
      results.push({
        url,
        error: result.error,
        status: 'failed'
      });
      console.log(`✗ 第 ${i + 1} 篇失败: ${result.error}`);
    }

    // 添加延迟避免速率限制
    if (i < urls.length - 1) {
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  // 生成汇总报告
  const successCount = results.filter(r => r.status === 'success').length;
  console.log(`\n完成！成功: ${successCount}/${urls.length}`);

  return results;
}

// 使用示例
const result = await fetchSingleArticle('https://x.com/user/article/123');
if (result.success) {
  console.log(result.data);
}

// 批量使用示例
const urls = [
  'https://x.com/user1/article/123',
  'https://x.com/user2/article/456'
];
const results = await fetchMultipleArticles(urls);
```

### 代码要点说明

1. **try-finally 模式** - 确保浏览器一定会被关闭
2. **数据验证** - 检查提取的内容是否完整
3. **错误处理** - 捕获并返回错误信息
4. **进度提示** - 批量处理时显示进度
5. **速率限制** - 添加延迟避免被封禁
6. **内存优化** - 每次处理后立即关闭浏览器

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

## 内存管理最佳实践 ⚠️

### 为什么需要内存管理

Playwright 浏览器实例会占用大量内存（通常 500MB-2GB），如果不正确管理会导致：
- JavaScript heap out of memory 错误
- 进程崩溃
- 系统性能下降

### 核心原则

1. **及时关闭浏览器** - 每次获取完成后立即关闭
2. **精确提取内容** - 只获取需要的数据，避免加载整个页面
3. **避免内存累积** - 批量处理时逐个处理并清理
4. **监控内存使用** - 处理大量文章时检查内存状态

### 实施要点

#### 1. 使用 browser_evaluate 替代 browser_snapshot

❌ **不推荐**（会加载整个可访问性树，数据量大）：
```javascript
// 获取整个页面快照
const snapshot = await browser_snapshot();
// 从快照中提取内容...
```

✅ **推荐**（精确提取需要的内容）：
```javascript
// 直接提取文章内容
const content = await browser_evaluate({
  function: `() => {
    const article = document.querySelector('article');
    return {
      title: document.querySelector('h1')?.innerText || '',
      author: document.querySelector('[data-testid="User-Name"]')?.innerText || '',
      content: article?.innerText || '',
      publishDate: document.querySelector('time')?.getAttribute('datetime') || ''
    };
  }`
});
```

#### 2. 必须添加浏览器关闭步骤

在获取内容后**立即**关闭浏览器：

```javascript
try {
  // 1. 导航到文章
  await browser_navigate({ url: articleUrl });

  // 2. 等待加载
  await browser_wait_for({ time: 3 });

  // 3. 提取内容
  const content = await browser_evaluate({ ... });

  // 4. 格式化输出
  const markdown = formatArticle(content);

  return markdown;
} finally {
  // ⚠️ 关键：无论成功或失败都要关闭浏览器
  await browser_close();
}
```

#### 3. 批量处理的内存优化

处理多篇文章时：

```javascript
// ✅ 正确：逐个处理，每次都关闭浏览器
for (const url of articleUrls) {
  try {
    const content = await fetchArticle(url);
    await saveArticle(content);
  } finally {
    await browser_close(); // 每次都关闭
  }

  // 可选：添加延迟避免速率限制
  await new Promise(r => setTimeout(r, 2000));
}

// ❌ 错误：一次性打开所有页面
const allContent = await Promise.all(
  articleUrls.map(url => fetchArticle(url))
); // 会导致内存溢出
```

#### 4. 内存监控（可选）

对于大批量处理，可以添加内存检查：

```javascript
// 检查内存使用
const memUsage = process.memoryUsage();
const heapUsedMB = memUsage.heapUsed / 1024 / 1024;

if (heapUsedMB > 3000) { // 超过 3GB
  console.warn(`内存使用过高: ${heapUsedMB.toFixed(2)} MB`);
  // 建议暂停处理或提示用户
}
```

### 故障排查

如果仍然遇到内存问题：

1. **增加 Node.js 堆内存限制**（临时方案）：
   ```bash
   NODE_OPTIONS="--max-old-space-size=8192" claude-code
   ```

2. **减少并发数量**：
   - 一次只处理 1-2 篇文章
   - 避免使用 Promise.all 并发处理

3. **检查浏览器是否正确关闭**：
   - 确保每次调用后都执行了 `browser_close`
   - 使用 try-finally 确保异常时也能关闭

4. **简化提取逻辑**：
   - 只提取必要的字段
   - 避免提取大量图片或媒体数据

## 未来改进

- [ ] 支持提取文章中的图片
- [ ] 支持提取评论内容
- [ ] 添加内容翻译功能
- [ ] 支持导出为 PDF 格式
- [ ] 添加文章归档功能
- [ ] 添加自动内存管理和清理机制
