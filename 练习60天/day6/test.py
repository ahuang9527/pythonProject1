import requests
from bs4 import BeautifulSoup
import os
import time

# 配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
BASE_URL = 'http://books.toscrape.com'
SAVE_DIR = 'C:/Users/a/Pictures/test'
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
            full_url = BASE_URL + '/' + a_tag['href']
            links.append(full_url)
    return links


def get_image_url(detail_url):
    """从详情页提取封面图片完整URL"""
    try:
        soup = get_soup(detail_url)
        img_tag = soup.find('div', class_='item active').find('img')
        if img_tag:
            src = img_tag['src'].replace('../../', '')
            return BASE_URL + '/' + src
    except Exception as e:
        print(f'解析图片URL出错: {e}')
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

    for i, link in enumerate(book_links):
        print(f'\n[{i + 1}/{len(book_links)}] 处理: {link}')

        img_url = get_image_url(link)
        if not img_url:
            print('未找到图片，跳过')
            continue

        # 用书籍名称或索引作为文件名，从URL末尾提取书名信息
        # 这里简单用详情页URL的最后一段作为标识
        book_name = link.rstrip('/').split('/')[-2]  # 如 "a-light-in-the-attic_1000"
        filename = f'{book_name}.jpg'

        download_image(img_url, filename)

        # 添加延时，避免请求过快
        time.sleep(1)

    print(f'\n全部完成！图片保存在 {SAVE_DIR} 文件夹')