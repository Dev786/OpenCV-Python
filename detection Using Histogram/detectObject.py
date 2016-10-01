import cv2
import numpy as np

cap = cv2.VideoCapture(1)

#Region of interest
roi = cv2.imread("roi.jpg")
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)


while(cap.isOpened()):

    ret,frame = cap.read()
   
#converting target to hsv
    hsvt = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#hand histogram
    hand_hist = cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256],1)

#normalise
    cv2.normalize(hand_hist,hand_hist,0,255,cv2.NORM_MINMAX)


#backprojection
    dst = cv2.calcBackProject([hsvt],[0,1],hand_hist,[0,180,0,256],1)

#blur the frame
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(dst,-1,kernel,dst)

#Thresholding
    ret,thresh = cv2.threshold(dst,125,255,0)
    thresh = cv2.erode(thresh,(3,3))
    thresh = cv2.dilate(thresh,(5,5))
    thresh  = cv2.merge((thresh,thresh,thresh))


    cv2.imshow("Threshold",thresh)

    if(cv2.waitKey(10) & 0xFF==27):
        break

cv2.destroyAllWindows()