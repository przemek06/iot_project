from display import Display
from ui.screen import Screen

class ErrorScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp

    def start(self):
        super().start()
        buzzer = Buzzer.get_instance("buzzer")
        buzzer.schedule_buzz(2)

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Error")

