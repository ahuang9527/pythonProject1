import re

import requests
from lxml import html

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
cookies = {
    "_ga_9YNMTB56NB": "GS2.1.s1777966089$o1$g0$t1777966089$j60$l0$h0",
    "_ga": "GA1.1.1656268399.1777966089",
    "w3s.theme": "null",
    "_sharedid": "8dd634b5-087f-4181-a30e-6f59a5c3c4b2",
    "_sharedid_cst": "zix7LPQsHA%3D%3D",
    "cto_bundle": "H25o219kYUFVWkJnSnNDRHZqJTJCbGVzVDNDU29ERjhnNlRFWXNzdDJDdDdwTDVMOUkzMFMyUHFTWjNjNiUyRjhOZ2R4WlVmeHg4aDBoYmVUb1NjQVJCcWF0UFVMU1VRNTVoc05waHQybEM3ZkdaOEtvdE55WXc4d3BGejRickZWM0VzMWFXdGVHbW1tV29BZUlhUkxHV0lQRllmd1NBJTNEJTNE",
    "connectId": "{\"ttl\":86400000,\"lastUsed\":1777966176433,\"lastSynced\":1777966176433}"
}
url = "https://www.w3schools.com/html/html_images.asp"
response = requests.get(url, headers=headers, cookies=cookies)

# 1. 解析 HTML
tree = html.fromstring(response.text)

# 2. XPath 筛选所有包含 background-image 样式的 div 元素
divs_with_bg = tree.xpath('//div[contains(@style, "background-image")]')

# 3. 正则模式：匹配 url('...') 或 url("...")
pattern = re.compile(r"background-image:\s*url\(['\"]?([^'\")]+)['\"]?\)", re.IGNORECASE)

img_urls = []

for div in divs_with_bg:
    style = div.get("style")  # 获取 style 属性字符串
    if style:
        match = pattern.search(style)
        if match:
            img_urls.append(match.group(1))

# 4. 输出结果
print("提取到的图片链接：")
for idx, url in enumerate(img_urls, 1):
    print(f"{idx}. https://www.w3schools.com/html/{url}")

