from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Sino(App):

    def build(self):
        
        layout = BoxLayout(orientation="vertical")
        label = Label(text="planning .....")
        layout.add_widget(label)
        btn = Button(text="status")
        btn.bind(on_click=lambda x: print("content still loading."))
        layout.add_widget(btn)
        return layout


Sino().run()
