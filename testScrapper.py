#dependencies
import feedparser

def check(count):
    try:
        x = document['items'][count]
        return True
    except Exception:
        return False
    return False

document = feedparser.parse('https://www.engadget.com/rss.xml')
count = 0
print('Number of topics available in Engadget is ',len(document),'\n')

while (count<len(document)):
    element = document['items'][count]
    print(count+1,'. ',element['title'])
    count = count + 1

count = 25
if(check(count)==True):
    print("More Available")
else:
    print("NotAvailable")
    
