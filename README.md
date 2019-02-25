# An Introduction
A Webscraping project. These scrapers typically break if the site changes their setup.
However, the site that we're scrapping is quotes.toscrape, which is a site meant for scraping practice and will likely not change. Thus, this code will work for the foreseeable future. Although scrapers only work for a limited number of sites, the concept behind it carries over to other projects.

# Funtionality  
TL;DR -
- Asks user for their choice of format.
- Asks user for their choice of name
- Asks user how many seconds to wait between pages (Can be 0)
- Goes to work
- Enjoy your new file!

This code scrapes practically everything that the site offers, from quotes, to the author's origins, to their biography, to even the tags. Everything. Every page. In addition, the user will be asked to save the data into a text, csv or json file. I spent a lot of time on error handling and giving user the maximum freedom with what to do.  

The program begins by asking which file type you would like to save the data to: json, csv or txt. It will not allow answers outside the realm of the 3, thus it will keep asking until you pick one of the 3. It will ask you to confirm to make sure you did not make the wrong choice, and proceed to ask you to pick a name for your file. Again, it will ask for you to confirm your answer. Oh also, it will ask how long you would like to wait before scraping the next page.   

Although this site allows scraping, some sites may not, and it is always better manners to wait a little in between pages. Finally, the program will proceed to scrape and an option to replay will be presented. 

# Tools

The code is built in python, using the classic combination of Requests and BeautifulSoup4 libraries to get and parse html data.
In addition to those two, the json and csv packages were also imported to work with json and csv file types respectively. In order to lessen the burden on servers that were scraped, I've also given users the option to call sleep() from the time library. This create a temporary pause on the execution of code and provides a moment of respite for the server. 



