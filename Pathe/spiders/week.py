from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Movie, Show
from Pathe.helpers import SelectHelper, DateHelper, MongoDBHelper

class WeekSpider(Spider):
    name = WEEK_NAME

    def start_requests(self):
        base_url = WEEK_URL
        self.db_helper = MongoDBHelper()
        self.theaters = self.db_helper.get(MONGODB_COLLECTION_THEATER)
        
        # get spider parameters
        theater_ids = ','.join(self.db_helper.get_attr(self.theaters, 'id'))
        date = DateHelper.now()
        
        # get date flag from shell command
        date_flag = getattr(self, 'start', None)
        if date_flag is not None: 
            date = DateHelper.strtodate(date_flag)

        # get spider date range
        date = DateHelper.prev_weekday(date, WEEK_CRAWL_UPDATE)    
        start_date = DateHelper.next_weekday(date, WEEK_CRAWL_START)
        end_date = DateHelper.add_days(start_date, WEEK_CRAWL_DAYS)

        if end_date < DateHelper.now():
            self.logger.info('Cannot crawl data from the past!')
            return
        if date > DateHelper.prev_weekday(DateHelper.now(), WEEK_CRAWL_UPDATE):
            self.logger.info('This week is not (yet) scheduled by Pathe.nl')
            return
            
        # add requests from start to end date
        for date in DateHelper.daterange(start_date, end_date):
            if date >= DateHelper.now():
                url = base_url + theater_ids + '/' + DateHelper.date(date)
                request = Request(url, self.parse)
                request.meta['date'] = DateHelper.date(date)
                yield request

        # close MongoDB connection
        self.db_helper.close()

    def parse(self, res):
        date = res.meta['date']
        for movie_item in res.css(SELECTORS['MOVIE_LIST']):
            movie = self.parse_movie(movie_item)
            yield movie

            for theater_item in movie_item.css(SELECTORS['MOVIE_THEATER_LIST']):
                theater = self.db_helper.get_by(self.theaters, 'name', SelectHelper.get(theater_item, SELECTORS['MOVIE_THEATER_NAME']))

                for show_item in theater_item.css(SELECTORS['SHOW_LIST']):
                    show = self.parse_show(show_item, date, movie['id'], theater['id'])   
                    yield show     

    def parse_movie(self, res):
        url = res.css(SELECTORS['MOVIE_URL'])
        obj = {
            'id': url.re_first(r'[/]([0-9]{1,})[/]'),
            'title': SelectHelper.get(res, SELECTORS['MOVIE_TITLE']),
            'description': SelectHelper.get(res, SELECTORS['MOVIE_DESCRIPTION']), 
            'image': SelectHelper.get(res, SELECTORS['MOVIE_IMAGE']), 
            'url': BASE_URL + url.extract_first(),    
        }    
        return Movie(obj)

    def parse_show(self, res, date, movie_id, theater_id):
        times = res.css(SELECTORS['SHOW_TIMES']).re(r'[0-9]{1,2}[:][0-9]{2}')
        obj = {
            'date': date, 
            'movie_id': movie_id,
            'theater_id': theater_id,
            'start': times[0], 
            'end': times[1],
            'type': SelectHelper.get(res, SELECTORS['SHOW_TYPE']),
            'url': BASE_URL + SelectHelper.get(res, SELECTORS['SHOW_URL']),    
        }
        return Show(obj)
        

