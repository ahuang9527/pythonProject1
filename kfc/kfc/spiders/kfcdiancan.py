import scrapy


class KfcdiancanSpider(scrapy.Spider):
    name = 'kfcdiancan'
    allowed_domains = ['www.kfc.com.cn']
    # scrapy默认请求为get请求
    # 这次需要使用post请求 如果没有参数 那么这个请求将没有任何意义
    # 所以start_urls 也没有用了
    # parse方法也没有用了
    #start_urls = ['http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword']
    kw = input('请输入要查询的城市：')
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    #重写start_requests方法
    def start_requests(self):


        data = {
            'cname': '',
            'pid': '',
            'keyword': self.kw,
            'pageIndex': '1',
            'pageSize': '10'
        }

        yield scrapy.FormRequest(url=self.url,formdata=data,callback=self.second_parse)

    def second_parse(self, response):

        #将post请求得到的json字符串转为python字典
        #html=requests.post(url=self.start_urls,params=params,headers={'user-agent': UserAgent().random}).json()
        #yield scrapy.Request(url=self.start_urls, callback=self.parse)
        html=response.json()
        #print(html['Table1'])

