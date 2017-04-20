import datetime
import json
from Pathe.settings import *
import pymongo

class SelectHelper(object):
    @staticmethod
    def get(res, selector):
        return res.css(selector).extract_first()

class MongoDBHelper(object):
    
    def __init__(self):
        self.connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
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
        date = d.strftime('%d-%m-%Y')
        return date
    
    @staticmethod
    def strtodate(d):
        return datetime.datetime.strptime(d, '%d-%m-%Y').date()

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + datetime.timedelta(n)

    @staticmethod
    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + datetime.timedelta(days_ahead + 7)
    
    @staticmethod
    def add_days(d, amount):
        return d + datetime.timedelta(days=amount)