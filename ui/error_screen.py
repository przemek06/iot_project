from display import Display
from ui.screen import Screen
from led import Led
from buzzer import Buzzer

class ErrorScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp

    def start(self):
        super().start()
        buzzer = Buzzer.get_instance("buzzer")
        buzzer.schedule_buzz(2)
        led = Led.get_instance("led")
        led.red_light()

    def on_red_button_click(self):
        led = Led.get_instance("led")
        led.turn_off()
        super().on_red_button_click()

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Error")

