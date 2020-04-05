#!/usr/bin/env python3
# coding=utf-8
import json
import pandas as pd
import requests
from datetime import datetime
from datetime import timedelta
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# sys.exit()
# import importlib
#
# moduleName = input('Enter module name:')
# importlib.import_module(moduleName)

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
response.encoding = 'utf-8'  # Optional: requests infers this internally
data = response.json()

confirmed_latest = data['latest']['confirmed']
deaths_latest = data['latest']['deaths']
recovered_latest = data['latest']['recovered']
deaths_updated_json = data['deaths']['last_updated']

def confirmed_func():
    print(confirmed_latest)


def print_latest():
    """
    prints latest stats
    """
    print("Confirmed: " + str(confirmed_latest))
    print("Deaths: " + str(deaths_latest))
    print("Last Updated: " + deaths_updated_json)
    print('Recovered: ' + str(recovered_latest))

print_latest()


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    confirmed = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.name.text, "Email: ", self.email.text)
        self.name.text = ""
        self.email.text = ""

    def txt(self):
        print()


class CovidApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    CovidApp().run()
