import datetime
import time
from Pathe.settings import *
import pymongo

class SelectHelper(object):
    @staticmethod
    def get(res, selector):
        return res.css(selector).extract_first()

    @staticmethod
    def get_array(res, selector):
        array = res.css(selector).extract()
        result = []
        for item in array:
            stripped_item = "".join(item.split())
            result.append(stripped_item)
        return result

class MongoDBHelper(object):
    def __init__(self, db_uri):
        self.connection = pymongo.MongoClient(db_uri)
        self.db = self.connection[MONGODB_DB]

    def get(self, collection):
        return self.db[collection].find()

    def get_by(self, items, attr, val):
        items.rewind()
        for item in items:
            if item[attr] == val:
                return item

    def get_attr(self, items, attr):
        items.rewind()
        for item in items:
            yield item[attr]

    def close(self):
        self.connection.close()

class DateHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def now():
        return datetime.datetime.now().date()

    @staticmethod
    def date(d):
        return d.strftime('%d-%m-%Y')
    
    @staticmethod
    def strtodatetime(dt):
        return datetime.datetime.strptime(dt, '%d-%m-%Y')

    @staticmethod
    def strtodate(d):
        return datetime.datetime.strptime(d, '%d-%m-%Y').date()
    
    @staticmethod
    def strtoseconds(t):
        x = time.strptime(t, '%H:%M')
        return int(datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min).total_seconds())

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + datetime.timedelta(n)

    @staticmethod
    def next_weekday(d, weekday):
        days_diff = weekday - d.weekday()
        if days_diff <= 0:
            days_diff += 7
        return d + datetime.timedelta(days_diff)
    
    @staticmethod
    def prev_weekday(d, weekday):
        days_diff = weekday - d.weekday()
        return d - datetime.timedelta(days_diff)
    
    @staticmethod
    def add_days(d, amount):
        return d + datetime.timedelta(days=amount)
