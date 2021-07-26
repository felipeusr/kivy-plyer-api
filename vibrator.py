from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
#:import vibrator plyer.vibrator

FloatLayout:
    Button:
        on_release: vibrator.vibrate(0.004);
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)


Body().run()


"""
requirements -->

requirements = plyer
android.permissions = VIBRATE
"""