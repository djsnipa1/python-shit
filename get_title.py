import requests

hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
n = requests.get('http://www.imdb.com/title/tt0108778/', headers=hearders)
al = n.text
al[al.find('<title>') + 7 : al.find('</title>')]
u'Friends (TV Series 1994\u20132004) - IMDb'