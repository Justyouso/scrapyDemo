import scrapy
from scrapyDemo.items import ScrapydemoItem


class NextSpiderSpider(scrapy.Spider):
    name = "nextSpider1"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        content = response.css('div.quote')  # 提取首页所有名言，保存至变量content
        for v in content:  # 循环获取每一条名言里面的：名言内容、作者、标签
            text = v.css('.text::text').extract_first()  # 提取名言
            author = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            item = ScrapydemoItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()  # css选择器提取下一页链接
        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
