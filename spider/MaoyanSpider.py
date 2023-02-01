import csv
import random
import re
import time
from urllib import request

from fake_useragent import UserAgent

#猫眼使用了反爬，使用JavaScript 加密，动态生成，等之后学习了JS逆向分析之后再进行重写此爬虫
'''
以面向对象方法编写爬虫程序时，思路简单、逻辑清楚，非常容易理解，上述代码主要包含了四个功能函数，它们分别负责了不同的功能，总结如下：
1) 请求函数
请求函数最终的结果是返回一个 HTML 对象，以方便后续的函数调用它。
2) 解析函数
解析函数用来解析 HTML 页面，常用的解析模块有正则解析模块、bs4 解析模块。通过分析页面，提取出所需的数据，在后续内容会做详细介绍。
3) 保存数据函数
该函数负责将抓取下来的数据保至数据库中，比如 MySQL、MongoDB 等，或者将其保存为文件格式，比如 csv、txt、excel 等。
4) 入口函数
入口函数充当整个爬虫程序的桥梁，通过调用不同的功能函数，实现数据的最终抓取。入口函数的主要任务是组织数据，比如要搜索的贴吧名、编码 url 参数、
拼接 url 地址、定义文件保存路径。 
'''
#定义一个爬虫类



class MaoyanSpider(object):
    #初始化
    #定义初始页面url
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'

    #请求函数
    def get_html(self,url):
        #print(url)
        req=request.Request(url=url,headers={'user-agent':UserAgent().random})
        res=request.urlopen(req)
        html=res.read().decode("utf-8","ignore")
        #将请求的结果直接调用解析函数
        self.parse_html(html)
        #print(html)
    #解析函数
    def parse_html(self,html):
        #解析html的正则表达式
        re_html= '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        #生成正则表达式对象
        pattern=re.compile(re_html,re.S)
        #根据正则表达式匹配字符串内容
        r_list=pattern.findall(html)
        #将解析的结果直接调用保存函数
        self.save_html(r_list)
        print(r_list)

    #保存函数,，使用python内置的csv模块
    def save_html(self,r_list):
        #生成文件对象
        with open('maoyan.csv', 'a', newline='', encoding="utf-8") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            # 整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                # 上映时间：2018-07-05
                # 切片截取时间
                time = r[2].strip()[5:15]
                L = [name, star, time]
                # 写入csv文件
                writer.writerow(L)
                print(name, time, star)
        # 主函数

    def run(self):
        # 抓取第一页数据
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))
        # 以脚本方式启动

if __name__ == '__main__':
        # 捕捉异常错误

    try:
        spider=MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:", e)



