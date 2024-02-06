from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Sino(App):

    def build(self):

        # mylayout = BoxLayout(orientation="vertical")
        # mylabel = Label(text="My App")
        # mybutton = Button(text="Click me!")
        # mylayout.add_widget(mylabel)
        # mybutton.bind(on_press=lambda a:print(mylabel.text))
        # mylayout.add_widget(mybutton)
        # return mylayout
        layout = BoxLayout(orientation="vertical")
        label = Label(text="planning .....")
        layout.add_widget(label)
        btn = Button(text="status")
        btn.bind(on_click=lambda x: print("content still loading."))
        layout.add_widget(btn)
        return layout


Sino().run()
