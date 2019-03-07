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
def ft_cropping(img, x, y, h, w, num, allign):
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
    while (counter + 1) < len(coordarray):
        crop_img.append(img[coordarray[counter + 1]:coordarray[counter + 1] + w, coordarray[counter]:(coordarray[counter] + h)])
        counter = counter + 2
    counter = 0
    return(crop_img)

##### EXAMPLE OF TEST ########### 
##MADE SOME SIMPLE GRAPHICAL INTERFACE FOR SETUP :3 
## LOOKING FOR SOME SETUPS
if __name__ == '__main__':
    def nothing(*arg):
        pass

img = cv.imread("furcrop.jpg")
cv.namedWindow('settings')

cv.createTrackbar('allign', 'settings', 0, 2, nothing)
cv.createTrackbar('num', 'settings', 0, 6, nothing)
cv.createTrackbar('x', 'settings', 0, 1277, nothing)
cv.createTrackbar('h', 'settings', 0, 1277, nothing)
cv.createTrackbar('y', 'settings', 0, 958, nothing)
cv.createTrackbar('w', 'settings', 0, 958, nothing)
####PRESETS####
#left_6 = ft_cropping(img,294,389,34,40,6,0)
#right_6 = ft
crange = [0,0,0, 0,0,0]
while True:
    h = 34
    w = 40
    num = 6
    allign = 0
    x = cv.getTrackbarPos('x', 'settings')
    y = cv.getTrackbarPos('y', 'settings')
    h = cv.getTrackbarPos('h', 'settings')
    w = cv.getTrackbarPos('w', 'settings')
    num = cv.getTrackbarPos('num', 'settings')
    allign = cv.getTrackbarPos('allign', 'settings')
    counter = 0
    if (h > 0 and w > 0):
        crop_img = ft_cropping(img,x,y,h,w,num, allign)
        while counter < len(crop_img):
            cv.imshow(str(counter), crop_img[counter])
            counter = counter + 1
    cv.imshow("ORGIN", img)
    ch = cv.waitKey(5)
    if ch == 27:
        break
cv.destroyAllWindows()