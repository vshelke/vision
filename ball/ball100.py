
import cv2
import numpy as np
import imutils 
greenLower = (29,86,6)
greenUpper = (64,255,255)

kernel = np.ones((2,2), np.uint8)
frame1= cv2.imread('test3.jpg')
frame=cv2.resize(frame1,(600,600))
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

	
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x,y), radius) = cv2.minEnclosingCircle(c)

	if radius > 10:
		cv2.circle(frame, (int(x),int(y)), int(radius),(255,0,0),2)

print ("X = ", int(x), " Y = ", int(y), " radius = " , int(radius))
frame2=imutils.resize(frame1,height=600,width=600)
hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

	
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x,y), radius) = cv2.minEnclosingCircle(c)

	if radius > 10:
		cv2.circle(frame2, (int(x),int(y)), int(radius),(255,0,0),2)

print ("X = ", int(x), " Y = ", int(y), " radius = " , int(radius))


cv2.imshow("mask", mask)
cv2.imshow("Frame", frame)
cv2.imshow("frame2",frame2)
cv2.waitKey(0)
cv2.destroyAllWindows()

