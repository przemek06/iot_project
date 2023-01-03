from display import Display
from screen import Screen
from PIL import Image,ImageDraw,ImageFont

class MainMenuScreen(Screen):

    def __init__(self):
        super().__init__()
        self.options = ["Buy tickets", "Check all tickets", "Check validity", "Check card ID"]
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        chosen_option = super.index % 4

        if chosen_option == 0:
            pass
        elif chosen_option == 1:
            pass
        elif chosen_option == 2:
            pass
        elif chosen_option == 3:
            pass

    def draw_screen(self):
        chosen_option = super.index % 4
        background = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK")

        for ind, option in enumerate(self.options):
            back_color = "BLACK"
            font_color = "WHITE"

            if ind == chosen_option:
                back_color = "WHITE"
                font_color = "BLACK"

            row = Image.new("RGB", (self.disp.width, 8), back_color)
            draw = ImageDraw.Draw(row)
            draw.text((8, 0), option, fill = font_color)
            background.paste(row, (0, 8*ind))

        self.disp.ShowImage(background,0,0)

            
            