#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to WeChat HTML Converter
将 Markdown 文档转换为适合微信公众号的美观 HTML 格式
"""

import sys
import os
import argparse
from pathlib import Path

try:
    import markdown
    from markdown.extensions import fenced_code, tables, codehilite
except ImportError:
    print("错误：缺少必需的依赖库。")
    print("请运行: pip install markdown")
    sys.exit(1)


# 简约清新风格的 CSS 样式
WECHAT_STYLE = """
<style>
    /* 全局样式 */
    #wechat-content {
        max-width: 750px;
        margin: 0 auto;
        padding: 20px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 16px;
        line-height: 1.8;
        color: #333;
        background-color: #fafafa;
    }

    /* 标题样式 */
    #wechat-content h1 {
        font-size: 28px;
        font-weight: 700;
        color: #1a1a1a;
        margin: 30px 0 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid #4A90E2;
        line-height: 1.4;
    }

    #wechat-content h2 {
        font-size: 24px;
        font-weight: 600;
        color: #2c2c2c;
        margin: 28px 0 16px;
        padding-left: 12px;
        border-left: 4px solid #4A90E2;
        line-height: 1.4;
    }

    #wechat-content h3 {
        font-size: 20px;
        font-weight: 600;
        color: #333;
        margin: 24px 0 12px;
        line-height: 1.4;
    }

    #wechat-content h4, #wechat-content h5, #wechat-content h6 {
        font-size: 18px;
        font-weight: 500;
        color: #444;
        margin: 20px 0 10px;
        line-height: 1.4;
    }

    /* 段落样式 */
    #wechat-content p {
        margin: 16px 0;
        text-align: justify;
        word-break: break-word;
    }

    /* 链接样式 */
    #wechat-content a {
        color: #4A90E2;
        text-decoration: none;
        border-bottom: 1px solid #4A90E2;
        padding-bottom: 2px;
        transition: all 0.3s ease;
    }

    #wechat-content a:hover {
        color: #357ABD;
        border-bottom-color: #357ABD;
    }

    /* 列表样式 */
    #wechat-content ul, #wechat-content ol {
        margin: 16px 0;
        padding-left: 30px;
    }

    #wechat-content li {
        margin: 8px 0;
        line-height: 1.8;
    }

    /* 引用块样式 */
    #wechat-content blockquote {
        margin: 20px 0;
        padding: 15px 20px;
        background: #f8f9fa;
        border-left: 4px solid #4A90E2;
        color: #555;
        font-style: italic;
        border-radius: 4px;
    }

    #wechat-content blockquote p {
        margin: 0;
    }

    /* 代码样式 */
    #wechat-content code {
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 14px;
        background: #f5f7fa;
        color: #e96900;
        padding: 3px 6px;
        border-radius: 3px;
        margin: 0 2px;
    }

    #wechat-content pre {
        margin: 20px 0;
        padding: 15px;
        background: #282c34;
        border-radius: 6px;
        overflow-x: auto;
        line-height: 1.6;
    }

    #wechat-content pre code {
        background: transparent;
        color: #abb2bf;
        padding: 0;
        margin: 0;
        display: block;
        font-size: 14px;
    }

    /* 表格样式 */
    #wechat-content table {
        width: 100%;
        margin: 20px 0;
        border-collapse: collapse;
        background: #fff;
        border-radius: 6px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    #wechat-content thead {
        background: #4A90E2;
        color: #fff;
    }

    #wechat-content th {
        padding: 12px 15px;
        text-align: left;
        font-weight: 600;
    }

    #wechat-content td {
        padding: 12px 15px;
        border-bottom: 1px solid #e9ecef;
    }

    #wechat-content tr:last-child td {
        border-bottom: none;
    }

    #wechat-content tbody tr:hover {
        background: #f8f9fa;
    }

    /* 水平分割线 */
    #wechat-content hr {
        margin: 30px 0;
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #ddd, transparent);
    }

    /* 图片样式 */
    #wechat-content img {
        max-width: 100%;
        height: auto;
        margin: 20px 0;
        border-radius: 6px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }

    /* 强调文本 */
    #wechat-content strong {
        font-weight: 600;
        color: #1a1a1a;
    }

    #wechat-content em {
        font-style: italic;
        color: #555;
    }
