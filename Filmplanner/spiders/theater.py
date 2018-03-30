from scrapy import Spider, Request
from Filmplanner.settings import *
from Filmplanner.items import Theater
from Filmplanner.helpers import SelectHelper

class TheaterSpider(Spider):
    """Spider to crawl all theaters from Pathe.nl"""
    name = THEATER_NAME
    start_urls = [BASE_URL]

    def parse(self, res):
        """Parses result from crawled URLs"""
        for item in res.css(SELECTORS['THEATER_LIST']):
            url = SelectHelper.get(item, SELECTORS['THEATER_HREF'])
            yield Request(url, self.parse_theater)

    def parse_theater(self, res):
        """Parses result to create a Theater item from crawled URL"""
        obj = {
            'id': int(SelectHelper.get(res, SELECTORS['THEATER_ID'])),
            'name': SelectHelper.get(res, SELECTORS['THEATER_NAME']),
            'city': SelectHelper.get(res, SELECTORS['THEATER_CITY']),
            'image': SelectHelper.get(res, SELECTORS['THEATER_IMAGE']),
        }
        return Theater(obj)