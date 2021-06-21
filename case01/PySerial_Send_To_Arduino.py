import serial #引用 pySerial 模組
import random
import time

COM_PORT = 'COM4' #指定通訊埠名稱
BUAD_RATES =  9600 #設定傳輸速率(鮑率)
ser = None

try:
    ser = serial.Serial(COM_PORT, BUAD_RATES)  # 初始化通訊埠
    while True:
        #data_row = str(random.randint(0, 99)) + "#" # "#"表示結束字元
        data_row = str(input("請輸入欲傳送數字: ")) + "#"
        data = data_row.encode()
        ser.write(data)
        print("Send", data_row, data)
        time.sleep(0.5)
except serial.SerialException:
    print("通訊埠無法建立, 請確認:")
    print("1.通訊埠名稱")
    print("2.傳輸速率(鮑率)")
    print("3.是否有關閉 Arduino IDE 的序列通訊埠視窗")
    print("exit")
except:
    if():
        ser.close() # 關閉通訊埠
    print("bye!");
