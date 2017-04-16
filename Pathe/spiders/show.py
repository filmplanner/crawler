from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Movie, Show
from Pathe.helpers import DateHelper, DataHelper

class ShowSpider(Spider):
    name = SHOW_NAME

    def start_requests(self):
        url = SHOW_URL

        dataHelper = DataHelper(THEATER_FILE)
        theater_ids = dataHelper.to_string(dataHelper.get('id'))
        date = DateHelper.now()

        dateFlag = getattr(self, 'startdate', None)
        if dateFlag is not None: 
            date = DateHelper.strtodate(dateFlag)
            
        start_date = DateHelper.next_weekday(date, SHOW_CRAWL_DAY)
        end_date = DateHelper.add_days(start_date, SHOW_CRAWL_DAYS)

        for date in DateHelper.daterange(start_date, end_date):
            if date >= DateHelper.now():
                fullUrl = url + theater_ids + '/' + DateHelper.date(date)
                yield Request(fullUrl, self.parse)

    def parse(self, response):
        pass

    def parse_movie(self, response):
        pass

    def parse_show(self, response):
        pass

    def get(self, response, selector):
        return response.css(selector).extract_first()
