from kivy.app import App  
from kivy.uix.gridlayout import GridLayout


class MainWindow(GridLayout):
    state = 0

    def active(self, win):
        print(win.active)
        
    def varr(self, win):
        print(int(win.value))


class OnSwitch(App):

    def build(self):
        return MainWindow()

    
OnSwitch().run()
