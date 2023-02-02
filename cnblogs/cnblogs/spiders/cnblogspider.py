import scrapy

from ..items import CnblogsItem


class CnblogspiderSpider(scrapy.Spider):
    name = 'cnblogspider'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']
    #scrapy启动时默认会使用start_urls中的url去调用默认的start_request方法，然后将返回的响应response传给默认的parse解析函数。
    #如果有特殊需要，可以重写上述的方法进而达成需求

    def parse(self, response):
        #实例化item对象
        item=CnblogsItem()
        #xpath提取标题
        item['title']=response.xpath('//*[@id="post_list"]/article/section/div/a/text()').extract()
        #xpath提取链接
        item['href']=response.xpath('//*[@id="post_list"]/article/section/div/a/@href').extract()

        #将item传递给pipeline处理
        print(item)
        yield item