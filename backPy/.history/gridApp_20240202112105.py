from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Shax(App):
    gridl = GridLayout(GridLayout.VERTICAL)

    def build(self):
        lb = Label(text="...")
        gridl.add_widget(lb)
        btn = Button(text="connect")

        return self.gridl


Shax().run()