import execjs
import requests
import urllib3


headers = {
    'Content-Length': '6',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Origin': 'https://www.python-spider.com',
    'Referer': 'https://www.python-spider.com/challenge/1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'timestamp': 'keep-alive',
    'safe': '1',
}
cookies = {
    'sessionid': '70fxmbaphvcx0kf4i342df2u3xwk3zjf'
}


session = requests.Session()

grand_total = 0
success_count = 0

for page in range(1, 101):
    data = {'page': page}
    try:
        # session自动维持会话
        response = session.post(
            'https://www.python-spider.com/api/challenge1',
            data=data,
            headers=headers,
            cookies=cookies,
            verify=False
        )
        # 解析 JSON 并计算该页数字总和
        resp_json = response.json()
        print(resp_json)
        items = resp_json.get('data', [])
        page_sum = sum(int(item['value'].strip()) for item in items)
        print(f'Page {page:3d}: sum = {page_sum}')
        grand_total += page_sum
        success_count += 1
    except Exception as e:
        print(f'Page {page:3d} 失败: {e}')

print(f'\n成功获取 {success_count}/100 页')
print(f'所有页面数字总和: {grand_total}')
