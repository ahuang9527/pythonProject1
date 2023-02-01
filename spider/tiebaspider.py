import random
import time
from urllib import request, parse

from fake_useragent import UserAgent

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
class TiebaSpider(object):
    #初始化构造函数，并在构造函数中初始化url属性，便于类中调用
    def __init__(self):
        self.url='https://tieba.baidu.com/f?kw={}&tab=good&pn={}'
        #保留两个{}，用于之后fromat()传入输入参数

    #请求函数，得到页面
    def get_html(self,url):
        req=request.Request(url=url,headers={'user-agent':UserAgent().random})
        res=request.urlopen(req)
        html=res.read().decode("utf-8","ignore")
        return html

    #解析函数，暂时pass
    def parse_html(self):
        '''
        pattern=re.compile(r'<a rel.*?class="j_th_tit ">(.*?)<.*?title="主题作者:(.*?)".*?title="创建时间">(.*?)<',re.S)
        r_list=pattern.findall(html.read())
        for i in r_list:
        print(i)
        print(r_list)
        :return:
        '''

        pass

    #保存文件函数，保存为本地文件
    def save_html(self,filename,html):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    #类的入口函数
    def run(self):
        name=input('请输入贴吧名：')
        begin=int(input('请输入精品贴的起始页：'))
        stop=int(input('请输入精品贴的结束页：'))
        #stop+1保证当结束页为1时，仍能取到整数
        for page in range(begin,stop+1):
            pn=str((page-1)*50)


        #拼接url地址
            print(pn)
            params_name=parse.quote(name)
            params_page=parse.quote(pn)
            url=self.url.format(params_name,params_page)

            #已定义了url，调用get_html方法发送请求
            html=self.get_html(url)
            #定义存储路径（明天把路径改到硬盘里）
            filename='{}，吧的{}页内容'.format(name,page)
            self.save_html(filename,html)
            #提示
            print('第%d页抓取成功'%page)
            #每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1,2))

#启动爬虫
if __name__=='__main__':
    start=time.time()
    spider=TiebaSpider()
    #为该类实例化一个对象spider
    spider.run()
    #调用入口函数
    end=time.time()
    #查看程序执行时间
    print('执行时间:%.2f'%(end-start))
    #爬虫执行时间





