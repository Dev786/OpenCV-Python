import cv2
import numpy as np

#callback pass
def nothing(x):
    pass


cap = cv2.VideoCapture(0)

#creating a trackbar
cv2.namedWindow("image")
cv2.createTrackbar('low_R','image',0,255,nothing)
cv2.createTrackbar('low_G','image',0,255,nothing)
cv2.createTrackbar('low_B','image',0,255,nothing)
cv2.createTrackbar('high_R','image',0,255,nothing)
cv2.createTrackbar('high_G','image',0,255,nothing)
cv2.createTrackbar('high_B','image',0,255,nothing)
kernel = np.ones((5,5),np.uint8)


while(cap.isOpened()):
    ret,image = cap.read()
    hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv_image_blurred = cv2.GaussianBlur(hsv_image,(5,5),0)

#low and high values   
    low_h = cv2.getTrackbarPos('low_H','image')
    low_s = cv2.getTrackbarPos('low_S','image')
    low_v = cv2.getTrackbarPos('low_V','image')

    high_h = cv2.getTrackbarPos('high_H','image')
    high_s = cv2.getTrackbarPos('high_S','image')
    high_v = cv2.getTrackbarPos('high_V','image')
    
#image preprocessing
    filtered_image = cv2.inRange(image,np.array([low_h,low_s,low_v]),np.array([high_h,high_s,high_v])) 
    closed_filtered_image = cv2.morphologyEx(filtered_image,cv2.MORPH_OPEN,kernel)
    closed_filtered_image = cv2.morphologyEx(filtered_image,cv2.MORPH_OPEN,kernel)
    finalThreshold = cv2.adaptiveThreshold(closed_filtered_image,255,1,1,11,2)
    
#find contours
    contours,heirarchy = cv2.findContours(filtered_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    biggestContour = None

#search for largest contour
    for i in contours:
        area = cv2.contourArea(i)
        if(area>1000):
            if(area>max_area):
                area = max_area
                biggestContour = i

#draw largest contour
    cv2.drawContours(image,[biggestContour],0,(255,0,0),3)
    cv2.imshow("Original",image)
  # cv2.imshow("Original_hsv",hsv_image_blurred)
    cv2.imshow("filtered_image",closed_filtered_image)
    if(cv2.waitKey(10) & 0xFF==27):
        break

cv2.destroyAllWindows()
