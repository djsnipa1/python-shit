# coding=utf-8
import requests
import pandas as pd
from pprint import pprint
import json

send_headers = {'Accept': 'application/json'}

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
response.encoding = 'utf-8'  # Optional: requests infers this internally
data = response.json()


def save_json():
    with open('covid19.json', 'w') as f:
        json.dump(data, f)


# save_json()

confirmed_latest = data['latest']['confirmed']
deaths_latest = data['latest']['deaths']
recovered_latest = data['latest']['recovered']


def print_latest():
    print("Confirmed: " + str(confirmed_latest))
    print("Deaths: " + str(deaths_latest))
    print('Recovered: ' + str(recovered_latest))


print_latest()
# print(pd_data['latest'])

for key, items in data['confirmed']['locations']:
    for item in items:
        price = item['country']
        print(price)

print(data['confirmed']['locations'].index("US"))

pd_data = pd.DataFrame(data['confirmed']['locations'])

pd_country = pd.DataFrame(data['confirmed']['locations'][0])

from pandas.io.json import json_normalize

jsoned = pd.json_normalize(data)

print(jsoned['confirmed.locations'])
from pandas.io.json import json_normalize

# with open('https://github.com/a9k00r/python-test/blob/master/raw_nyc_phil.json') as f:
#     d = json.load(f)
