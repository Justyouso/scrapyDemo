import scrapy
from scrapyDemo.items import DianyingItem


class DianyingSpider(scrapy.Spider):
    name = "dianyingSpider"
    allowed_domians = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com"]

    def parse(self, response):
        print(response.status)
        print(response.xpath("//select/option/@value").extract())
        # for page in response.xpath("//select/option/@value").extract:
        #     url = "https://www.dy2018.com" + page
        #     yield scrapy.Request(url, callback=self.parseDetail)

    # def parseDetail(self, response):
    #     item = DianyingItem()
    #     content = response.xpath('//*[@id="Zoom"]')
    #     item["url"] = response.url
    #     item["title"] = content.xpath('/text()[2]').extract()
    #     item["magnet"] = content.xpath('//a/@href').extract()
    #     yield item
