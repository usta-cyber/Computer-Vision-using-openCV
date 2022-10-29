# Lab-05: Video to Frames conversion
# Capture Multiple Images and Store in a folder
import cv2
vidcap = cv2.VideoCapture(0)
ret,image = vidcap.read()
count = 0
while True:
  if ret == True:
      # save frame as JPEG file
      cv2.imwrite("E:\\mydata\\Frames\\image_%d.jpg" % count, image)
      # used to hold speed of frame generation
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
      ret,image = vidcap.read()
      cv2.imshow("res",image)
      print ('Read a new frame:',count ,ret)
      count += 1
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
          cv2.destroyAllWindows()
  else:
      break
vidcap.release()
cv2.destroyAllWindows()
