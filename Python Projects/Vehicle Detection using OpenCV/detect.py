import cv2

cap = cv2.VideoCapture('video.avi')
# XML File cars.xml contains classifiers for cars which can be detected.
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frames = cap.read()
    # Convert to gray
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detect Cars of different sizes using Cascade in the frame of Video.
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw BoundBox on each car detected
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    cv2.imshow('video2', frames)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()