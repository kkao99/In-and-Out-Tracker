import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config


class TrackerApp(App):
    def build(self):
        return Button(text='click me')


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    TrackerApp().run()
