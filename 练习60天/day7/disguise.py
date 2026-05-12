import random
from fake_useragent import UserAgent

# 初始化一次，避免每次创建浪费资源
ua = UserAgent()

def get_random_headers(referer=None):
    """
    生成一套随机的、完整的浏览器请求头
    :param referer: 可选，模拟来源页面
    """
    headers = {
        'User-Agent': ua.random,   # 随机一个主流浏览器 UA
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    if referer:
        headers['Referer'] = referer
    return headers