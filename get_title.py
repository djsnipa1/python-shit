import requests
import mechanize

br = mechanize.Browser()
br.open("https://google.com")

print(br.title)