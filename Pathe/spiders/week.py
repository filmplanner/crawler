from scrapy import Spider, Request
from Pathe.settings import *
from Pathe.items import Movie, Show 
from Pathe.helpers import SelectHelper, DateHelper, MongoDBHelper

class WeekSpider(Spider):
    """Spider to crawl week schedule from Pathe.nl"""
    name = WEEK_NAME

    def start_requests(self):
        """Initializes the URL's that need to be parsed"""
        base_url = WEEK_URL
        self.db_helper = MongoDBHelper(self.crawler.settings.get('MONGODB_URI'))
        self.theaters = self.db_helper.get(MONGODB_COLLECTION_THEATER)
        
        # get theater ids
        theater_ids = ','.join(str(x) for x in self.db_helper.get_attr(self.theaters, '_id'))

        # get crawl dates
        today = DateHelper.now()
        update_date = DateHelper.prev_weekday(today, WEEK_CRAWL_UPDATE)           
        start_date = DateHelper.next_weekday(update_date, WEEK_CRAWL_START)
        end_date = DateHelper.add_days(start_date, WEEK_CRAWL_DAYS)        
                
        # add requests from start to end date
        self.logger.info("Scraping schedule from " + str(today) + " - " + str(end_date))
        for date in DateHelper.daterange(today, end_date):
            url = base_url + theater_ids + '/' + DateHelper.date(date)
            request = Request(url, self.parse)
            request.meta['date'] = DateHelper.date(date)
            yield request

        # close MongoDB connection
        self.db_helper.close()

    def parse(self, res):
        """Parses result from crawled URLs"""
        date = res.meta['date']
        for movie_item in res.css(SELECTORS['MOVIE_LIST']):
            movie = self.parse_movie(movie_item)
            yield movie

            for theater_item in movie_item.css(SELECTORS['MOVIE_THEATER_LIST']):
                theater = self.db_helper.get_by(self.theaters, 'name', SelectHelper.get(theater_item, SELECTORS['MOVIE_THEATER_NAME']))

                for show_item in theater_item.css(SELECTORS['SHOW_LIST']):
                    show = self.parse_show(show_item, date, movie['_id'], theater['_id'])
                    yield show

    def parse_movie(self, res):
        """Parses result to create a Movie item from crawled URL"""
        url = res.css(SELECTORS['MOVIE_URL'])
        obj = {
            '_id': int(url.re_first(r'[/]([0-9]{1,})[/]')),
            'title': SelectHelper.get(res, SELECTORS['MOVIE_TITLE']),
            'description': SelectHelper.get(res, SELECTORS['MOVIE_DESCRIPTION']),
            'advisory': SelectHelper.get_array(res, SELECTORS['MOVIE_ADVISORY']),
            'image': SelectHelper.get(res, SELECTORS['MOVIE_IMAGE']),
            'url': BASE_URL + url.extract_first(),    
        }    
        return Movie(obj)

    def parse_show(self, res, date, movie_id, theater_id):
        """Parses result to create a Show item from crawled URL"""
        times = res.css(SELECTORS['SHOW_TIMES']).re(r'[0-9]{1,2}[:][0-9]{2}')
        obj = {
            'movie_id': movie_id,
            'theater_id': theater_id,
            'date': DateHelper.strtodatetime(date),
            'start': DateHelper.strtoseconds(times[0]),
            'end': DateHelper.strtoseconds(times[1]),
            'type': SelectHelper.get_array(res, SELECTORS['SHOW_TYPE']),
            'url': BASE_URL + SelectHelper.get(res, SELECTORS['SHOW_URL']),
        }
        return Show(obj)
        

