import cv2

#設定 Webcam 位置
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

# 設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024) # 800, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768) # 600, 480

while True:
    ret, frame = cap.read()
    freme = cv2.flip(frame, -1) # 鏡頭鏡像處理
    print(ret, frame)

    # 圖像灰階畫
    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #劃出每個臉的範圍
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=15,
            minSize=(5, 5),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        eyes_y = 0
        for(x,y,w,h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            eyes_y = y + h
        smile = smile_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=100,
            minSize=(10, 10),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in  smile:
            if y > eyes_y:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 顯示在 frame UI 上面
    cv2.imshow('My Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
# 資源釋放
cap.release()