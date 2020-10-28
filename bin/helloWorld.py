import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text = "ip = "))
        self.ip = TextInput(multiline = False)
        self.add_widget(self.ip)

        self.add_widget(Label(text = "Port = "))
        self.port = TextInput(multiline = False)
        self.add_widget(self.port)

        self.add_widget(Label(text = "Username = "))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.join = Button(text = "Join")
        self.join.bind(on_press = self.join_button)
        self.add_widget(self.join)

 
class MyApp(App):
    def build(self):
        return ConnectPage()



MyApp().run()
