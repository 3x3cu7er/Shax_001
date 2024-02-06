from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


class Shax(App):

    def build(self):
        # setting the app's layout
        self.gridl = GridLayout()
        self.gridl.cols = 1
        # designing window content
        self.gridl.size_hint = (
            0.5, 0.5
        )
        
        self.gridl.pos_hint = {'center_x':.5, 'center_y':.5}
        
        # adding image icons to the app
        img = Image(source="./prioritize.png")
        self.gridl.add_widget(img)
        
        # adding a label on top of user input
        handle = Label(
            text="#user handle %",
            color='#00ffce',
            font_size=60
        )
        self.gridl.add_widget(handle)
        # output a label on top of user input
        self.out = Label(text="handle inputed")
        self.gridl.add_widget(self.out)
        
        # taking the input from the user 
        
        self.userin = TextInput(
            multiline=False,
            padding_
            
        )
        self.gridl.add_widget(self.userin)
        
        # adding a button to the app
        
        self.btn = Button(text="enter")
        self.btn.bind(on_press=self.callback)
        self.gridl.add_widget(self.btn)
        self.msg = self.userin
        return self.gridl

    def callback(self, instance):
        self.out.text = self.userin.text


Shax().run()
