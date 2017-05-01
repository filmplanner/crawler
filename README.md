#filmplanner/crawler
filmplanner/crawler is a crawler written in Python that retrieves theater, film and schedule data from Pathé. It uses Scrapy as its core library and stores all it's scraped data via a pipeline in a MongoDB database, which is used by the Film Planner application.
## Usage
**Crawl theaters**
``` bash
# Use the following code to crawl all theaters (locations) of Pathé NL
scrapy crawl theater
```
``` js
// Example data set that will be stored in the theaters MongoDB collection
{
    id: 23, // identifier (int)
    name: 'Pathé Spuimarkt', // name of theater (string)
    city: 'Den Haag', // city where theater is lcoated (string)
    image: 'http://image.url', // url of theater image (string)
}
```
**Crawl week schedule**
> Pathé adds a new schedule every monday for the next Thursday till Wednesday.
``` bash
# Use the following code to crawl all movies and schedule of the most recent scheduled week. 
scrapy crawl week
```
``` js
// Example data set that will be stored in the movies MongoDB collection
{
    id: 2334, // identifier (int)
    title: 'The Dark Knight', // movie title (string)
    description: 'Movie description', // short description of movie (string)
    advisory: ['http://image.url', 'http://image.url'] // kijkwijzer advisory (array)
    image: 'http://image.url', // url of movie image (string)
    url: 'http://info.url', // url of Pathé movie info (string)
}

// Example data set that will be stored in the shows MongoDB collection
{
    theater_id: 23, // identifier of theater (int)
    movie_id: 2334, // identifier of movie (int)
    date: 'Thu Apr 20 2017 00:00:00', // date of show (date)
    start: 340243, // start time of show in seconds (int)
    end: 504948, // end time of show in seconds (int)
    type: ['IMAX', 'Grote zaal'], // type of show (array)
    url: 'http://ticket.url', // url of Pathé ticket sale (string)                  
}
```