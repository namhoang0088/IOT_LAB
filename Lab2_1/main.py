import serial.tools.list_ports
import random
import time
import sys
from  Adafruit_IO import  MQTTClient
import time
from SimpleAI import image_detector

AIO_FEED_ID = ["led","temperature","log"]
AIO_USERNAME = "huyquang0081"
AIO_KEY = "aio_qEtD47qyP9ZprNXfILlQ3Ib1L8V2"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    if(feed_id == "led"):
        print("led:" + payload )

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    ai_result = image_detector()
    client.publish("log",ai_result)
    time.sleep(5)