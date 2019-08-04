import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# local files
from tracker import TrackerScreen
from login import LoginScreen


class TrackerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TrackerScreen(name='tracker'))
        return sm


if __name__ == '__main__':
    Config.set('graphics', 'resizable', True)
    Window.clearcolor = (0.8, 0.8, 0.8, 1)
    TrackerApp().run()
