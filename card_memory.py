class CardMemory:
    def __init__(self, uid, balance, tickets):
        self.card_id = uid
        self.balance = balance
        self.tickets = tickets

    def get_writeable_balance(self):
        balance_bytes = self.balance.to_bytes(16, byteorder='big')
        return list(balance_bytes)

    def can_buy_ticket(self, price):
        return self.balance - price > 0