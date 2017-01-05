#dependencies
import feedparser

document = feedparser.parse('https://www.engadget.com/rss.xml')
count = 0
print('Number of topics avoilable in Engadget is ',len(document),'\n')

while (count<len(document)):
    element = document['items'][count]
    print(element['title'])
    count = count + 1
