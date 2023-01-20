from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont
from card_handler import RFID
from ticket import Ticket

class ResetCardScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.disp = Display.get_instance("display").disp
        self.rfid = RFID.get_instance("rfid")

    def start(self):
        self.rfid.start_read()
        super().start()

    def on_red_button_click(self):
        self.rfid.end_read()
        super().on_red_button_click()
        

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Apply card")

    def on_card_read(self, card_memory):
        try:
            card_memory.balance = 0
            for i in range(46):
                card_memory.tickets[i] = Ticket(0, 0, 0)

            self.rfid.write_all_to_card(card_memory)
            super().parent.start()

        except Exception as e:
            print(e)
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            # stop reading etc
            error_screen.start()

        finally:
            self.rfid.end_read()

