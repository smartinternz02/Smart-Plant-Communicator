import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "5y7njo",
        "typeId": "device",
        "deviceId":"1"
    },
    "auth": {
        "token": "saurabhPandey"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data)
    m=cmd.data['command']
    print (m)
    if m=="mon":
        print("motor is switched on")
    elif m=="moff":
            print("motor is switched off")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temprature=random.randint(-20,125)
    humidity=random.randint(0,100)
    moisture=random.randint(0,100)
    myData={'temprature':temprature, 'humidity':humidity, 'moisture':moisture}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
