from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class AnchorLayoutWidget(AnchorLayout):
    pass


class GridContent():
    pass


class TheLabApp(App):

    def build(self):
        return GridContent()


TheLabApp().run()
