# fetcher.py
import asyncio
import random

import aiohttp

from config import HEADERS, TIMEOUT, MIN_DELAY, MAX_DELAY, API_URL


async def fetch_top_list(session, type_id, start=0, limit=50):
    """调用豆瓣 API，获取指定分类的电影列表（带重试 + 随机延时）"""
    params = {
        'type': type_id,
        'interval_id': '100:90',
        'action': '',
        'start': start,
        'limit': limit
    }
    try:
        await asyncio.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        async with session.get(API_URL, headers=HEADERS, params=params,
                               timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as resp:
            resp.raise_for_status()
            return await resp.json()
    except Exception as e:
        print(f'[-] 请求失败 type={type_id}: {e}')
        return []