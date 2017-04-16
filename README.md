# pathe-crawler
pathe-crawler is a crawler written in Python to retrieve theater & movie data from Pathé. It uses Scrapy as its core library and stores all data in a MongoDB database which is used by the Pathé Planner application.
## Usage
**Theater**
Use the following code to crawl all theaters (locations) of Pathé
```
scrapy crawl theater
```
**Week**
Use the following code to crawl all movies and show times of the most recent planned week. Pathé adds a new planning every monday for the next Thursday till Wednesday.
```
scrapy crawl week
```
You can also make use of the startdate flag to adjust the week that will be crawled. For example:
Use the following code to crawl data from 13-04-2017 (next Thursday) till 19-04-2017 (following Wednesday).
```
scrapy crawl week -a start=03-04-2017
```