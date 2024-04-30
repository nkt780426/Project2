import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('PARK', img)

# Video này nói về COLOR CHANNEL (tách-spilit và hợp nhất-merge các kênh màu)
# Đọc file word
# Chia ma trận ảnh thành 3 ma trận r, g, b

b, g, r = cv.split(img)

# 3 hình ảnh này sẽ được biểu diễn dưới dạng grayscale, do opencv hiểu ma trận 2 chiều là grayscale
# So sánh ảnh gốc và ảnh Blur: bầu trời màu trắng => Có cường độ màu xanh lam tập trung trên bầu trời
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Hợp nhất 3 ma trận làm 1 ảnh, nhớ merge theo thứ tự blue, green, red
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# Để xem 3 ảnh này với màu thực tế mà không phải grayscale
import numpy as np

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Green-Merge', cv.merge([blank, g, blank]))

cv.waitKey(0)