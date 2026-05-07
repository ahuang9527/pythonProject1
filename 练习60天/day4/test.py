import requests
from bs4 import BeautifulSoup


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.jianshu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
cookies = {
    "read_mode": "day",
    "default_font": "font2",
    "locale": "zh-CN",
    "sajssdk_2015_cross_new_user": "1",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219dfdc2b728394-0cee5f4f4accf1-26061e51-1327104-19dfdc2b7291504%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2219dfdc2b728394-0cee5f4f4accf1-26061e51-1327104-19dfdc2b7291504%22%7D",
    "Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068": "1778078890",
    "HMACCOUNT": "4049A67AF1690399",
    "BAIDU_SSP_lcr": "https://www.baidu.com/link?url=Td05QYN62UvCQtgqJQMbspqrep-ZJDLk18owxyNMHTp059CXZFhsl50KSMTeGDed&wd=&eqid=d3d55e3700034ed40000000269fb54a1",
    "pagefrom": "d6f98ac96420",
    "_m7e_session_core": "7d772f29d26fb12c274ae91602244036",
    "signin_redirect": "https://www.jianshu.com/p/02260ad85308",
    "Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068": "1778078911"
}
url = "https://www.jianshu.com/p/02260ad85308"
response = requests.get(url, headers=headers, cookies=cookies)

#print(response.text)
#print(response)

response.encoding = 'utf-8'  # 根据网页实际编码调整

# 2. 创建 BeautifulSoup 对象
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 提取标题（CSS 选择器方式）
title = soup.select_one('h2._1RuRku')
if title:
    title_text = title.get_text(strip=True)  # strip=True 去掉首尾空格
    print('标题:', title_text)

# 4. 提取正文（可能包含多个段落）
content_div = soup.select_one('div._gp-ck')
if content_div:
    # 获取该 div 下所有文本，并用换行分隔段落
    paragraphs = content_div.find_all('p')
    full_text = '\n'.join(p.get_text(strip=True) for p in paragraphs)
    print('正文:', full_text)

