from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label


def MainWidget():
    pass


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
