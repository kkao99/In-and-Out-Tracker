import kivy
kivy.require('1.11.1')

from kivy.app import App

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class TrackerScreen(Screen):
    def __init__(self, **kwargs):
        super(TrackerScreen, self).__init__(**kwargs)
        btn = Button(text='click')
        btn.bind(on_release=self.change_page)
        self.add_widget(btn)

    def change_page(self, event):
        print('changing page')
        app = App.get_running_app()
        app.root.current = 'login'
