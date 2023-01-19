from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont


class CardInfoScreen(Screen):

    def __init__(self, parent):
        super().__init__(parent)
        self.card_memory = None
        self.disp = Display.get_instance("display").disp

    def draw_screen(self):
        if self.card_memory == None:
            super().draw_centered_text(self.disp, "No card read")
            return

        background = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK")
        attributes = ["UID", "Balance", "Tickets number"]

        for i, attribute in enumerate(attributes):
            row = Image.new("RGB", (self.disp.width, 12), "BLACK")
            draw = ImageDraw.Draw(row)
            draw.text((8, 0), attribute + ": " + "test", fill = "WHITE")
            background.paste(row, (8, 12 + 12*i))

        self.disp.ShowImage(background, 0, 0)  
