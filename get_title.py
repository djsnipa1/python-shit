#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
the web url matching regex used by markdown
http://daringfireball.net/2010/07/improved_regex_for_matching_urls
https://gist.github.com/gruber/8891611
"""

import lxml.html
# from urllib2 import urlopen
import requests
import re
from urlextract import URLExtract

html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

title = doc.find(".//title").text

# print("Title = " + title)


urls = ["https://www.beatport.com", "https://www.github.com"]

s = 'This is my tweet check it out http://tinyurl.com/blah and http://blabla.com'
print(re.findall(r'(https?://\S+)', s))

with open('parse.txt', 'r', encoding="utf8") as fh:
    data = fh.read().replace('\n', '')
    # print(data)
    # links = re.findall(r'(https?://\S+)', data)
    # print(links)

    extractor = URLExtract()
    urls = extractor.find_urls(data)
    # print(urls)  # prints: ['janlipovsky.cz']
    # print(type(urls))

    for url in urls:
        html = requests.get(url)
        doc = lxml.html.fromstring(html.content)
        title = doc.find(".//title").text
        description = doc.xpath('.//meta[@name="description"]/@content')
        # print(url)
        # print(title)
        # print(description)
        # print("---------------------------------")
        print("\n[" + title + "](" + url + ")")  # adds new line in front of markdown links
        split = str(description)[2:-2]  # Removes the [ ] and ' ' from each description line
        print(split + '\n')  # adds a new line after the description
        print("- - -")  # obviously adds a hr to the file
