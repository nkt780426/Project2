import cv2 as cv

# Lấy image từ 1 path và chuyển nó thành ma trận pixels
img = cv.imread('Resources/Photos/cat.jpg')

# Ảnh trên là 640*427 nên có thể nhìn được, nếu thử ảnh 2400*1600 thì sẽ không nhìn được
# img = cv.imread('Resources/Photos/cat_large.jpg')
# Cần phải resize lại ảnh sao cho phù hợp với kích thước màn sẽ nói ở phần sau

# display image, nó sẽ hiển thì 1 windown. Cần cung cấp title của windown và ma trận pixel mà windown sẽ hiển thị
cv.imshow('Cat', img)

# deplay cho đến khi người dùng nhấn 1 key trên bàn phím. 
# Khi dòng này được đặt ở cuối nghĩa là khi người dùng nhấn 1 phím bất kỳ, tiến trình kết thúc, toàn bộ windown bị đóng
cv.waitKey(delay=0)