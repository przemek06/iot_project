import RPi.GPIO as GPIO

import time 

class Button:

    instances = {}

    def __init__(self, pin): 
        self.pin = pin 
        self.last_change = 0  
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   
        GPIO.add_event_detect(self.pin, GPIO.BOTH, self.handle_click) 

    @classmethod
    def add_instance(cls, id, button):
        cls.instances[id] = button

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def on_click(self):
        pass 
        
    def handle_click(self, pin): 
        current_time = time.time() 
        if current_time - self.last_change > 0.2:  
            self.last_change = current_time 
            if GPIO.input(pin) == 0:  
                self.on_click()
