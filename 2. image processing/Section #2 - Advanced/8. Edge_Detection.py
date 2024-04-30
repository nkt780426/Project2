import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# DDepth: độ sâu của data, set là 64F với mọi th
lap = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)
# Kết hợp 2 ảnh lại
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny
canny = cv.Canny(image=gray, threshold1=150, threshold2=175)
cv.imshow('Canny', canny)

cv.waitKey(0)