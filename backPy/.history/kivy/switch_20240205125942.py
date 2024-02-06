from kivy.app import App  
from kivy.uix.gridlayout import GridLayout


class MainWindow(GridLayout):

    def active(self, win):
        print(win.active)


class OnSwitch(App):

    def build(self):
        return MainWindow()

    
OnSwitch().run()
