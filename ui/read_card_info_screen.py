from display import Display
from ui.screen import Screen


class ReadCardInfoScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
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
            pass
            # synchronize, validate data and write new ticket
            # open ticket list screen
        except:
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            # stop reading etc
            error_screen.start()
