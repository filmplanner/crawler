from scrapy.exporters import JsonItemExporter
from Pathe.settings import *
import pymongo

class JsonExportPipeline(object):

    def open_spider(self, spider):
        if spider.name == THEATER_NAME:
            self.file = open('%s_items.json' % spider.name, 'wb')
            self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
            self.exporter.start_exporting()
 
    def close_spider(self, spider):
        if spider.name == THEATER_NAME:
            self.exporter.finish_exporting()
            self.file.close()
 
    def process_item(self, item, spider):
        if spider.name == THEATER_NAME:
            self.exporter.export_item(item)
        return item

class MongoDBPipeline(object):

    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
        self.db = self.connection[MONGODB_DB]

    def close_spider(self, spider):
        self.connection.close()
        
    def process_item(self, item, spider):
        self.collection_name = item.__class__.__name__.lower() + 's'

        if self.collection_name == MONGODB_COLLECTION_THEATER:
            theaterExists = self.db[self.collection_name].find({'id': item['id']}).count() > 0
            if theaterExists:
                return item

        if self.collection_name == MONGODB_COLLECTION_MOVIE:
            movieExists = self.db[self.collection_name].find({'id': item['id']}).count() > 0
            if movieExists:
                return item
        
        if self.collection_name == MONGODB_COLLECTION_SHOW:
            showExists = self.db[self.collection_name].find(
                {
                    'movie_id': item['movie_id'], 
                    'theater_id': item['theater_id'],
                    'date': item['date'],
                    'start': item['start'],
                }
            ).count() > 0
            if showExists:
                return item

        self.db[self.collection_name].insert(dict(item))
        return item