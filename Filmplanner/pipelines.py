import json

class JsonPipeline(object):

    def open_spider(self, spider):
        self.file = open(spider.name + ".json", 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item