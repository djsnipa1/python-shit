import requests
import lxml.html


# tutorial from An Intro to Web Scraping With lxml and Python – Python Tips
# https://pythontips.com/2018/06/20/an-intro-to-web-scraping-with-lxml-and-python/

# REGEX
# ╔══════════════════════════════════════════════════════════════════════╗
# ║ ([^https?:\/\/][^kinogo.by\/]\d?\d?)                                 ║
# ╚══════════════════════════════════════════════════════════════════════╝

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
