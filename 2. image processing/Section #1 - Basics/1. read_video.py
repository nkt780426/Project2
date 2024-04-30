import cv2 as cv

# Reading Videos
# Hàm VideoCaptrure sử dụng webcam nếu nó có các tham số 0, 1, 2, 3 hoặc video có sẵn nếu tham số là path
# Thường sẽ là 0, nếu sử dụng nhiều webcam thì sẽ tham khảo các đối số khác
capture = cv.VideoCapture(0)

# Đọc video là 1 hàm loop và đọc từng frame của video
while True:
    # isTrue để xem rằng frame đã được đọc hay chưa
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    # Đợi 20 s tắt video hoặc nhấn d để thoát
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Giải phóng tài nguyên được sử dụng cho video
capture.release()
# Xóa tất cả windown đã mở bởi file này
cv.destroyAllWindows()