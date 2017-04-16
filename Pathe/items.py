from scrapy import Item, Field


class Theater(Item):
    id = Field()
    name = Field()
    city = Field()
    image = Field()

class Movie(Item):
    id = Field()
    title = Field()
    description = Field()
    image = Field()

class Show(Item):
    theater_id = Field()
    movie_id = Field()
    date = Field()
    start = Field()
    end = Field()
    duration = Field()
    type = Field()
    url = Field()
    
