#coding:utf8
import random
import time

import requests
from fake_useragent import UserAgent
from lxml import etree

'''
用xpath写了一半发现，类型需要再从values中再截取，不如正则表达式re方便，但是出于练习还是用xpath写了
但是等结束之后会将正则re的方式写入最下方的备注中
抓取动态页面与二级页面的练习，使用xpath解析
1.从一级页面获取二级页面的url
2.根据输入的类型获得对应页面的url
3.解析对应页面的json抓包地址

通过观察可知，电影详细信息通过异步加载的形式访问
剧情
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20

爱情
https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20
https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=20&limit=20
通过观察url可知，由type，start两个参数控制访问
构建的params参数查询时，只有type类型，与start两个参数是需要变动的
type为每个电影的类型，通过解析一级页面中的访问二级页面url得到type
start为开始长度，控制页面的加载，规律为(n-1)*20

'''


class DoubanSpider(object):
    def __init__(self):
        #要查询数据的url，调用时直接拼接params参数查询
        self.url='https://movie.douban.com/j/chart/top_list?'
        self.i=0
    #获取页面
    def get_html(self,url):
        res=requests.get(url=url,headers={'user-agent': UserAgent().random},timeout=3)
        html=res.text
        return html

    #获取get请求带params的页面
    def get_page(self,params):
        #将json格式的响应体进行反序列化为python字典
        html=requests.get(url=self.url,headers={'user-agent': UserAgent().random},params=params).json()
        self.parse_html(html)

    #解析函数,解析字典列表，得到要提取的数据
    def parse_html(self,html):
        #此处使用三个固定keys，每次遍历更新字典，如果有需要可以改为持久化存储，保留所有的数据
        item={}
        for one in html:
            item['电影名称']=one['title']
            item['电影评分']=one['score']
            item['豆瓣链接']=one['url']
            print(item)
            self.i += 1

    # 获取电影总数
    def total_number(self, type_number):
        # F12抓包抓到的地址，type表示电影类型
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        #反序列化——将json格式字符串转换成python字典，用于对其进行分析和处理。json.loads()
        #而在requests库中，不用json.loads方法进行反序列化，而是提供了响应对象的json方法.json()，用来对json格式的响应体进行反序列化为python字典
        # 得到json数据方案一 通过python内置的json模块
        # result = json.loads(response.text)
        # 得到json数据方案二 通过requests提供的得到json数据的方式
        html = requests.get(url=url, headers={'user-agent': UserAgent().random}).json()
        total = int(html['total'])
        return total

    #获取一级页面中的类型与对应的二级页面拼接url
    def get_all_film_type(self):
        url='https://movie.douban.com/chart'
        html=self.get_html(url)
        # 调用etree模块的HTML()方法来创建html解析对象
        p = etree.HTML(html)
        h_list=p.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/a')
        #print(h_list) a
        #h_list得到含有是所有要爬取内容列表的基准表达式
        #遍历该表达式并将名称url传入字典item中，方便后续调用
        item = {}
        for h in h_list:

            h_name=h.xpath('text()')
            h_href=h.xpath('@href')
            item[h_name[0]]=h_href[0]
        #print(item.keys())
        #当调用该函数最后返回字典
        return item







    #定义入口函数
    def run(self):
        #self.get_all_film_type()
        #调用函数get_all_film_type()并将返回值传给menu,制作菜单
        a=self.get_all_film_type()
        print("----------------------------------------------")
        for menu in a.keys():
            print(menu,end=' |')
        print("\n----------------------------------------------")
        film=input("上述为菜单，请输入您想要的电影类型:")
        #通过输入的名称keys得到values，再通过values截取得到对应类型的url_type
        film_type=str(a[film])
        url_type_1=film_type.index('type=')
        url_type_2=film_type.index('&interval')
        type_number=film_type[url_type_1+5:url_type_2]
        #print(url_type)
        total=self.total_number(type_number)
        for start in range(0,(total+1),20):
            #构建get请求的查询params参数
            params = {
                'type': type_number,
                'interval_id': '100:90',
                'action': '',
                'start': start,
                'limit': '20'
            }
            self.get_page(params)
            time.sleep(random.randint(1,2))
        #%d占位符
        print('电影总数:%d'%self.i)





if __name__=='__main__':
    #初始化对象
    spider=DoubanSpider()
    #调用函数
    spider.run()

