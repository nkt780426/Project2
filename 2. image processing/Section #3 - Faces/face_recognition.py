import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('Section #3 - Faces/haar_face.xml')

# Điền tên những người cần phát hiện
people= []
DIR = r'Resources/Faces/train'

for i in os.listdir(DIR):
    people.append(i)
    
print(people)

features = np.load('Section #3 - Faces/features.npy', allow_pickle=True)
labels = np.load('Section #3 - Faces/labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Section #3 - Faces/face_trained.yml')

img = cv.imread('Resources/Faces/val/ben_afflek/5.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]
   
    label, accuaracy = face_recognizer.predict(face_roi)
    print(f'Label = {label} with a accuracy of {accuaracy}')
    
    # Put text trên ảnh để biết điều gì đang xảy ra
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0),  thickness=2)
    
cv.imshow('Detected Face', img)

cv.waitKey(0)

# Face recognition trong opencv không phải là tốt nhất và dữ liệu trong bài này quá ít chỉ có 100 hình ảnh nên không chạy được deep learning