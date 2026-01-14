# Figma UI Analyzer Skill

**Version**: 1.0.0
**Author**: Claude Code
**Last Updated**: 2025-01-14

---

## 概述

专业的 Figma 设计稿分析工具，通过 Figma MCP 获取设计信息，提供详细的 UI 还原开发思路和实现方案。

---

## 核心功能

### 1. 设计稿分析
- 调用 Figma MCP 获取设计节点信息
- 提取布局结构、组件层级、样式属性
- 识别设计模式和组件类型

### 2. 开发思路输出
- 组件拆分建议（原子组件 → 复合组件）
- 布局方案（Flexbox/Grid）
- 响应式策略
- 状态管理建议

### 3. 技术栈映射
- React 组件结构
- Tailwind CSS 类名
- TypeScript 类型定义
- shadcn/ui 组件推荐

---

## 使用场景

### 触发条件
用户提供以下任一信息时激活：
- Figma 设计稿 URL
- Figma 文件 key + 节点 ID
- 明确要求"分析 Figma 设计"、"还原 UI 设计"

### 典型用例
```
用户: "分析这个 Figma 设计稿 https://figma.com/design/abc123/..."
用户: "给出这个 UI 的开发思路"
用户: "如何还原这个设计"
```

---

## 工作流程

### 阶段 1: 信息提取
1. 解析 Figma URL 或接收 fileKey/nodeId
2. 调用 `mcp__figma__get_design_context` 获取设计上下文
3. 调用 `mcp__figma__get_screenshot` 获取设计截图
4. 调用 `mcp__figma__get_metadata` 获取节点元数据（如需要）

### 阶段 2: 设计分析
1. **布局分析**
   - 识别容器类型（Frame/Group/Section）
   - 分析布局方式（Auto Layout/Absolute）
   - 提取间距、对齐、尺寸信息

2. **组件识别**
   - 识别 UI 组件类型（Button/Input/Card/Modal 等）
   - 分析组���状态（hover/active/disabled）
   - 识别可复用组件

3. **样式提取**
   - 颜色（填充、边框、阴影）
   - 字体（family/size/weight/line-height）
   - 圆角、间距、尺寸
   - 特效（阴影、模糊、渐变）

4. **交互分析**
   - 识别交互元素
   - 分析状态变化
   - 提取动画效果

### 阶段 3: 开发思路输出

#### 3.1 组件拆分方案
```markdown
## 组件层级结构

### 页面级组件
- `ProductListPage` - 主页面容器

### 功能组件
- `ProductGrid` - 产品网格布局
- `ProductCard` - 单个产品卡片
- `ProductFilter` - 筛选器

### 原子组件
- `Button` - 按钮（shadcn/ui）
- `Badge` - 标签（shadcn/ui）
- `Image` - 图片容器
```

#### 3.2 布局方案
```markdown
## 布局实现

### 整体布局
- 使用 CSS Grid 实现响应式网格
- 列数：`grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4`
- 间距：`gap-6`

### 卡片布局
- Flexbox 垂直布局：`flex flex-col`
- 图片区域：固定高宽比 `aspect-square`
- 内容区域：`flex-1` 自适应
```

#### 3.3 样式映射
```markdown
## Tailwind CSS 类名映射

### 颜色
- 主色：`bg-primary` (#3B82F6)
- 文本：`text-foreground` (#1F2937)
- 边框：`border-border` (#E5E7EB)

### 字体
- 标题：`text-xl font-semibold`
- 正文：`text-sm text-muted-foreground`
- 价格：`text-lg font-bold text-primary`

### 间距
- 卡片内边距：`p-4`
- 元素间距：`space-y-2`
```

#### 3.4 技术实现建议
```markdown
## 技术栈选择

### 组件库
- 使用 shadcn/ui 的 `Card`, `Button`, `Badge`
- 自定义 `ProductCard` 组件

### 状态管理
- 产品列表：React Query (`useQuery`)
- 筛选状态：Zustand store
- 本地 UI 状态：`useState`

### 性能优化
- 图片懒加载：`loading="lazy"`
- 虚拟滚动：`react-window`（如列表很长）
- 骨架屏：`Skeleton` 组件
```

#### 3.5 响应式策略
```markdown
## 响应式设计

### 断点
- Mobile: < 768px - 1 列
- Tablet: 768px - 1024px - 2 列
- Desktop: 1024px - 1440px - 3 列
- Large: > 1440px - 4 列

### 适配要点
- 图片：保持宽高比，使用 `object-cover`
- 文本：移动端减小字号
- 间距：移动端减小 padding/gap
```

### 阶段 4: 代码示例（可选）
如果用户需要，提供关键组件的代码示例：
```tsx
// ProductCard.tsx 示例
interface ProductCardProps {
  product: {
    id: string;
    name: string;
    price: number;
    image: string;
    badge?: string;
  };
}

export function ProductCard({ product }: ProductCardProps) {
  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow">
      <div className="aspect-square relative">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-full object-cover"
        />
        {product.badge && (
          <Badge className="absolute top-2 right-2">
            {product.badge}
          </Badge>
        )}
      </div>
      <CardContent className="p-4 space-y-2">
        <h3 className="text-lg font-semibold line-clamp-2">
          {product.name}
        </h3>
        <p className="text-xl font-bold text-primary">
          ${product.price}
        </p>
        <Button className="w-full">Add to Cart</Button>
      </CardContent>
    </Card>
  );
}
```

---

## 输出格式

