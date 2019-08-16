import scrapy


class varsity(scrapy.Spider):
    name = "new_varsity"
    start_urls = [
        'http://172.18.58.238/varsity/',
    ]

    def parse(self, response):
                css_selector = 'img'
                for x in response.css(css_selector):
                            newsel= '@src'
                            yield{
                                'image link':x.xpath(newsel).extract_first()
                            }
                Page_selector = '.next a ::attr(href)'
                next_page = response.css(Page_selector).extract_first()
                if next_page:
                    yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                    )