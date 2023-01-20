from display import Display
from ui.screen import Screen
from ui.components.amount_choice_menu_option import AmountChoiceMenuOption

class RechargeOptionsScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)

        menu_option_1 = AmountChoiceMenuOption("10 zł", 10)
        menu_option_2 = AmountChoiceMenuOption("25 zł", 25)
        menu_option_3 = AmountChoiceMenuOption("50 zł", 50)
        menu_option_4 = AmountChoiceMenuOption("100 zł", 100)

        self.options = [menu_option_1, menu_option_2, menu_option_3, menu_option_4]
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        super().open_chosen_menu(self.options)

    def draw_screen(self):
        super().draw_option_menu(self.disp, self.options)

