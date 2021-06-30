# import the necessary packages
import cv2
import numpy as np
import argparse
import time
import os
import imutils



cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
x=0

while True:
  ret, img=cap.read()
  if not cap:
    print ("Error opening webcam device")
    sys.exit(1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  minisize = (img.shape[1],img.shape[0])
  miniframe = cv2.resize(img, minisize)
  try:
   x=faces[0][0]
   y=faces[0][1]
   w=faces[0][2]
   h=faces[0][3]
   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   print (img.shape)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]
   
   sub_face = img[y:y+h, x:x+w]
   
   cv2.imshow('imshow',img)
   key = cv2.waitKey(1) & 0xFF

   if key == ord("k"):
	    FaceFileName = "unknownfaces/face_" + str(y) + ".jpg"
	    cv2.imwrite(FaceFileName, sub_face)   	
   if key == ord("q"):
    break
  except:
   print ("wait")
print (x,y,w,h)
print (img.shape)
cap.release()