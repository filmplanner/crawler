from scrapy import Spider, Request
from Filmplanner.settings import *
from Filmplanner.items import Theater
from Filmplanner.helpers import SelectHelper

class TheaterSpider(Spider):
    name = 'theater'
    start_urls = [BASE_URL]

    def parse(self, res):
        for item in res.css(SELECTORS['THEATER_LIST']):
            url = SelectHelper.get(item, SELECTORS['THEATER_HREF'])
            yield Request(BASE_URL + url, self.parse_theater)

    def parse_theater(self, res):
        obj = {
            'id': SelectHelper.get(res, SELECTORS['THEATER_ID']),
            'name': SelectHelper.get(res, SELECTORS['THEATER_NAME']),
            'city': SelectHelper.get(res, SELECTORS['THEATER_CITY']),
            'image': SelectHelper.get(res, SELECTORS['THEATER_IMAGE']),
        }
        return Theater(obj)