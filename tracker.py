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
from functools import partial


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

        for i in range(1, 6):
            """ Create grade 9-12 dropdown list. """
            self.ids[f'grade_dropdown_{i}'] = DropDown()
            btn = Button(size_hint_y=None, text='9', height=dp(40), font_size=dp(18))
            btn.bind(on_release=partial(self._select_grade, index=i))
            self.ids[f'grade_dropdown_{i}'].add_widget(btn)

            btn = Button(size_hint_y=None, text='10', height=dp(40), font_size=dp(18))
            btn.bind(on_release=partial(self._select_grade, index=i))
            self.ids[f'grade_dropdown_{i}'].add_widget(btn)

            btn = Button(size_hint_y=None, text='11', height=dp(40), font_size=dp(18))
            btn.bind(on_release=partial(self._select_grade, index=i))
            self.ids[f'grade_dropdown_{i}'].add_widget(btn)

            btn = Button(size_hint_y=None, text='12', height=dp(40), font_size=dp(18))
            btn.bind(on_release=partial(self._select_grade, index=i))
            self.ids[f'grade_dropdown_{i}'].add_widget(btn)

            # self.ids[f'grade_dropdown_{i}'].bind(on_select=lambda instance, x: setattr(self.ids[f'grade_btn_{i}'], 'text', x))

    def _select_grade(self, event, index):
        self.ids[f'grade_dropdown_{index}'].select(event.text)
        self.ids[f'grade_btn_{index}'].text = event.text

    def change_page(self, event):
        app = App.get_running_app()
        app.root.current = 'login'
        pass

    def _open_grade_dropdown(self, widget, index):
        self.ids[f'grade_dropdown_{index}'].open(widget)

    def _update(self, index):

        # TODO: save info to database, clear input field, and validate

        print(self.ids[f'check_btn_{index}'].text)

        if self.ids[f'check_btn_{index}'].text == 'Check in':

            # save the "get in time" to json
            current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(current)
            self.time_data.put(f"{self.ids[f'first_name_{index}'].text}{self.ids[f'last_name_{index}'].text}", in_time=current)

            self.ids[f'check_btn_{index}'].text = 'Check out'

        else:

            """ Write first_name,last_name,grade,in_time,out_time to csv file. """

            current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(current)

            handler = open('report.csv', 'a')
            name = f"{self.ids[f'first_name_{index}'].text},{self.ids[f'last_name_{index}'].text}"
            in_time = self.time_data.get(name.replace(',', ''))['in_time']
            msg = f"{name},{self.ids[f'grade_btn_{index}'].text},{in_time},{str(current)}\n"
            handler.write(msg)

            # reset this row's input fields
            self.ids[f'check_btn_{index}'].text = 'Check in'
            self.ids[f'first_name_{index}'].text = ''
            self.ids[f'last_name_{index}'].text = ''
            self.ids[f'grade_btn_{index}'].text = 'Grade'

            self.time_data.delete(name.replace(',', ''))


class GradeDropdown(DropDown):
    pass
