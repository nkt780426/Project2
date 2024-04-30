import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('PARK', img)

# Video này nói về chuyển đổi ảnh trong các hệ màu khác nhau
# Ảnh được biểu diễn bởi 1 ma trận pixel colors
# Có rất nhiều hệ màu khác nhau: RGB (ảnh màu bình thường), grayscale (đen trắng), HSV, NAB

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (hue saturation: bão hòa màu sắc)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
# OPENCV mặc định đọc image ở BGR format, nó không phải là hệ màu chuẩn RGB bên ngoài opencv
# Nếu bạn có gắng mở hình ảnh được đọc bởi opencv bằng 1 hệ thống bên ngoài, ảnh sẽ bị đảo ngược màu sắc
import matplotlib.pyplot as plt

# plt.imshow(img)
# plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)