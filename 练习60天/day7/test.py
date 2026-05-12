import requests
from bs4 import BeautifulSoup
import os
import time
import re
import json
from urllib.parse import urljoin

# 导入伪装模块（假设上面代码保存在 disguise.py 同目录）
# 如果直接写在一个脚本里，把 get_random_headers 函数拷贝过来即可
from disguise import get_random_headers

BASE_URL = 'http://books.toscrape.com'
SAVE_DIR = 'C:/Users/a/Pictures/test'
os.makedirs(SAVE_DIR, exist_ok=True)

# 创建全局会话，自动处理Cookie
session = requests.Session()


# 也可以给Session设置默认headers，但这里我们每次请求动态生成，更随机

def get_soup(url, referer=None):
    """获取页面的BeautifulSoup对象，带上随机请求头和Referer"""
    headers = get_random_headers(referer=referer)
    resp = session.get(url, headers=headers, timeout=10)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'html.parser')


def download_image(img_url, filename, referer=None):
    """下载图片，同样使用随机头和Referer"""
    headers = get_random_headers(referer=referer)
    try:
        resp = session.get(img_url, headers=headers, stream=True, timeout=15)
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


# 其他函数 get_book_links(), get_book_info() 保持不变，
# 只需把 get_soup 调用传入 referer 即可，让跳转看起来来自上一页

def get_book_links():
    """从首页获取所有书籍详情页链接，首页referer为空"""
    soup = get_soup(BASE_URL)
    links = []
    for article in soup.find_all('article', class_='product_pod'):
        a_tag = article.find('a')
        if a_tag and a_tag.get('href'):
            full_url = urljoin(BASE_URL, a_tag['href'])
            links.append(full_url)
    return links


def get_book_info(detail_url, referer):
    """提取书籍信息，referer设为首页"""
    soup = get_soup(detail_url, referer=referer)
    # ... 提取逻辑与之前完全相同，不再重复 ...
    # return {...}


# 主程序
if __name__ == '__main__':
    print('正在获取书籍列表...')
    book_links = get_book_links()
    print(f'共发现 {len(book_links)} 本书')
    all_books = []

    for i, link in enumerate(book_links):
        print(f'\n[{i + 1}/{len(book_links)}] 处理: {link}')
        # 模拟从首页跳转过来
        book = get_book_info(link, referer=BASE_URL + '/')
        if not book:
            continue
        all_books.append(book)

        if book['image_url']:
            safe_title = re.sub(r'[\\/*?:"<>|]', '', book['title'])
            filename = f'{safe_title}.jpg'
            # 下载图片时referer设为当前详情页
            download_image(book['image_url'], filename, referer=link)

        time.sleep(1)

    with open('books_info.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, ensure_ascii=False, indent=2)
    print(f'\n全部完成！')