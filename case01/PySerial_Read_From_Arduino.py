import serial #引用 pySerial 模組

COM_PORT = 'COM4' #指定通訊埠名稱
BUAD_RATES =  9600 #設定傳輸速率(鮑率)
ser = None

try:
    ser = serial.Serial(COM_PORT, BUAD_RATES)  # 初始化通訊埠
    while True:
        while ser.in_waiting: # 若有收到序列資料(相當於Arduino 的 Serial.available)
            data_row = ser.readline()  # 讀取一行(含斷行符號\r\n)原始資料
            data = data_row.decode();  # 預設是用 UTF-8 解碼
            data = data.strip("\r").strip("\n") # 除去斷行符號
            print(data)
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
