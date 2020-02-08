from ttn import*
from time import sleep
from datetime import datetime
from base64 import*
from threading import*
from Logger import WritePayloadDataToFile
import json

access_key = "ttn-account-v2.3SWn_pzU0kjQNqJjXVyXkFUJhVfsxTWL6rSKyn_Znt8"
app_id = "vibration_meassurement"

Database = [7020, 2012, 7063, 7568 ,1569]
Start_date = datetime.now()
date = str(Start_date.day)+"." + str(Start_date.month)+"." + str(Start_date.year)

mtx = Lock()



def check_code(code, list):
    if code in list:
        return True
    else:
        return False


def uplink_callback(msg, client):
    global date, mtx
    print("Received uplink from ", msg.dev_id, datetime.now())
    if msg.port == 2:
        print("EVENT!")
    if msg.port == 8:
        print("Still alive...")
    #Convert received data to int:
    uplink_payload = b64decode(msg.payload_raw)
    header = int.from_bytes(uplink_payload[0:1], byteorder='big')
    meta = msg.metadata
    WritePayloadDataToFile(msg.dev_id, msg.port, uplink_payload, meta, date)
    clien.send(msg.dev_id, b64encode("0".encode()).decode("utf-8"), msg.port, sched="first")

    

handler = HandlerClient(app_id, access_key,discovery_address="discovery.thethings.network:1900")

mqtt_application = handler.application()

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
print("Serving ", app_id)
my_app = mqtt_application.get()
print(my_app)
my_devices = mqtt_application.devices()
print(my_devices)


while True:
    if(Start_date.day != datetime.now().day):
        Start_date = datetime.now()
        mtx.acquire()
        date = str(Start_date.day)+"." + str(Start_date.month)+"." + str(Start_date.year)
        mtx.release()
        print("New Day!")
    pass

mqtt_client.close()


