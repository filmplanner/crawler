# pathe-crawler
pathe-crawler is a crawler written in Python that retrieves theater, film and schedule data from Pathé. It uses Scrapy as its core library and stores all it's scraped data via a pipeline in a MongoDB database, which is used by the Pathé Planner application.
## Usage
**Theater**
```
# Use the following code to crawl all theaters (locations) of Pathé NL
scrapy crawl theater
```
**Week**
> Pathé adds a new schedule every monday for the next Thursday till Wednesday.
```
# Use the following code to crawl all movies and schedule of the most recent scheduled week. 
scrapy crawl week

# Use the following code to crawl data from 13-04-2017 (next Thursday) till 19-04-2017 (following Wednesday).
scrapy crawl week -a start=03-04-2017
```