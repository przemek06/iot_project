import RPi.GPIO as GPIO
from button import Button
from encoder import Encoder
from card_handler import RFID
from display import Display
from ui.screen import Screen
from ui.main_menu import MainMenuScreen
from ui.ticket_term_choice_screen import TicketTermChoiceScreen
from ui.short_term_tickets_screen import ShortTermTicketsScreen
from ui.long_term_tickets_screen import LongTermTicketsScreen
from ui.buy_ticket_screen import BuyTicketScreen
from ui.error_screen import ErrorScreen
from ui.success_screen import SuccessScreen
from ui.read_ticket_list_screen import ReadTicketListScreen
from ui.ticket_list_screen import TicketListScreen
from ui.reset_card_screen import ResetCardScreen

GPIO.setmode(GPIO.BCM)

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
    main_menu_screen = MainMenuScreen(None)
    ticket_term_choice_screen = TicketTermChoiceScreen(main_menu_screen)
    short_term_tickets_screen = ShortTermTicketsScreen(ticket_term_choice_screen)
    long_term_tickets_screen = LongTermTicketsScreen(ticket_term_choice_screen)
    buy_ticket_screen = BuyTicketScreen(ticket_term_choice_screen)
    error_screen = ErrorScreen(main_menu_screen)
    success_screen = SuccessScreen(main_menu_screen)
    read_ticket_list_screen = ReadTicketListScreen(main_menu_screen)
    ticket_list_screen = TicketListScreen(main_menu_screen)
    reset_card_screen = ResetCardScreen(main_menu_screen)

    Screen.add_instance("main_menu_screen", main_menu_screen)
    Screen.add_instance("ticket_term_choice_screen", ticket_term_choice_screen)
    Screen.add_instance("short_term_tickets_screen", short_term_tickets_screen)
    Screen.add_instance("long_term_tickets_screen", long_term_tickets_screen)
    Screen.add_instance("buy_ticket_screen", buy_ticket_screen)
    Screen.add_instance("error_screen", error_screen)
    Screen.add_instance("success_screen", success_screen)
    Screen.add_instance("read_ticket_list_screen", read_ticket_list_screen)
    Screen.add_instance("ticket_list_screen", ticket_list_screen)
    Screen.add_instance("reset_card_screen", reset_card_screen)


def main():
    initialize_multitons()
    card_handler = RFID.get_instance("rfid")
    main_menu_screen = Screen.get_instance("main_menu_screen")
    main_menu_screen.start()
    
    while True:     
        card_handler.read_card()

if __name__ == "__main__":
    main()