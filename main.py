from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SampleScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Hello World!!"))



class SampleApp(App):
    def build(self):
        return SampleScreen()

SampleApp().run()