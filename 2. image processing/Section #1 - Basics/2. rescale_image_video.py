import cv2 as cv

# Thay đổi kích thước, áp dụng cho cả image, video, Live video
def rescaleFrame(frame, scale=0.75):
    # 0 là chiều cao của màn hình, 1 là chiều dài của màn hình
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimenstion = (width, height)
    # Lưu ý không resize lại frame gốc
    # interpolation: nội suy
    return cv.resize(frame, dimenstion, interpolation=cv.INTER_AREA)

# Thay đổi độ phân giải, chỉ áp đụng được cho Live Video như webcam
def changeRes(width, height):
    # Capture class có các trường, trong đó trường 3 và 4 tương ứng là width và height, muốn đổi độ phân giải làm như vậy
    # Thay đổi độ sáng của frame là 10
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('Resources/Photos/cat.jpg')
img_resized = rescaleFrame(img, scale=0.2)

cv.imshow('Cat Orginal', img)
cv.imshow('Cat Resized', img_resized)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Original', frame)
    cv.imshow('Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()