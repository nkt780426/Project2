import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Video này nói về blur technique: 2 khái niệm blur (làm mờ) và smoothing (làm mịn), đọc file word

# Làm mờ
# Adveraging blur (trung bình): Phổ biến nhất
kernel_size = 9
adveraged = cv.blur(img, (kernel_size, kernel_size))
cv.imshow('Adveraged', adveraged)

# Gaussian blur
sigma = 1 # Đọc công thức trong file word, nó là độ lệnh chuẩn theo hướng x
gauss = cv.GaussianBlur(img, (kernel_size, kernel_size), sigma)
cv.imshow('Gaussian Blur', gauss)

# Media Blur (median filtering)
median = cv.medianBlur(img, kernel_size)
cv.imshow('Median Blur', median)

# Bilateral Blur
neighborhood = 5
sigmaColor = 15
sigmaSpace = 15
bilateral = cv.bilateralFilter(img, neighborhood, sigmaColor, sigmaSpace)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)