from kivy.app import App
from kivy.uix.widget import Widget


def Counter(Widget):
    pass


class CounterApp(App):

    def build(self):
        return Counter()


CounterApp().run()
