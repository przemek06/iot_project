from display import Display
from ui.screen import Screen
from PIL import Image,ImageDraw,ImageFont

class ErrorScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Error")

