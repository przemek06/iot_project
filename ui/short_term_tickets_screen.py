from display import Display
from ui.screen import Screen
from ui.components.ticket_choice_menu_option import TicketChoiceMenuOption
from ticket import Ticket
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from config import Config

class ShortTermTicketsScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        line_number = Config.read_property("line_number")

        ticket_1 =  Ticket(0, line_number, self.get_date(15))
        ticket_2 =  Ticket(0, line_number, self.get_date(30))
        ticket_3 =  Ticket(0, line_number, self.get_date(60))
        ticket_4 =  Ticket(1, line_number, self.get_date(15))
        ticket_5 =  Ticket(1, line_number, self.get_date(30))
        ticket_6 =  Ticket(1, line_number, self.get_date(60))

        ticket_1.price = 2
        ticket_2.price = 3
        ticket_3.price = 4
        ticket_4.price = 4       
        ticket_5.price = 6
        ticket_6.price = 8

        menu_option_1 = TicketChoiceMenuOption("15 min, full", ticket_1)
        menu_option_2 = TicketChoiceMenuOption("30 min, full", ticket_2)
        menu_option_3 = TicketChoiceMenuOption("1 h, full", ticket_3)
        menu_option_4 = TicketChoiceMenuOption("15 min, reduced", ticket_4)
        menu_option_5 = TicketChoiceMenuOption("30 min, reduced", ticket_5)
        menu_option_6 = TicketChoiceMenuOption("1 h, reduced", ticket_6)

        self.options = [menu_option_1, menu_option_2, menu_option_3, menu_option_4, menu_option_5, menu_option_6]
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        super().open_chosen_menu(self.options)

    def draw_screen(self):
        super().draw_option_menu(self.disp, self.options)

    def get_date(self, to_add):
        new_date = datetime.today() + relativedelta(minute=to_add)
        return int((new_date-datetime(1970,1,1)).total_seconds())