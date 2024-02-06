from kivy.app import App  
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class MainWindow(GridLayout):
    state = StringProperty("0")

    def active(self, win):
        print(win.active)
        
    def varr(self, win):
        self.state = str(int(win.value))


class BLayouts(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 10):
            btn = Button(
                text=f"{str(i)}",
                size_hint=(.2, .2)
            )
        self.add_widget(btn)


class OnSwitch(App):

    def build(self):
        return BLayouts()

    
OnSwitch().run()
