from scrapy import Item, Field


class Theater(Item):
    _id = Field()
    name = Field()
    city = Field()
    image = Field()

class Movie(Item):
    _id = Field()
    title = Field()
    description = Field()
    advisory = Field()
    image = Field()
    url = Field()

class Show(Item):
    theater_id = Field()
    movie_id = Field()
    date = Field()
    start = Field()
    end = Field()
    type = Field()
    url = Field()
