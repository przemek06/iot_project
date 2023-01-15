import RPi.GPIO as GPIO
from button import Button
from encoder import Encoder
from card_handler import RFID
from display import Display
from ui.main_menu import MainMenuScreen
from ui.screen import Screen

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
    display = Display()
    Display.add_instance("display", display)
    main_menu_screen = MainMenuScreen()
    Screen.add_instance("main_menu_screen", main_menu_screen)

def main():
    initialize_multitons()
    card_handler = RFID.get_instance("rfid")
    main_menu_screen = Screen.get_instance("main_menu_screen")
    main_menu_screen.start()
    
    while True:     
        card_handler.read_card()

if __name__ == "__main__":
    main()