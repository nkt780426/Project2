import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# img = cv.imread('Resources/Photos/cats.jpg')
# Thử với ảnh khác
img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Thực hiện phân tích histogram của ảnh grayscale và rgb
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray, gray, mask=mask)

cv.imshow('Mask', mask)

# imgaes: chứa các ảnh muốn phân tích, ở đây chỉ có 1 image là gray
# channels: index của các color channel muốn phân tích 
# masks: cung cấp nếu muốn computering histogram cho 1 vùng cụ thể trong ảnh
# histSize: số lượng bins mà chúng ta muốn sử dụng để tính toán histogram
# range: phạm vi giá trị của pixel có thể tính toán
gray_hist = cv.calcHist(images=[gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of labels')
plt.plot(gray_hist)
plt.xlim([0, 256]) # Đặt giá trị giới hạn cho trục x
# plt.show()

# Color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask=mask, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256]) # Đặt giá trị giới hạn cho trục x

plt.title('Color Histogram')
plt.show()

cv.waitKey(0)