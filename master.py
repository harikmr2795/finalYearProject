from openpyxl.reader.excel import load_workbook
import feedparser
import requests
from bs4 import BeautifulSoup

wb = load_workbook('db.xlsx')
ws = wb.active

sourceLinksRSS = []
sourceLinksHTML_H3 = []
sourceLinksHTML_H2 = []
sourceLinksHTML_H1 = []
titles = []
newTitles = []

for i, x in enumerate(ws['A']):
                titles.append(ws['A'+str(i+1)].value)
oldCount = len(titles)

try:
        # RSS Scrapping
        for link in sourceLinksRSS:
                print('\nFecthing RSS from',link,'...')
                x = feedparser.parse(link)
                for element in x['items']:
                        title = element['title']
                        if(title not in titles):
                            titles.append(title)
        # BeautifulSoup Scrapping h3
        for link in sourceLinksHTML_H3:
                print('\nFetching News from',link)
                r  = requests.get(link)
                html_doc = r.text
                soup = BeautifulSoup(html_doc,'html.parser')
                headings = soup.find_all('h3')
                for heading in headings:
                        title = heading.get_text()
                        if(title not in titles):
                            titles.append(title)
        # BeautifulSoup Scrapping h2
        for link in sourceLinksHTML_H2:
                print('\nFetching News from',link)
                r  = requests.get(link)
                html_doc = r.text
                soup = BeautifulSoup(html_doc,'html.parser')
                headings = soup.find_all('h2')
                for heading in headings:
                        title = heading.get_text()
                        if(title not in titles):
                            titles.append(title)
        # BeautifulSoup Scrapping h1
        for link in sourceLinksHTML_H1:
                print('\nFetching News from',link)
                r  = requests.get(link)
                html_doc = r.text
                soup = BeautifulSoup(html_doc,'html.parser')
                headings = soup.find_all('h1')
                for heading in headings:
                        title = heading.get_text()
                        if(title not in titles):
                            titles.append(title)
                            
except requests.ConnectionError:
        print('No Internet Connection')

# To display & store the parsed titles
finally:
        newCount = len(titles)
        print('\n')
        for x in range(oldCount,newCount):
            ws['A'+str(x+1)].value = titles[x]
            newTitles.append(titles[x])
            x+=1
            print(x, '. ', titles[x-1])
        wb.save('db.xlsx')
