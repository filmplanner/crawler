from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Theater
from Pathe.helpers import SelectHelper

class TheaterSpider(Spider):
    name = THEATER_NAME
    start_urls = [BASE_URL]

    def parse(self, res):
        for item in res.css(SELECTORS['THEATER_LIST']):
            url = SelectHelper.get(item, SELECTORS['THEATER_HREF'])
            yield Request(url, self.parse_theater)

    def parse_theater(self, res):
        obj = {
            'id': int(SelectHelper.get(res, SELECTORS['THEATER_ID'])),
            'name': SelectHelper.get(res, SELECTORS['THEATER_NAME']),
            'city': SelectHelper.get(res, SELECTORS['THEATER_CITY']),
            'image': SelectHelper.get(res, SELECTORS['THEATER_IMAGE']),
        }
        return Theater(obj)