# config.py

# 豆瓣排行榜主页
BASE_URL = 'https://movie.douban.com/chart'

# AJAX 接口模板
API_URL = 'https://movie.douban.com/j/chart/top_list'

# 每个分类抓取条数
LIMIT = 50

# 请求超时（秒）
TIMEOUT = 150

# 线程池大小，根据网络和反爬调整
MAX_WORKERS = 5

# 异步aiohttp同时请求的最大数量
CONCURRENCY = 5

# 随机延时范围（秒）
MIN_DELAY = 2.0
MAX_DELAY = 5.0

# 请求头（关键：绕过反爬）
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://movie.douban.com/chart',
    'Connection': 'keep-alive',
}
# 来源：[reference:8]



#REDIS相关配置


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = ''


#存储相关配置
FILE_PATH = r'E:\study\download\douban_top50.json'


