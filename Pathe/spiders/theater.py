from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Theater

class TheaterSpider(Spider):
    name = THEATER_NAME
    start_urls = [BASE_URL]

    def parse(self, response):
        for item in response.css(SELECTORS['THEATER_LIST']):
            url = self.get(item, SELECTORS['THEATER_HREF'])
            yield Request(url, self.parse_theater)

    def parse_theater(self, response):
        obj = {
            'id': self.get(response, SELECTORS['THEATER_ID']),
            'name': self.get(response, SELECTORS['THEATER_NAME']),
            'city': self.get(response, SELECTORS['THEATER_CITY']),
            'image': self.get(response, SELECTORS['THEATER_IMAGE']),
        }
        return Theater(obj)

    def get(self, response, selector):
        return response.css(selector).extract_first()