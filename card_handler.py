import mfrc522.MFRC522 as MFRC522

class RFID:

    instances = {}

    def __init__(self):
        self.reading = True
        self.reader = MFRC522.MFRC522()

    @classmethod
    def add_instance(cls, id, handler):
        cls.instances[id] = handler

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def read_loop(self):
        if (self.reading):
            self.read_all()

    def read_all(self):
        if self.reading:
            data = []

            for i in range(64):
                data.append(self.read(i))
            
            self.callback(data)
        

    def read(self, block_number):
        status, data = self.reader.ReadMFRC522(block_number)
        if status == MFRC522.MI_OK:
            return data
        else:
            return None

    def write(self, block_number, data):
        # Write data to the specified block
        status = self.reader.WriteMFRC522(block_number, data)
        if status == MFRC522.MI_OK:
            return True
        else:
            return False

    def callback(self, data):
        pass