from kivy.app import App  
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout


class SysCong(App):

    def build(self):
        app = BoxLayout()

        # adding content
        lb = Label(
            text="# configuration .",
            color="#00ffce"
            )
        return app

    
SysCong().run()
