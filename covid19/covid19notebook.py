import json
import pandas as pd
import requests
from datetime import datetime
from datetime import timedelta


# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
# send_headers = {'Accept': 'application/json'}

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
response.encoding = 'utf-8'  # Optional: requests infers this internally
data = response.json()


# + [markdown] nteract={"transient": {"deleting": false}}
# ### save `covid19.json` 

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
def save_json():
    with open('covid19.json', 'w') as f:
        json.dump(data, f)

save_json()


# + [markdown] nteract={"transient": {"deleting": false}}
# #### latest variables

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
confirmed_latest = data['latest']['confirmed']
deaths_latest = data['latest']['deaths']
recovered_latest = data['latest']['recovered']
deaths_updated_json = data['deaths']['last_updated']

def confirmed_func():
    print(confirmed_latest)

confirmed_func()


# + [markdown] nteract={"transient": {"deleting": false}}
# ## print death locations
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
def print_latest():
    """
    prints latest stats
    """
    print("Confirmed: " + str(confirmed_latest))
    print("Deaths: " + str(deaths_latest))
    print("Last Updated: " + deaths_updated_json)
    print('Recovered: ' + str(recovered_latest))

print_latest()

# + [markdown] nteract={"transient": {"deleting": false}}
# ## Confirmed
# confirmed locations DataFrame
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
pd_confirmed_locations = pd.DataFrame(data['confirmed']['locations'],
                                      columns=["country", "latest",
                                               "province"])

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
print(pd_confirmed_locations.head())
print("-=" * 40)
print(pd_confirmed_locations.sort_values(ascending=False,
                                         by=['latest']).head())
print("-=" * 40)
print('Number of colums in Dataframe : ', len(pd_confirmed_locations.columns))
print(pd_confirmed_locations.columns)
print('Number of rows in Dataframe : ', len(pd_confirmed_locations.index))


# + [markdown] nteract={"transient": {"deleting": false}}
# ### deaths
#
# death locations

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
pd_death_locations = pd.DataFrame(data['deaths']['locations'],
                                  columns=["country", "latest", "province"]
                                  ).sort_values(ascending=False, by='latest')
print(pd_death_locations.head())

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
test_pd = pd.DataFrame(data['deaths']['locations'],
                       columns=["country", "history"])

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
history = pd.DataFrame(data['deaths']['locations'],
                       columns=["history"]).apply(pd.Series)

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
now = datetime.now()
d = now.strftime("%#m/%d/%y")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%#m/%d/%y")
print(d)
print("yesterday = " + yesterday)
