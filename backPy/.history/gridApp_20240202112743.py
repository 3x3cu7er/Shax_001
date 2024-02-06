from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Shax(App):

    def build(self):
        gridl = GridLayout(rows=1)
        lb = Label(text="...")
        gridl.add_widget(lb)
        getVal = TextInput(text="handle")
        gridl.add_widget(getVal)
        btn = Button(text="connect")
        gridl.add_widget(btn)

        return gridl


Shax().run()
