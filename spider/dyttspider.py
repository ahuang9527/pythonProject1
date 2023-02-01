# -*- coding: utf-8 -*-
import re
import time
from urllib import request

from fake_useragent import UserAgent

'''
这是参考网络例子写的电影天堂爬虫，目的是爬取电影简介信息，照片与下载链接
练习的内容为抓取多级页面数据与抓取网络照片
1) 请求函数
2) 解析函数
3) 保存数据函数
4) 入口函数
'''


class DyttSpider(object):
    #初始化自动调用的构造方法
    def __init__(self):
        self.url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

    #定义请求函数
    def get_html(self,url):
        req = request.Request(url=url, headers={'user-agent': UserAgent().random})
        res = request.urlopen(req)
        html = res.read().decode("gb2312", "ignore")
        return html

    #正则解析函数,传入正则表达式与要解析的对应html内容
    def re_func(self,re_bds,html):
        #生成正则表达式对象
        pattern=re.compile(re_bds,re.S)
        #根据正则表达式匹配传入的内容
        r_list=pattern.findall(html)

        return r_list

    #提取数据函数，从一级页面提取二级页面的url信息
    def first_html(self,one_url):
        #根据传入的one_url参数，调用请求函数，获取一级页面
        one_html=self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        #有html与正则表达式后，调用解析函数得到二级页面的访问地址
        link_list=self.re_func(re_bds,one_html)
        print(link_list)
        for link in link_list:
            two_url='https://www.dytt8.net' + link
            #直接调用二级页面解析函数
            print(two_url)
            self.second_html(two_url)

    #解析二级页面，获取数据（名称与下载链接）
    def second_html(self,two_url):
        two_html=self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<a.*?target="_blank" href="(.*?)".*?>.*?style="BACKGROUND-COLOR:.*?</a>'
        #有html与正则表达式后，调用解析函数得到二级页面中的电影名称与下载链接
        film_list=self.re_func(re_bds,two_html)
        print(film_list)

    #定义存储函数
    def save_html(self,filename,html):
        pass

    #主函数
    def run(self):
        begin=int(input('请输入要爬取电影天堂最新的起始页：'))
        stop=int(input('请输入要爬取电影天堂最新电影的结束页：'))
        #stop加一避免结束页为第一页
        for page in range(begin,stop+1):
            url=self.url.format(page)
            self.first_html(url)
            #提示
            print('第%d页抓取成功'%page)

#以脚本的形式启动爬虫
if __name__=='__main__':
    start=time.time()
    spider=DyttSpider() #实例化一个对象spider
    spider.run() #调用入口函数
    end=time.time()
    #查看程序执行时间
    print('执行时间:%.2f'%(end-start))  #爬虫执行时间

