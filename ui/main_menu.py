from display import Display
from ui.screen import Screen
from ui.components.new_screen_menu_option import NewScreenMenuOption
from PIL import Image,ImageDraw,ImageFont


class MainMenuScreen(Screen):

    def __init__(self, parent):
        super().__init__(parent)
        menu_option_1 = NewScreenMenuOption("Buy tickets", Screen.get_instance("ticket_term_choice_screen"))
        menu_option_2 = NewScreenMenuOption("List tickets", Screen.get_instance("read_ticket_list_screen"))
        menu_option_3 = NewScreenMenuOption("Check validity", None)
        menu_option_4 = NewScreenMenuOption("Show card info", Screen.get_instance("read_card_info_screen"))
        menu_option_5 = NewScreenMenuOption("Clean card", Screen.get_instance("reset_card_screen"))

        self.options = [menu_option_1, menu_option_2, menu_option_3, menu_option_4, menu_option_5]
        self.options_length = len(self.options)
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        super().open_chosen_menu(self.options)

    def draw_screen(self):
        super().draw_option_menu(self.disp, self.options)
