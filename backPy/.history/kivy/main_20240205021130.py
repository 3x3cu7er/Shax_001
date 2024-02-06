from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.ancholayout import AnchorLayout


class MainWidget(Widget):
    pass


class ContentLabel(Label):
    pass


class AnchorLayoutWidget(AnchorLayout):
    pass


class TheLabApp(App):

    def build(self):
        return AnchorLayout()


TheLabApp().run()
