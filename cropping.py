import cv2 as cv
import numpy as np  
from croppsetup import *

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

def add_to_list(array, file):
    with open(file, 'a') as f:
        for item in array:
            f.writelines("%s\n" % item)
        f.writelines("\n")
    f.close()

## function takes x, y - as starting values.
## h and w are - size of our rectangle
## num - is number of rectangles
## allignc = 0 - horizontal, 1 - vert, 2 - hor + vert
def ft_cropping(img, x, y, h, w, num, allign):
    global coordarray
    counter = 0
    coordarray = []
    crop_img = []
    if allign == 0:
        array_add(coordarray, x, y, h, 0, num)
    elif allign == 1:
        array_add(coordarray, x, y, 0, w, num)
    elif allign == 2:
        array_add(coordarray, x, y, h, w, num)
    elif allign == 3:
        array_add(coordarray, x, y, -h, -w, num)
    while (counter + 1) < len(coordarray):
        crop_img.append(img[coordarray[counter + 1]:coordarray[counter + 1] + w, coordarray[counter]:(coordarray[counter] + h)])
        counter = counter + 2
    return(crop_img)

def read_preset(file):
    with open(file) as f:
        mylist = f.read().splitlines()
        mylist = [i.split(',') for i in mylist]
    return(mylist)

##### EXAMPLE OF TEST ########### 
##MADE SOME SIMPLE GRAPHICAL INTERFACE FOR SETUP :3 
## LOOKING FOR SOME SETUPS
if __name__ == '__main__':
    def nothing(*arg):
        pass

def croppsetup(image):
    img = cv.imread(image)
    
    barposition = []
    barposition = read_preset("presetting.txt")
    barindex_x = 0

    cv.namedWindow('settings')
    open('array_file.txt', 'w').close()

    cv.createTrackbar('allign', 'settings', 0, 3, nothing)
    cv.createTrackbar('num', 'settings', 0, 6, nothing)
    cv.createTrackbar('x', 'settings', 0, 1277, nothing)
    cv.createTrackbar('h', 'settings', 0, 1277, nothing)
    cv.createTrackbar('y', 'settings', 0, 958, nothing)
    cv.createTrackbar('w', 'settings', 0, 958, nothing)

    cv.setTrackbarPos('x', 'settings', int(barposition[barindex_x][0]))
    cv.setTrackbarPos('y', 'settings', int(barposition[barindex_x][1]))
    cv.setTrackbarPos('h', 'settings', int(barposition[barindex_x][2]))
    cv.setTrackbarPos('w', 'settings', int(barposition[barindex_x][3]))
    cv.setTrackbarPos('num', 'settings', int(barposition[barindex_x][4]))
    cv.setTrackbarPos('allign', 'settings', int(barposition[barindex_x][5]))

    crange = [0,0,0, 0,0,0]
    crop_img = []
    count_a = 0
    color = (0,255,0)
    while count_a < 8:
        dimg = cv.imread(image)
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
        temp_img = []
        if (h > 0 and w > 0 and (x + h * num) < 1277 and (y + w * num) < 958):
            temp_img = ft_cropping(img,x,y,h,w,num, allign)
            while counter < len(crop_img):
                cv.imshow(str(counter), crop_img[counter])
                counter = counter + 1
        i = 0
        while i < len(coordarray):
            left_angle = (coordarray[i], coordarray[i + 1])
            right_angle = (coordarray[i] + h, coordarray[i + 1] + w)
            cv.rectangle(dimg, left_angle,right_angle,color, 3)
            i = i + 2;
        cv.imshow("ORIGIN1", dimg)
        if cv.waitKey(33) == ord('a'):
            crop_img.extend(temp_img)
            count_a = count_a + 1
            add_to_list(coordarray, 'array_file.txt')
            barindex_x = barindex_x + 1
            if barindex_x < 8:
                cv.setTrackbarPos('x', 'settings', int(barposition[barindex_x][0]))
                cv.setTrackbarPos('y', 'settings', int(barposition[barindex_x][1]))
                cv.setTrackbarPos('h', 'settings', int(barposition[barindex_x][2]))
                cv.setTrackbarPos('w', 'settings', int(barposition[barindex_x][3]))
                cv.setTrackbarPos('num', 'settings', int(barposition[barindex_x][4]))
                cv.setTrackbarPos('allign', 'settings', int(barposition[barindex_x][5]))
        ch = cv.waitKey(5)
        if ch == 27:
            break
    cv.destroyAllWindows()
    return(crop_img)

###MAIN TEST
croppsetup("images/2019-03-02-151637.jpg");