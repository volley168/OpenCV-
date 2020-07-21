import cv2 as cv
import numpy as np

def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转灰度图
    face_detect = cv.CascadeClassifier("")  # 级联检测器  (此部分未训练)
    faces = face_detect.detectMultiScale(gray, 1.1, 5)  # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)# 后两个参数，一个是颜色，一个是边框宽度
    cv.imshow("result", image)
print("  Hello world  ")
src = cv.imread("xigua.png")
capture = cv.VideoCapture(0)
while (True):
    ret, fram = capture.read()
    fram = cv.flip(fram, 1)
    face_detect_demo(fram)
    if cv.waitKey(10):
        break
cv.waitKey(0)
cv.destroyAllWindows()
