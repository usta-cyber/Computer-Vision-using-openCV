'''
Computer vision Lab 01
image processing basics
image read, write,resize,grayscale,flipe,get path from user
'''
# openCV use as cv2 in python
import cv2
# Loads a color image. Any transparency of image will be neglected. It is the default flag.
img1 = cv2.imread('E:\\mydata\\1.jpg', 1)
# resize(image, (width ,height)
img1 = cv2.resize(img1, (1280, 700))

# It accept two parameters 1)- Name of screen ,2) -  Image
cv2.imshow("Colored Image", img1)
print("Give image with color==\n", img1)

#  Loads image in grayscale mode
img2 = cv2.imread('E:\\mydata\\2.jpg', 0)
img2 = cv2.resize(img2, (1280, 700))
cv2.imshow("Gray Scale Image", img2)
print("Image in gray scale==\n", img2)

# Loads image as such including alpha channel
img3 = cv2.imread('E:\\mydata\\3.jpg')
img3 = cv2.resize(img3, (1280, 700))
cv2.imshow("Original Image", img3)
print("Image in original value==\n", img3)

# Color conversion
# Gray scale
grayimage=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray scal Image",grayimage)
# Blur Image
blurimage=cv2.GaussianBlur(img3,(3,3),0)
cv2.imshow("Blur Image",blurimage)
# Edge Detection
cannyimg=cv2.Canny(img3,150,200)
cv2.imshow("Edge Image",cannyimg)
# image dilation
dilateimg=cv2.dilate(cannyimg,(5,5),iterations=1)
cv2.imshow("dilate Image",dilateimg)
# image Erode
erodeimg=cv2.erode(dilateimg,(5,5),iterations=1)
cv2.imshow("Erode Image",erodeimg)
# here parameter inside waitkey handle the life duration of an image
cv2.waitKey(0)
cv2.destroyAllWindows()

# path = input("Enter the Path and name of an image===")
# print("You Enter this===",path)

# Now read image,convert image into grayscale,flip and save
img1 = cv2.imread("E:\\mydata\\4.jpg", 0)  #
img1 = cv2.resize(img1, (560, 700))
img1 = cv2.flip(img1, 0)  # it accept 3 parameters 0,-1,1
cv2.imshow("converted image==", img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("E:\\mydata\\ouput.png", img1)  # it accept name of image and data
    cv2.destroyAllWindows()
