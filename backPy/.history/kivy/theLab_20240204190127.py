from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class TheLab(App):

    def build(self):
        win = BoxLayout()
    
        return win


TheLab().run()
