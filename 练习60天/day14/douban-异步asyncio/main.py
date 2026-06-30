# main.py
import re
import requests
from config import BASE_URL, HEADERS, LIMIT, MAX_WORKERS
from fetcher import fetch_top_list
from parser_douban import parse_movie
from storage import save_to_json, save_to_redis
from concurrent.futures import ThreadPoolExecutor, as_completed
import time



def get_type_ids():
    """从排行榜主页提取所有分类 ID 和名称（动态获取）"""
    html = requests.get(BASE_URL, headers=HEADERS).text
    # 用正则从 <div class="types"> 中提取所有 type=数字 和 分类名
    pattern = r'<a href=".*?type=(\d+).*?">(.*?)</a>'
    matches = re.findall(pattern, html)
    # 去重 + 保留首次出现
    seen, result = set(), []
    for type_id, name in matches:
        if type_id not in seen:
            seen.add(type_id)
            result.append((type_id, name.strip()))
    return result

def fetch_category(type_id, name):
    """抓取单个分类的电影列表（供线程调用）"""
    print(f'[*] 正在抓取：{name} (type={type_id})')
    movies = fetch_top_list(type_id, start=0, limit=LIMIT)
    parsed = [parse_movie(m) for m in movies]
    print(f'    已获取 {name}: {len(parsed)} 部电影')
    return name, parsed


def main():
    start_time = time.time()          # 开始计时

    # 1. 获取所有分类
    categories = get_type_ids()
    print(f'[+] 发现 {len(categories)} 个电影分类')
    all_data = {}

    # 使用线程池并发抓取
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有任务 遍历分类，逐个爬取
        future_to_cat = {
            executor.submit(fetch_category, type_id, name): name
            for type_id, name in categories
        }
        # 收集结果
        for future in as_completed(future_to_cat):
            try:
                name, parsed = future.result()
                all_data[name] = parsed
            except Exception as e:
                cat_name = future_to_cat[future]
                print(f'[-] 分类 {cat_name} 抓取失败: {e}')


    # 3. 存储结果
    save_to_json(all_data)
    # save_to_redis(all_data)  # 按需启用
    end_time = time.time()  # 结束计时
    print(f'总耗时: {end_time - start_time:.2f} 秒')

if __name__ == '__main__':
    main()