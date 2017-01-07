import feedparser
import requests
#To check connection
def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False
def more_title_available(count):
    try:
        x = document[i]['items'][count]
        return True
    except Exception:
        return False
    return False
if(connected_to_internet()==True):
    #List of all RSS feeds
    sourceLinks = ['https://www.engadget.com/rss.xml','https://techcrunch.com/feed/','http://www.windowscentral.com/rss']
    titles = []
    document = []
    i=0
    available = 0    
    
    for link in sourceLinks:
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
    i=1
    print('\n\n')
    for title in titles:
        print(i,'. ',title)
        i=i+1
