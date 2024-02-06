from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


class Shax(App):

    def build(self):
        # setting the app's layout
        gridl = GridLayout(cols=1)
        
        # adding image icons to the app
        img = Image(source="./prioritize.png")
        gridl.add_widget(img)
        
        # adding a label on top of user input
        handle = Label(text="#user handle %")
        gridl.add_widget(handle)
        
        # taking the input from the user 
        
        userin = TextInput(text="text %")
        gridl.add_widget(userin)
        
        return gridl


Shax().run()
