import scrapy
from mapfinder.items import NapiaItem


class NapiaSpider(scrapy.Spider):
    name = "napia"
    allowed_domains = ["napia.com"]
    start_urls = ["https://www.napia.com/Custom_MemberDirectory.asp?pagesize=200&version=1&keyword=&intpage=1&page=1&dlist=-1&city=&state=&zip=&country=",
                  "https://www.napia.com/Custom_MemberDirectory.asp?version=1&pagesize=200&keyword=&intpage=2&page=1&dlist=-1&city=&state=&zip=&country="]

    def parse(self, response):
        for i in response.xpath('//table[@class="width-max"]'):
            item = NapiaItem()
            link = i.xpath(".//a[contains(@href, 'af_directory.asp?memberid=')]/@href").get()
            item['link'] = f'https://www.napia.com/{link}'
            item['name'] = i.xpath(".//a[contains(@href, 'af_directory.asp?memberid=')]//font/text()").get()
            item['email'] = i.xpath(".//a[contains(@href, 'javascript')]/text()").get()
            yield item
