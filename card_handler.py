import mfrc522.MFRC522 as MFRC522
import RPi.GPIO as GPIO
import signal
from card_memory import CardMemory
from ticket import Ticket

class RFID:

    instances = {}

    def __init__(self):
        self.reading = False
        self.reader = MFRC522()

    @classmethod
    def add_instance(cls, id, handler):
        cls.instances[id] = handler

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def end_read(self, signal, frame):
        print("Ending read.")
        self.reading = False
        GPIO.cleanup()

    def start_read(self):
        self.reading = True

    def read_card(self):
        if self.reading:
            # Scan for cards    
            (status,TagType) = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)

            # If a card is found
            if status == self.reader.MI_OK:
                print("Card detected")
            
            # Get the UID of the card
            (status,uid) = self.reader.MFRC522_Anticoll()

            if status == self.reader.MI_OK:
                print("Card UID: {} {} {} {}".format(hex(uid[0]), hex(uid[1]), hex(uid[2]), hex(uid[3])))
                
                # Read card memory
                key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                self.read_card_memory(self.reader, key, uid) 
        
    def read_block(self, MifareReader, key, uid, blockAddr):
        # Authenticate
        status = MifareReader.MFRC522_Auth(MifareReader.PICC_AUTHENT1A, blockAddr, key, uid)
        # Check if authenticated
        if not(status == MifareReader.MI_OK):
            print ("Authentication error for block {}".format(blockAddr))
            return (status, [])
    
        recvData = []
        recvData.append(MifareReader.PICC_READ)
        recvData.append(blockAddr)
        
        pOut = MifareReader.CalulateCRC(recvData)
        
        recvData.append(pOut[0])
        recvData.append(pOut[1])
        
        (status, backData, backLen) = MifareReader.MFRC522_ToCard(MifareReader.PCD_TRANSCEIVE, recvData)
        
        if not(status == MifareReader.MI_OK):
            return (status, [])

        return (status, backData) 

    def read_card_memory(self, MifareReader, key, uid):
        # Select the scanned tag
        MifareReader.MFRC522_SelectTag(uid)

        data = []
        tickets = []
        balance = None
    
        for block in range(64):
            (status, mem) = self.read_block(MifareReader, key, uid, block)
            if status == MifareReader.MI_OK:

                if (block == 1):
                    balance = int.from_bytes(mem[0:5], byteorder="big")
                elif (block != 0 and (block+1)%4 != 0):
                    ticket = ticket(
                        mem[0], # is_reduced
                        mem[1], # line
                        int.from_bytes(mem[2:10], byteorder="big") # validity date
                    )
                    tickets.append(ticket)

                data.append(mem)
                print ("Block {:2d} [{:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x}]".format(block, 
                    mem[0],mem[1],mem[2],mem[3],mem[4],mem[5],mem[6],mem[7],mem[8],mem[9],mem[10],mem[11],mem[12],mem[13],mem[14],mem[15]))
            else:
                print ("Read error for block {}".format(block))
        
        MifareReader.MFRC522_StopCrypto1()
        self.reading = False
        print ("Card memory read end") 

        card_memory = card_memory(
            uid,
            balance,
            tickets
        )
    
        self.callback(card_memory)

    def write_all_to_card(self, data):
        # Create an object of the class MFRC522
        MIFAREReader = self.reader

        status = -1

        while not(status == MIFAREReader.MI_OK):
            # Scan for cards    
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print("Card detected")

            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:

                print("Card read UID: %s,%s,%s,%s" % (hex(uid[0]), hex(uid[1]), hex(uid[2]), hex(uid[3])))
            
                key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                
                MIFAREReader.MFRC522_SelectTag(uid)

                block = 0
                i = 0

                while i < len(data.tickets):

                    # Authenticate
                    status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, block, key, uid)

                    if status == MIFAREReader.MI_OK:
                        if (block == 1):
                            MIFAREReader.MFRC522_Write(block, data.balance.get_writeable_balance(), 16)
                        elif (block != 0 and (block+1)%4 != 0):
                            MIFAREReader.MFRC522_Write(block, data.tickets[i].get_writeable(), 16)
                            i = i+1

                        block = block+1

                zeroes = [0] * 16

                while block < 64:
                    MIFAREReader.MFRC522_Write(block, zeroes, 16)
                    block = block+1
                
                MIFAREReader.MFRC522_StopCrypto1()

    def callback(self, data):
        pass