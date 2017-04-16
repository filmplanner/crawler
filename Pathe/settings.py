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

## THEATER CSS SELECTORS
THEATER_SELECTOR = {
    'LIST': '.nav-primary__has-sub.js-main-menu-left:nth-child(2) ul li a[href*="bioscoop/"]',
    'LIST_HREF': '::attr(href)',
    'ID': '.favoritebutton a:first-child::attr(data-cinema)',
    'NAME': '.visual-cinema__location::text',
    'CITY': '.visual-cinema__city::text',
    'IMAGE': '#js-carousel-home .visual-home__item:first-child img::attr(src)',
}

SHOW_NAME = 'show'
SHOW_URL = 'https://www.pathe.nl/update-schedule/' # {theaterIds}/{date}
SHOW_CRAWL_DAY = 3 # Thursday
SHOW_CRAWL_DAYS = 6 # Thursday -> Wednesday

## SHOW CSS SELECTORS
SELECTOR_SHOW = {}