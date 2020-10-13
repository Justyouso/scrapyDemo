import scrapy
from scrapyDemo.items import DianyingItem


class DianyingSpider(scrapy.Spider):
    name = "dianyingSpider"
    allowed_domians = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com/html/gndy/dyzz/index.html"]

    def parse(self, response):
        # print("*" * 40)
        # print("response text: %s" % response.text)
        # print("response headers: %s" % response.headers)
        # print("response meta: %s" % response.meta)
        # print("request headers: %s" % response.request.headers)
        # print("request cookies: %s" % response.request.cookies)
        # print("request meta: %s" % response.request.meta)
        for page in response.xpath("//select/option/@value").extract():
            url = "https://www.dy2018.com" + page
            yield scrapy.Request(url, callback=self.parseDetail)

    def parseDetail(self, response):
        item = DianyingItem()
        content = response.xpath('//*[@id="Zoom"]')
        item["url"] = response.url
        item["title"] = content.xpath('/text[4]').extract()
        item["magnet"] = content.xpath('//a/@href').extract()
        yield item
