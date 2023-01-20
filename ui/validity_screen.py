from display import Display
from ui.screen import Screen
from buzzer import Buzzer

class ValidityScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp
        self.is_valid = False

    def start(self):
        super().start()
        if not self.is_valid:
            buzzer = Buzzer.get_instance("buzzer")
            buzzer.schedule_buzz(2)

    def draw_screen(self):
        if self.is_valid:
            super().draw_centered_text(self.disp, "Valid ticket")
        else:
            super().draw_centered_text(self.disp, "No valid ticket")




