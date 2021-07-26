from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from plyer import battery


KV = '''
FloatLayout:
    Label:
        id: label
        font_size: '50dp'
        pos_hint: {"center_x":0.500, "center_y":0.500}
'''


class Body(App):
    label = ObjectProperty()

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.label.text = str(battery.status['percentage']) + "%"


Body().run()

"""
requirements -->

requirements = plyer
android.permissions = BATTERY_STATS
"""