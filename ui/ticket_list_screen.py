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
        current_ticket = super().get_index() % len(self.tickets)

        id_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(id_row)
        draw.text((0, 0), "ID: " + current_ticket, fill = "WHITE")
        background.paste(id_row, (0, 0))

        line_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(line_row)
        draw.text((0, 0), "Line: " + self.tickets[current_ticket].line, fill = "WHITE")
        background.paste(line_row, (0, 12))

        valid_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(valid_row)
        draw.text((0, 0), "Valid to:", fill = "WHITE")
        background.paste(valid_row, (0, 24))

        date_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(date_row)
        draw.text((0, 0), self.tickets[current_ticket].get_readable_date(), fill = "WHITE")
        background.paste(date_row, (0, 36))

        student_row = Image.new("RGB", (self.disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(student_row)
        draw.text((0, 0), "Student: " + bool(self.tickets[current_ticket].is_reduced), fill = "WHITE")
        background.paste(student_row, (0, 48))

        self.disp.ShowImage(background, 0, 0)  
