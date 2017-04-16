BOT_NAME = 'Pathe'
SPIDER_MODULES = ['Pathe.spiders']
NEWSPIDER_MODULE = 'Pathe.spiders'
ROBOTSTXT_OBEY = True
BASE_URL = 'https://www.pathe.nl'

## THEATER CSS SELECTORS
SELECTOR_THEATER = {
    'LIST': '.nav-primary__has-sub.js-main-menu-left:nth-child(2) ul li a[href*="bioscoop/"]',
    'LIST_HREF': '::attr(href)',
    'ID': '.favoritebutton a:first-child::attr(data-cinema)',
    'NAME': '.visual-cinema__location::text',
    'CITY': '.visual-cinema__city::text',
    'IMAGE': '#js-carousel-home .visual-home__item:first-child img::attr(src)',
}
