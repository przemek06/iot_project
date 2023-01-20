from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont


class TicketTermChoiceScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.options = []

    def start(self):
        menu_option_1 = NewScreenMenuOption("Short term", Screen.get_instance("short_term_tickets_screen"))
        menu_option_2 = NewScreenMenuOption("Long term", Screen.get_instance("long_term_tickets_screen"))

        self.options = [menu_option_1, menu_option_2]
        self.disp = Display.get_instance("display").disp
        super().start()
    
    def on_green_button_click(self):
        super().open_chosen_menu(self.options)


    def draw_screen(self):
        super().draw_option_menu(self.disp, self.options)
