import cv2 as cv
import numpy as np
import tensorflow as tf
import time

# Load mô hình đã train
smile_detect_model = tf.keras.models.load_model('model/model.keras')

# Load Haar Cascade để phát hiện khuôn mặt
face_cascade = cv.CascadeClassifier('utils/haar_face.xml')

# Trả về tọa độ các khuôn mặt trong frame chứa face
def detect_faces(grayFrame):
    return face_cascade.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=40, minSize=(30, 30))

# Hàm để dự đoán cười trả về giá trị sigmoid, gần 1 là cười, gần 0 là không cười
def predict_smile(img):
    # Chuyển ảnh về kích thước (64*64) và tensor để đưa vào model
    img_resized = cv.resize(img, (64, 64))
    # Thêm chiều batch
    img_tensor = np.expand_dims(img_resized, axis=0)
    # Dự đoán cười hay không cười
    return smile_detect_model.predict(img_tensor)[0][0]

if __name__ == '__main__':
    # Load ảnh
    img_path = 'test4.jpg'
    img = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Nhận diện mặt trong ảnh
    faces = detect_faces(gray)
    for (x, y, w, h) in faces:
        cv.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.imshow('gray', gray)
        
        # Cắt mặt ra
        face_img = gray[y:y+h, x:x+w]
        cv.imwrite('face4.jpg', face_img)
        
        # Dự đoán
        start_time = time.time()
        print (predict_smile(face_img))
        end_time = time.time()
        print("Thời gian dự đoán: " + str(end_time-start_time))
    cv.waitKey(0)