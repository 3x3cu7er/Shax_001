from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.properties import StringProperty


class MainWidget(Widget):
    _ = StringProperty("whoa..")

    def msg(self):
        print("event occured")
        self._ = [x for x in range(1, 20)]


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
