A Webscraping project. These scrapers typically break if the site changes their setup.
However, the site that we're scrapping is quotes.toscrape, which is a site meant for scraping practice and will likely not change. Thus, this code will work for the foreseeable future.

This code scrapes practically everything that the site offers, from quotes, to the author's origins, to their biography. Everything. Every page. In addition, the user will be asked to save the data into a text, csv or json file. I spent a lot of time on error handling and giving user the maximum freedom with what to do.

The code is built in python, using the classic combination of requests and BeautifulSoup libraries to get and parse html data.
In addition to those two, the json and csv packages were also imported to work with json and csv file types respectively.

I added an optional sleep() call from the time library which is a more polite way of scraping as it creates a pause between requests, lessening the potential burden on their servers.

Also, added documentation.
