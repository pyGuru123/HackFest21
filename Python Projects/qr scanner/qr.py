import cv2 #reading input images or videos
from pyzbar.pyzbar import decode

images=cv2.imread('qr.png')
print(decode(images))

capture=cv2.VideoCapture(0)
capture.set(3,650) #3 here is width
capture.set(4,480) #4 here is height
camera=True
while camera==True: 
    success,frame=capture.read()


    for code in decode(images):
        print(code.type)   #check whether its bar or qr or something else
        print(code.data.decode('utf-8'))
    cv2.imshow('Testing-code-scan',frame)
    cv2.waitKey(2)
