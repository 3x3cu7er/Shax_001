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
        handle = Label(
            text="#user handle %",
            color='#00ffce'
        )
        gridl.add_widget(handle)
        # output a label on top of user input
        out = Label(text="handle inputed")
        gridl.add_widget(out)
        
        # taking the input from the user 
        
        userin = TextInput(multiline=False)
        gridl.add_widget(userin)
        
        # adding a button to the app
        
        btn = Button(text="enter")
        gridl.add_widget(btn)
        btn.bind(on_press=self.callback)
        return gridl

    def callback(self, *args):
        self.out.text = self.handle


Shax().run()
