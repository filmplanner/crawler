BOT_NAME = 'Pathe'
SPIDER_MODULES = ['Pathe.spiders']
NEWSPIDER_MODULE = 'Pathe.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'Pathe.pipelines.MongoDBPipeline': 300,
}
LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 2

## MONGODB SETTINGS
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "pathe-server"
MONGODB_COLLECTION_THEATER = "theaters"
MONGODB_COLLECTION_MOVIE = "movies"
MONGODB_COLLECTION_SHOW = "shows"

## CUSTOM SETTINGS
BASE_URL = 'https://www.pathe.nl'

THEATER_NAME = 'theater'
WEEK_NAME = 'week'

WEEK_URL = 'https://www.pathe.nl/update-schedule/' # {theaterIds}/{date}
WEEK_CRAWL_UPDATE = 1 # Schedule update is on Monday
WEEK_CRAWL_START = 3 # Thursday
WEEK_CRAWL_DAYS = 6 # Thursday -> Wednesday

# CSS SELECTORS
SELECTORS = {
    # Theater
    'THEATER_LIST': '.nav-primary__has-sub.js-main-menu-left:nth-child(2) ul li a[href*="bioscoop/"]',
    'THEATER_HREF': '::attr(href)',
    'THEATER_ID': '.favoritebutton a:first-child::attr(data-cinema)',
    'THEATER_NAME': '.visual-cinema__location::text',
    'THEATER_CITY': '.visual-cinema__city::text',
    'THEATER_IMAGE': '#js-carousel-home .visual-home__item:first-child img::attr(src)',
    # Movie
    'MOVIE_LIST': '.schedule-default__item',
    'MOVIE_ID': '',
    'MOVIE_TITLE': '.schedule-default__figure a::attr(title)',
    'MOVIE_DESCRIPTION': '.schedule-default__synopsis p::text',
    'MOVIE_ADVISORY': '.schedule-default__icons li img::attr(src)',
    'MOVIE_IMAGE': '.schedule-default__figure img::attr(src)',
    'MOVIE_URL': '.schedule-default__figure a::attr(href)',
    'MOVIE_THEATER_LIST': '.schedule-table tr',
    'MOVIE_THEATER_NAME': 'th::text',
    # Show
    'SHOW_LIST': 'td form',
    'SHOW_TIMES': '.tooltip p',
    'SHOW_TYPE': 'a span:not(:first-child)::text',
    'SHOW_URL': '::attr(action)',  
}