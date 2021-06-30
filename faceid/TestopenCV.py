import cv2

#設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024) # 800, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 76) # 600, 480

while True:
    # 捕捉 frame-by-frame
    # ret : 偵測到 frame 若是正確的會回傳 true
    # frame : 捕捉到的區域資料
    ret, frame = cap.read()
    print(ret, frame)
    # 顯示在 frame UI 上面
    cv2.imshow('My Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# 資源釋放
cap.release()



