# coding=utf-8
import urllib.parse
import urllib.request
from datetime import datetime
import time

starttime = time.time()
while True:

    url = 'https://www.writeguard.com/catalog/Tax-Forms-Supplies/' \
          'Affordable-Care-Act-Tax-Forms/Form-1095-B-Health-Coverage-B1095B05'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python'}
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()

    print("1 good")

    someurl = "https://www.writeguard.com/catalog/Health-Care/" \
              "Generic-Billing-Statements/" \
              "WLCS107-BK-Generic-Laser-Statments-MCVISADISCAMEX-Blue"
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    req = Request(someurl)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print("everything is fine")

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m/%d/%Y, %I:%M:%S%p")
    # print("date and time:",date_time)

    print(date_time)
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
