from display import Display
from ui.screen import Screen
from buzzer import Buzzer
from led import Led

class ValidityScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp
        self.is_valid = False

    def start(self):
        led = Led.get_instance("led")

        if self.is_valid:
            led.green_light()
        else:
            buzzer = Buzzer.get_instance("buzzer")
            buzzer.schedule_buzz(2)
            led.red_light()

        super().start()

    def on_red_button_click(self):
        led = Led.get_instance("led")
        led.turn_off()
        super().on_red_button_click()

    def draw_screen(self):
        if self.is_valid:
            super().draw_centered_text(self.disp, "Valid ticket")
        else:
            super().draw_centered_text(self.disp, "No valid ticket")




