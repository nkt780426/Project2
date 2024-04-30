import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)
# cv.imshow('Mask', circle)

retangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

wried_shape = cv.bitwise_and(circle, retangle)
cv.imshow('WriedShape', wried_shape)

masked = cv.bitwise_and(img, img, mask=wried_shape)
cv.imshow('Masked', masked)

cv.waitKey(0)