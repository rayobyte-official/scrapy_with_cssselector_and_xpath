import scrapy


class PlzscrapeXpathSpider(scrapy.Spider):
    name = "plzscrape_xpath"
    allowed_domains = ["plzscrape.com"]
    start_urls = ["https://plzscrape.com/basic/xpath-selectors"]

    def parse(self, response):
        main_heading = response.xpath('//h1[@class="mt-5 text-center text-primary"]/text()').get()
        
        for product in response.xpath('//div[contains(@class, "card shadow-sm")]'):
            yield {
                'title': product.xpath('.//h2[@class="card-title"]/text()').get(),
                'description': product.xpath('.//p[@class="card-text"]/text()').get(),
                'price': product.xpath('.//span[@class="price"]/text()').get(),
                'reviews': product.xpath('.//div[@class="review"]/text()').get().strip(),
                'main_heading': main_heading
            }