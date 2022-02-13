import cv2
import numpy as np
from pyzbar.pyzbar import decode 

img = cv2.imread('code.png')
code = decode (img)
for qrCode in code:
  myText = qrCode.data
print (myText)