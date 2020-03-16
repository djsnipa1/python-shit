import lxml.html
from bs4 import BeautifulSoup
# from urllib2 import urlopen
import requests
import html2text
import re
from urlextract import URLExtract

html = requests.get("https://www.dataquest.io/blog/web-scraping-tutorial-python/")
# html = open(response).read()
# doc = lxml.html.fromstring(html.content)

# soup = BeautifulSoup(html)
soup = BeautifulSoup(html.content, 'html.parser')

# print(soup.prettify()
body = soup.find("body")
pretty = body.prettify()
print(html2text.html2text(pretty))

# import io
with open('lassie_test.md', 'w', encoding='utf-8') as outfile: 
    outfile.write(html2text.html2text(pretty))

# print(soup.encode("utf-8")
