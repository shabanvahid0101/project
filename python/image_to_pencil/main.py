import cv2
image = cv2.imread('D:/code\python\python pj\image_to_pencil/4.JPG')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted=255-gray_image
blur=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blur
sketh=cv2.divide(gray_image,invertedblur,scale=255.0)
cv2.imwrite("D:/code\python\python pj\image_to_pencil/sketch_image.png",sketh)
cv2.imshow("image",sketh)

