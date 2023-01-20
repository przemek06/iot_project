from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from card_handler import RFID
from config import Config

class ReadValidityScreen(Screen):
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
            validity_screen = Screen.get_instance("validity_screen")
            for ticket in card_memory.tickets:
                line_number = Config.read_property("line_number")
                if ticket.is_fully_valid(line_number):
                    validity_screen.is_valid = True
                    validity_screen.start()
                    return
            
            validity_screen.is_valid = False
            validity_screen.start()

        except Exception as e:
            print(e)
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            error_screen.start()

        finally:
            self.rfid.end_read()

