import requests
import lxml.html
import json

# tutorial from An Intro to Web Scraping With lxml and Python – Python Tips
# https://pythontips.com/2018/06/20/an-intro-to-web-scraping-with-lxml-and-python/

# REGEX
# ╔═══════════════════════════════════════════════════════════════════════════════╗
# ║ ([^https?:\/\/][^kinogo.by\/]\d?\d?)                                          ║
# ╚═══════════════════════════════════════════════════════════════════════════════╝

original_url = "https://kinogo.by/7047-babylon-berlin_1-3-sezon.html"
download_url = "https://kinogo.by/engine/ajax/cdn_download.php?news_id=7047"

html = requests.get(download_url)
# html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')
doc = lxml.html.fromstring(html.content)
print(new_releases)

seasons = doc.xpath('//b/text()')

print(seasons)

for season in seasons:
  print(season)

links = doc.xpath('.//a[text()="480"]/@href')
ids = doc.xpath('.//a/@data-id[contains(text(), "480")]')
ids2 = doc.xpath('//*[contains(text(), "480")]/text()')

print(ids)
print(ids2)
# print(links)
# print(text(test))
"""    
print(doc.findall(".//b")[1].text)

print(doc.find(".//b").text)

print(next(doc.iterfind(".//b")).text)

print(next(doc.iter("b")).text)
"""

"""


new_releases = doc.xpath('//b[@class="cdn_download_season"]')[0]
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
print(titles)

prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')
print(prices)

# tags = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
# total_tags = []
# for tag in tags:
#     total_tags.append(tag.text_content())
#
# print(total_tags)

tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
tags = [tag.split(', ') for tag in tags]
print(tags)

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

print(total_platforms)


output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

print(output)

with open('output.json', 'w') as outfile:
    json.dump(output, outfile)

"""
