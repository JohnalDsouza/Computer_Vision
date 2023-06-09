import cv2
import numpy as np

#################
### FUNCTION#####
#################

def draw_circle(event,x,y,flags,param): #x,y=mouse position, event = what mouse did
    if event == cv2.EVENT_LBUTTONDOWN: # left button is clicked down
        cv2.circle(img,(x,y), 100, (0,255,0),-1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255,0, 0), -1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

#################################
####SHOWING IMAGE WITH OPENCV####
#################################

img = np.zeros((512,512,3), np.int8) # even if we remove np.int8 it will work but screen will be black
while True:
    cv2.imshow("my_drawing", img) # my_drawing is connected to draw_circle
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()