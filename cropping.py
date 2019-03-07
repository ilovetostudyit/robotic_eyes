import cv2 as cv
import numpy as np

# coordarray is our array of coords
# function takes x, y - as starting values.
# xadd and yadd are - size of our rectangle
# num - is number of rectangles
# the function basically put starting cords of rectangle into array
def array_add(coordarray, x, y, xadd, yadd, num):
    max1 = x + xadd * num
    max2 = y + yadd * num
    while (x < max1 or y < max2):
        coordarray.append(x)
        coordarray.append(y)
        x = x + xadd
        y = y + yadd

## function takes x, y - as starting values.
## h and w are - size of our rectangle
## num - is number of rectangles
## allign = 0 - horizontal, 1 - vert, 2 - hor + vert
def ft_cropping(x, y, h, w, num, allign):
    counter = 0
    coordarray =[]
    crop_img = []
    if allign == 0:
        array_add(coordarray, x, y, h, 0, num)
    elif allign == 1:
        array_add(coordarray, x, y, 0, w, num)
    elif allign == 2:
        array_add(coordarray, x, y, h, w, num)
    print(coordarray)
    img = cv.imread("furcrop.jpg")
    while (counter + 1) < len(coordarray):
        crop_img.append(img[coordarray[counter + 1]:coordarray[counter + 1] + w, coordarray[counter]:(coordarray[counter] + h)])
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
allign = 0
ft_cropping(x,y,h,w,num, allign)