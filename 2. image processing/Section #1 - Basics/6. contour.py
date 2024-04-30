import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Orginal', img)

# Contour detection: Phát hiện đường viền (ranh giới) giữa các vật thể
# Theo quan điểm toán học edges và contour detection là khác nhau
# contour detection là công cụ hữu ích cho shape analysis và object detection, recognition

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # C1: Dùng canny edge detector để tìm tất cả các edge trong img
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# C2: Sử dụng threshold
# Sẽ nói kỹ hơn ở phần sau, về cơ bản nó sẽ xem xét 1 image và cố gắng nhị phân hóa nó, nếu mật độ của pixel < 125 sẽ được đặt là 0 hoặc bỏ trống
# Đây là phương pháp để tìm contour
ret, thresh = cv.threshold(gray, 125, 125, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


# Để tìm contour cho các vật thể bằng cách sử dụng các hàm find contours method
# Các hàm này trả về 2 thứ, contour và phân cấp chúng (edges thuộc về đối tượng nào)
# contour: danh sách tọa độ tất cả contour tìm thấy được trong ảnh
# hierarchies: phân cấp các contour trên. Ví dụ có n vật thể thì nó sẽ phân cấp các contour về n bậc tương ứng
# cv.RETR_LIST: trả về 1 list các contour tìm được trong img. Ngoài ra còn có cv.RETR_EXTERNAL
# cv.CHAIN_APPROX_NONE: phương pháp để tìm edges thuộc về vật thể nào-contour approximation method (ước tính đường viền)
# Ngoài ra còn có cv.CHAIN_APPROX_SIMPLE: nén tất cả contour được trả về những contour có ý nghĩa nhất. Ví dụ có 1 đường thẳng trong img, nếu sử dụng cv.CHAIN_APPROX_NONE bạn sẽ nhận được tất cả các tọa độ thuộc đường đó, còn sử dụng cv.CHAIN_APPROX_SIMPLE sẽ chỉ lấy 2 điểm đầu và cuối của đường đó
# Thực tế 1 ảnh phức tạp thường ko nén được nhiều nên tốt nhất dùng cv.CHAIN_APPROX_NONE
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')


# Sau khi tìm được các contour, opencv có thể visualize được chúng
import numpy as np

blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours, -1, (0,0,255), 1)

cv.imshow('Contours drawn', blank)

cv.waitKey(0)

# Để cho chất lượng tốt nhất, hãy sử dụng scanning method trước sau đó tìm contour
# Sử dụng threshold mặc dù đơn giản hơn nhưng có nhược điểm sẽ nói ở phần advanced. Nhưng trong hầu hết th thực tế lại sử dụng thresold bởi vì nó đơn giản và kết quả chấp nhận được