### 标准输出结构
```markdown
# [设计名称] UI 还原开发思路

## 1. 设计概览
- 设计类型：[页面/组件/模块]
- 复杂度：[简单/中等/复杂]
- 预估工作量：[X 小时/天]

## 2. 设计分析
### 2.1 布局结构
[布局分析内容]

### 2.2 组件识别
[组件列表和说明]

### 2.3 样式特征
[颜色、字体、间距等]

## 3. 开发方案
### 3.1 组件拆分
[组件层级结构]

### 3.2 技术选型
[技术栈和工具]

### 3.3 实现步骤
1. [步骤 1]
2. [步骤 2]
...

## 4. 关键实现点
### 4.1 布局实现
[Tailwind 类名和布局方案]

### 4.2 响应式处理
[断点和适配策略]

### 4.3 性能优化
[优化建议]

## 5. 潜在挑战
- [挑战 1 及解决方案]
- [挑战 2 及解决方案]

## 6. 下一步行动
- [ ] [任务 1]
- [ ] [任务 2]
```

---

## Figma MCP 工具使用

### 主要工具

#### 1. `mcp__figma__get_design_context`
**用途**: 获取设计节点的完整上下文和代码
```typescript
{
  nodeId: "1:2",           // 从 URL 提取
  fileKey: "abc123",       // 从 URL 提取
  clientFrameworks: "react",
  clientLanguages: "typescript"
}
```

#### 2. `mcp__figma__get_screenshot`
**用途**: 获取设计节点的截图
```typescript
{
  nodeId: "1:2",
  fileKey: "abc123",
  clientFrameworks: "react",
  clientLanguages: "typescript"
}
```

#### 3. `mcp__figma__get_metadata`
**用途**: 获取节点元数据（结构概览）
```typescript
{
  nodeId: "1:2",
  fileKey: "abc123",
  clientFrameworks: "react",
  clientLanguages: "typescript"
}
```

#### 4. `mcp__figma__get_variable_defs`
**用途**: 获取设计变量定义（颜色、字体等）
```typescript
{
  nodeId: "1:2",
  fileKey: "abc123"
}
```

### URL 解析规则
```
输入: https://figma.com/design/abc123/FileName?node-id=1-2
提取:
- fileKey: "abc123"
- nodeId: "1:2" (注意：1-2 转换为 1:2)
```

---

## 最佳实践

### 1. 分析顺序
1. 先获取截图（视觉理解）
2. 再获取设计上下文（详细信息）
3. 最后获取元数据（结构验证）

### 2. 组件识别策略
- 优先识别 shadcn/ui 可用组件
- 识别可复用的自定义组件
- 标注需要从零实现的组件

### 3. 响应式分析
- 检查设计稿是否有多尺寸版本
- 如果只有一个尺寸，推断其他断点的适配方案
- 明确标注推断的部分

### 4. 性能考虑
- 大列表 → 虚拟滚动
- 大图片 → 懒加载 + 压缩
- 复杂动画 → CSS 优先，必要时用 JS

---

## 注意事项

### ⚠️ 限制
- Figma MCP 需要用户已登录 Figma
- 需要有设计文件的访问权限
- 某些私有文件可能无法访问

### ⚠️ 错误处理
- URL 解析失败 → 提示用户提供正确格式
- 权限不足 → 提示检查 Figma 登录状态
- 节点不存在 → 提示检查 nodeId 是否正确

### ⚠️ 不要做的事
- ❌ 不要直接生成完整代码（除非用户明确要求）
- ❌ 不要假设设计意图（基于实际数据分析）
- ❌ 不要忽略响应式需求
- ❌ 不要推荐项目外的技术栈

---

## 与其他 Skills 的协作

### 配合 `react-component-generator`
分析完成后，如果用户要求生成代码：
```
用户: "根据这个分析生成 ProductCard 组件"
→ 调用 react-component-generator
```

### 配合 `feature-builder`
如果是完整功能（多组件 + 逻辑 + API）：
```
用户: "实现这个产品列表页面"
→ 调用 feature-builder
```

### 配合 `ui-analyzer`
如果用户提供的是截图而非 Figma 链接：
```
用户: "分析这个截图"
→ 调用 ui-analyzer（基于图像分析）
```

---

## 示例对话

### 示例 1: 完整分析
```
用户: "分析这个 Figma 设计 https://figma.com/design/abc123/ProductPage?node-id=1-2"

Claude:
1. 调用 mcp__figma__get_screenshot 获取截图
2. 调用 mcp__figma__get_design_context 获取设计上下文
3. 输出完整的开发思路文档
```

### 示例 2: 快速建议
```
用户: "这个设计用什么布局方案？[Figma URL]"

Claude:
1. 调用 mcp__figma__get_metadata 快速获取结构
2. 分析布局类型
3. 给出 Tailwind 布局方案
```

### 示例 3: 组件识别
```
用户: "这个设计可以用哪些 shadcn/ui 组件？[Figma URL]"

Claude:
1. 调用 mcp__figma__get_design_context
2. 识别可用的 shadcn/ui 组件
3. 列出组件清单和使用建议
```

---

## 版本历史

### v1.0.0 (2025-01-14)
- 初始版本
- 支持 Figma MCP 集成
- 提供完整的开发思路输出
- 支持组件拆分、布局方案、样式映射

---

## 相关资源

- [Figma MCP 文档](https://github.com/modelcontextprotocol/servers/tree/main/src/figma)
- [shadcn/ui 组件库](https://ui.shadcn.com/)
- [Tailwind CSS 文档](https://tailwindcss.com/)
- [React 最佳实践](https://react.dev/)
