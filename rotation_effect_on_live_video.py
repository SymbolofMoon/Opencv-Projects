import cv2
import numpy as np 
import matplotlib.pyplot as  plt 
import time

windowName='Live Video Rotation Feed'
cv2.namedWindow(windowName)
cap=cv2.VideoCapture(0)

angle=0 

if cap.isOpened():
    ret, frame = cap.read()
   
else:
   ret = False    
while ret:

   ret,frame=cap.read() 
   rows,columns,channels=frame.shape
   R= cv2.getRotationMatrix2D((columns/2,rows/2),angle,0.5)# this column/2 and rows/2 represent the origin of rotation

   
   print(R)
   frame= cv2.warpAffine(frame,R,(columns,rows))
   cv2.imshow('Rotating Image',frame)
   angle=angle+1
   if angle==360:
       angle=0
   time.sleep(0.01)   
   if cv2.waitKey(1)==27:
       break 

cv2.destroyAllWindows()