</style>
"""


def convert_markdown_to_html(md_content: str) -> str:
    """
    将 Markdown 内容转换为 HTML

    Args:
        md_content: Markdown 格式的文本内容

    Returns:
        转换后的 HTML 内容
    """
    # 配置 markdown 扩展
    extensions = [
        'fenced_code',      # 代码块支持
        'tables',           # 表格支持
        'nl2br',            # 换行支持
        'sane_lists',       # 更好的列表处理
    ]

    # 转换 Markdown 为 HTML
    html_content = markdown.markdown(
        md_content,
        extensions=extensions,
        output_format='html5'
    )

    return html_content


def wrap_with_template(html_content: str) -> str:
    """
    将 HTML 内容包装在完整的模板中

    Args:
        html_content: 转换后的 HTML 内容

    Returns:
        包含样式的完整 HTML 文档
    """
    template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>公众号文章</title>
    {WECHAT_STYLE}
</head>
<body>
    <div id="wechat-content">
        {html_content}
    </div>
</body>
</html>"""

    return template


def get_copyable_html(html_content: str) -> str:
    """
    生成可直接复制粘贴到公众号的 HTML 内容（带内联样式）

    Args:
        html_content: 转换后的 HTML 内容

    Returns:
        带内联样式的 HTML 内容
    """
    # 为了让公众号能够识别样式，我们将内容包装在一个带有样式的 div 中
    copyable = f'<div style="max-width: 750px; margin: 0 auto; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'Helvetica Neue\', Arial, sans-serif; font-size: 16px; line-height: 1.8; color: #333;">\n{html_content}\n</div>'

    return copyable


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='将 Markdown 文档转换为适合微信公众号的 HTML 格式'
    )
    parser.add_argument(
        'input_file',
        help='输入的 Markdown 文件路径'
    )
    parser.add_argument(
        '-o', '--output',
        help='输出的 HTML 文件路径（默认为输入文件同目录下的 .html 文件）'
    )
    parser.add_argument(
        '--no-file',
        action='store_true',
        help='不生成输出文件，只在控制台显示'
    )

    args = parser.parse_args()

    # 检查输入文件是否存在
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"错误：文件不存在 - {input_path}")
        sys.exit(1)

    # 读取 Markdown 文件
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"错误：无法读取文件 - {e}")
        sys.exit(1)

    # 转换为 HTML
    html_content = convert_markdown_to_html(md_content)

    # 生成完整的 HTML 文档（用于文件输出）
    full_html = wrap_with_template(html_content)

    # 生成可复制的 HTML（用于控制台输出）
    copyable_html = get_copyable_html(html_content)

    # 输出结果
    if not args.no_file:
        # 确定输出文件路径
        if args.output:
            output_path = Path(args.output)
        else:
            output_path = input_path.with_suffix('.html')

        # 保存 HTML 文件
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"[成功] HTML 文件已生成: {output_path}")
            print(f"       可以在浏览器中打开预览效果\n")
        except Exception as e:
            print(f"错误：无法保存文件 - {e}")
            sys.exit(1)

    # 在控制台显示可复制的 HTML
    print("=" * 80)
    print("可复制到公众号的 HTML 内容（复制下方内容）：")
    print("=" * 80)
    try:
        print(copyable_html)
    except UnicodeEncodeError:
        # 如果控制台不支持 UTF-8，使用 ASCII 安全输出
        print(copyable_html.encode('ascii', 'xmlcharrefreplace').decode('ascii'))
    print("=" * 80)
    print("\n使用方法：")
    print("1. 复制上方的 HTML 内容")
    print("2. 打开微信公众号后台")
    print("3. 新建图文消息")
    print("4. 在编辑器中切换到 HTML 源码模式")
    print("5. 粘贴复制的内容")
    print("6. 切换回可视化模式即可看到效果")


if __name__ == '__main__':
    main()
