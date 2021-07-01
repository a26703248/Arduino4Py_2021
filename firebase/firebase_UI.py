'''
+----+----+----+
|25.4|52.1|  on|
+----+----+----+
'''
import threading

import firebase_admin
from PIL import Image, ImageTk
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk

def door(event):
    stat =event.data
    if (int(stat) == 0):
        doorLabel.config(image=clodoor)
        doorLabel.image = clodoor
    elif (int(stat) == 1):
        doorLabel.config(image=opdoor)
        doorLabel.image = opdoor

def temp(dht):
    tempValue.set(dht.data)

def humi(dht):
    humiValue.set(dht.data)

def listen():
    firebase_admin.db.reference('/door').listen(door)
    firebase_admin.db.reference('/dht/temp').listen(temp)
    firebase_admin.db.reference('/dht/humi').listen(humi)

win = tk.Tk()
win.title('firebase')
win.geometry('600x400')

tempValue = tk.StringVar()
tempValue.set("0")

humiValue = tk.StringVar()
humiValue.set("0")

doorValue = tk.StringVar()
doorValue.set("0")

opdoor = ImageTk.PhotoImage(Image.open('opendoor.png'))
clodoor = ImageTk.PhotoImage(Image.open('closedoor.png'))

tempLabel = tk.Label(textvariable=tempValue)
humiLabel = tk.Label(textvariable=humiValue)
doorLabel = tk.Label(textvariable=doorValue, image=clodoor)

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://arduino-iot-20210701-default-rtdb.firebaseio.com/'
})

win.rowconfigure((0), weight=1)  # 列 0, 列 1 同步放大縮小
win.columnconfigure((0, 1, 2), weight=1)  # 欄 0, 欄 1, 欄 2 ...同步放大縮小

tempLabel.grid(row= 0,column=0, columnspan=1, sticky='EWNS')
humiLabel.grid(row=0, column=1, columnspan=1, sticky='EWNS')
doorLabel.grid(row=0, column=2, columnspan=1, sticky='EWNS')

t1 = threading.Thread(target= listen)
t1.start()

win.mainloop()