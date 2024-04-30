import cv2 as cv
import numpy as np

# Có 2 cách để vẽ lên 1 ảnh, vẽ trực tiếp lên ảnh này hoặc tạo 1 ảnh trống và vẽ lên

# Nhớ lại. hàm imreade có tác dụng đọc ma trận pixel của ảnh => Kết quả thu được là 1 ma trận => Tương tác với ma trận dùng numpy
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Tạo ảnh trống 550*500 pixels và 3 màu r,g,b
blank_img = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank_img)

# # 1. Đổi màu toàn ảnh
# blank_img[:] = 0,255,0
# cv.imshow('1.1', blank_img)
# blank_img[200:300, 300:400] = 0,0,255
# cv.imshow('1.2', blank_img)

# 2. Vẽ hình chữ nhật
# Khi set thickness là 2 thì đơn giản color là màu của thichness và nó chỉ là đường viền chia img ra
# Nết set thickness=cv.FILLED (hoặc -1) thì nó sẽ vẽ 1 hình chữ nhật có color lên ảnh gốc thay vì chỉ là đường viền
cv.rectangle(blank_img, pt1=(0,0), pt2=(250, 250), color=(0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank_img)
# Để ý thấy pt1 và pt2 là giá trị cố định, nếu ta muốn nó dựa vào dimentions của img thì sao
cv.rectangle(blank_img, pt1= (0, 0), pt2=(blank_img.shape[1]//2, blank_img.shape[0]//2), color=(0, 255, 0), thickness= -1)
cv.imshow('Square', blank_img)

# 3. Vẽ hình tròn
cv.circle(blank_img, center=(blank_img.shape[1]//2, blank_img.shape[0]//2), radius=40, color = (0, 0, 255), thickness=3)
cv.imshow('Circle', blank_img)

# 4. Vẽ đường thẳng
cv.line(blank_img, pt1=(0,0), pt2= (blank_img.shape[1]//2, blank_img.shape[0]//2), color=(255,255,255), thickness=3)
cv.imshow('Line', blank_img)

# 5. Write Text
cv.putText(blank_img, 'Hello', (255, 255), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow('Put Text', blank_img)

cv.waitKey(0)