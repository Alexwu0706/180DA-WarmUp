import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([40,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    result = cv.bitwise_and(frame,frame, mask= mask)

    #Return contours of your GRAY image target as an array
    contours,hierarchy = cv.findContours(mask, 1, 2)
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #Display
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',result)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()