

# In[2]:





# In[3]:


import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2 as cv
from tkinter import *
from tkinter import filedialog
global root
global frame
global filename    
    
root = Tk()
root.title('Qr code Scanner')
root.configure(background='#8BB381')
frame = LabelFrame(root, padx = 80 , pady = 80 , bg = '#9B9E9F')
frame.grid(padx = 60, pady = 60)
button = Button(frame , text = "Click here to upload image" , bg = 'black', fg = 'white' , width = 20 , font = ('Neue Helvetica', 12, 'bold'), command=UploadAction)
button.grid(row = 4 , column = 0 , pady= 20)
root.mainloop()

def decoding(img):
    global root
    global frame
    decoded_items = pyzbar.decode(img)
    for item in decoded_items:
        print('Type is : ', item.type)
        print('Data is : ', item.data)
        frame.grid_forget()
        frame = LabelFrame(root, padx = 80 , pady = 80 , bg = '#9B9E9F')
        frame.grid(padx = 60, pady = 60)
        label = Label(frame , text = item.data , fg = "red" , relief = FLAT ,  font = ('Neue Helvetica', 14 , 'bold'))
        label.grid(row = 8 , column = 0)
        button = Button(frame , text = "Click here to upload image" , bg = 'black', fg = 'white' , width = 20 , font = ('Neue Helvetica', 12, 'bold'), command=UploadAction)
        button.grid(row = 4 , column = 0 , pady= 20)
    return decoded_items

def UploadAction(event=None):
    global frame
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    im = cv.imread(filename)
    obj = decoding(im)
    show(im, obj)
    
def show(im , decoded_items):
    global frame
    global root
    for d_obj in decoded_items:
        points_detected = d_obj.polygon
        if(len(points_detected)) > 4:
            convex_hull = cv2.convexHull(np.array([point for point in points_detected], dtype=np.float32))
            convex_hull = list(map(tuple, np.squeeze(convex_hull)))
        else:
            convex_hull = points_detected
        n = len(convex_hull)
        for j in range(0,n):
            cv.line(im, convex_hull[j], convex_hull[ (j+1) % n], (0,255,255), 3)
        im = cv.resize(im , (500 , 500))
        cv.imshow("Results", im)
        cv.waitKey(3000)
        cv.destroyAllWindows()

