from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label


def MainWidget(Widget):
    pass


class Counter(App):

    def build(self):
        return MainWidget()


Counter().run()
