import cv2 as cv
from utils.smile_detect import detect_faces, predict_smile

# Địa chỉ IP và cổng của máy tính host chạy MJPEG Streamer
host_ip = "192.168.1.136"
port = "8000"

# URL của luồng MJPEG
mjpeg_url = f"http://{host_ip}:{port}/?action=stream"

# Khởi tạo VideoCapture để đọc từ luồng MJPEG
capture = cv.VideoCapture(mjpeg_url)

# Biến đếm tổng số lần cười
num_smiles = 0
smile_text = None

while True:
    # Đọc từng frame, ret là bool nếu đọc được frame
    ret, frame = capture.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    # Toạ độ các mặt trong frame
    faces = detect_faces(frame)
    
    # Lặp qua các khuôn mặt được phát hiện
    for (x, y, w, h) in faces:
        # Cắt ảnh khuôn mặt
        face_img = frame[y:y+h, x:x+w]
        # Dự đoán cười trên ảnh khuôn mặt
        prediction = predict_smile(face_img)
        # Nếu có cười, tăng biến đếm và vẽ hình chữ nhật xung quanh khuôn mặt
        if prediction > 0.5:
            smile_text = 'Smiling'
            num_smiles += 1
        else:
            smile_text = 'Not smiling'
        # Vẽ xung quanh faces phát hiện được và hiển thị kết quả predictions
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame, smile_text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Hiển thị tổng số lần cười từ đầu video
    cv.putText(frame, f'Smiles: {num_smiles}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Hiển thị video, nhấn 'q' để thoát project
    cv.imshow('Face Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print('Exit')
        break

# Giải phóng bộ nhớ và đóng cửa sổ
capture.release()
cv.destroyAllWindows()