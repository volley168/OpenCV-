import cv2


img = cv2.imread("beauty.jpg")

img[100:200,150:200] = [255,255,255]

cv2.imshow("demo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("beauty1.jpg",img)
