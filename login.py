import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

# layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

# widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.container = FloatLayout(size=(dp(700), dp(500)))
        self.container.add_widget(LoginLayout(cols=1))
        self.add_widget(self.container)


class LoginLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.size_hint = (0.6, 1)
        self.pos_hint = {'x': 0.2}
        self.padding = [0, dp(60), 0, dp(40)]
        self.spacing = [0, dp(60)]
        self.row_default_height = dp(30)
        self.row_force_default = True

        self.user_container = self._create_user_layout()
        self.pass_container = self._create_pass_layout()

        self.add_widget(self.user_container)
        self.add_widget(self.pass_container)

        # TODO: create kivy lang file for layout
        btn = Button(text='login')
        btn.bind(on_release=self._login)
        self.add_widget(btn)

    def _create_user_layout(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Username:'))
        layout.add_widget(TextInput(text=''))
        return layout

    def _create_pass_layout(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Password:'))
        layout.add_widget(TextInput(text='', password=True))
        return layout


    def _login(self, event):

        # TODO: add verification
        app = App.get_running_app()
        app.root.current = 'tracker'
