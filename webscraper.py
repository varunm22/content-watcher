from urllib.request import urlopen # lets us request a url
from urllib.error import HTTPError
import urllib.request
from bs4 import BeautifulSoup

#prompts user to enter site to be scraped & parses it 
#example: https://www.nytimes.com/
page = input("Enter website to be searched: ")
html = urllib.request.urlopen(page).read()
soup = BeautifulSoup(html, 'html.parser')

#kill all script and style elements to take text within these tags
for script in soup(["script", "style"]):
    script.extract()    # rip it out

#takes all visible text on page
text = soup.get_text()

#prompts user to enter topic/item to be searched
#example "covid"
search = input("Enter topic to search: ")

#counts number of results of topic/item on page & ignores case sensitivty
results = text.lower().count(search)

#prints results
print('Website: ' + page)
print('Number of results for ' + search + ': ' + str(results))