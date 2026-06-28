import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/111.0.0.0 Safari/537.36',
}
cookies = {
    'sessionid': 'hie9wnrkxw66g6z45f37476mc1p7sbx3'
}
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}



grand_total = 0
success_count = 0

for page in range(1, 101):
    data = {'page': page}
    try:
        # 前置请求（激活会话状态）
        requests.get('https://www.python-spider.com/cityjson',
                     headers=headers, cookies=cookies,
                     verify=False, proxies=proxies)
        response = requests.post(
            'https://www.python-spider.com/api/challenge7',
            data=data,
            headers=headers,
            cookies=cookies,
            verify=False,
            proxies=proxies
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