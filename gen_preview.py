import os
from PIL import Image
import json

def get_category_dict():
    with open('classification_result.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    category_dict = {}
    for tpl in data['templates']:
        cat = tpl['category']
        num = tpl['number']
        title = tpl.get('title', '')
        if cat not in category_dict:
            category_dict[cat] = []
        category_dict[cat].append((num, title))
    return category_dict

def crop_image(img_path):
    try:
        im = Image.open(img_path)
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
            im.save(img_path)
    except Exception as e:
        print(f"裁剪失败: {img_path}, {e}")

def generate_category_page(thumbnail_dir, category_dict, output_file):
    html = ['<html><head><meta charset="utf-8"><title>模板分类预览</title><style>body{font-family:sans-serif;}h2{margin-top:40px;}img{border-radius:8px;border:1px solid #eee;} .tpl{margin:10px;text-align:center;display:inline-block;width:320px;vertical-align:top;} .tpl-title{font-size:14px;color:#333;margin-top:6px;}</style></head><body>']
    html.append('<h1>网站模板分类预览</h1>')
    for category, sites in category_dict.items():
        html.append(f"<h2>{category}</h2><div>")
        for num, title in sites:
            img_path = os.path.join(thumbnail_dir, f"{num}.png")
            if os.path.exists(img_path):
                html.append(f"<div class='tpl'><img src='{img_path}' width='300'><div class='tpl-title'>{num} {title}</div></div>")
        html.append("</div>")
    html.append("</body></html>")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    category_dict = get_category_dict()
    generate_category_page("thumbnails", category_dict, "分类预览.html")
