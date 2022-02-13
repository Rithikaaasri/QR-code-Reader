import cv2
import numpy as np
from pyzbar.pyzbar import decode 

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
  success,img = cap.read()
  cv2.imshow('Result Image', img)
  cv2.waitKey(2)
  
code = decode (img)
for qrCode in code:
  myText = qrCode.data.decode('utf-8')
print (myText)