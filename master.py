import feedparser
import requests
from bs4 import BeautifulSoup

sourceLinksRSS = ['https://www.engadget.com/rss.xml','https://techcrunch.com/feed/','http://www.phonearena.com/feed','http://www.windowscentral.com/rss','http://feeds.gawker.com/kotaku/full','http://digg.com/channel/technology.rss','http://www.dailytech.com/rss.aspx','http://www.lifehacker.co.in/rss_tag_section_feeds.cms?query=downloads','http://www.lifehacker.co.in/rss_tag_section_feeds.cms?query=android','http://www.theinquirer.net/feeds/rss']
sourceLinksHTML = ['http://www.fonearena.com/','http://bgr.com/','http://www.gsmarena.com/']
titles = []

try:
	# RSS Scrapping
	for link in sourceLinksRSS:
		print('\nFecthing RSS from ',link,'...')
		x = feedparser.parse(link)
		for element in x['items']:
			titles.append(element['title'])
	# BeautifulSoup Scrapping
	for link in sourceLinksHTML:
		print('\nFetching News from ',link)
		r  = requests.get(link)
		html_doc = r.text
		soup = BeautifulSoup(html_doc,'html.parser')
		headings = soup.find_all('h3')
		for heading in headings:
			titles.append(heading.get_text())
except requests.ConnectionError:
	print('No Internet Connection')

# To display the parsed titles, if any
print('\n\n')
for index, title in enumerate(titles):
	print(index+1, '. ', title)
