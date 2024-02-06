from kivy.app import App  
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


class MainWindow(GridLayout):
    state = StringProperty("0")

    def active(self, win):
        print(win.active)
        
    def varr(self, win):
        state = win.value


class OnSwitch(App):

    def build(self):
        return MainWindow()

    
OnSwitch().run()
