from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class StackContent(Label):
    pass


class AnchorLayoutWidget(AnchorLayout):
    pass


class GridContent(GridLayout):
    pass


class TheLabApp(App):

    def build(self):
        return StackContent()


TheLabApp().run()
