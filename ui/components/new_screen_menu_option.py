from ui.components.menu_option import MenuOption

class NewScreenMenuOption(MenuOption):

    def __init__(self, text, screen):
        super().__init__(text)
        self.screen = screen

    def on_click(self):
        if self.screen is not None:
            self.screen.start()