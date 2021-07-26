from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_string('''
#:import proximity plyer.proximity

<MyFloatLayout>:
    proximity: proximity
    ToggleButton:
        text: "off"
        id: bt
        size_hint: 0.3, 0.2
        pos_hint: {"center_x":0.500, "center_y":0.500}
        on_state:
            if bt.state == "down": root.enable(); bt.text = "on"
            else: root.disable(); bt.text = "off";
''')


class MyFloatLayout(FloatLayout):
    proximity = ObjectProperty()
    is_near = BooleanProperty(False)

    def enable(self):
        self.proximity.enable()
        Clock.schedule_interval(self.get_proxime, 0.5)

    def disable(self):
        self.proximity.disable()
        Clock.unschedule(self.get_proxime)

    def get_proxime(self, dt):
        self.is_near = self.proximity.proximity

        if self.is_near is True:
            MDApp.get_running_app().theme_cls.theme_style = "Light"
        else:
            MDApp.get_running_app().theme_cls.theme_style = "Dark"


class Body(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MyFloatLayout()

    def on_pause(self):
        return True


Body().run()
