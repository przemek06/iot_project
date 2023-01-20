import neopixel
import board

class Led:
        
    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def __init__(self) -> None:
        self.ledStrip = neopixel.NeoPixel(board.D18, 8, brightness=1.0/32, auto_write=False)

    def update_led(self, color_arr):
        for i in range(8):
            self.ledStrip[i] = color_arr

        self.ledStrip.show()

    def red_light(self):
        self.update_led([255, 0, 0])

    def green_light(self):
        self.update_led([0, 255, 0])

    def turn_off(self):
        self.update_led([0, 0, 0])

