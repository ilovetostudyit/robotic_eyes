import cv2 as cv
import numpy as np

## function takes x, y - as starting values.
## h and w are - size of our rectangle
## num - is number of rectangles
def ft_cropping(x, y, h, w, num):
    counter = 0
    coordarray =[]
    crop_img = []
    max = x + h * num
    counter2 = 0
    while x < max:
        coordarray.append(x)
        coordarray.append(y + w)
        x = x + h
        #y = y + w
    print(coordarray)
    img = cv.imread("furcrop.jpg")
    while (counter + 1) < len(coordarray):
        crop_img.append(img[y:coordarray[counter + 1], coordarray[counter]:(coordarray[counter] + h)])
        counter = counter + 2
    counter = 0
    while counter < len(crop_img):
        cv.imshow(str(counter), crop_img[counter])
        counter = counter + 1
    cv.imshow("ORGIN", img)
    cv.waitKey(0)
    return(crop_img)

##### EXAMPLE OF TEST ########### 
y = 389
x = 294
h = 34
w = 40
num = 6
ft_cropping(x,y,h,w,num)