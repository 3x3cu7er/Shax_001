from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class AnchorLayoutWidget(AnchorLayout):
    pass


class GridContent(GridLayout):
    pass


class TheLabApp(App):

    def build(self):
        stc = StackLayout()
        for i in range(1, 10):
            stc.add_widget(btn)


TheLabApp().run()
