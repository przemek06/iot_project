from display import Display
from ui.screen import Screen
from PIL import Image,ImageDraw,ImageFont
from led import Led

class SuccessScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp

    def start(self):
        super().start()

        led = Led.get_instance("led")
        led.green_light()

    def on_red_button_click(self):
        led = Led.get_instance("led")
        led.turn_off()
        super().on_red_button_click()


    def draw_screen(self):
        super().draw_centered_text(self.disp, "Success")

