import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Chuyển hình ảnh sáng grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
# cv.THRESH_BINARY: só sánh giá trị từng pixel với thresh, nếu nó lớn hơn thì set là 255 nhỏ hơn thì set 0
threshold, thresh = cv.threshold(src=gray, thresh=100, maxval=255, type=cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

# Tạo ra ảnh có ngưỡng nghịch đảo (inverse thresholding)
threshold, thresh_inv = cv.threshold(src=gray, thresh=100, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inv)

# Adaptive thresholding
# cv.ADAPTIVE_THRESH_MEAN_C: giá trị trung bình của 1 vùng lân cận nào đó
# Blocksize: kích thước vùng lân cận (có thể coi là kernel) dùng để tính toán ADAPTIVE_THRESH_MEAN_C
# C: là 1 số nguyên và là tham số quan trọng để điều chỉnh threshol được áp dụng cho từng pixel, bằng cách này ta có thể điều chỉnh threshold tùy thuốc vào đặc tính của vùng lân cận
# Khi thực hiện Adaptive threshold, threshold được tính toán bằng means của các pixel trong kernel. Tuy nhiên có những trường hợp giá trị mean không phản ánh sự khác biệt giữa các pixel
# Để điều chỉnh cho những trường hợp này, tham số C được sử dụng để thêm hoặc trừ vào threshold tính ra được khi áp dụng cho pixel đó
# Ý nghĩa 2 dòng dưới đây có thể bị ngược
# C>0, threshold = mean - C, threshold nhỏ hơn. Điều này có nghĩa trong 1 vùng pixel sáng hơn trung bình thì ta áp dụng ngưỡng này để chấp nhận nhiều điểm sáng hơn
# C<0, threshold = mean - C, ảnh có ít điểm sáng hơn do threshold lớn hơn. 1 vùng lân cận có nhiều điểm tối hơn trung bình thì nó sẽ áp dụng ngưỡng này 
# adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=10)
adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=0)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)