from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Theater

class TheaterSpider(Spider):
    name = "theater"
    start_urls = [BASE_URL]

    def parse(self, response):
        for items in response.css(SELECTOR_THEATER['LIST']):
            url = self.get(items, SELECTOR_THEATER['LIST_HREF'])
            yield Request(url, self.parse_theater)

    def parse_theater(self, response):
        obj = {
            'id': self.get(response, SELECTOR_THEATER['ID']),
            'name': self.get(response, SELECTOR_THEATER['NAME']),
            'city': self.get(response, SELECTOR_THEATER['CITY']),
            'image': self.get(response, SELECTOR_THEATER['IMAGE']),
        }
        
        # store theater object
        yield Theater(obj)

    def get(self, response, selector):
        return response.css(selector).extract_first()