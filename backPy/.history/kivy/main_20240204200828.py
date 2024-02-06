from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class TheLab(Widget):

    def build(self):
        return MainWidget()


TheLab().run()
