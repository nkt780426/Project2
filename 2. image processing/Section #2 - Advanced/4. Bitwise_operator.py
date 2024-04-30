import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

retangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Retangle', retangle)
cv.imshow('Circle', circle)

# bitwise AND (trả về tất cả vùng giao nhau)
bitwise_and = cv.bitwise_and(retangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR (trả về tất cả vùng không giao nhau vả giao nhau)
bitwise_or = cv.bitwise_or(retangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise xor (trả về các vùng không giao nhau)
bitwise_xor = cv.bitwise_xor(retangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# bitwise_not
bitwise_not = cv.bitwise_not(retangle)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)