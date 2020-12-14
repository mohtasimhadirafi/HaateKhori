import numpy as np
import cv2
import matplotlib.pyplot as plt

nose_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_mcs_nose.xml')

ds_factor = 0.5

image = cv2.imread('Images/Input/DSCF4356.JPG')

image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in nose_rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)


cv2.imwrite('Images/Output/final_imageGray.png', image)
