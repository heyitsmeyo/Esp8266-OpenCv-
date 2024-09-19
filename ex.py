import numpy as np
import cv2 , time
from PIL import Image
import co 
from co import send



cap = cv2.VideoCapture(0) 

while True : 
	ret , frame = cap.read()
	width = int(cap.get(10))
	height= int(cap.get(10))
	
	hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
	lowyellow = np.array([20,100,100])
	highyellow = np.array([30, 255,255])
	mask = cv2.inRange(hsv, lowyellow, highyellow)
	#result = cv2.bitwise_and(frame , frame , mask=mask)
	#cv2.imshow('mask',)
	mask_ = Image.fromarray(mask)
	box = mask_.getbbox()
	
	if box is not None:
		x1 , y1 , x2 , y2 = box
		cv2.rectangle(frame , (x1 , y1) , (x2, y2) ,(0,255,0) , 5 ) 
		
		send('0')
	elif box is None : 
		
		send('1') 
		
	cv2.imshow('frame', frame)
	cv2.imshow('mask' , mask)
	
	if cv2.waitKey(1) == ord('q'):
		break
	
cap.release()
cap.destroyAllWindows()
