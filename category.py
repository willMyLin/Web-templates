import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def generate_thumbnails(base_dir, output_dir, width=1200, height=800, delay=2):
    os.makedirs(output_dir, exist_ok=True)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        for folder in sorted(os.listdir(base_dir)):
            folder_path = os.path.join(base_dir, folder)
            index_html = os.path.join(folder_path, "index.html")
            if os.path.isfile(index_html):
                url = f"file://{os.path.abspath(index_html)}"
                driver.get(url)
                time.sleep(delay)
                # 获取body实际内容高度
                page_height = driver.execute_script("return Math.ceil(document.querySelector('body').getBoundingClientRect().height);")
                driver.set_window_size(width, page_height)
                time.sleep(1)
                out_path = os.path.join(output_dir, f"{folder}.png")
                driver.save_screenshot(out_path)
                print(f"{folder} -> {out_path}")
    finally:
        driver.quit()

if __name__ == "__main__":
    generate_thumbnails(
        base_dir="349套HTML5+CSS3各行各业网站模板",
        output_dir="thumbnails",
        width=1200,
        height=800,
        delay=2
    )