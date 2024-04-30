import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Person', img)

# Faces không liên quan gì đến màu da, color, .... có trong hình ảnh
# Haar cascade sẽ nhìn vào các vật thể bên trong 1 image và sử dụng edges để cố gắng xác định xem đó có phải khuôn mặt không nên không cần ảnh màu
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('Section #3 - Faces/haar_face.xml')

# minNeighbors: số lượng neighbor retangle nên có để gọi là 1 khuôn mặt
# detect multiscale: biến haar_casscade sẽ lấy image và sử dụng các biến của chúng được gọi là scaleFactor và miniNeighbor để phát hiện face và trả về danh sách các tọa độ hình chữ nhật có mặt
faces_rect = haar_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

# Lặp lại các tọa độ tìm được và vẽ hình chữ nhật lên nó
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)