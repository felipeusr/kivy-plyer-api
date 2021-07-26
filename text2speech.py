from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import tts

KV = """
FloatLayout:
    MDTextField:
        hint_text: "Digit here"
        helper_text: "ex: car"
        size_hint: 0.80, 0.07
        helper_text_mode: "on_focus"
        id: input
        pos_hint: {"center_x":0.500, "center_y":0.550}
        on_text_validate: app.to_voice()
"""


class Body(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def to_voice(self):
        tts.speak(self.root.ids.input.text)


Body().run()
