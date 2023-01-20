import datetime
import time

class Ticket:
    def __init__(self, is_reduced, line, date):
        self.is_reduced = is_reduced
        self.line = line
        self.validity_date = date
        self.price = 0

    def get_writeable(self):
        is_reduced_bytes = list(self.is_reduced.to_bytes(1, byteorder='big'))
        line_bytes = list(self.line.to_bytes(1, byteorder='big'))
        validity_date_bytes = list(self.validity_date.to_bytes(8, byteorder='big'))
        zeroes = [0] * (64-10)

        writeable_ticket = is_reduced_bytes
        writeable_ticket.extend(line_bytes)
        writeable_ticket.extend(validity_date_bytes)
        writeable_ticket.extend(zeroes)

        return writeable_ticket

    def get_readable_date(self):
        return str(datetime.datetime.utcfromtimestamp(self.validity_date))

    def is_valid(self):
        return self.validity_date > time.time()

    def is_fully_valid(self, line_number):
        return self.is_valid() and self.line == line_number

    def __repr__(self):
        return "TICKET: \n" +  "is_reduced: " + str(self.is_reduced) + "\n" + "line: " + str(self.line) + "\n" + "validity_date: " + str(self.validity_date) + "\n"