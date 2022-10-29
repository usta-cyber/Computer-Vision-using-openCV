# Lab-09
# Color Picker project using tracebar

import cv2
import numpy as np

def cross(x):
    pass

# create a black imgae
img = np.zeros((250, 512, 3), np.uint8)  # empty image
cv2.namedWindow("Color Picker Tool")


# Creating TrackBars For Adjusting Colors
cv2.createTrackbar("R", "Color Picker Tool", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker Tool", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker Tool", 0, 255, cross)

# Now creating logic to handle trackbars
while True:
    cv2.imshow("Color Picker Tool", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # for exit
        break

    # set current positions of four bars

    r = cv2.getTrackbarPos("R", "Color Picker Tool")
    g = cv2.getTrackbarPos("G", "Color Picker Tool")
    b = cv2.getTrackbarPos("B", "Color Picker Tool")

    img[:] = [b, g, r]
cv2.destroyAllWindows()
