from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.property import StringProperty


class MainWidget(Widget):

    def msg(self):
        print("event occured")


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
