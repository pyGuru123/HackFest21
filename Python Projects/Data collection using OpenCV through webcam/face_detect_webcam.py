import cv2
import sys

face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
count=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    faces = face_classifier.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
    )

    for (x, y, w, h) in faces:
        count+=1
#        file_name_path='<Your local file path>'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1)== 13 or count==100:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
