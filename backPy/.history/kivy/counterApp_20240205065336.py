from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.properties import StringProperty
import sys
import time


class MainWidget(Widget):
    _ = StringProperty("whoa..")
    count = 0

    def quit(self):
        self._ = "system exiting.."
        time.sleep(5)
        return sys.exit(0)

    def msg(self):
        print("event occured")
        self.count += 1
        self._ = f"Counter: {str(self.count)}"


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
