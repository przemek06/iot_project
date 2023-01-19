from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont


class BuyTicketScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.ticket = None
        self.disp = Display.get_instance("display").disp

    def start(self):
        super().start()
        # start reading

    def on_red_button_click(self):
        super().on_red_button_click()
        # stop reading etc

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Apply your card to the scanner")


    def on_card_read(self, data):
        try:
            # synchronize, validate data and write new ticket
            success_screen = Screen.get_instance("success_screen")
        except:
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            # stop reading etc
            error_screen.start()
