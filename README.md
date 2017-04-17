# pathe-crawler
pathe-crawler is a crawler written in Python that retrieves theater, film and schedule data from Pathé. It uses Scrapy as its core library and stores all it's scraped data via a pipeline in a MongoDB database, which is used by the Pathé Planner application.
## Usage
**Crawl theaters**
``` bash
# Use the following code to crawl all theaters (locations) of Pathé NL
scrapy crawl theater
```
``` js
// Example data set that will be stored in the theaters MongoDB collection
{
    id: '23',                   // identifier
    name: 'Pathé Spuimarkt',    // name of theater
    city: 'Den Haag',           // city where theater is lcoated
    image: 'http://image.url',  // url of theater image
}
```
**Crawl week schedule**
> Pathé adds a new schedule every monday for the next Thursday till Wednesday.
``` bash
# Use the following code to crawl all movies and schedule of the most recent scheduled week. 
scrapy crawl week

# Use the following code to crawl data from 13-04-2017 (next Thursday) till 19-04-2017 (following Wednesday).
scrapy crawl week -a start=03-04-2017
```
``` js
// Example data set that will be stored in the movies MongoDB collection
{
    id: '2334',                 // identifier
    title: 'The Dark Knight',   // movie title
    description: 'Den Haag',    // short description of movie
    image: 'http://image.url',  // url of movie image
    url: 'http://info.url',     // url of Pathé movie info
}

// Example data set that will be stored in the shows MongoDB collection
{
    theater_id: '23',           // identifier of theater
    movie_id: '2334',           // identifier of movie
    date: '12-04-2017',         // date of show
    start: '16:00',             // start of show
    end: '18:00',               // end of show
    type: 'IMAX',               // type of show
    url: 'http://ticket.url',   // url of Pathé ticket sale                    
}
```