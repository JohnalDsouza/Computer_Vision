import cv2
img = cv2.imread('00-puppy.jpg')
while True:
    cv2.imshow('Puppy',img)
    # if we waited for 1 millisecond and pressed esc key, then break
    # can use other keys by typing ord('q'), ie break when 1 is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()