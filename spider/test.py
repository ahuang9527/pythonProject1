#coding:utf8
import requests

'''
params = {
    'type': 11,
    'interval_id': '100:90',
    'action': '',
    'start': 20,
    'limit': '20'
}
url = 'https://movie.douban.com/j/chart/top_list?'
html = requests.get(url=url,params=params,headers={'user-agent': UserAgent().random}).json()
for one in html:
    print(one)
    print(type(one))
print(type(html))
'''



'''
url = 'https://app.mi.com/categotyAllListApi?page=1&categoryId=6&pageSize=30'
html = requests.get(url=url,headers={'user-agent': UserAgent().random}).json()

print(type(html))
for item in html['data']:
    print(item)
    
'''

# 需求：爬取搜狗首页的页面数据



if __name__ == '__main__':
    # 1.指定url
    url = "https://www.sogou.com/"
    # 2.发起请求
    response = requests.get(url=url)  # get发起请求成功后，返回请求对象
    # 3.获取响应数据
    page_text = response.text  # 返回字符串
    print(page_text)
    # 4.持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')