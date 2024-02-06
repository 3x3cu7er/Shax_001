from kivy.app import App
from kivy.uix.widget import Widget


def counter(Widget):
    pass


class CounterApp(App):

    def build(self):
        return counter()


CounterApp().run()
