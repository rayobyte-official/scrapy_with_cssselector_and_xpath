import scrapy


class PlzscrapeCssselectorSpider(scrapy.Spider):
    # Spider name
    name = "plzscrape_cssselector"
    # Allowed domain
    allowed_domains = ["plzscrape.com"]
    # start urls
    start_urls = ["https://plzscrape.com/basic/css-selectors"]

    def parse(self, response):
        # Extracting the main heading
        main_heading = response.css('h1.text-primary::text').get()
        
        # Extracting the articles
        for article in response.css('.card'):
            yield {
                'title': article.css('h2.card-title::text').get(),
                'description': article.css('p.card-text::text').get(),
                'image_src': article.css('img.card-img-top::attr(src)').get(),
                'main_heading': main_heading
            }
