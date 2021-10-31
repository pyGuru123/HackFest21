import cv2
import mediapipe as mp
import time
import math
print("enter url")
url= input()
print(url) 
#url = 'http://192.168.43.206:8080/video' 
#url='http://100.101.157.27:8080/video'
url='http://100.98.207.187:8080/video'
cap = cv2.VideoCapture(url) 
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
dirn='no input'
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                if id==4:
                    lm1=lm
                if id ==8:
                    lm2=lm   
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
       	    m1=lm2.y-lm1.y
            m2=lm2.x-lm1.x
            m=m1/m2
            #print(m)
            if lm2.x<lm1.x:
               hand='right'
            if lm2.x>lm1.x:
               hand='left'
            print(hand)
            angle=math.atan(m)
            print(angle)
            if m<0 and hand=='right':
               dirn='left'
               cv2.arrowedLine(img, (100,120), (70,120), (0, 255, 0),2,tipLength = .5)#left  
            if m>0 and hand=='right' :
               dirn='reverse'
               cv2.arrowedLine(img, (100,120), (100,100), (0, 255, 0),2,tipLength = .5)#reverse
            if m<0 and hand=='left':
               dirn='straight'
            if m>0 and hand=='left':
               dirn='Right'
               cv2.arrowedLine(img, (70,120), (100,120), (0, 255, 0),2,tipLength = .5)#right

    else:
        dirn='no input'		
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.putText(img,dirn, (70,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
