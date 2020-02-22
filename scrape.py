import requests
import lxml.html

html = requests.get("https://www.beatport.com/genre/psy-trance/13/top-100")
doc = lxml.html.fromstring(html.content)