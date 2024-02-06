from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty
import sys
import time


class MainWidget(Widget):
    state = StringProperty("whoa..")
    count = 0
    active = BooleanProperty(False)

    def quit(self, mode):
        print(f"Button mode: {mode.state}")
        # time.sleep(5)
        # return sys.exit(0)
        if mode.state == "normal":
            mode.text = "off"
            self.active = True
        else:
            mode.text = "on"
            self.active = False

    def msg(self):
        print("event occured")
        if  True:
            self.count += 1
            self.state = f"Counter: {str(self.count)}"


class CounterApp(App):

    def build(self):
        return MainWidget()


CounterApp().run()
