import feedparser
import requests
from bs4 import BeautifulSoup

sourceLinksRSS = ['https://www.wired.com/category/gear/feed/','http://www.webpronews.com/feed/','http://feeds.feedburner.com/venturebeat/SZYF','http://www.theregister.co.uk/emergent_tech/artificial_intelligence/headlines.atom','http://www.theregister.co.uk/software/headlines.atom','http://rss.slashdot.org/Slashdot/slashdotMain','http://www.businessinsider.in/rss_section_feeds/21807543.cms','http://scobleizer.com/feed/','http://readwrite.com/feed/','http://www.pcworld.com/index.rss','https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/column/bits/rss.xml','http://feeds.mashable.com/Mashable','http://feeds.feedburner.com/LouisgraycomLive','http://www.informationweek.com/rss_simple.asp','http://feeds.feedburner.com/ilounge','http://www.i4u.com/i4u.xml','http://www.gizmodo.in/rss_section_feeds/2147477989.cms','http://www.gizmodo.in/rss_section_feeds/19124833.cms','http://www.gizmodo.in/rss_tag_section_feeds.cms?query=google','https://gigaom.com/feed/','https://www.geek.com/feed/','http://www.macnn.com/macnn.rss','http://www.huffingtonpost.com/feeds/verticals/technology/index.xml','https://techcrunch.com/gadgets/feed/','https://techcrunch.com/feed/','http://feed.cnet.com/feed/topics/mobile','https://www.cnet.com/rss/all/','http://www.windowscentral.com/rss','https://www.engadget.com/rss.xml','http://www.phonearena.com/feed','http://feeds.gawker.com/kotaku/full','http://digg.com/channel/technology.rss','http://www.dailytech.com/rss.aspx','http://www.lifehacker.co.in/rss_tag_section_feeds.cms?query=downloads','http://www.lifehacker.co.in/rss_tag_section_feeds.cms?query=android','http://www.theinquirer.net/feeds/rss','http://www.wsj.com/xml/rss/3_7455.xml','http://feeds.arstechnica.com/arstechnica/index/']
#LifeHacker RSS needs review
sourceLinksHTML_H3 = ['http://www.fonearena.com/','http://www.gsmarena.com/','http://bgr.com/','http://bgr.com/page/2/','http://bgr.com/page/3/','http://bgr.com/page/3/','http://bgr.com/page/4/','http://bgr.com/page/5/','http://bgr.com/page/6/','https://www.bloomberg.com/technology']
sourceLinksHTML_H2 = ['http://www.in.techspot.com/news']
sourceLinksHTML_H1 = ['http://valleywag.gawker.com/page_2','http://valleywag.gawker.com/page_1','http://valleywag.gawker.com/']
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
	# BeautifulSoup Scrapping h1
	for link in sourceLinksHTML_H1:
		print('\nFetching News from',link)
		r  = requests.get(link)
		html_doc = r.text
		soup = BeautifulSoup(html_doc,'html.parser')
		headings = soup.find_all('h1')
		for heading in headings:
			titles.append(heading.get_text())
except requests.ConnectionError:
	print('No Internet Connection')

# To display the parsed titles
finally:
        print('\n')
        for index, title in enumerate(titles):
                print(index+1, '. ', title)
