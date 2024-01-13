import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#frame size
framewidth = 1000
frameheight = 2000

#Setting Webcab size
cap = cv.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)

def designatedRec(x,y,w,h,brgInputImage):
    temp = cv.rectangle(brgInputImage,(x,y),(x+w,y+h),(0,255,0),2)
    img = cv.cvtColor(temp, cv.COLOR_BGR2RGB)
    return img

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

while(1):
    # Take each frame
    _, frame = cap.read()  

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask= mask)
    # Your crop image of frame(which is your target area of the frame)
    img = cv.cvtColor(frame[150:310,250:400], cv.COLOR_BGR2RGB)
    #Contour of your rectangle (Display of the rectangle)
    designatedRec(250,150,150,160,frame)
  
    # Display of your usual four images
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow('crop',img)
    
    # K-mean Algorithm (sorting color)
    img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(img)
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

    # Stop condition
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()