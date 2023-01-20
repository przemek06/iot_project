import RPi.GPIO as GPIO
import time, datetime 
from dateutil.relativedelta import relativedelta

BUZZER_PIN = 23

class Buzzer:
    
    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def __init__(self) -> None:
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        GPIO.output(BUZZER_PIN, 1)

        self.off_time = 0 

    def update(self):
        if self.off_time < time.time():
            GPIO.output(BUZZER_PIN, 0)


    def schedule_buzz(self, seconds):
        GPIO.output(BUZZER_PIN, 1)
        end_date = datetime.today() + relativedelta(seconds=seconds)
        self.off_time = int((end_date-datetime(1970,1,1)).total_seconds())
        