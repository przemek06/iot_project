from button import Button
from card_handler import RFID
from encoder import Encoder

class Screen:

    instances = {}

    def __init__(self):
        super().__init__()
        self.index = 0

    @classmethod
    def add_instance(cls, id, screen):
        cls.instances[id] = screen

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]
    
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
        pass

    def on_green_button_click(self):
        pass

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