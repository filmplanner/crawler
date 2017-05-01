from Pathe.helpers import MongoDBHelper

class MongoDBPipeline(object):
    """MongoDB Pipeline which stores crawled objects in a MongoDB database."""
    db_helper = None

    def open_spider(self, spider):
        """Called when spider is opened."""
        self.db_helper = MongoDBHelper(spider.crawler.settings.get('MONGODB_URI'))

    def close_spider(self, spider):
        """Called when spider is closed."""
        self.db_helper.close()

    def process_item(self, item, spider):
        """Called when object is generated in a a spider."""
        collection_name = item.__class__.__name__.lower() + 's'

        if (collection_name == spider.crawler.settings.get('MONGODB_COLLECTION_THEATER') or collection_name == spider.crawler.settings.get('MONGODB_COLLECTION_MOVIE')):
            item_exists = self.db_helper.db[collection_name].find({'_id': item['_id']}).count() > 0
            if item_exists:
                return item

        if collection_name == spider.crawler.settings.get('MONGODB_COLLECTION_SHOW'):
            show_exists = self.db_helper.db[collection_name].find(
                {
                    'movie_id': item['movie_id'],
                    'theater_id': item['theater_id'],
                    'date': item['date'],
                    'start': item['start'],
                }
            ).count() > 0
            if show_exists:
                return item

        self.db_helper.db[collection_name].insert(dict(item))
        return item
