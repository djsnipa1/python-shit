import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env

PASTERY_API_KEY = os.getenv("PASTERY_API_KEY")

# POST https://www.pastery.net/api/paste/
#     ?api_key=<api_key>
#     &duration=<duration>
#     &title=<title>
#     &language=<language>
#     &max_views=<max_views>

# GET "https://www.pastery.net/api/paste/?api_key=" + PASTERY_API_KEY

# send_headers = {'Accept': 'application/json'}

response = requests.get('https://www.pastery.net/api/paste/?api_key=' + PASTERY_API_KEY)
response.encoding = 'utf-8'  # Optional: requests infers this internally

print(response.json())

def get_joke():
    """
    Get's joke from web api
    """
    # print(response.content)
    # print(response.text)
    # print(response.headers)
    # print(response.json())  # This is the JSON response
    response_json = response.json()

    joke = response_json['joke']
    # print(joke)
    joke_split = joke.split("? ")
    print(joke_split[0])
    print("--------------------------------------------------------")
    time.sleep(1.5)  # Sleep for 1.5 seconds
    print("3")
    time.sleep(1.5)  # Sleep for 1.5 seconds
    print("2")
    time.sleep(1.5)  # Sleep for 1.5 seconds
    print("1")
    time.sleep(1.5)  # Sleep for 1.5 seconds
    print(joke_split[1])


# get_joke()
