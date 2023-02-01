import requests
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
# 网上找的免费代理ip
proxies = {
    'http': 'http://47.254.47.61:8080',
    'https': 'https://47.254.47.61:8080'
}
html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)