from display import Display
from ui.screen import Screen
from PIL import Image,ImageDraw,ImageFont
from card_handler import RFID


class MainMenuScreen(Screen):

    def __init__(self):
        super().__init__()
        self.options = ["Buy tickets", "Check all tickets", "Check validity", "Check card ID"]
        self.disp = Display.get_instance("display").disp
    
    def on_green_button_click(self):
        chosen_option = super().get_index() % 4
        if chosen_option == 0:
            card_reader = RFID.get_instance("rfid")
            card_reader.start_read()


        elif chosen_option == 1:
            pass
        elif chosen_option == 2:
            pass
        elif chosen_option == 3:
            pass

    def draw_screen(self):
        chosen_option = super().get_index() % 4
        background = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK")

        for ind, option in enumerate(self.options):
            back_color = "BLACK"
            font_color = "WHITE"

            if ind == chosen_option:
                back_color = "WHITE"
                font_color = "BLACK"

            row = Image.new("RGB", (self.disp.width, 12), back_color)
            draw = ImageDraw.Draw(row)
            draw.text((8, 0), option, fill = font_color)
            background.paste(row, (0, 12*ind))

        self.disp.ShowImage(background,0,0)

            
    def on_card_read(self, datat):
        data = []

        for x in range(0x0, 0x08):
            data.append(x)
        
        for x in range(0x0, 0xF8):
            data.append(0)

        card_reader = RFID.get_instance("rfid")
        card_reader.write_to_card(2, data)
        print(card_reader.reading)