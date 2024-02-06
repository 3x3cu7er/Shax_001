from kivy.app import App  
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout


class SysCong(App):

    def build(self):
        self.app = BoxLayout("vertical")

        # adding content
        self.lb = Label(
            text="# configuration .",
            color="#00ffce",
            font_size=30
            )
        self.app.add_widget(self.lb)
        self.img = Image(source="./prioritize.png")
        self.app.add_widget(self.img)
        
        return self.app

    
SysCong().run()
