# main.py
import re
import requests
from config import BASE_URL, HEADERS, LIMIT
from fetcher import fetch_top_list
from parser_douban import parse_movie
from storage import save_to_json, save_to_redis
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

def main():
    start_time = time.time()          # 开始计时

    # 1. 获取所有分类
    categories = get_type_ids()
    print(f'[+] 发现 {len(categories)} 个电影分类')
    all_data = {}

    # 2. 遍历分类，逐个爬取
    for type_id, name in categories:  # 示例只抓前5个分类，去掉 [:5] 抓全部
        print(f'[*] 正在抓取：{name} (type={type_id})')
        # 调用fetch_top_list，拿了每个分类的原始字典
        movies = fetch_top_list(type_id, start=0, limit=LIMIT)
        # 定义一个列表，将原始字典遍历传入parse_movie解析后加入列表
        parsed = [parse_movie(m) for m in movies]
        #传入字典数据 键值对 键：name 值：对应name下解析后的数据列表
        all_data[name] = parsed
        print(f'    已获取 {len(parsed)} 部电影')

    # 3. 存储结果
    save_to_json(all_data)
    # save_to_redis(all_data)  # 按需启用
    end_time = time.time()  # 结束计时
    print(f'总耗时: {end_time - start_time:.2f} 秒')

if __name__ == '__main__':
    main()