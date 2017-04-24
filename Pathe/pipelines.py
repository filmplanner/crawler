from Pathe.settings import *
from Pathe.helpers import MongoDBHelper

class MongoDBPipeline(object):

    def open_spider(self, spider):
        self.db_helper = MongoDBHelper()

    def close_spider(self, spider):
        self.db_helper.close()
        
    def process_item(self, item, spider):
        self.collection_name = item.__class__.__name__.lower() + 's'

        if self.collection_name == MONGODB_COLLECTION_THEATER:
            theaterExists = self.db_helper.db[self.collection_name].find({'_id': item['_id']}).count() > 0
            if theaterExists:
                return item

        if self.collection_name == MONGODB_COLLECTION_MOVIE:
            movieExists = self.db_helper.db[self.collection_name].find({'_id': item['_id']}).count() > 0
            if movieExists:
                return item
        
        if self.collection_name == MONGODB_COLLECTION_SHOW:
            showExists = self.db_helper.db[self.collection_name].find(
                {
                    'movie_id': item['movie_id'], 
                    'theater_id': item['theater_id'],
                    'date': item['date'],
                    'start': item['start'],
                }
            ).count() > 0
            if showExists:
                return item

        self.db_helper.db[self.collection_name].insert(dict(item))
        return item