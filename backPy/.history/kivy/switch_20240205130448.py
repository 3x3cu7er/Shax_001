from kivy.app import App  
from kivy.uix.gridlayout import GridLayout


class MainWindow(GridLayout):

    def active(self, win):
        print(win.active)
        
    def varr(self, win):
        print(wint(in.value))


class OnSwitch(App):

    def build(self):
        return MainWindow()

    
OnSwitch().run()
