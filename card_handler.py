import mfrc522.MFRC522 as MFRC522
import RPi.GPIO as GPIO
import signal

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
        print("Ctrl+C captured, ending read.")
        self.reading = False
        GPIO.cleanup()

    def start_read(self):
        self.reading = True

    def read_card(self):
        if self.reading:
            #signal.signal(signal.SIGINT, self.end_read)

            MIFAREReader = self.reader
            print("Press Ctrl-C to stop.")

            while self.reading:
                # Scan for cards    
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

                # If a card is found
                if status == MIFAREReader.MI_OK:
                    print("Card detected")
                
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                if status == MIFAREReader.MI_OK:
                    print("Card UID: {} {} {} {}".format(hex(uid[0]), hex(uid[1]), hex(uid[2]), hex(uid[3])))
                    
                    # Read card memory
                    key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                    self.read_card_memory(MIFAREReader, key, uid) 
        
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
    
        for block in range(64):
            (status, mem) = self.read_block(MifareReader, key, uid, block)
            if status == MifareReader.MI_OK:
                data.append(mem)
                print ("Block {:2d} [{:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x}]".format(block, 
                    mem[0],mem[1],mem[2],mem[3],mem[4],mem[5],mem[6],mem[7],mem[8],mem[9],mem[10],mem[11],mem[12],mem[13],mem[14],mem[15]))
            else:
                print ("Read error for block {}".format(block))
        
        MifareReader.MFRC522_StopCrypto1()
        print ("Card memory read end") 

        self.reading = False
    
        self.callback(data)

    def get_balance(self, data):
        # TODO return just value (number)
        return data[0]

    # TODO synchronize tickets

    # TODO get first free block number

    def can_buy_ticket(self, data, price):
        current_balance = self.get_balance(data)
        difference = current_balance - price
        return difference > 0

    def save_balance(self, new_balance_data):
        self.write_to_card(new_balance_data)

    def buy_ticket(self, data, price):
        can_buy_ticket = self.can_buy_ticket(data, price)

        if (not can_buy_ticket):
            return False
        else:
            # get first free block number
            # write_to_card
            # save balance
            return True

    # TODO read all tickets ?

    # Data is of type array and consists of 16 elements max.
    # Except for the first segment, we have 3 blocks in each segment to write to.
    # In Each block, we can write up to 16 bytes.
    # TODO what if we change screen or interrupt writing to card?
    def write_to_card(self, block_number, data):
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

                # Authenticate
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, block_number, key, uid)

                # Check if authenticated
                if status == MIFAREReader.MI_OK:

                    # TODO use this in read_by_block function
                    # print("Block 8 looked like this:")
                    # # Read block 8
                    # bd = MIFAREReader.MFRC522_Read(8)
                    # print("Block 8 ", bd, "\n")

                    MIFAREReader.MFRC522_Write(block_number, data)
                    status = MIFAREReader.MI_OK
                    MIFAREReader.MFRC522_StopCrypto1()

    def callback(self, data):
        pass