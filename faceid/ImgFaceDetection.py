import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
eyes_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

# image = cv2.imread('./image/test.jpg')
image = cv2.imread('./image/what.jpg')
# image = cv2.imread('./image/test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)



for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255),2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_image = image[y:y + h, x:x + w]

        eyes = eyes_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(5, 5),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in eyes:
            cv2.putText(roi_image, 'eye', (x , y), cv2.FONT_HERSHEY_COMPLEX,0.7, (0, 255, 0),2)
            cv2.rectangle(roi_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(5, 5),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in smile:
            cv2.putText(roi_image, 'smile', (x , y), cv2.FONT_HERSHEY_COMPLEX,0.7, (0, 255, 0), 2)
            cv2.rectangle(roi_image, (x, y), (x + w, y + h), (255, 0,0), 2)

print(len(faces))
cv2.imshow('Face', image)
c = cv2.waitKey(0)