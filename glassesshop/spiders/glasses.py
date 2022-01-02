import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers',callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        })

    def parse(self, response):
        glasses =response.xpath("//div[@id='product-lists']/div")
        for glasses_ in glasses:
            yield{
                'url': glasses_.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'image_url': glasses_.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'product_name': glasses_.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'price': glasses_.xpath(".//div[@class='p-price']//span/text()").get(),
                # 'User-Agent': response.request.headers['User-Agent']
                }
        next_page = response.xpath(
            "//lu[@class='pagination']/li[position()=last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse,headers={
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
                })

            