from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from plyer import tts


class MainApp(MDApp):
    def speak(self, message):
        tts.speak(message)

MainApp().run()