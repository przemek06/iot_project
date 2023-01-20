class CardMemory:
    def __init__(self, uid, balance, tickets):
        self.card_id = uid
        self.balance = balance
        self.tickets = tickets

    def get_writeable_balance(self):
        balance_bytes = self.balance.to_bytes(16, byteorder='big')
        balance_arr = list(balance_bytes)
        balance_arr.extend(48 * [0]) 
        print((balance_arr))
        return (balance_arr)

    def can_buy_ticket(self, price):
        return self.balance - price > 0

    def get_valid_tickets(self):
        return list(filter(lambda ticket: ticket.is_valid(), self.tickets))

    def __str__(self):
        return "UID: " + str(self.card_id) + "\n" + "Balance: " + str(self.balance) + "\n" + "Tickets: " + str(self.tickets) + "\n"