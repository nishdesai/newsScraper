from urllib.request import urlopen
from bs4 import BeautifulSoup
import html.parser
_htmlparser = html.parser.HTMLParser()
unescape = _htmlparser.unescape


url = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss"
html = urlopen(url).read()
soup = BeautifulSoup(html)



all_articles = soup.find_all('item')


def find_attributes(l):
    output_list = []
    for item in l:
        title = unescape(item.find('title').contents[0]).encode('utf-8')
        link = item.find('link').contents[0].encode('utf-8')
        date = item.find('pubdate').contents[0].encode('utf-8')
        
        description = BeautifulSoup(unescape(item.find('description').string))
        text = description.find_all('font')[5].contents
        if len(text) != 2:
            content = "**IRREGULAR HTML ENCOUNTERED**"
        else:
            content = text[0].string.encode("utf-8")
        output_list.append((title, link, content, date))
    return output_list

printout_list = find_attributes(all_articles)

def print_elements(articles):
    for article in articles:
        print(("Title: " + article[0].decode('utf-8')))
        print (("Date: " + article[3].decode('utf-8')))
        if type(article[2] == str):
            print ("Content: " + str(article[2]))
        else:
            print (("Content: " + article[2].decode('utf-8')))
        print (("Link: " + article[1].decode('utf-8')))
        print ("\n")

print_elements(printout_list)

