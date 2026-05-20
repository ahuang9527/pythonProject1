# fetcher.py
import requests
import time
import random
from config import HEADERS, TIMEOUT, MIN_DELAY, MAX_DELAY, API_URL

def fetch_top_list(type_id, start=0, limit=50):
    """调用豆瓣 API，获取指定分类的电影列表（带重试 + 随机延时）"""
    params = {
        'type': type_id,
        'interval_id': '100:90',
        'action': '',
        'start': start,
        'limit': limit
    }
    try:
        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        resp = requests.get(API_URL, headers=HEADERS,
                            params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    except requests.RequestException as e:
        print(f'[-] 请求失败 type={type_id}: {e}')
        return []