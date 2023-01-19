class Ticket:
    def __init__(self, is_reduced, line, date):
        self.is_reduced = is_reduced
        self.line = line
        self.validity_date = date

    def get_writeable(self):
        is_reduced_bytes = list(self.is_reduced.to_bytes(1, byteorder='big'))
        line_bytes = list(self.line.to_bytes(1, byteorder='big'))
        validity_date_bytes = list(self.validity_date.to_bytes(8, byteorder='big'))
        zeroes = [0] * 6

        writeable_ticket = is_reduced_bytes
        writeable_ticket.extend(line_bytes)
        writeable_ticket.extend(validity_date_bytes)
        writeable_ticket.extend(zeroes)

        return writeable_ticket