from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer import gravity
from kivy.properties import NumericProperty

Builder.load_string('''
<GravityInterface>:
    orientation: 'vertical'
    Label:
        id: x_label
        text: 'X: '
    Label:
        id: y_label
        text: 'Y: '
    Label:
        id: z_label
        text: 'Z: '

    Button
        text: 'Start Gravity Sensor'
        on_press: root.operations()
''')


class GravityInterface(BoxLayout):
    def __init__(self):
        super().__init__()
        self.sensorEnabled = False

    def operations(self):
        if not self.sensorEnabled:
            gravity.enable()
            Clock.schedule_interval(self.get_gravity, 1 / 20.)
            self.sensorEnabled = True

    def get_gravity(self, dt):
        val = gravity.gravity

        if not val == (None, None, None):
            self.ids.x_label.text = "X: " + str(val[0])
            self.ids.y_label.text = "Y: " + str(val[1])
            self.ids.z_label.text = "Z: " + str(val[2])


class GravityApp(App):
    def build(self):
        return GravityInterface()


GravityApp().run()
