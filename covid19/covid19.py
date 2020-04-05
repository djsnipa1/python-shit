# coding=utf-8
import json
import pandas as pd
import requests
from datetime import datetime
from datetime import timedelta
send_headers = {'Accept': 'application/json'}

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
response.encoding = 'utf-8'  # Optional: requests infers this internally
data = response.json()


def save_json():
    with open('covid19.json', 'w') as f:
        json.dump(data, f)


save_json()

confirmed_latest = data['latest']['confirmed']
deaths_latest = data['latest']['deaths']
recovered_latest = data['latest']['recovered']
deaths_updated_json = data['deaths']['last_updated']
deaths_updated = datetime.fromisoformat(deaths_updated_json)


def print_latest():
    """
    prints latest stats
    """
    print("Confirmed: " + str(confirmed_latest))
    print("Deaths: " + str(deaths_latest))
    print("Last Updated: " + deaths_updated)
    print('Recovered: ' + str(recovered_latest))


print_latest()

pd_death_locations = pd.DataFrame(data['deaths']['locations'],
                                  columns=["country", "latest", "province"]
                                  ).sort_values(ascending=False, by='latest')
print(pd_death_locations.head())

test_pd = pd.DataFrame(data['deaths']['locations'],
                       columns=["country", "history"])

history = pd.DataFrame(data['deaths']['locations'],
                       columns=["history"]).apply(pd.Series)

now = datetime.now()
d = now.strftime("%#m/%d/%y")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%#m/%d/%y")
print(d)
print("yesterday = " + yesterday)

# # Filter dictionary by keeping elements whose values are string of length 6
# newDict = {key: value for (key, value) in data['deaths']['locations']dictOfNames.items() if len(value) == 6 } # noqa
# print('Filtered Dictionary : ')
# print(newDict)


def historyish():
    for dat in data['deaths']['locations']:
        # print(dat['history'])
        # Filter dictionary by keeping elements whose values are string of length 6 # noqa
        print(d)
        print(yesterday)
        newDict = {key: value for (key, value) in dat['history'].items() if key == yesterday} # noqa
        print('Filtered Dictionary : ')
        print(newDict)


historyish()


# finaltest = pd.concat([test_pd['country'], test_pd['history'].apply(pd.Series)], axis=1) # noqa
# test_to_list = test_pd['history'].apply(pd.Series)
# cols_as_date = [datetime.strptime(x, '%d-%m-%Y') for x in finaltest.columns]

# cols_as_date = [pd.to_datetime(x, errors='ignore') for x in history.columns] # noqa


# test_pd = pd.to_datetime(test_pd['history'], errors='ignore')
# finaltest = finaltest[sorted(test_pd['history'])]

print(history)


pd_confirmed_locations = pd.DataFrame(data['confirmed']['locations'],
                                      columns=["country", "latest",
                                               "province"])

# print_latest()
print(pd_confirmed_locations.head())
print("-=" * 40)
print(pd_confirmed_locations.sort_values(ascending=False,
                                         by=['latest']).head())
print("-=" * 40)
print('Number of colums in Dataframe : ', len(pd_confirmed_locations.columns))
print(pd_confirmed_locations.columns)
print('Number of rows in Dataframe : ', len(pd_confirmed_locations.index))

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)
# print(pd_confirmed_locations)

# dataframe with country = US
us = pd_confirmed_locations.loc[pd_confirmed_locations['country'] == "US"]
print(us)
print(us.shape)
print(type(us))

# deletes rows from us with a ,
us_final = us[~us.province.str.contains(",")]
# sort us_final by latest cases
us_final = us_final.sort_values(ascending=False, by=['latest'])
print(us_final)
print(us_final.shape)

locations = data['confirmed']['locations']

countries = []
provinces = []

for location in locations:
    country = location['country']
    countries.append(country)
    province = location['province']
    # if not province:
    #     # print("Nope = " + country)
    # else province !=
    #     provinces.append(province)


# print(provinces)


def locations_len(location):
    return len(location)

# locations.sort(key = locations_len(locations))
# print(locations)


# locations_len(locations)
# def get_locations(data):
#     return int(data['nbaDebutYear'])
#
#
# nba_pla
# yers.sort(key=get_nba_debut_year)
# print(nba_players)
#
# for location in locations:
#     print(str(locations['country']))

# TODO This block of code
# for key, items in data['confirmed']['locations']:
#     for item in items:
#         price = item['country']
#         print(price)

# print(data['confirmed']['locations'].index("US"))
#
# pd_data = pd.DataFrame(data['confirmed']['locations'])
#
# pd_country = pd.DataFrame(data['confirmed']['locations'][0])
#
# json_data = pd.json_normalize(data)
#
# print(json_data['confirmed.locations'])
