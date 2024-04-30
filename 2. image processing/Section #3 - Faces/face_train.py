import os
import cv2 as cv
import numpy as np

# Điền tên những người cần phát hiện
people= []
DIR = r'Resources/Faces/train'

for i in os.listdir(DIR):
    people.append(i)
    
print(people)

haar_cascade = cv.CascadeClassifier('Section #3 - Faces/haar_face.xml')

# Các folder trong thư mục train là training set
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        # loop tất cả các ảnh trong thư mục
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            # Cắt cái mặt ra khỏi ảnh và thêm vào features list
            # Để giảm căng thẳng khi máy tính train model, đỏi label từ string sang number
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()
print(f"Length of features = {len(features)}")
print(f"Length of features = {len(labels)}")
# Sau khi có training set, tiến hành train

print('Start training')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

print('Training done')
# Lưu lại model để sử dụng trong 1 tệp khác
face_recognizer.save('Section #3 - Faces/face_trained.yml')

np.save('Section #3 - Faces/features.npy', features)
np.save('Section #3 - Faces/labels.npy', labels)
