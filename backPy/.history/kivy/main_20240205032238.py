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


class StackContent(StackLayout):

    btn = Button()
    for i in range(1, 10):
        self.add_widget(btn)


class AnchorLayoutWidget(AnchorLayout):
    pass


class GridContent(GridLayout):
    pass


class TheLabApp(App):

    def build(self):
        for i in range(1, 10):
            return StackContent()


TheLabApp().run()
