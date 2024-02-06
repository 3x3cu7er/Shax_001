from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class StackContent(StackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(100):
            b = Button(text=str(i + 1), size_hint=(.2, .2))
            self.add_widget(b)


class AnchorLayoutWidget(AnchorLayout):
    pass


class ScrollViewContent(ScrollView):
    pass


class GridContent(GridLayout):
    pass


class TheLabApp(App):

    def build(self):
        return ScrollViewContent()


TheLabApp().run()
