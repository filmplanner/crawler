import scrapy
import Pathe.settings
from Pathe.items import Theater
from Pathe.settings import *

class TheaterSpider(scrapy.Spider):
    name = "theater"
    start_urls = [BASE_URL]

    def parse(self, response):
        ## Get all theater URLs
        for items in response.css(SELECTOR_THEATER['LIST']):
            ## Parse Theater objects
            url = self.get(items, SELECTOR_THEATER['LIST_HREF'])
            yield scrapy.Request(url, self.parse_theater)

    def parse_theater(self, response):
        id = self.get(response, SELECTOR_THEATER['ID'])
        name = self.get(response, SELECTOR_THEATER['NAME'])
        city = self.get(response, SELECTOR_THEATER['CITY'])
        image = self.get(response, SELECTOR_THEATER['IMAGE'])
    
    def get(self, response, selector):
        return response.css(selector).extract_first()