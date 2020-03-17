import requests
from lxml.html import fromstring


def Get_PageTitle(url):
    req = requests.get(url)
    tree = fromstring(req.content)
    title = tree.findtext('.//title')
    return title


url = "http://www.google.com"
title = Get_PageTitle(url)

if "404" in title:
    # title has 404
    print("Title has 404 in it")

else:
    print(title)
    # no 404 in title
    pass
