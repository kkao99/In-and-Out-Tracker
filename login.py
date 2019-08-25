import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

# layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

# widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.container = FloatLayout(size=(dp(700), dp(500)))
        self.container.add_widget(LoginLayout(cols=1))
        self.add_widget(self.container)


class LoginLayout(GridLayout):

    """
    default username: admin
    default password: abc123
    """

    username_input = StringProperty()
    password_input = StringProperty()

    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.size_hint = (0.6, 1)
        self.pos_hint = {'x': 0.2}
        self.padding = [0, dp(120), 0, dp(40)]
        self.spacing = [0, dp(60)]
        self.row_default_height = dp(40)
        self.row_force_default = True

        self.username_input = ''
        self.password_input = ''

    def _login(self, event):

        if (self.username_input.strip() == 'admin' and
            self.password_input == 'abc123'):

            # redirect to tracker page
            app = App.get_running_app()
            app.root.current = 'tracker'

        else:

            # error message popup window
            error_popup = Popup(title='Error Message',
                        title_color=[1, 1, 0, 1],
                        title_align='center',
                        title_size=dp(20),
                        content=Label(text='Incorrect username or password.', color=[1, 0, 0, 1], font_size=dp(18)),
                        size_hint=(None, None),
                        size=(dp(300), dp(300)),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

            error_popup.open()
