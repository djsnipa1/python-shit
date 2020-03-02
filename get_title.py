import lxml.html
# from urllib2 import urlopen
import requests


html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

title = doc.find(".//title").text

# print("Title = " + title)


urls = ["https://www.beatport.com", "https://www.github.com"]

for url in urls:
  html = requests.get(url)
  doc = lxml.html.fromstring(html.content)
  title = doc.find(".//title").text
  description = doc.xpath('.//meta[@name="description"]/@content')
  print(url)
  print(title)
  print(description)
  print("---------------------------------")