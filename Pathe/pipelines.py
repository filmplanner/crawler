from scrapy.exporters import JsonItemExporter
from Pathe.settings import *

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
        pass
    def close_spider(self, spider):
        pass
    def process_item(self, item, spider):
        pass