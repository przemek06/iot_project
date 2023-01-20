from display import Display
from ui.screen import Screen
from ticket import Ticket
from card_handler import RFID
from mqtt_queue import Queue


class RechargeScreen(Screen):
    def __init__(self, parent):
        super().__init__(parent)
        self.amount = 0
        self.disp = Display.get_instance("display").disp
        self.rfid = RFID.get_instance("rfid")

    def start(self):
        self.rfid.start_read()
        super().start()

    def on_red_button_click(self):
        self.rfid.end_read()
        super().on_red_button_click()

    def draw_screen(self):
        super().draw_centered_text(self.disp, "Apply card (" + str(self.ticket.price) + " zł)")

    def on_card_read(self, card_memory):
        try:
            card_memory.balance = card_memory.balance + self.amount

            mqqt_queue = Queue.get_instance("queue")
            mqqt_queue.send_recharge_info(card_memory.card_id, self.amount)
                        
            self.rfid.write_all_to_card(card_memory)
            success_screen = Screen.get_instance("success_screen")
            success_screen.start()

        except Exception as e:
            error_screen = Screen.get_instance("error_screen")
            error_screen.parent = self
            error_screen.start()

        finally:
            self.rfid.end_read()


