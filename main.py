import cv2
import numpy as np 
car_cascade = cv2.CascadeClassifier('cars.xml')
cap=cv2.VideoCapture('car2.mp4')
while True:
    ret,frame=cap.read()
    
    car=car_cascade.detectMultiScale(frame,1.4,2)
    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.putText(frame,'car',(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow('cars',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()