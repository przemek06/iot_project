from button import Button
from card_handler import RFID
from encoder import Encoder
from PIL import Image,ImageDraw,ImageFont
from display import Display

class Screen:

    instances = {}

    def __init__(self, parent):
        super().__init__()
        self.index = 0
        self.parent = parent
        self.__y_translation = 0

    @classmethod
    def add_instance(cls, id, screen):
        cls.instances[id] = screen

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]
        
    def get_index(self):
        return self.index
    
    def start(self):
        red_btn = Button.get_instance("red")
        red_btn.on_click = self.on_red_button_click

        green_btn = Button.get_instance("green")
        green_btn.on_click = self.on_green_button_click

        encoder = Encoder.get_instance("encoder")
        encoder.callback = self.on_encoder_change

        card_handler = RFID.get_instance("rfid")
        card_handler.callback = self.on_card_read

        self.draw_screen()

    def on_red_button_click(self):
        if self.parent is not None:
            self.parent.start()

    def on_green_button_click(self):
        pass

    def open_chosen_menu(self, options):
        options_length = len(options)
        chosen_option = self.get_index() % options_length
        if options[chosen_option] is not None:
            options[chosen_option].on_click()

    def on_encoder_change(self, direction):
        if direction == 'L':
            self.index = self.index - 1
        else:
            self.index = self.index + 1

        self.draw_screen()

    def on_card_read(self, data):
        pass

    def draw_screen(self):
        pass

    def draw_option_menu(self, disp, options):
        options_length = len(options)
        chosen_option = self.get_index() % options_length
        background = Image.new("RGB", (disp.width, disp.height), "BLACK")

        self.update_translation(chosen_option, disp.height)

        for ind, option in enumerate(options):
            back_color = "BLACK"
            font_color = "WHITE"

            if ind == chosen_option:
                back_color = "WHITE"
                font_color = "BLACK"

            row = Image.new("RGB", (disp.width, 12), back_color)
            draw = ImageDraw.Draw(row)
            draw.text((2, 0), option.text, fill = font_color)
            background.paste(row, (0, 12*ind))

        disp.ShowImage(background, 0, self.__y_translation)

    def update_translation(self, chosen_index, display_height):
        upper_line = 12*chosen_index
        bottom_line = 12 + upper_line

        if bottom_line + self.__y_translation > display_height:
            self.__y_translation = display_height - bottom_line

        if upper_line + self.__y_translation < 0:
            self.__y_translation = - upper_line
            

    def draw_centered_text(self, disp, text):
        background = Image.new("RGB", (disp.width, disp.height), "BLACK")

        row = Image.new("RGB", (disp.width, 12), "BLACK")
        draw = ImageDraw.Draw(row)
        draw.text((0, 0), text, fill = "WHITE")
        font = draw.font
        offset = 48 - font.getsize(text)[0] // 2

        background.paste(row, (offset, 30))

        disp.ShowImage(background, 0, 0)  