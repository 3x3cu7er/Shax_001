from kivy.app import App  
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout


class SysCong(App):

    def build(self):
        self.app = BoxLayout()

        # adding content
        self.lb = Label(
            text="# configuration .",
            color="#00ffce"
            )
        self.app.add_widget(self.lb)
        return app

    
SysCong().run()
