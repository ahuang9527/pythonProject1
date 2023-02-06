#coding:utf8
import requests
from fake_useragent import UserAgent
from lxml import etree
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




url = 'https://bj.lianjia.com/ershoufang/c1111062788544/'
html = requests.get(url=url,headers={'user-agent': UserAgent().random}).text

p=etree.HTML(html)
h_list=p.xpath('//*[@id="content"]/div[1]/ul/li')
item = {}
for h in h_list:
    # item = {}
    # xpath匹配房源名称
    name_list = h.xpath('.//div[@class="title"]/a/text()')
    # 判断列表是否为空,此处使用了三目运算符,如果if后的条件非真，就将else的结果赋给最前面的表达式
    item['name'] = name_list[0] if name_list else None
    # xpath匹配房源相关信息
    info_list = h.xpath('.//div[@class="houseInfo"]/text()')
    item['info'] = info_list[0] if info_list else None
    # 地址
    address_list = h.xpath('.//div[@class="positionInfo"]/a/text()')
    item['address'] = address_list[0] if address_list else None
    # 总价
    total_list1 = h.xpath(
        './/div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()|.//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/i[2]/text()')
    total_list = ''.join(total_list1)

    item['total_list'] = total_list if total_list else None
    # 单价
    price_list = h.xpath('.//div[@class="unitPrice"]/span/text()')
    item['price_list'] = price_list[0] if price_list else None
    print(item)
    # print(item)

# 需求：爬取搜狗首页的页面数据

'''

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
    print('爬取数据结束！！！')'''