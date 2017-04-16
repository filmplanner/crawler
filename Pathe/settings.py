BOT_NAME = 'Pathe'
SPIDER_MODULES = ['Pathe.spiders']
NEWSPIDER_MODULE = 'Pathe.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'Pathe.pipelines.JsonExportPipeline': 300,
}

## CUSTOM SETTINGS
BASE_URL = 'https://www.pathe.nl'

THEATER_NAME = 'theater'
THEATER_FILE = 'theater_items.json'

SHOW_NAME = 'show'
SHOW_URL = 'https://www.pathe.nl/update-schedule/' # {theaterIds}/{date}
SHOW_CRAWL_DAY = 3 # Thursday
SHOW_CRAWL_DAYS = 6 # Thursday -> Wednesday

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
    'MOVIE_IMAGE': '.schedule-default__figure img::attr(src)',
    'MOVIE_URL': '.schedule-default__figure a::attr(href)',
    'MOVIE_THEATER_LIST': '.schedule-table tr',
    'MOVIE_THEATER_NAME': 'th::text',
    # Show
    'SHOW_LIST': 'td form',
    'SHOW_START': 'a span:first-child::text', 
    'SHOW_END': '',
    'SHOW_TYPE': 'a span:nth-child(2)::text',
    'SHOW_URL': '::attr(action)',  
}