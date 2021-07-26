from kivy.app import App
from plyer import notification
from kivy.lang.builder import Builder

KV = """
FloatLayout:
    Button:
        size_hint: 0.5, 0.5
        pos_hint: {"center_x":0.500, "center_y":0.500}
        on_release: app.do_notify();
"""


class Body(App):
    def build(self):
        return Builder.load_string(KV)

    @staticmethod
    def do_notify(mode='toast'):
        title = "Hello title"
        message = "Hello message"
        ticker = "Hello ticker"
        kwargs = {'title': title, 'message': message, 'ticker': ticker}
        notification.notify(**kwargs)


Body().run()
