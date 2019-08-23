import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

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

    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.size_hint = (0.6, 1)
        self.pos_hint = {'x': 0.2}
        self.padding = [0, dp(120), 0, dp(40)]
        self.spacing = [0, dp(60)]
        self.row_default_height = dp(40)
        self.row_force_default = True

        self.add_widget(Label(text='[Insert Titile]', font_size=dp(40)))

        self.user_container = self._create_user_layout()
        self.pass_container = self._create_pass_layout()
        self.btn_container = self._create_btn()

        self.add_widget(self.user_container)
        self.add_widget(self.pass_container)
        self.add_widget(self.btn_container)


    def _create_btn(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        btn = Button(text='login', size_hint=(None, None), width=dp(100), height=dp(50), font_size=dp(20))
        btn.bind(on_release=self._login)
        layout.add_widget(btn)
        return layout

    def _create_user_layout(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Username:'))
        layout.username_input = TextInput(text='', write_tab=False)
        layout.add_widget(layout.username_input)
        return layout

    def _create_pass_layout(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text='Password:'))
        layout.password_input = TextInput(text='', password=True, write_tab=False)
        layout.add_widget(layout.password_input)
        return layout


    def _login(self, event):

        if (self.user_container.username_input.text.strip() == 'admin' and
            self.pass_container.password_input.text.strip() == 'abc123'):

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
