from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.properties import StringProperty
import sys
import time


class MainWidget(Widget):
    _ = StringProperty("whoa..")
    count = 0
    active = False

    def quit(self, mode):
        print(f"Button mode: {mode.state}")
        # time.sleep(5)
        # return sys.exit(0)
        if mode.state == "normal":
            mode.text = "off"
            self.active = False
        else:
            mode.text = "on"
            self.active = True

    def msg(self):
        print("event occured")
        if self.active:
            self.count += 1
            self._ = f"Counter: {str(self.count)}"


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
