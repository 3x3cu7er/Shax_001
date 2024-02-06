from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.properties import StringProperty


class MainWidget(Widget):
    _ = StringProperty("whoa..")
    count = 0

    def msg(self):
        print("event occured")
        self.count += 1


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
