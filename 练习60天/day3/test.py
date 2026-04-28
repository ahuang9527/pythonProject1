#豆瓣读书的网站，练习xpath和正则
from lxml import etree
import requests
import re

cookies = {
    'bid': '-Qao_v7iS80',
    'b-user-id': 'bd416fd2-d5fa-fba0-6c02-ee280fad9b85',
    'ap_v': '0,6.0',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1777367503%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D4BaU6GZonCTy2CJZtV7i9f014CT-61IpE6_RTnpG40RRDXFcGAPEs8IKPaBht1S_%26wd%3D%26eqid%3Df22f5e67000265830000000369f079c3%22%5D',
    '_pk_id.100001.3ac3': '5285fde2288f75e0.1777367503.',
    '_pk_ses.100001.3ac3': '1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.baidu.com/link?url=4BaU6GZonCTy2CJZtV7i9f014CT-61IpE6_RTnpG40RRDXFcGAPEs8IKPaBht1S_&wd=&eqid=f22f5e67000265830000000369f079c3',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': 'bid=-Qao_v7iS80; b-user-id=bd416fd2-d5fa-fba0-6c02-ee280fad9b85; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1777367503%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D4BaU6GZonCTy2CJZtV7i9f014CT-61IpE6_RTnpG40RRDXFcGAPEs8IKPaBht1S_%26wd%3D%26eqid%3Df22f5e67000265830000000369f079c3%22%5D; _pk_id.100001.3ac3=5285fde2288f75e0.1777367503.; _pk_ses.100001.3ac3=1',
}

response = requests.get('https://book.douban.com/review/best/', cookies=cookies, headers=headers)


#print(response.text,response.url,response.status_code)
# 1. 解析HTML
tree = etree.HTML(response.text)

# 2. 用XPath选中所有 review-item 容器
review_items = tree.xpath('//div[contains(@class, "review-item")]')

# 3. 遍历每个评论，提取图片和简介
results = []
for item in review_items:
    # 提取书籍封面图片（只取第一个subject-img下的图片）
    img_xpath = './/a[contains(@class, "subject-img")]/img/@src'
    img_urls = item.xpath(img_xpath)
    img = img_urls[0] if img_urls else None

    # 提取简介文本（short-content内的纯文本）
    short_xpath = './/div[contains(@class, "short-content")]//text()'
    short_parts = item.xpath(short_xpath)
    raw_text = ''.join(short_parts).strip()

    # 4. 用正则清洗文本：去除多余空白、换行、&nbsp; 以及“(展开)”部分
    cleaned_text = re.sub(r'\s+', ' ', raw_text)  # 将连续空白压缩成一个空格
    cleaned_text = re.sub(r'&nbsp;', '', cleaned_text)  # 去除 &nbsp;
    cleaned_text = re.sub(r'\(展开\)$', '', cleaned_text)  # 去掉尾部的“(展开)”
    cleaned_text = cleaned_text.strip()

    results.append({
        'image_url': img,
        'short_review': cleaned_text
    })

# 打印结果
for r in results:
    print("图片链接:", r['image_url'])
    print("书评:", r['short_review'])
    print("-" * 50)
