import requests
from fake_useragent import UserAgent

class SougouSpider():
    #初始化
    def __init__(self):
        self.url='https://www.sogou.com/web'

    #请求函数
    def get_html(self):
        #input('prompt') prompt :提示信息
        kw=input('请输入要搜索的内容:')
        #此处可使用page += 1,一直请求完所有的页数
        page=input('请输入要搜索的页数')
        #params,get请求带上参数
        param={
            'query':kw,
            'page':page
        }
        res=requests.get(url=self.url,params=param,headers={'user-agent': UserAgent().random},timeout=1)
        html=res.text
        file_name=kw+'.html'
        with open(file_name,'w',encoding='utf-8') as f:
            f.write(html)
        print(file_name+'保存成功')



    #定义入口函数
    def run(self):
        self.get_html()


if __name__=='__main__':
    #初始化对象
    spider=SougouSpider()
    #调用函数
    spider.run()