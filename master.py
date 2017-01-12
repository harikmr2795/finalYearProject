import feedparser
import requests
from bs4 import BeautifulSoup

sourceLinksRSS = ["""url of rss feeds go here"""]
sourceLinksHTML_H3 = []
sourceLinksHTML_H2 = []
titles = []

try:
	# RSS Scrapping
	for link in sourceLinksRSS:
		print('\nFecthing RSS from',link,'...')
		x = feedparser.parse(link)
		for element in x['items']:
			titles.append(element['title'])
	# BeautifulSoup Scrapping h3
	for link in sourceLinksHTML_H3:
		print('\nFetching News from',link)
		r  = requests.get(link)
		html_doc = r.text
		soup = BeautifulSoup(html_doc,'html.parser')
		headings = soup.find_all('h3')
		for heading in headings:
			titles.append(heading.get_text())
        # BeautifulSoup Scrapping h2
	for link in sourceLinksHTML_H2:
		print('\nFetching News from',link)
		r  = requests.get(link)
		html_doc = r.text
		soup = BeautifulSoup(html_doc,'html.parser')
		headings = soup.find_all('h2')
		for heading in headings:
			titles.append(heading.get_text())
except requests.ConnectionError:
	print('No Internet Connection')

# To display the parsed titles
finally:
        print('\n')
        for index, title in enumerate(titles):
                print(index+1, '. ', title)
                
