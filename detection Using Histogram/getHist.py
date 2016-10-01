import cv2
import numpy as np

cap = cv2.VideoCapture(0)
roi_captures = False

print "*****************************\n"
print "Press c to capture the ROI\n"
print "*****************************\n"

while cap.isOpened():
    ret,frame = cap.read()
    w,h = frame.shape[:2]

    cv2.rectangle(frame,(h/2,w/2),(h/2+80,w/2+80),(0,255,0))
    roi = frame[w/2:w/2+70,h/2:h/2+70]
    if(cv2.waitKey(10) & 0xFF==99):
        if(roi_captures == False):
            cv2.imwrite("roi.jpg",roi)
            roi_captures = True
            break
    
    if(cv2.waitKey(10) & 0xFF == 27):
        break
    cv2.imshow("frame",frame)
    cv2.imshow("ROI",roi)

cv2.destroyAllWindows()
