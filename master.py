import feedparser
import requests
from bs4 import BeautifulSoup
#To check internet connection
def connected_to_internet(url):
    try:
        _ = requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        if(url=='http://www.google.com/'):
            print('No Internet Connection')
    return False
def more_title_available(count):
    try:
        x = document[i]['items'][count]
        return True
    except Exception:
        return False
    return False
if(connected_to_internet('http://www.google.com/')==True):
    #RSS Scrapping
    sourceLinksRSS = ['https://www.engadget.com/rss.xml','https://techcrunch.com/feed/','http://www.windowscentral.com/rss','http://www.phonearena.com/feed']
    titles = []
    document = []
    i=0
    available = 0    
    
    for link in sourceLinksRSS:
        if(connected_to_internet(link)):
            print('\nFecthing RSS from ',link,'...')
            document.append(feedparser.parse(link))
            count=0
            available = 0
            while(more_title_available(available)==True):
                available = available + 1
            while(count<available):
                element = document[i]['items'][count]
                titles.append(element['title'])
                count=count+1
        i=i+1
    #BeautifulSoup Scrapping for FoneArena, BGR
    i=0
    sourceLinksHTML = []
    sourceLinksHTML = ['http://www.fonearena.com/','http://bgr.com/']
    for link in sourceLinksHTML:
        if(connected_to_internet(link)):
            print('\nFetching News from ',link)
            r  = requests.get(link)
            html_doc = r.text
            soup = BeautifulSoup(html_doc,'html.parser')
            headings = soup.find_all('h3')
            for heading in headings:
                if(i<len(headings)):
                    titles.append(headings[i].get_text())
                    i=i+1
        
   
    i=1
    print('\n\n')
    for title in titles:
        print(i,'. ',title)
        i=i+1
