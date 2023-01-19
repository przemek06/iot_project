from display import Display
from ui.screen import Screen
from ui.components.ticket_choice_menu_option import TicketChoiceMenuOption
from PIL import Image,ImageDraw,ImageFont


class LongTermTicketsScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        menu_option_1 = TicketChoiceMenuOption("1 day ticket, full price", None)
        menu_option_2 = TicketChoiceMenuOption("1 week ticket, full price", None)
        menu_option_3 = TicketChoiceMenuOption("1 month ticket, full price", None)
        menu_option_4 = TicketChoiceMenuOption("1 day ticket, reduced price", None)
        menu_option_5 = TicketChoiceMenuOption("1 week ticket, reduced price", None)
        menu_option_6 = TicketChoiceMenuOption("1 month ticket, reduced price", None)

        self.options = [menu_option_1, menu_option_2, menu_option_3, menu_option_4, menu_option_5, menu_option_6]
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        super().open_chosen_menu(self.options)

    def draw_screen(self):
        super().draw_option_menu(self.disp, self.options)
