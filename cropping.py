from setup import *

def cropping(image):
    img = cv.imread(image)
    cropping_result = []
    with open("result.txt") as f:
        mylist = f.read().splitlines()
    i = 0
    while ((i + 6) < len(mylist)):
        cropping_result.extend(ft_cropping(img, int(mylist[i]), int(mylist[i+1]),int(mylist[i+2]),int(mylist[i+3]),int(mylist[i+4]),int(mylist[i+5])))
        i = i + 6
    counter = 0
    #UNCOMMENT FOR VISUAL RESULT
    #while True:
    #    while counter < len(cropping_result):
    #        cv.imshow(str(counter), (cropping_result[counter]))
    #        counter = counter + 1
    #    ch = cv.waitKey(5)
    #    if ch == 27:
    #        break
    return(cropping_result)

cropping("images/2019-03-02-151637.jpg")