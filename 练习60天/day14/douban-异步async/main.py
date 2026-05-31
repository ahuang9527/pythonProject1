# main.py
import asyncio
import re
import time

import aiohttp
import requests

from config import BASE_URL, HEADERS, CONCURRENCY, TIMEOUT
from fetcher import fetch_top_list
from parser_douban import parse_movie
from storage import save_to_json


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

async def fetch_category(session, sem, type_id, name):
    """抓取单个分类，返回 (分类名, 电影列表)"""
    async with sem:   # 用信号量控制并发数
        print(f'[*] 正在抓取：{name} (type={type_id})')
        movies = await fetch_top_list(session, type_id, start=0, limit=50)
        parsed = [parse_movie(m) for m in movies]
        print(f'    已获取 {name}: {len(parsed)} 部电影')
        return name, parsed



async def main():
    start_time = time.time()          # 开始计时

    # 1. 获取所有分类
    categories = get_type_ids()
    print(f'[+] 发现 {len(categories)} 个电影分类')


    # 创建并发控制信号量
    sem = asyncio.Semaphore(CONCURRENCY)

    # 创建一个 aiohttp 会话，设置全局请求头
    async with aiohttp.ClientSession(
            headers=HEADERS,
            timeout=aiohttp.ClientTimeout(total=TIMEOUT)
    ) as session:
        # 创建所有分类的抓取任务
        tasks = [fetch_category(session, sem, type_id, name)
                 for type_id, name in categories]
        # 并发执行，收集结果
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # 整理结果（跳过异常）
    all_data = {}
    for result in results:
        if isinstance(result, Exception):
            print(f'[-] 某个分类抓取失败: {result}')
        else:
            name, parsed = result
            all_data[name] = parsed

    save_to_json(all_data)
    # save_to_redis(all_data)  # 按需启用
    end_time = time.time()  # 结束计时
    print(f'总耗时: {end_time - start_time:.2f} 秒')

if __name__ == '__main__':
    asyncio.run(main())