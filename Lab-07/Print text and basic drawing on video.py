# Lab-07: Print Text and basic drawing on Video
import cv2
import datetime
#for warn 0 just pass cv2.CAP_DSHOW
cap = cv2.VideoCapture(0)
print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 600)  #here 3 for width
cap.set(4, 800)  #here 4 for height
print("Width====",cap.get(3))
print("Height===",cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3))
       date_data = "Date: "+str(datetime.datetime.now())

       # putText(img,text,start_co,font,fontsize,color,thickness,linetype)
       frame = cv2.putText(frame, text, (10, 40), font, 1,(0, 155, 255), 1, cv2.LINE_AA)
       frame = cv2.putText(frame, date_data, (20, 80), font, 1,(100, 255, 255), 1, cv2.LINE_AA)

       #rectangle(img,start_co,end_co,color ,thickness)
       cv2.rectangle(frame, (8, 10), (450, 100), (128, 121, 255), 4)
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()
