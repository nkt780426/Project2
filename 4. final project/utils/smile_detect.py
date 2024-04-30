import cv2 as cv
import numpy as np
import tensorflow as tf
import time

# Load mô hình đã train
smile_detect_model = tf.keras.models.load_model('model/model.keras')

# Load Haar Cascade để phát hiện khuôn mặt
face_cascade = cv.CascadeClassifier('utils/haar_face.xml')

# Trả về tọa độ các khuôn mặt trong frame chứa face
def detect_faces(frame):
    # Phải chuyển về grayscale mới dùng haar_casadra
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Phát hiện khuôn mặt trong ảnh grayscale
    return face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=40, minSize=(30, 30))

# Hàm để dự đoán cười trả về giá trị sigmoid, gần 1 là cười, gần 0 là không cười
def predict_smile(img):
    # Chuyển ảnh về kích thước (28x28) và tensor để đưa vào model
    img_resized = cv.resize(img, (64, 64))
    # OpenCV mặc định đọc ảnh theo hệ màu BGR cần chuyển sang RGB trước khi đưa vào model
    rgb_image = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)
    # Chuẩn hóa ảnh bằng cách chia cho 255 để đưa giá trị về khoảng [0, 1]
    normalized_image = rgb_image / 255.0
    # Thêm chiều batch
    img_tensor = np.expand_dims(normalized_image, axis=0)
    # Dự đoán cười hay không cười
    return smile_detect_model.predict(img_tensor)[0][0]

if __name__ == '__main__':
    img_path = 'model/dataset/Kaggle/test/Zoran_Djindjic_0004.jpg'
    img = cv.imread(img_path)
    start_time = time.time()
    prediction = predict_smile(img)
    end_time = time.time()
    # Chuyển đổi giá trị dự đoán thành chuỗi có ý nghĩa
    if prediction >= 0.5:
        prediction_text = 'Smile'
    else:
        prediction_text = 'Not Smile'
    # Convert prediction to string before putting it onto the image
    cv.putText(img, prediction_text, (10, 20), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
    cv.imshow('Test', img)
    print("Thời gian dự đoán:", end_time - start_time, "giây")
    cv.waitKey(0)