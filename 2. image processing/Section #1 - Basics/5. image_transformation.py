import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)

# Bài này nói về image_transformation như translation(dịch), rotation(xoay), resizing(thay đổi kích thước), flipping (lật), cropping
# Translation (có thể dịch trên, dưới, trái, phải)
def translate(img, x, y):
    # Ý tưởng trả lại ma trận dịch x và y của ảnh
    transMat = np.float32([[1,0,x], [0,1,y]])
    
    # Xác định kích thước của hình ảnh sau khi dịch (bằng kích thước ảnh ban đầu)
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

translated = translate(img, 100, -100)
cv.imshow('Translated', translated)

# Rotation: xoay
# Có thể trọn bất kỳ điểm nào trong ảnh là tâm quay (thường là tâm ảnh)
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)

# Xoay theo chiều kim đồng hồ để angle >0, ngược thì angle <0
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Flipping(lật): 0 lật theo chiều dọc, 1 lật theo trục x, âm là trục y (có thể sai, tự trải nhiệm)
flip = cv.flip(img, -1)
cv.imshow('Flip-0', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)