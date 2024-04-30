import cv2 as cv
from utils.smile_detect import detect_faces, predict_smile

# Địa chỉ IP và cổng của máy tính host chạy MJPEG Streamer
host_ip = "192.168.1.136"
port = "8000"

# URL của luồng MJPEG
mjpeg_url = f"http://{host_ip}:{port}/?action=stream"

# Khởi tạo VideoCapture để đọc từ luồng MJPEG
capture = cv.VideoCapture(mjpeg_url)

while True:
    # Đọc từng frame, ret là bool nếu đọc được frame
    ret, frame = capture.read()
    if not ret:
        print("Failed to capture frame")
        break
    # Toạ độ các mặt trong frame
    faces = detect_faces(frame)
    
    for (x, y, w, h) in faces:
        # Cắt ảnh khuôn mặt
        face_img = frame[y:y+h, x:x+w]
        # Vẽ xung quanh faces phát hiện được và hiển thị kết quả predictions
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame, "Smile", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Hiển thị video, nhấn 'q' để thoát project
    cv.imshow('Face Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print('Exit')
        break