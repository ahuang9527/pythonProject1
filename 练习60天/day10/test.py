import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('test', 'hello redis')
print(r.get('test'))   # 输出：hello redis
r.set('total_requests', 0)
r.incr('total_requests')   # 自增 1
r.incrby('total_requests', 10)  # 加 10
print(r.get('total_requests'))  # 11

book = {
    'title': 'A Light in the Attic',
    'price': '£51.77',
    'image_url': 'http://...',
    'status': 'crawled'
}
r.hset('book:1001', mapping=book)   # 一次写入多个字段
# 读取所有字段
data = r.hgetall('book:1001')
print(data['title'])
# 只读取某个字段
print(r.hget('book:1001', 'price'))


r.lpush('pending_urls', 'http://example.com/page1')
r.lpush('pending_urls', 'http://example.com/page2')
# 从右侧弹出一个任务（FIFO）
url = r.rpop('pending_urls')
print(url)  # b'http://example.com/page1'


r.sadd('crawled_urls', 'http://books.toscrape.com/catalogue/book1')
r.sadd('crawled_urls', 'http://books.toscrape.com/catalogue/book1')  # 重复，不会加进去
print(r.smembers('crawled_urls'))  # 输出所有成员
print(r.sismember('crawled_urls', 'http://...'))  # 检查是否存在，O(1)


r.zadd('books_by_price', {'book_A': 51.77, 'book_B': 35.00})
# 按价格从低到高获取
print(r.zrange('books_by_price', 0, -1, withscores=True))



