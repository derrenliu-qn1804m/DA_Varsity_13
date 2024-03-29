#Imports scrapy package
import scrapy


#Scrap all image links on website
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/varsity']
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                    'Image Link': x.xpath(newsel).extract_first(),
            }
# To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page is not None:
            yield scrapy.Request(
            response.urljoin(next_page), callback=self.parse
            )











