import cv2
import numpy as np

#Variables
#True while mouse button down
drawing = False
ix = -1
iy = -1

#Function
def draw_rect(event,x,y,flags,params):
    
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    
    
#Connect Window
cv2.namedWindow(winname='drawing')
cv2.mouseCallback('drawing',draw_rect)

#Window Functionality
img = np.zeros((512,512,3))

while True:
    
    cv2.imshow('drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()