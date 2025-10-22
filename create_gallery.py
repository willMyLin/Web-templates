#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def generate_template_gallery():
    """生成模板缩略图画廊页面"""
    
    base_dir = "349套HTML5+CSS3各行各业网站模板"
    thumbnail_dir = "thumbnails"
    
    # 收集所有模板信息
    templates = []
    
    for i in range(1, 350):
        folder_num = f"{i:03d}"
        folder_path = os.path.join(base_dir, folder_num)
        index_file = os.path.join(folder_path, "index.html")
        thumbnail_file = os.path.join(thumbnail_dir, f"{folder_num}.png")
        
        if os.path.exists(index_file) and os.path.exists(thumbnail_file):
            # 提取标题
            title = "未命名模板"
            try:
                with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
                if title_match:
                    title = title_match.group(1).strip()
                    if not title or title.lower() in ['home', 'index', '']:
                        title = f"模板 {folder_num}"
            except:
                title = f"模板 {folder_num}"
                
            templates.append({
                'number': folder_num,
                'title': title,
                'path': folder_path,
                'thumbnail': thumbnail_file
            })
    
    # 生成HTML页面
    html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>网站模板画廊 - 349套精美模板</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .search-box {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .search-input {
            width: 100%;
            max-width: 500px;
            padding: 15px 20px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .template-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }
        
        .template-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
        }
        
        .template-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            object-position: top;
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
            line-height: 1.4;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .template-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(102, 126, 234, 0.9);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .template-card:hover .template-overlay {
            opacity: 1;
        }
        
        .stats {
            text-align: center;
            color: white;
            margin-bottom: 20px;
            font-size: 1.1em;
        }
        
        .loading {
            text-align: center;
            color: white;
            font-size: 1.2em;
            margin-top: 50px;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            
            .gallery {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 15px;
            }
            
            body {
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎨 网站模板画廊</h1>
        <p>349套精美HTML5+CSS3模板，点击缩略图即可预览</p>
    </div>
    
    <div class="search-box">
        <input type="text" class="search-input" placeholder="🔍 搜索模板编号或标题..." onkeyup="searchTemplates(this.value)">
    </div>
    
    <div class="stats">
        <span>📊 共 """ + str(len(templates)) + """ 个模板</span>
    </div>
    
    <div class="gallery" id="gallery">
"""
    
    # 添加每个模板卡片
    for template in templates:
        html_content += f"""
        <div class="template-card" data-number="{template['number']}" data-title="{template['title']}" onclick="openTemplate('{template['number']}')">
            <img src="{template['thumbnail']}" alt="模板 {template['number']}" class="template-image" loading="lazy">
            <div class="template-info">
                <div class="template-number">#{template['number']}</div>
                <div class="template-title">{template['title']}</div>
            </div>
            <div class="template-overlay">
                点击预览
            </div>
        </div>
"""
    
    html_content += """
    </div>
    
    <div class="loading" id="loading" style="display: none;">
        正在加载模板...
    </div>
    
    <script>
        function openTemplate(templateNumber) {
            const templatePath = `349套HTML5+CSS3各行各业网站模板/${templateNumber}/index.html`;
            // 在新窗口中打开模板
            window.open(templatePath, '_blank');
        }
        
        function searchTemplates(query) {
            const cards = document.querySelectorAll('.template-card');
            const queryLower = query.toLowerCase();
            let visibleCount = 0;
            
            cards.forEach(card => {
                const number = card.dataset.number.toLowerCase();
                const title = card.dataset.title.toLowerCase();
                
                if (number.includes(queryLower) || title.includes(queryLower)) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });
            
            // 更新统计信息
            const stats = document.querySelector('.stats span');
            if (query.trim()) {
                stats.textContent = `🔍 找到 ${visibleCount} 个匹配的模板`;
            } else {
                stats.textContent = `📊 共 """ + str(len(templates)) + """ 个模板`;
            }
        }
        
        // 图片懒加载优化
        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('img[loading="lazy"]');
            
            if ('IntersectionObserver' in window) {
                const imageObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const img = entry.target;
                            img.src = img.src;
                            img.classList.remove('lazy');
                            imageObserver.unobserve(img);
                        }
                    });
                });
                
                images.forEach(img => imageObserver.observe(img));
            }
        });
        
        // 键盘快捷键支持
        document.addEventListener('keydown', function(e) {
            if (e.key === '/' || (e.ctrlKey && e.key === 'f')) {
                e.preventDefault();
                document.querySelector('.search-input').focus();
            }
        });
        
        console.log('🎨 模板画廊加载完成！');
        console.log('💡 提示：按 "/" 键快速搜索');
    </script>
</body>
</html>"""
    
    # 保存文件
    output_file = "模板画廊.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file, len(templates)

def main():
    print("🎨 正在生成模板画廊页面...")
    html_file, template_count = generate_template_gallery()
    
    print(f"✅ 页面生成完成！")
    print(f"📄 文件名: {html_file}")
    print(f"📊 包含模板: {template_count} 个")
    print(f"🌐 请在浏览器中打开 {html_file} 查看")
    print(f"💡 支持搜索功能，可按模板编号或标题查找")

if __name__ == "__main__":
    main()