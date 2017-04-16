import scrapy


class Theater(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    image = scrapy.Field()
