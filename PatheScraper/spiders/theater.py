import scrapy
from PatheScraper.items import Theater

class TheaterSpider(scrapy.Spider):
    name = "theater"
    start_urls = ['https://www.pathe.nl']

    def parse(self, response):
        ## Get all theater URLs
        cinemaselector = '.nav-primary__has-sub.js-main-menu-left:nth-child(2) ul li a[href*="bioscoop/"]'
        for items in response.css(cinemaselector):
            ## Parse Theater objects
            url = items.css('::attr(href)').extract_first()
            yield scrapy.Request(url, self.parse_theater)

    def parse_theater(self, response):
        id = response.css('.favoritebutton a:first-child::attr(data-cinema)').extract_first()
        name = response.css('.visual-cinema__location::t    ext').extract_first()
        city = response.css('.visual-cinema__city::text').extract_first()
        image = response.css('#js-carousel-home .visual-home__item:first-child img::attr(src)').extract_first()
