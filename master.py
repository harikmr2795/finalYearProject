import feedparser
import requests

#To check internet connection
def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

if(connected_to_internet()==True):
    #List of all RSS feeds
    sourceLinks = ['https://www.engadget.com/rss.xml','https://techcrunch.com/feed/','http://www.windowscentral.com/rss']

    titles = []
    document = []
    i=0
    
    
    for link in sourceLinks:
        print('\nFecthing RSS from ',link,'...')
        document.append(feedparser.parse(link))
        titleCount=0
        count=0
        print(len(document[i]),' Headlines Fetched')
        while (count<len(document[i])):
           element=document[i]['items'][count]
           titles.append(element['title'])
           count=count+1
        i=i+1

    i=1
    print('\n\n')
    for title in titles:
        print(i,'. ',title)
        i=i+1
