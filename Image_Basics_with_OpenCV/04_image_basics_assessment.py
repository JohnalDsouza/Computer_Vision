# -*- coding: utf-8 -*-
"""04-Image-Basics-Assessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_3QDWdeZtBpMZWDw-N7KgQJVNJCNX4TY

<a href="https://www.pieriandata.com"><img src="../DATA/Logo.jpg"></a>

# Image Basics Assessment

## Complete the Tasks in bold below. Keep in mind, you may need to run some of these tasks as Python scripts.

----------
#### TASK: Open the *dog_backpack.jpg* image from the DATA folder and display it in the notebook. Make sure to correct for the RGB order.
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('dog_backpack.jpg')
type(img)

plt.imshow(img)
plt.show()


fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(fix_img)
plt.show()


"""#### TASK: Flip the image upside down and display it in the notebook."""

flip_img = cv2.flip(fix_img,0)
plt.imshow(flip_img)
plt.show()


"""#### TASK: Draw an empty RED rectangle around the dogs face and display the image in the notebook."""

cv2.rectangle(fix_img,(200,400),(600,700),(255,0,0),5)
plt.imshow(fix_img)
plt.show()


traingle = np.array([[200,800],[500,400],[800,800]])
pts = traingle.reshape((-1,1,2))
plt.show()


"""#### TASK: Draw a BLUE TRIANGLE in the middle of the image. The size and angle is up to you, but it should be a triangle (three sides) in any orientation."""

cv2.polylines(fix_img,[pts],isClosed=True, color=(0,0,255), thickness =5)
plt.imshow(fix_img)
plt.show()


"""### BONUS TASK. Can you figure our how to fill in this triangle? It requires a different function that we didn't show in the lecture! See if you can use google search to find it.

[CLICK ME FOR A DIRECT LINK TO THE HINT](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html#fillpoly)
"""

cv2.fillPoly(fix_img,[pts], color=(0,0,255))
plt.imshow(fix_img)
plt.show()


"""#### TASK: (NOTE: YOU WILL NEED TO RUN THIS AS A SCRIPT). Create a script that opens the picture and allows you to draw empty red circles whever you click the RIGHT MOUSE BUTTON DOWN."""

def draw_circle(event,x,y,flags,param): #x,y=mouse position, event = what mouse did

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(fix_img, (x, y), 100, (0,0, 255), 3)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)
fix_img = fix_img.astype(np.uint8)
while True:
    cv2.imshow("my_drawing", fix_img) # my_drawing is connected to draw_circle
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()