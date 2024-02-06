from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


class Shax(App):

    def build(self):
        gridl = GridLayout(cols=1)
        img = Image(source="./prioritize.png")
        gridl.add_widget(img)
        return gridl


Shax().run()
