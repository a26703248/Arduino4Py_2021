import serial #引用 pySerial 模組

COM_PORT = "COM4"
BUAD_RATES =  9600
ser = None

try:
    ser = serial.Serial(COM_PORT, BUAD_RATES)
    while True:
        data_row = str(input("請輸入控制的數值(0 ~ 7): ")) + "#"
        data = data_row.encode()
        ser.write(data)
        print("Send", data)
except serial.SerialException:
    print("通訊埠無法建立, 請確認:")
    print("1.通訊埠名稱")
    print("2.傳輸速率(鮑率)")
    print("3.是否有關閉 Arduino IDE 的序列通訊埠視窗")
    print("exit")
except:
    if():
        ser.close() # 關閉通訊埠
    print("bye!")