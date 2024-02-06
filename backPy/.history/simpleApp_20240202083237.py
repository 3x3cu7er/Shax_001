# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button


# class Sino(App):

#     def build(self):
        
#         layout = BoxLayout(orientation="vertical")
#         label = Label(text="planning .....")
#         layout.add_widget(label)
#         btn = Button(text="status")
#         btn.bind(on_click=lambda x: print("content still loading."))
#         layout.add_widget(btn)
#         return layout


# Sino().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.event import EventDispatcher
Builder.load_string("""
<CustLab1@Label>
 size_hint:0.3,1
<CustLab2@Label>
 text: "Result"
 size_hint: 0.5,1
<CustButton@Button>
 text: "+1"
 size_hint: 0.1,1
<CustTextInput@TextInput>:
 multiline: False
 size_hint:0.1,1
<Tuto_Property>:
 orientation: "vertical"
 padding:10,10
 spacing: 10
 Label:
 text: "Press the 3 button (+1) several times and then modify the number in the
TextInput.The first counter (with StringProperty but no binding) doesn't take into account the
change that happened in the app, but the second one does.String Property makes it easy to pass
the update from the python side to the user interface, binding pass the changes that happened
on the user interface to the python side. "
 text_size: self.size
 padding: 20,20
 Property_no_Binding:
 Property_with_Binding:
 Simple:
<Property_no_Binding>:
 spacing: 10
 label_ObjectProperty: result
 CustLab1:
 text: "With Property but no Binding"
 CustButton:
 on_press: root.counter_textInput_StringProperty()
 CustTextInput: