from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class TheLabApp(App):

    def build(self):
        return ContentLabel()


TheLabApp().run()