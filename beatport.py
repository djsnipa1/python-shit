import requests
import lxml.html
import json

# html = requests.get("https://www.beatport.com/genre/psy-trance/13/top-100")
html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')
doc = lxml.html.fromstring(html.content)
print(new_releases)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
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

tags = [tag.text_content() for tag in new_releases.xpath(
    './/div[@class="tab_item_top_tags"]')]
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
