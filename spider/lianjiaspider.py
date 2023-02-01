#coding:utf8
import random
import time

import requests
from fake_useragent import UserAgent
from lxml import etree

'''
这是一个用于爬取链家最新二手房相关信息的爬虫，主要练习xpath库解析提取信息
使用requests库请求得到html网页,并使用lxml库创建html解析对象，xpath匹配解析需要的内容
爬取的内容为链家上最新发布的北京二手房相关信息
'''

#创建类

class LianjiaSpider(object):
    #初始化构造方法
    def __init__(self):
        self.url='https://bj.lianjia.com/ershoufang/pg{}co32/'

    #使用requests定义请求函数
    def get_html(self,url):
        res=requests.get(url=url,headers={'user-agent': UserAgent().random},timeout=3)
        html=res.text
        return html

    #解析html提取数据,注意xpath匹配的结果为列表
    def parse_html(self,url):
        #调用请求函数，返回html
        html=self.get_html(url)
        if html:
            #调用etree模块的HTML()方法来创建html解析对象
            p=etree.HTML(html)
            #基准xpath表达式得到30个房源节点对象列表，将匹配到的内容放入[]列表中
            h_list=p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            #遍历所有列表节点对象，遍历列表中待二次匹配提取数据的内容
            for h in h_list:
                item={}
                #xpath匹配房源名称
                name_list=h.xpath('.//div[@class="title"]/a/text()')
                #判断列表是否为空,此处使用了三目运算符,如果if后的条件非真，就将else的结果赋给最前面的表达式
                item['name']=name_list[0] if name_list else None
                #xpath匹配房源相关信息
                info_list=h.xpath('.//div[@class="houseInfo"]/text()')
                item['info'] = info_list[0] if info_list else None
                # 户型+面积+方位+是否精装..['2室1厅 | 88.62平米 | 北 南 | 简装 | 顶层(共6层) | 2004年建 | 板楼']
                #判断列表是否为空
                '''
                注释是因为写完才发现房源中分隔符的数目不一致，因此房源相关信息作为整体传入
                if info_list:
                    #使用split方法分割字符串，分隔符为|
                    L=info_list[0].split('|')
                    # ['2室1厅 ', ' 88.62平米 ', ' 北 南 ', ' 简装 ', ' 顶层(共6层) ', ' 2004年建 ', ' 板楼']
                    if len(L) >= 5:
                        #starp()方法处理字符串，括号中为空时，默认去除字符串中前后的空格
                        item['model']=L[0].strip()
                        item['area']=L[1].strip()
                        item['direction']=L[2].strip()
                        item['perfect']=L[3].strip()
                        item['floor']=L[4].strip()
                '''
                #地址
                address_list=h.xpath('.//div[@class="positionInfo"]/a/text()')
                item['address']=address_list[0].strip() if address_list else None
                #总价
                total_list1 = h.xpath('.//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()|.//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/i[2]/text()')
                total_list = ''.join(total_list1)

                item['total_list']=total_list.strip() if total_list else  None
                #单价
                price_list=h.xpath('.//div[@class="unitPrice"]/span/text()')
                item['price_list']=price_list[0].strip() if price_list else None
                print(item)

    #定义入口函数
    def run(self):
        begin = int(input('请输入查找链家二手房最新发布的起始页：'))
        stop = int(input('请输入链家二手房最新发布的结束页：'))
        # stop+1保证当结束页为1时，仍能取到整数
        #遍历页数，每遍历一次，执行一次整个函数
        for page in range(begin, stop + 1):
            #拼接url
            url=self.url.format(page)
            #调用解析函数
            self.parse_html(url)
            #每抓取一页随机sleep几秒
            time.sleep(random.randint(1, 3))

if __name__=='__main__':
    #初始化对象
    spider=LianjiaSpider()
    #调用函数
    spider.run()



