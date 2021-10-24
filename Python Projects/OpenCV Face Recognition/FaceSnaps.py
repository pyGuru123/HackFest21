import cv2


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_eye.xml')

pic_number = 0
while True:
    ret, frame = cap.read()

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi = frame[y-100:y+h+100, x-100:x+w+100]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            pic_number += 1
            filename = "Image_" + str(pic_number) + ".png"
            cv2.imwrite(filename, roi)

            cv2.rectangle(roi_gray, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)  # This method gets, The Frame or Window on which it has to draw, Starting Co-ordinates, Ending Co-ordinates, color for Rectangle, Stroke of Rectangle

        color = (255, 0, 0)
        stroke = 2
        cv2.rectangle(frame, (x,y), (x + w, y + h), color, stroke)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()