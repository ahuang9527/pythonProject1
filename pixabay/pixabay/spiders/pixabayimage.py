import scrapy

from ..items import PixabayItem


class PixabayimageSpider(scrapy.Spider):
    name = 'pixabayimage'
    allowed_domains = ['pixabay.com']
    start_urls = ['http://pixabay.com/']
    url='https://pixabay.com/images/search/?order=ec&pagi={}'

    page=3
    #没写好，导致重复调用，还好scrapy默认有去重
    #page=int(input('请输入要爬取的页数:'))
    #自增爬取所有图片
    #page+=1

    def parse(self, response):
        #遍历得到基准表达式
        li_list=response.xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div/div/a')
        #将item中的类实例化
        item=PixabayItem()
        item={}
        #遍历基准表达式得到值写入字典item中
        for h in li_list:
            href_list=h.xpath('.//img/@src').extract()
            item['href']=href_list[0] if href_list else None
            type_list=h.xpath('.//img/@alt').extract()
            item['type']=type_list[0] if type_list else None
            #print(href_list)
            yield item


        for i in range(1,self.page+1 ):
            new_url = self.url.format(i)
            yield scrapy.Request(url=new_url,callback=self.parse)
