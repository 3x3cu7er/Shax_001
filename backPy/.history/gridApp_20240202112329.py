from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Shax(App):

    def build(self):
        gridl = GridLayout(cols=1)
        lb = Label(text="...")
        
        btn = Button(text="connect")
        gridl.add_widget(lb, btn)

        return gridl


Shax().run()
