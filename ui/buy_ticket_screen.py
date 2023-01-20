from display import Display
from ui.screen import Screen
from ticket import Ticket
from card_handler import RFID

class BuyTicketScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.ticket = None
        self.disp = Display.get_instance("display").disp
        self.rfid = RFID.get_instance("rfid")

    def start(self):
        self.rfid.start_read()
        super().start()

    def on_red_button_click(self):
        self.rfid.end_read()
        super().on_red_button_click()

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Apply card (" + str(self.ticket.price) + " zł)")

    def on_card_read(self, card_memory):
        try:
            if not card_memory.can_buy_ticket(self.ticket.price):
                raise Exception()

            card_memory.balance = card_memory.balance - self.ticket.price
            valid_tickets = card_memory.get_valid_tickets()
            valid_tickets.append(self.ticket)

            num_of_valid = len(valid_tickets)

            if num_of_valid > 46:
                raise Exception()

            valid_i = 0
                
            for i in range(46):
                if i < num_of_valid:
                    card_memory.tickets[i] = valid_tickets[valid_i]
                    valid_i = valid_i + 1
                else:
                    card_memory.tickets[i] = Ticket(0, 0, 0)
                        
            self.rfid.write_all_to_card(card_memory)
            success_screen = Screen.get_instance("success_screen")
            success_screen.start()

        except Exception as e:
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            error_screen.start()

        finally:
            self.rfid.end_read()


