import paho.mqtt.client as mqtt
from config import Config
import json

class Queue:

    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]
    
    def __init__(self) -> None:
        mqtt.Client.connected_flag=False
        self.client = mqtt.Client("adfgadfasgfdbvsdf234234sadf2r") 
        self.client.on_connect = self.on_connect
        host = Config.read_property("broker_host")
        port = Config.read_property("port")
        username = Config.read_property("adafruit_user")
        key = Config.read_property("adafruit_key")
        self.client.username_pw_set(username, password=key)
        self.client.connect(host, port=port)   
        self.client.loop_start()
        self.topic = Config.read_property("topic")

    def send_recharge_info(self, uid, price):
        message = {"uid": uid, "price": price}
        message_json = json.dumps(message)
        self.client.publish(self.topic, message_json, 2, True)

    def on_connect(self, client, userdata, flags, rc):                # function called on connected
        if rc==0:
            client.connected_flag=True              # set flag
            print("Connected OK")
        else:
            print("Bad connection Returned code=",rc)