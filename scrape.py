import requests
import lxml.html

# html = requests.get("https://www.beatport.com/genre/psy-trance/13/top-100")
html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')
doc = lxml.html.fromstring(html.content)
print(new_releases)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
titles = new_releases.xpath('//div[@class="tab_item_name"]/text()')
print(titles)