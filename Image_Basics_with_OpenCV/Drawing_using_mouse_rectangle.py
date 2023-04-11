# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vsd5DPpfMMhmn-OYEMo0KaI96LoVpmwh
"""

import cv2
import numpy as np

#Variable
drawing = False #True while mouse button down, False when mouse button up
ix=-1
iy=-1


#Function
def draw_rectangle(event,x,y,flags,param):
  global ix, iy,drawing
  if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix,iy = x,y # position when we clicked the left mouse
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
      #(ix,iy) = start position, (x,y) = where the mouse currently is

  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False
    cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1) 



#Showing the Image

#Black
img = np.zeros((512,512,3))
cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:
    cv2.imshow("my_drawing", img) 
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()