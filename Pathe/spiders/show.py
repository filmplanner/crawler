from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Movie, Show
from Pathe.helpers import DateHelper

class ShowSpider(Spider):
    name = "show"

    def start_requests(self):
        url = SHOW_URL

        theater_ids = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20,22,23,27,28,29,30,31' # TODO: Dynamically get Theater IDS
        date = DateHelper.now()

        dateFlag = getattr(self, 'startdate', None)
        if dateFlag is not None: 
            date = DateHelper.strtodate(dateFlag)
            
        start_date = DateHelper.next_weekday(date, WD_THURSDAY)
        end_date = DateHelper.add_days(start_date, 6)

        for date in DateHelper.daterange(start_date, end_date):
            if date >= DateHelper.now():
                fullUrl = url + theater_ids + '/' + DateHelper.date(date)
                yield Request(fullUrl, self.parse)

    def parse(self, response):
        self.logger.info('test')

    def get(self, response, selector):
        return response.css(selector).extract_first()
