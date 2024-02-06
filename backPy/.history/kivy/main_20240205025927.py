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

    def __init__(self, *args):
        super().__init__(self, *args)
        for i in range(1, 20):
            btn = Button(text=str(i + 1), size_hint=(.2, .2))
            self.add_widget(btn)


class AnchorLayoutWidget(AnchorLayout):
    pass


class GridContent(GridLayout):
    pass


class TheLabApp(App):

    def build(self):
        return StackContent()


TheLabApp().run()
