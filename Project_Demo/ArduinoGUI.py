'''
+-----------------+
| ___3___   傳送   |
| 766,20.50,52.00 |
+-----------------+
'''

import tkinter
import serial
import threading
import Project_Demo.OpenWeather as pd
from io import BytesIO
from PIL import Image, ImageTk


COM_PORT = 'COM4'  # 指定通訊埠名稱
BAUD_RATES = 9600  # 設定傳輸速率(鮑率)
play = True

def sendData(num):
    data_row = str(num) + '#'
    data = data_row.encode()
    ser.write(data)

def receiveData():
    while play:
        try:
            global ser
            data_row = ser.readline()  # 讀取一行(含換行符號\r\n)原始資料
            data = data_row.decode()  # 預設是用 UTF-8 解碼
            data = data.strip("\r").strip("\n")  # 除去換行符號
            respText.set(data)
            try:
                values = data.split(",")
                cdsValue.set('{} lu'.format(float(values[2])))
                tempValue.set('{} C'.format(float(values[1])))
                humiValue.set('{} %'.format(float(values[0])))
            except :
                pass
        except Exception as e:
            respText.set("Serial closed ...")
            try:
                ser = serial.Serial(COM_PORT, BAUD_RATES)
            except Exception as e:
                print("Serial closed ...")

def getOpenWeatherData():
    status_code, main, icon, temp, feels_like, humidity = pd.openWeather()
    owmainValue.set(main)
    owiconValue.set(icon)
    #  取得 icon 圖片 bytes 資料
    raw_data = pd.openWeatherIcon(icon)
    # 轉成 image 格式
    im = Image.open(BytesIO(raw_data))
    #轉乘 TK 的 photo 格式
    photo = ImageTk.PhotoImage(im)
    # 配置到目標區(owiconLabel)
    owiconLabel.config(image=photo)
    owiconLabel.image = photo

    owtempValue.set('%.1f C' % (float(temp)-273.25))
    owfeelsLikeValue.set('%.1f C' % (float(feels_like)-273.25))
    owhumidityValue.set('%.1f %%' % float(humidity))
    string = 'A{:.1f},{:.1f},{:.1f}'.format((float(temp)-273.25), (float(feels_like)-273.25), humidity)
    sendPyToAdr(string)

def sendPyToAdr(string):
    data_row = str(string)+ '#'
    data = data_row.encode()
    ser.write(data)

if __name__ == '__main__':#主方法

    try:
        ser = serial.Serial(COM_PORT, BAUD_RATES)
    except Exception as e:
        print("Serial closed ...")

    root = tkinter.Tk()
    root.geometry("600x400")
    root.title("智能家庭管家")

    buzeeropen = ImageTk.PhotoImage(Image.open('buzzeropen.png'))
    buzeerclose = ImageTk.PhotoImage(Image.open('buzzerclose.png'))
    clodoor = ImageTk.PhotoImage(Image.open('closedoor.png'))
    opdoor = ImageTk.PhotoImage(Image.open('opendoor.png'))
    clean = ImageTk.PhotoImage(Image.open('clean.png'))
    redlight = ImageTk.PhotoImage(Image.open('redlight.png'))
    greenlight = ImageTk.PhotoImage(Image.open('greenlight.png'))
    yellowlight = ImageTk.PhotoImage(Image.open('yellowlight.png'))

    # 網路爬蟲--------------------------------------------------------------
    owmainValue = tkinter.StringVar()
    owmainValue.set("click")

    owiconValue = tkinter.StringVar()
    owiconValue.set("weather")

    owtempValue = tkinter.StringVar()
    owtempValue.set("0")

    owfeelsLikeValue = tkinter.StringVar()
    owfeelsLikeValue.set("0")

    owhumidityValue = tkinter.StringVar()
    owhumidityValue.set("0")
    # ---------------------------------------------------------------------

    cdsValue = tkinter.StringVar()
    cdsValue.set("0")

    tempValue = tkinter.StringVar()
    tempValue.set("0")

    humiValue = tkinter.StringVar()
    humiValue.set("0")

    respText = tkinter.StringVar()
    respText.set("0,0.0,0.0")

    sendButton0 = tkinter.Button(text='16', image=buzeerclose, command=lambda: sendData('16'))
    sendButton1 = tkinter.Button(text='1', image=redlight, command=lambda: sendData('1'))
    sendButton2 = tkinter.Button(text='2', image=greenlight, command=lambda: sendData('2'))
    sendButton3 = tkinter.Button(text='3', image=yellowlight, command=lambda: sendData('3'))
    sendButton4 = tkinter.Button(text='4', image=opdoor, command=lambda: sendData('4'))
    sendButton8 = tkinter.Button(text='8', image=clodoor, command=lambda: sendData('8'))

    # 網路爬蟲--------------------------------------------------------------
    owmainButton = tkinter.Button(textvariable=owmainValue, command=lambda: getOpenWeatherData())
    owiconLabel = tkinter.Label(root, textvariable=owiconValue)
    owtempLabel = tkinter.Label(root, textvariable=owtempValue, font = 'Arial -26', fg = 'green')
    owfeelsLikeLabel = tkinter.Label(root, textvariable=owfeelsLikeValue, font = 'Arial -26', fg = 'green')
    owhumidityLabel = tkinter.Label(root, textvariable=owhumidityValue, font = 'Arial -32', fg = 'blue')
    # ---------------------------------------------------------------------

    receiveLabel = tkinter.Label(root, textvariable=respText)
    cdsLabel = tkinter.Label(root, textvariable=cdsValue, font = 'Arial -32', fg = 'red')
    tempLabel = tkinter.Label(root, textvariable=tempValue, font = 'Arial -32', fg = 'green')
    humiLabel = tkinter.Label(root, textvariable=humiValue, font = 'Arial -32', fg = 'blue')

    root.rowconfigure((0,1,2), weight=1) # 列 0, 列 1 同步放大縮小
    root.columnconfigure((0,1,2,3,4,5), weight=1) # 欄 0, 欄 1, 欄 2 ...同步放大縮小

    sendButton0.grid(row=0,   column=0, columnspan=1, sticky='EWNS')
    sendButton1.grid(row=0,   column=1, columnspan=1, sticky='EWNS')
    sendButton2.grid(row=0,   column=2, columnspan=1, sticky='EWNS')
    sendButton3.grid(row=0,   column=3, columnspan=1, sticky='EWNS')
    sendButton4.grid(row=0,   column=4, columnspan=1, sticky='EWNS')
    sendButton8.grid(row=0,   column=5, columnspan=1, sticky='EWNS')

    # 網路爬蟲--------------------------------------------------------------
    owmainButton.grid(row=1, column=0, columnspan=1, sticky='EWNS')
    owiconLabel.grid(row=1, column=1, columnspan=2, sticky='EWNS')
    owtempLabel.grid(row=1, column=3, columnspan=1, sticky='EWNS')
    owfeelsLikeLabel.grid(row=1, column=4, columnspan=1, sticky='EWNS')
    owhumidityLabel.grid(row=1, column=5, columnspan=1, sticky='EWNS')
    # ---------------------------------------------------------------------

    cdsLabel.grid(row=2, column=0, columnspan=2, sticky='EWNS')
    tempLabel.grid(row=2, column=2, columnspan=2, sticky='EWNS')
    humiLabel.grid(row=2, column=4, columnspan=2, sticky='EWNS')
    receiveLabel.grid(row=3,  column=0, columnspan=9, sticky='EWNS')

    t1 = threading.Thread(target=receiveData)
    t1.start()

    root.mainloop()
