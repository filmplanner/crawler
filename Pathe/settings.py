BOT_NAME = 'Pathe'
SPIDER_MODULES = ['Pathe.spiders']
NEWSPIDER_MODULE = 'Pathe.spiders'
ROBOTSTXT_OBEY = True
#FEED_FORMAT = "json"
#FEED_URI = 'output/%(name)s.json'

## CUSTOM SETTINGS
BASE_URL = 'https://www.pathe.nl'
SHOW_URL = 'https://www.pathe.nl/update-schedule/' # {theaterIds}/{date}
WD_THURSDAY = 3

## THEATER CSS SELECTORS
SELECTOR_THEATER = {
    'LIST': '.nav-primary__has-sub.js-main-menu-left:nth-child(2) ul li a[href*="bioscoop/"]',
    'LIST_HREF': '::attr(href)',
    'ID': '.favoritebutton a:first-child::attr(data-cinema)',
    'NAME': '.visual-cinema__location::text',
    'CITY': '.visual-cinema__city::text',
    'IMAGE': '#js-carousel-home .visual-home__item:first-child img::attr(src)',
}
