import oled.SSD1331 as SSD1331

class Display:

    instances = {}

    def __init__(self): 
        self.disp = SSD1331.SSD1331()
        self.disp.Init()
        self.disp.clear()

    @classmethod
    def add_instance(cls, id, display):
        cls.instances[id] = display

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

