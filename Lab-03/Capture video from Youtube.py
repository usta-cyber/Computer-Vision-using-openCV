
# Capture video from youtube
import pafy
import cv2
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url)
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture()
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
# Various codec --
# DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("E:\\mydata\\download2.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret==True:
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Colorframe',gray)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break

# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()

#if any os error regarding youtube-dl occur thn
#conda install -c forge youtube-dl
#pip install youtube-dl
"""
open backend youtube-dl file and replace the following
self._likes = self._ydl_info.get('like_count',0)
self._dislikes = self._ydl_info.get('dislike_count',0)
"""









