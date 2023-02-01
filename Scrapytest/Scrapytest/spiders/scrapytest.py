import scrapy

from ..items import ScrapytestItem


class ScrapytestSpider(scrapy.Spider):
    name = 'scrapytest'
    allowed_domains = ['c.biancheng.net']
    start_urls = ['http://c.biancheng.net/python_spider/scrapy-case.html']

    #用于解析提取数据的response会直接被传入parse解析模块，只需要对response进行解析就行

    def parse(self, response):
        #需要注意的是，crapy中xpath分析的是scrapy的response的数据，返回的是解析器列表
        #xpath函数返回的为列表，列表中存放的数据为Selector类型数据。解析到的内容被封装在Selector对象中，需要调用extract()函数将解析的内容从Selector中取出。
        #如果可以保证xpath返回的列表中只有一个列表元素，则可以使用extract_first(), 否则必须使用extract()
        result_1 = response.selector.xpath('/html/body/div[3]/div[2]/div/h1/text()')
        #extract使提取内容转换为Unicode字符串()
        result_2=response.selector.xpath('/html/body/div[3]/div[2]/div/h1/text()').extract()

        item=ScrapytestItem()
        item['title']=result_1
        item['info']=result_2

        yield item
        #print(item)

        #print(result_1)
        #print('-' * 60)
        #print(result_2)
        '''h_list = response.xpath('//*[@id="hotsearch-content-wrapper"]')
        for h in h_list():
            result_1 = h.xpath('//*[@class="title-content-title"]/test()').extract()
            result_2 = h.xpath('//*[@class="title-content-title"]/test()')
            print(result_1)
            print('-' * 60)
            print(result_2)'''

