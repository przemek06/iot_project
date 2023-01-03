import RPi.GPIO as GPIO
from button import Button
from encoder import Encoder
from card_handler import RFID

GPIO.setmode(GPIO.BCM)  

def print_sth():
    print("clicked")

def print_dir(direction):
    print(direction)

def print_data(data):
    print(data)

def initialize_multitons():
    red_btn = Button(5)
    green_btn = Button(6)
    Button.add_instance("red", red_btn)
    Button.add_instance("green", green_btn)
    encoder = Encoder(27, 17)
    Encoder.add_instance("encoder", encoder)
    card_handler = RFID()
    RFID.add_instance("rfid", card_handler)

def main():
    initialize_multitons()
    red_btn = Button.get_instance("red")
    red_btn.on_click = print_sth
    encoder = Encoder.get_instance("encoder")
    encoder.callback = print_dir
    card_handler = RFID.get_instance("rfid")
    card_handler.callback = print_data

    while True:     
        card_handler.read_all()

if __name__ == "__main__":
    main()