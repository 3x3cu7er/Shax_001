from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.text


class Shax(App):

    def build(self):
        gridl = GridLayout(cols=1)
        lb = Label(text="...")
        gridl.add_widget(lb)
        btn = Button(text="connect")

        return gridl


Shax().run()
