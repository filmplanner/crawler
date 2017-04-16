import datetime
import json

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

class DataHelper(object):
    items = []

    def __init__(self, file):
        with open(file) as data:
            self.items = json.load(data)
    
    def get(self, element):
        for item in self.items:
            yield item[element]

    def to_string(self, obj):
        return ','.join(obj)
        
