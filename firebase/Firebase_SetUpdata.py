import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://arduino-iot-20210701-default-rtdb.firebaseio.com/'
})

# db.reference('/dht').set({
#     'humi': 10.1,
#     'temp':20.2
# })
# db.reference('/door').set(0)

db.reference('/dht11').set(30.3)






print('Ok')
