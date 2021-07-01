import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://arduino-iot-20210701-default-rtdb.firebaseio.com/'
})
door = db.reference('/door').get()
print(door)

temp = db.reference('/dht/temp').get()
humi = db.reference('/dht/humi').get()
print(temp, humi)
dht = db.reference('/dht').get()
print(dht['temp'],dht['humi'])

def listener(event):
    print(event.data)

# listener
firebase_admin.db.reference('/door').listen(listener)
