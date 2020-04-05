# coding=utf-8
# coding=utf-8
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class My2App(App):
    def build (self):
        return FloatLayout()


if __name__ == "__main__":
    My2App().run()