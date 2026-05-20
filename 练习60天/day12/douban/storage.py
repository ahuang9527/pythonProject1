# storage.py
import json
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, FILE_PATH

# Redis 连接池（高并发推荐）
pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
    max_connections=10
)
r = redis.Redis(connection_pool=pool)

def save_to_json(data, filepath=FILE_PATH):
    """保存完整数据到本地 JSON 文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'[+] 已保存到 {filepath}，共 {len(data)} 个分类')

def save_to_redis(data):
    """将每部电影存为 Redis Hash（去重 + 结构化）"""
    for movie in data:
        movie_id = movie.get('id', movie.get('title'))
        key = f"douban:movie:{movie_id}"
        if not r.exists(key):
            r.hset(key, mapping=movie)
            r.expire(key, 86400)  # 24 小时过期