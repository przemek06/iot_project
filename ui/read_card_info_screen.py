from display import Display
from ui.screen import Screen
from card_handler import RFID

class ReadCardInfoScreen(Screen):
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
            card_info_screen = Screen.get_instance("card_info_screen")
            card_info_screen.card_memory = card_memory
            card_info_screen.start()
            
        except Exception as e:
            print(e)
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            error_screen.start()

        finally:
            self.rfid.end_read()

