import cv2

#設定 Webcam 位置
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

# 設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024) # 800, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 786) # 600, 480

while True:
    # 捕捉 frame-by-frame
    # ret : 偵測到 frame 若是正確的會回傳 true
    # frame : 捕捉到的區域資料
    ret, frame = cap.read()
    freme = cv2.flip(frame, -1) # 鏡頭鏡像處理
    print(ret, frame)

    # 圖像灰階畫
    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #劃出每個臉的範圍
    faces = face_cascade.detectMultiScale(
        gray,              # 待檢測圖片,一般來說設定成灰度圖像可以加快檢測速度
        scaleFactor=1.1,   # 檢測粒度,若粒度增加會加快檢測速度,但會影響準確率
        minNeighbors=20,    # 每個目標至少要檢測到幾次以上，才被認定真數據
        minSize =(30, 30), # 數據搜尋的最小尺寸
        # CASCADE_DO_CANNY_PRUNING=1 -> 利用canny邊緣檢測來排除一些邊緣很少或者很多的影象區域
        # CASCADE_SCALE_IMAGE=2 -> 正常比例檢測
        # CASCADE_FIND_BIGGEST_OBJECT=4 -> 只檢測最大的物體
        # CASCADE_DO_ROUGH_SEARCH=8 粗略的檢測
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        # 繪文字 putText(來源, 文字, 左下座標, 字型大小, 文字線條寬度)
        cv2.putText(frame, 'Li', (x + 100,y-10), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0,255,0), 2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

    # 顯示在 frame UI 上面
    cv2.imshow('My Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
# 資源釋放
cap.release()