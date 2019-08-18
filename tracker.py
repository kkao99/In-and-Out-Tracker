import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen
# from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore

# layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

import datetime


class TrackerScreen(Screen):
    def __init__(self, **kwargs):
        super(TrackerScreen, self).__init__(**kwargs)
        self.container = FloatLayout(size=(dp(700), dp(500)))
        self.container.add_widget(TrackerLayout())
        self.add_widget(self.container)


class TrackerLayout(GridLayout):

    time_data = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TrackerLayout, self).__init__(**kwargs)

        # basic setting
        self.cols = 1
        self.size_hint = (0.7, 1)
        self.pos_hint = {'x': 0.15}
        self.padding = [0, dp(60), 0, dp(40)]
        self.spacing = [0, dp(50)]
        self.row_default_height = dp(45)
        self.row_force_default = True

        self.time_data = JsonStore('time_data.json')

        self.grade_dropdown = GradeDropdown()
        self.grade_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.grade_btn, 'text', x))

    def change_page(self, event):
        app = App.get_running_app()
        app.root.current = 'login'
        pass

    def _open_grade_dropdown(self, widget):
        self.grade_dropdown.open(widget)

    def _update(self):

        # TODO: save info to database, clear input field, and validate

        print(self.ids.check_btn.text)

        if self.ids.check_btn.text == 'Check in':
            current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(current)
            self.ids.check_btn.text = 'Check out'
            self.time_data.put(f"{self.ids.first_name.text}{self.ids.last_name.text}", in_time=current)

        else:
            current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(current)

            handler = open('report.csv', 'a')
            name = f"{self.ids.first_name.text},{self.ids.last_name.text}"
            in_time = self.time_data.get(name.replace(',', ''))['in_time']
            out_time = f"{str(current)}"
            msg = f"{name},{self.ids.grade_btn.text},{in_time},{out_time}\n"
            handler.write(msg)

            self.ids.check_btn.text = 'Check in'
            self.ids.first_name.text = ''
            self.ids.last_name.text = ''


class GradeDropdown(DropDown):
    pass
