from kivy.app import App  
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainWindow(GridLayout):
    state = StringProperty("0")

    def active(self, win):
        print(win.active)
        
    def varr(self, win):
        self.state = str(int(win.value))


class BLayouts(BoxLayout):

    def __init__(self, **kwargs):
        super().__init(**kwargs)
        for i in range(1, 10):
            return Button(
                text=f"{str(i)}"
            )


class OnSwitch(App):

    def build(self):
        return MainWindow()

    
OnSwitch().run()
