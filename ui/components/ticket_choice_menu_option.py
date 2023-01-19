from ui.components.menu_option import MenuOption
from ui.screen import Screen

class TicketChoiceMenuOption(MenuOption):

    def __init__(self, text, ticket):
        super().__init__(text)
        self.ticket = ticket

    def on_click(self):
        buy_ticket_screen = Screen.get_instance("buy_ticket_screen")
        buy_ticket_screen.ticket = self.ticket
        buy_ticket_screen.start()