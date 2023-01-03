import RPi.GPIO as GPIO
import time 

class Encoder:

    instances = {}

    def __init__(self, pin_a, pin_b):
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.state = '00'
        self.direction = None

        # Set up the GPIO pins
        GPIO.setup(self.pin_a, GPIO.IN)
        GPIO.setup(self.pin_b, GPIO.IN)

        # Set up the event handlers
        GPIO.add_event_detect(self.pin_a, GPIO.BOTH, self.update_position)
        GPIO.add_event_detect(self.pin_b, GPIO.BOTH, self.update_position)

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def update_position(self, pin):
        p1 = GPIO.input(self.pin_a)
        p2 = GPIO.input(self.pin_b)
        newState = "{}{}".format(p1, p2)

        if self.state == "00":
            if newState == "01":
                self.direction = "R"
            elif newState == "10":
                self.direction = "L"

        elif self.state == "01":
            if newState == "11":
                self.direction = "R"
            elif newState == "00":
                if self.direction == "L":
                    if self.callback is not None:
                        self.callback(self.direction)

        elif self.state == "10":
            if newState == "11":
                self.direction = "L"
            elif newState == "00":
                if self.direction == "R":
                    if self.callback is not None:
                        self.callback(self.direction)

        else:
            if newState == "01":
                self.direction = "L"
            elif newState == "10":
                self.direction = "R"
            elif newState == "00":
                if self.direction == "L":
                    if self.callback is not None:
                        self.callback(self.direction)
                elif self.direction == "R":
                    if self.callback is not None:
                        self.callback(self.direction)
                
        self.state = newState
                

    def callback(self, direction):
        pass
