import cv2

img_grey = cv2.inread ("D:/image.png', cv2.IMREAD_GRAYSCALE)
                       
thresh = 128
                       
img_binary = cv2.threshold (img_grey, thresh, 255, cV2.THRESH_BINARY) [1]
                       
cv2.imwrite('D:/final.png', img_binary)
                       
                     
                       # natrix dev
                       # full code from my github (github.com/natrixdev) 
