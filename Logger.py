import os
from json import dumps
from datetime import datetime, timedelta
import csv
import dateutil.parser as dp


Datarates = ["SF12BW125", "SF11BW125", "SF10BW125","SF9BW125", "SF8BW125", "SF7BW125"]
current_directory = os.getcwd()
testpayload = bytearray( b'\x02\x01"\x04\x8d\xfcn\x00 \x03\x90\xfco\x00\x1e\x03\x8d\xfcp\x00"\x03\x90\xfcn\x00"\x03\x8e\xfcq\x00!\x03\x8e\xfcl\x00!\x03\x8d\xfcn\x00 \x03\x8e\xfcq')

def WritePayloadDataToFile(dev_id, port, payload, Metadata, date):
    payload_data = bytearray()
    battery_lvl = 0
    light_lvl = 0
    dev_timestamp = 0
    if port == 4:
        payload_data = payload
    elif port == 2 or port == 8:
        dev_timestamp = int.from_bytes(payload[0:4], byteorder='big')
        battery_lvl = int.from_bytes(payload[4:5], byteorder='big')
        light_lvl = int.from_bytes(payload[5:6], byteorder='big')
        temperature = int.from_bytes(payload[6:7], byteorder='big', signed=True)
        payload_data = payload[7:]
    directory = 'Logs '+str(dev_id)
    final_directory = os.path.join(current_directory, (r''+directory))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    servertime =  int(dp.parse(str(Metadata[0])).timestamp())
    try:
        Log = open(directory+"/Logs "+date+".csv",'x')
        Last_line = open(directory+"/last_line.txt",'x')
        Last_line.close()
        Last_line = open(directory+"/last_line.txt",'w+')
        temp_line = Last_line.read()
        templist = []
        if port == 2  or port == 8:
            templist.append(battery_lvl)
            templist.append(light_lvl)
            templist.append(temperature)
        try:
            for i in range(0, len(payload_data), 2):
                templist.append(int.from_bytes(payload_data[(i):(i+2)], byteorder='big', signed=True))
        except  (ValueError, IndexError):
            for i in range(0, len(payload_data), 2):
                templist.append(int.from_bytes(payload_data[(i):(i+2)], byteorder='big', signed=True))
        line = dumps(templist)
        line = line[1:len(line)-1].replace(" ","")
        if temp_line != line:
            Last_line.write(line)
            if port == 2  or port == 8:
                templist.insert(0, port)
                templist.insert(1, servertime)
                templist.insert(2, dev_timestamp)
                line = dumps(templist)
                line = line[1:len(line)-1].replace(" ","")
            if port != 4: 
                line = line
            else:
                line = "," + line
            Log.write(line)
        Log.close()
        Last_line.close()
    except FileExistsError:
        Log = open(directory+"/Logs "+date+".csv",'a')
        Last_line = open(directory+"/last_line.txt",'r')
        temp_line = Last_line.read()
        Last_line.close()
        templist = []
        if port == 2  or port == 8:
            templist.append(battery_lvl)
            templist.append(light_lvl)
            templist.append(temperature)
        try:
            for i in range(0, len(payload_data), 2):
                templist.append(int.from_bytes(payload_data[(i):(i+2)], byteorder='big', signed=True))
        except (ValueError, IndexError):
            for i in range(0, len(payload_data), 2):
                templist.append(int.from_bytes(payload_data[(i):(i+2)], byteorder='big', signed=True))
        line = dumps(templist)
        line = line[1:len(line)-1].replace(" ","")
        if temp_line != line:
            Last_line = open(directory+"/last_line.txt",'w')
            Last_line.write(line)
            Last_line.close()
            if port == 2  or port == 8:
                templist.insert(0, port)
                templist.insert(1,servertime)
                templist.insert(2, dev_timestamp)
                line = dumps(templist)
                line = line[1:len(line)-1].replace(" ","")
            if port != 4: 
                line = "\n" + line
            else:
                line = "," + line
            Log.write(line)
        Log.close()





some_date = "21.12.2018"
#Metadata format:

meta = ["2018-11-08T11:41:52.772067729Z", 868.1, "LORA", "SF12BW125", 1155072000, "4/5", [
["trt-vm-loragw01", True, 1040756148, "2018-11-08T11:39:10Z", 0, -120, -8.75, 1, 63.42883, 10.385698, 20], 
["trt-sluppen-loragw01", True, 1338177276, "2018-11-08T11:39:43Z", 0, -114, 2.75, 1, 63.397568, 10.400948, 21], 
["trt-samf-loragw01", True, 1567384756, "2018-11-08T12:02:07Z", 0, -111, 3.5, 1, 63.422485, 10.395755, 20], 
["eui-008000000000a447", False,1628454124, "2018-11-08T13:04:42.647744Z", 0, -119, -13.8, 0, 63.41785, 10.4021, 112],
["trt-olav-loragw01", True, 3798105164, "2018-11-08T11:40:27Z", 0, -117, -14.25, 1, 63.43338, 10.403285, 19], 
["ntnu1", True, 2597174828, "2018-11-08T11:41:52Z", 0, -119, -15, 1, 63.41831, 10.400998, 60, "registry"]]
]

#WritePayloadDataToFile("lorakeypad", testpayload, meta, some_date)
#WritePayloadDataToFile("lorakeypad", testpayload, meta, some_date)
