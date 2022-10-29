# Lab-10:Color Image Split and Merge
import cv2

#Read colored image from system
img = cv2.imread("E:\\mydata\\5.jpg")
img = cv2.resize(img,(600,400))
cv2.imshow("Orignal",img)
print("shape==",img.shape)        #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size)  #returns Total number of pixels is accessed
print("datatype==",img.dtype)     #returns Image datatype is obtained
print("Imagetype==",type(img))

#Now try to split an image
#Two different methods to split an image using split function and manualy
#split  -  return 3 channel of ur image which is blue,green,red
#b,g,r = cv2.split(img)
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)
"""
#Now if you want to mix the the channels then use merge
"""
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)

cv2.waitKey()
cv2.destroyAllWindows()
