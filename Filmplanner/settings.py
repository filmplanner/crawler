BOT_NAME = 'Filmplanner'
SPIDER_MODULES = ['Filmplanner.spiders']
NEWSPIDER_MODULE = 'Filmplanner.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {		
    'Filmplanner.pipelines.JsonPipeline': 300,		
}
LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 2

## CUSTOM SETTINGS
BASE_URL = 'https://www.pathe.nl'
WEEK_URL = 'https://www.pathe.nl/update-schedule/' # {theaterIds}/{date}
WEEK_CRAWL_UPDATE = 1 # Pathe updates schedules on Monday
WEEK_CRAWL_START = 3 # Thursday
WEEK_CRAWL_DAYS = 6 # Thursday -> Wednesday

# CSS SELECTORS
SELECTORS = {
    # Theater
    'THEATER_LIST': '.nav-primary__item.nav-primary__item--has-sub:nth-child(2) ul li a[href*="bioscoop/"]',
    'THEATER_HREF': '::attr(href)',
    'THEATER_ID': '.tabs-wrapper--schedule ul li:first-child a::attr(data-cinema-id)',
    'THEATER_NAME': '.visual-cinema__location::text',
    'THEATER_CITY': '.visual-cinema__city::text',
    'THEATER_IMAGE': '.visual-fullpage__slideshow .visual-fullpage__slide:first-child img::attr(src)',
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