import numpy as np
import cv2 as cv
font = cv.FONT_HERSHEY_COMPLEX

#Webcam Capture
cap = cv.VideoCapture(0)

#Function of Contour (input image(your target image), output image(your base image))
def getContour(img,imgContour):
    contours,hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(imgContour,contours, -1, (255,0,255),7)


while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # copy of frame as base
    imgContour = frame.copy()
    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])

    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([40,255,255])

    # Threshold the HSV image to get only yellow colors
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    #Contour of our three images
    getContour(mask,imgContour)
    #Display
    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)
    cv.imshow('contour',imgContour)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

