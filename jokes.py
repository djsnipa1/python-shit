import lxml.html
# from urllib2 import urlopen
import requests

url = "https://icanhazdadjoke.com/"

shields_url = 'https://img.shields.io/endpoint?url=' + url + '&style=plastic'

html = requests.get(url)
doc = lxml.html.fromstring(html.content)

print(html.json())
print(doc)