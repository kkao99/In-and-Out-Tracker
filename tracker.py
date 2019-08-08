import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.metrics import dp

# layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

import datetime


class TrackerScreen(Screen):
    def __init__(self, **kwargs):
        super(TrackerScreen, self).__init__(**kwargs)
        self.container = FloatLayout(size=(dp(700), dp(500)))
        self.container.add_widget(TrackerLayout())
        self.add_widget(self.container)


class TrackerLayout(GridLayout):
    def __init__(self, **kwargs):
        super(TrackerLayout, self).__init__(**kwargs)

        # TODO: change cols to 1 and add gridlayout and anchorlayout for each row
        self.cols = 3
        self.size_hint = (0.7, 1)
        self.pos_hint = {'x': 0.15}
        self.padding = [0, dp(60), 0, dp(40)]
        self.spacing = [0, dp(50)]
        self.row_default_height = dp(45)
        self.row_force_default = True
        # btn = Button(text='click')
        # btn.bind(on_release=self.change_page)
        # self.add_widget(btn)

    def change_page(self, event):
        app = App.get_running_app()
        app.root.current = 'login'
        pass

    def _update(self):

        # TODO: save info to database, clear input field

        print('get time')
        print(self.ids.sign_btn.text)

        # TODO: regex retrieve '08:00 am mm/dd/yy'
        if self.ids.sign_btn.text == 'Check in':
            current = datetime.datetime.now()
            print(current)
            self.ids.sign_btn.text = 'Check out'
        else:
            current = datetime.datetime.now()
            print(current)
            self.ids.sign_btn.text = 'Check in'
