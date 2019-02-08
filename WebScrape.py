import requests
from bs4 import BeautifulSoup
from csv import DictWriter
import json
from time import sleep


url = 'http://quotes.toscrape.com/'
# Scrapes website for author's quotes, name, bio, and tags and writes into a text file.
def scrape_to_file(timer):
    # Receives user input for file name. We will use that file to record our scraped data.
    filename = get_filename() + '.txt'
    file = open(filename, 'w', encoding = "utf-8")
    
    # Scrapes from page one, the goal is to scrape until the last page.
    page_link = '/page/1'
    count = 1
    while page_link:
        response = requests.get(f'{url}{page_link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'Now scraping {url}{page_link}...')
        # Searches for each relevant item on the page, and for each item: get it, add it into file.
        for each_quote in soup.find_all(class_='quote'):
            quote = each_quote.find(class_='text').get_text()
            author = each_quote.find(class_='author').get_text()
            bio_link = each_quote.find('a')['href']
            
            # Not every single quote has a tag. This allows our scraper to continue when a tag does not exist. 
            try:
                tag = each_quote.find(class_='tag').get_text()
            except AttributeError:
                continue
            
            # Each biography is located in a different url. We will scrape that too.
            history = requests.get(f'{url}{bio_link}')
            history_soup = BeautifulSoup(history.text, 'html.parser')
            biography = history_soup.find(class_='author-description').get_text()
            author_born_date = history_soup.find(class_='author-born-date').get_text()
            author_born_location = history_soup.find(class_='author-born-location').get_text()
            
            # Formatting is arbitrary. This format returns 'quote' - 'author', 'born date' in 'location' 'tags':
            file.write(quote + ' - ' + author + ', born ' + author_born_date + 
                       ' ' + author_born_location + '    Tags: ' + tag + '\n' +
                       biography + '\n \n')
            
            # This print statement is to provide transparency for each action. Shows the program is running.
            # If this is annoying, remove this print statement.
            print('Scraping...')
            
        print(f'Page {count} Scraped! Data written to {filename}.')    
        next_page = soup.find(class_='next')
        if next_page:
            page_link = next_page.find('a')['href']
            count += 1
            sleep(timer)
        else:
            page_link = False
    print(f'Website scraping complete! All data has been written to {filename}')
    file.close()
    

# Receives the user's choice filename
def get_filename():
    # Make sure to double check, user!
    while True:
        choice = input('What would you like to name the file? ')
        while True:
            yes_or_no = input(f'Your filename will be {choice}. Is this what you want? Yes/No ').lower()
            if yes_or_no == 'yes' or yes_or_no == 'no':
                break
        if yes_or_no == 'yes':
            break
    return choice      


# Scrape the data into a csv or json file (up to the user)
def scrape_to_csv_or_json(format, timer):
    
    filename = get_filename()
    file_format = format
    complete_filename = filename + file_format
    page_link = '/page/1'
    count = 1
    data = []
    while page_link:
        response = requests.get(f'{url}{page_link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'Now scraping {url}{page_link}...')
        # Searches for each relevant item on the page, and for each item: get it, add it into dictionary.
        for each_quote in soup.find_all(class_='quote'):
            
            bio_link = each_quote.find('a')['href']
            
            # Not every single quote has a tag. This allows our scraper to continue when a tag does not exist. 
            try:
                tag = each_quote.find(class_='tag').get_text()
            except AttributeError:
                continue
            
            # Each biography is located in a different url. We will scrape that too.
            history = requests.get(f'{url}{bio_link}')
            history_soup = BeautifulSoup(history.text, 'html.parser')
            data.append({
                'quote': each_quote.find(class_='text').get_text(),
                'author': each_quote.find(class_='author').get_text(),
                'tag': tag,
                'biography': history_soup.find(class_='author-description').get_text(),
                'date_born': history_soup.find(class_='author-born-date').get_text(),
                'location_born': history_soup.find(class_='author-born-location').get_text()
            })

            print('Scraping...')
        # Continues to scrape until the last page
        print(f'Page {count} Scraped!')
        next_page = soup.find(class_='next')
        if next_page:
            page_link = next_page.find('a')['href']
            count += 1
            sleep(timer)
        else:
            page_link = False
            
    if file_format == '.csv':        
        with open(complete_filename, 'w', encoding = "utf-8") as file:
            headers = ['quote', 'author', 'tag', 'biography', 'date_born', 'location_born']
            csv_writer = DictWriter(file, fieldnames = headers)
            csv_writer.writeheader()
            for quote in data:
                csv_writer.writerow(quote)
        print(f'Scraping completed! A .csv file, {complete_filename} has been created')
                
    elif file_format == '.json':
        with open(complete_filename, 'w', encoding = 'utf-8') as file:
            json.dump(data, file)
        print(f'Scraping completed! A .json file, {complete_filename} has been created')

# Asks what file they want to save to.       
def welcome():
    print('Welcome to my WebScraping project! You can save the data to a .txt file, .csv file, or .json file.')
    while True:
        choice = input('Take your pick: ').lower()
        if choice in 'json' or choice in 'csv' or choice in 'txt':
            break
        else:
            print('The choices are txt, csv, or json')
    return '.' + choice  
        
# Asks if the user wants to use the other 2 formats as well.
def again():
    while True:
        yes_or_no = input('Would you like to run the script again and try out the other two formats? ').lower()
        if yes_or_no == 'yes' or yes_or_no == 'no':
            break
    if yes_or_no == 'yes':
        return True
    else:
        return False

# This will be passed into the sleep() function to determine how long you would like to wait inbetween pages.        
def sleep_timer():
    while True:
        sleep = input('How long would you like to wait inbetween pages? ')
        try:
            val = int(sleep)
            break
        except ValueError:
            print('Please give an integer value!')
    return val

# Main method. This is where we'll execute our code.
def main():
    while True:
        pick = welcome()
        sleep_time = sleep_timer()
        if pick in '.txt':
            scrape_to_file(sleep_time)
        elif pick in '.csv' or pick in '.json':
            scrape_to_csv_or_json(pick, sleep_time)
        if not again():
            break
    print('Thanks for using my work.')
        
            
if __name__ == '__main__':
    main()