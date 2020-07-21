import cv2

# 加载灰度图
img = cv2.imread('beauty.jpg')
cv2.namedWindow('beauty2')
cv2.imshow('beauty',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
