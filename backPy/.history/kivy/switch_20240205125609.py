from kivy.app import App  
from kivy.uix.gridlayout import GridLayout


class MainWindow(GridLayout):
    pass


class OnSwitch(App):

    def active(self):
        pass

    def build(self):
        return MainWindow()

    
OnSwitch().run()
