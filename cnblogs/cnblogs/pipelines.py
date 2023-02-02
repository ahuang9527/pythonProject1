import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#配置管道写入csv文件

class CnblogsPipeline:
    def __init__(self):
        self.f = open('Cnblogs.csv','w',encoding='utf-8',newline='')       # line1
        self.file_name = ['title', 'href']  # line2
        self.writer = csv.DictWriter(self.f, fieldnames=self.file_name)     # line3
        self.writer.writeheader()


    def process_item(self, item, spider):
        self.writer.writerow(dict(item))
        return item

    #关闭文件
    def close_spider(self,spider):
        self.f.close()