# coding=utf-8
import requests
import pandas as pd
import time
import json

send_headers = {'Accept': 'application/json'}

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
response.encoding = 'utf-8'  # Optional: requests infers this internally
data = response.json()

def save_json():
    with open('covid19.json', 'w') as f:
        json.dump(data, f)

country = data['confirmed']['locations'][0]

# print(pd_data['latest'])

pd_data = pd.DataFrame(data['confirmed']['locations'])

pd_country = pd.DataFrame(data['confirmed']['locations'][0])

from pandas.io.json import json_normalize
jsoned = pd.json_normalize(data)

print(jsoned['confirmed.locations'] )
from pandas.io.json import json_normalize

# with open('https://github.com/a9k00r/python-test/blob/master/raw_nyc_phil.json') as f:
#     d = json.load(f)
