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
            super().draw_centered_text(self.disp, "No card")
            return

        background = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK")

        uid_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(uid_row)
        draw.text((0, 0), "UID: " + self.card_memory.card_id, fill = "WHITE")
        background.paste(uid_row, (0, 0))

        balance_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(balance_row)
        draw.text((0, 0), "Balance: " + self.card_memory.balance, fill = "WHITE")
        background.paste(balance_row, (0, 12))

        tickets_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(tickets_row)
        draw.text((0, 0), "Tickets: " + len(self.card_memory.get_valid_tickets()), fill = "WHITE")
        background.paste(tickets_row, (0, 24))

        self.disp.ShowImage(background, 0, 0)  
