from ui.components.menu_option import MenuOption
from ui.screen import Screen

class AmountChoiceMenuOption(MenuOption):

    def __init__(self, text, amount):
        super().__init__(text)
        self.amount = amount

    def on_click(self):
        recharge_screen = Screen.get_instance("recharge_screen")
        recharge_screen.amount = self.amount
        recharge_screen.start()