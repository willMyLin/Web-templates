#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import defaultdict

def analyze_and_categorize():
    """分析模板并分类"""
    base_dir = "349套HTML5+CSS3各行各业网站模板"
    categories = defaultdict(list)
    
    # 定义分类关键词
    category_keywords = {
        "电商购物": ["shop", "store", "cart", "buy", "product", "ecommerce", "shopping", "mall", "商店", "购物"],
        "企业公司": ["business", "corporate", "company", "about", "service", "agency", "consulting", "企业", "公司"],
        "博客新闻": ["blog", "news", "article", "post", "magazine", "journal", "博客", "新闻", "文章"],
        "作品展示": ["portfolio", "gallery", "photo", "design", "creative", "work", "作品", "展示", "相册"],
        "餐饮美食": ["restaurant", "food", "cafe", "menu", "cooking", "recipe", "餐厅", "美食", "菜谱"],
        "医疗健康": ["health", "medical", "doctor", "clinic", "hospital", "healthcare", "医疗", "健康"],
        "教育培训": ["education", "school", "course", "learning", "university", "教育", "学校", "培训"],
        "娱乐媒体": ["music", "video", "game", "entertainment", "media", "movie", "娱乐", "音乐", "视频"],
        "登录注册": ["login", "register", "signup", "auth", "account", "登录", "注册"],
        "其他类型": []  # 默认分类
    }
    
    for i in range(1, 350):
        folder_num = f"{i:03d}"
        folder_path = os.path.join(base_dir, folder_num)
        index_file = os.path.join(folder_path, "index.html")
        
        if not os.path.exists(index_file):
            continue
            
        try:
            with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
            
            # 提取标题
            title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else "未命名"
            
            # 分类判断
            categorized = False
            for category, keywords in category_keywords.items():
                if category == "其他类型":
                    continue
                    
                if any(keyword in content for keyword in keywords):
                    categories[category].append((folder_num, title))
                    categorized = True
                    break
            
            if not categorized:
                categories["其他类型"].append((folder_num, title))
                
        except Exception as e:
            print(f"分析 {folder_num} 失败: {e}")
            categories["其他类型"].append((folder_num, "分析失败"))
    
    return categories

def generate_html_page(categories, output_file="模板分类预览.html"):
    """生成HTML页面"""
    
    html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>349套网站模板分类预览</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            font-weight: 700;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        
        .stat-item {
            background: rgba(255,255,255,0.2);
            padding: 15px 25px;
            border-radius: 10px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            display: block;
        }
        
        .category-section {
            margin-bottom: 50px;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        
        .category-header {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 25px;
            position: relative;
        }
        
        .category-title {
            font-size: 1.8em;
            font-weight: 600;
            margin-bottom: 5px;
        }
        
        .category-count {
            opacity: 0.9;
            font-size: 1.1em;
        }
        
        .templates-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
            padding: 30px;
        }
        
        .template-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 3px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .template-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .template-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-bottom: 3px solid #f0f0f0;
        }
        
        .template-info {
            padding: 15px;
        }
        
        .template-number {
            font-weight: bold;
            color: #667eea;
            font-size: 1.1em;
            margin-bottom: 5px;
        }
        
        .template-title {
            color: #555;
            font-size: 0.95em;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .search-box {
            margin-bottom: 30px;
            text-align: center;
        }
        
        .search-input {
            width: 100%;
            max-width: 500px;
            padding: 15px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s ease;
        }
        
        .search-input:focus {
            border-color: #667eea;
        }
        
        .navigation {
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        
        .nav-link {
            display: block;
            color: #667eea;
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 2px 0;
            font-size: 14px;
            transition: background-color 0.3s ease;
        }
        
        .nav-link:hover {
            background-color: #f0f0f0;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            
            .stats {
                flex-direction: column;
                align-items: center;
            }
            
            .navigation {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 网站模板大全</h1>
            <p>349套精美HTML5+CSS3模板，按类别精心整理</p>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">349</span>
                    <span>总模板数</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{total_categories}</span>
                    <span>分类数量</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">100%</span>
                    <span>响应式设计</span>
                </div>
            </div>
        </div>
        
        <div class="search-box">
            <input type="text" class="search-input" placeholder="🔍 搜索模板编号或标题..." onkeyup="searchTemplates(this.value)">
        </div>
        
        <div class="navigation">
            <strong>快速导航</strong>
{navigation_links}
        </div>
        
{category_sections}
    </div>
    
    <script>
        function openTemplate(templateNumber) {{
            const templatePath = `349套HTML5+CSS3各行各业网站模板/${{templateNumber}}/index.html`;
            window.open(templatePath, '_blank');
        }}
        
        function searchTemplates(query) {
            const sections = document.querySelectorAll('.category-section');
            const queryLower = query.toLowerCase();
            
            sections.forEach(section => {
                const cards = section.querySelectorAll('.template-card');
                let hasVisibleCards = false;
                
                cards.forEach(card => {
                    const number = card.dataset.number.toLowerCase();
                    const title = card.dataset.title.toLowerCase();
                    
                    if (number.includes(queryLower) || title.includes(queryLower)) {
                        card.style.display = 'block';
                        hasVisibleCards = true;
                    } else {
                        card.style.display = 'none';
                    }
                });
                
                section.style.display = hasVisibleCards ? 'block' : 'none';
            });
        }
        
        // 平滑滚动到指定分类
        function scrollToCategory(categoryId) {
            document.getElementById(categoryId).scrollIntoView({
                behavior: 'smooth'
            });
        }
    </script>
</body>
</html>"""
    
    # 生成导航链接
    navigation_links = ""
    for category in categories.keys():
        category_id = category.replace(" ", "-")
        navigation_links += f'            <a href="#{category_id}" class="nav-link" onclick="scrollToCategory(\'{category_id}\')">{category}</a>\n'
    
    # 生成分类部分
    category_sections = ""
    for category, templates in categories.items():
        category_id = category.replace(" ", "-")
        
        category_sections += f"""
        <div class="category-section" id="{category_id}">
            <div class="category-header">
                <div class="category-title">{category}</div>
                <div class="category-count">{len(templates)} 个模板</div>
            </div>
            <div class="templates-grid">
"""
        
        for template_num, title in templates:
            thumbnail_path = f"thumbnails/{template_num}.png"
            category_sections += f"""
                <div class="template-card" data-number="{template_num}" data-title="{title}" onclick="openTemplate('{template_num}')">
                    <img src="{thumbnail_path}" alt="模板 {template_num}" class="template-image">
                    <div class="template-info">
                        <div class="template-number">#{template_num}</div>
                        <div class="template-title">{title[:50]}{'...' if len(title) > 50 else ''}</div>
                    </div>
                </div>
"""
        
        category_sections += """
            </div>
        </div>
"""
    
    # 替换模板变量
    final_html = html_content.format(
        total_categories=len(categories),
        navigation_links=navigation_links,
        category_sections=category_sections
    )
    
    # 保存文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✅ 分类页面已生成: {output_file}")
    return output_file

def main():
    print("🔍 正在分析和分类模板...")
    categories = analyze_and_categorize()
    
    print("📊 分类结果:")
    total_templates = 0
    for category, templates in categories.items():
        count = len(templates)
        total_templates += count
        print(f"  {category}: {count} 个模板")
    
    print(f"\n📄 生成HTML页面...")
    html_file = generate_html_page(categories)
    
    print(f"\n🎉 完成！")
    print(f"📂 总计分析: {total_templates} 个模板")
    print(f"🌐 请在浏览器中打开: {html_file}")

if __name__ == "__main__":
    main()