from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Theater

class TheaterSpider(Spider):
    name = "theater"
    start_urls = [BASE_URL]

    def parse(self, response):
        for items in response.css(THEATER_SELECTOR['LIST']):
            url = self.get(items, THEATER_SELECTOR['LIST_HREF'])
            yield Request(url, self.parse_theater)

    def parse_theater(self, response):
        obj = {
            'id': self.get(response, THEATER_SELECTOR['ID']),
            'name': self.get(response, THEATER_SELECTOR['NAME']),
            'city': self.get(response, THEATER_SELECTOR['CITY']),
            'image': self.get(response, THEATER_SELECTOR['IMAGE']),
        }
        
        # store theater object
        yield Theater(obj)

    def get(self, response, selector):
        return response.css(selector).extract_first()