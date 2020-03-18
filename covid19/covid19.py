# coding=utf-8
import json
import pandas as pd
import requests

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


# pd_data = pd.json_normalize(data)
pd_locations = pd.DataFrame(data['confirmed']['locations'], columns=["country", "latest", "province"])

# print_latest()
print(pd_locations.head())

print(pd_locations.sort_values(by=['latest']))

# TODO This block of code
# for key, items in data['confirmed']['locations']:
#     for item in items:
#         price = item['country']
#         print(price)

# print(data['confirmed']['locations'].index("US"))
#
#
# pd_country = pd.DataFrame(data['confirmed']['locations'][0])
#
#
# print(json_data['confirmed.locations'])
