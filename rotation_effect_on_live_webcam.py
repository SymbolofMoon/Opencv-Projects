import cv2
import numpy as np 
import matplotlib.pyplot as  plt 
import time

img= cv2.imread('color.jpg',1)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rows,columns,channels=img.shape
angle=0 
while True:
   R= cv2.getRotationMatrix2D((columns/2,rows/2),angle,1)# this column/2 and rows/2 represent the origin of rotation
   
   print(R)
   img= cv2.warpAffine(img,R,(columns,rows))
   cv2.imshow('Rotating Image',img)
   angle=angle+1
   if angle==360:
       angle=0
   time.sleep(0.08)   
   if cv2.waitKey(1)==27:
       break 

cv2.destroyAllWindows()