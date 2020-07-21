import cv2

capture=cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("video",frame)
    key=cv2.waitKey(50)
    if key == ord('q'):
        break
    cv2.destroyAllWindows()