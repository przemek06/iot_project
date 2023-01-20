from display import Display
from ui.screen import Screen

class ValidityScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp
        self.is_valid = False

    def draw_screen(self):
        if self.is_valid:
            super().draw_centered_text(self.disp, "Valid ticket")
        else:
            super().draw_centered_text(self.disp, "No valid ticket")

