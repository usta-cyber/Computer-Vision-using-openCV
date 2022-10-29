# Lab-04: Screen Recorder
# Screen Recorder using pyautogui
# pip install pyautogui
# pip install pillow

import pyautogui as p
import cv2 as c
import numpy as np

# Get screen resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and Path")
#Fix the frame rate
fps = 30.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

# Create recording window
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)

# Resize the window
c.resizeWindow("Live_Recording",(600,400))

while True:
    # capture screenshots
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) == ord("q"):
        break

c.destroyAllWindows()
output.release()
