import json  # ✨ 新增：保存字典为 JSON
import os
import re  # ✨ 新增：清理文件名非法字符
import time
from urllib.parse import urljoin  # ✨ 新增：安全拼接 URL

import requests
from bs4 import BeautifulSoup

# 配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
BASE_URL = 'http://books.toscrape.com'
SAVE_DIR = 'C:/Users/root/Pictures/test'
os.makedirs(SAVE_DIR, exist_ok=True)


# ---------- 辅助函数 ----------
def get_soup(url):
    """获取页面的BeautifulSoup对象"""
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'html.parser')


def get_book_links():
    """从首页获取所有书籍详情页链接"""
    soup = get_soup(BASE_URL)
    links = []
    for article in soup.find_all('article', class_='product_pod'):
        a_tag = article.find('a')
        if a_tag and a_tag.get('href'):
            # 使用 urljoin 自动处理相对路径，更稳健
            full_url = urljoin(BASE_URL, a_tag['href'])
            links.append(full_url)
    return links


# ✨ 改造：原来只返回图片 URL，现在返回整个字典
def get_book_info(detail_url):
    """从详情页提取书籍信息，返回包含所有字段的字典"""
    try:
        soup = get_soup(detail_url)

        # 标题
        title = soup.find('h1').text.strip()

        # 价格
        price_tag = soup.select_one('p.price_color')
        price = price_tag.text.strip() if price_tag else 'N/A'

        # 库存
        stock_tag = soup.select_one('p.instock.availability')
        stock = stock_tag.text.strip() if stock_tag else 'N/A'

        # 图片 URL
        img_tag = soup.find('div', class_='item active').find('img')
        img_url = None
        if img_tag:
            src = img_tag['src']
            img_url = urljoin(BASE_URL, src)  # urljoin 自动处理 ../../ 等

        # 返回打包好的字典
        return {
            'title': title,
            'price': price,
            'stock': stock,
            'image_url': img_url,
            'detail_url': detail_url
        }
    except Exception as e:
        print(f'解析书籍信息出错: {e}')
        return None


def download_image(img_url, filename):
    """下载图片并保存"""
    try:
        resp = requests.get(img_url, headers=HEADERS, stream=True, timeout=15)
        if resp.status_code == 200:
            filepath = os.path.join(SAVE_DIR, filename)
            with open(filepath, 'wb') as f:
                for chunk in resp.iter_content(1024):
                    f.write(chunk)
            print(f'✓ 已保存: {filename}')
        else:
            print(f'✗ 下载失败: {img_url} 状态码{resp.status_code}')
    except Exception as e:
        print(f'下载异常: {e}')


# ---------- 主程序 ----------
if __name__ == '__main__':
    print('正在获取书籍列表...')
    book_links = get_book_links()
    print(f'共发现 {len(book_links)} 本书')

    all_books = []  # ✨ 新增：收集所有书籍信息的列表

    for i, link in enumerate(book_links):
        print(f'\n[{i + 1}/{len(book_links)}] 处理: {link}')

        # ✨ 获取结构化字典
        book = get_book_info(link)
        if not book:
            print('获取信息失败，跳过')
            continue

        all_books.append(book)  # ✨ 存入列表

        # 下载图片（从字典中取图片 URL）
        if book['image_url']:
            # ✨ 用书名为文件名，先清理非法字符
            safe_title = re.sub(r'[\\/*?:"<>|]', '', book['title'])
            filename = f'{safe_title}.jpg'
            download_image(book['image_url'], filename)
        else:
            print('未找到图片，跳过下载')

        time.sleep(1)

    # ✨ 新增：所有信息保存为 JSON
    with open('books_info.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, ensure_ascii=False, indent=2)

    print(f'\n全部完成！图片保存在 {SAVE_DIR}，书籍信息保存在 books_info.json')