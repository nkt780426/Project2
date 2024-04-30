import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park', img)

# Converting to gray scale (đổi ảnh sang đen trắng)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur (làm mờ ảnh, hay loại bỏ noise. Ngoài ra còn có giảm tiếng ồn trong video, ...)
# Có rất nhiều công nghệ Blur (làm mờ) sẽ nói kỹ hơn ở phần Advance, đây là basics
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (Tìm đường biên trong 1 image)
# Có rất nhiều cascade có sẵn nhưng phần này chỉ nói qua
# Dùng candy edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Phóng to edge ra bằng cách chỉ định 1 phần tử có cấu trúc
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilate', dilate)

# Eroding (xói mòn) dilated image để lấy lại phần từ có cấu trúc
eroded = cv.erode(dilate, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
# Nếu thu nhỏ ảnh sử dụng cv.INTER_AREA, phóng to sử dụng cv.INTER_CUBIC/cv.INTER_LINEAR
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Crop
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)