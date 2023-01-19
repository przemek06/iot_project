from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont


class TicketListScreen(Screen):

    def __init__(self, parent):
        super().__init__(parent)
        self.tickets = []
        self.disp = Display.get_instance("display").disp

    def draw_screen(self):
        if len(self.tickets) == 0:
            super().draw_centered_text(self.disp, "No tickets")
            return

        background = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK")
        attributes = ["ID", "Line number", "Valid to", "Reduced price"]

        for i, attribute in enumerate(attributes):
            row = Image.new("RGB", (self.disp.width, 12), "BLACK")
            draw = ImageDraw.Draw(row)
            draw.text((8, 0), attribute + ": " + "test", fill = "WHITE")
            background.paste(row, (8, 12 + 12*i))

        self.disp.ShowImage(background, 0, 0)  
