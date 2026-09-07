#red colour mask 
import cv2 
import numpy as np 
vid = cv2.VideoCapture(0) 

prev_x = None
prev_y = None
 
while True:  
    success, frame=vid.read() 
    if not success or cv2.waitKey(1) & 0xFF==ord('q'): 
        break 
 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    low = np.array([0, 80, 40])     
    high = np.array([15, 255, 255])
 
    mask=cv2.inRange(hsv,low,high) 
    output= cv2.bitwise_and(frame,frame,mask=mask) 
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for cnt in contours: 
        area=cv2.contourArea(cnt) 

        if area>500: 
 
            #cv2.drawContours(frame,cnt,-1,(255,0,0),2) 
            x, y, w, h = cv2.boundingRect(cnt) 
            center_x = x + w // 2 
            center_y = y + h // 2 

            cv2.rectangle(frame,(x, y),(x + w, y + h), (255, 0, 0),2) 
            margin=10;
            if prev_x is not None:
                if center_x > prev_x+margin:
                    direction = "Right"
                elif center_x < prev_x-margin:
                    direction = "Left"
                elif center_y> prev_y+margin:
                    direction = "Down"
                elif center_y < prev_y-margin:
                    direction = "Up"
                else:
                    direction = "Not Moving"

                print("Coordinates=" + str(center_x) +" , "+ str(center_y))
                print("Direction=" + direction)

                cv2.putText(frame, "Coordinates= " + str(center_x) + " , " + str(center_y), (x, y - 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,150,0), 2)

                cv2.putText(frame, "Direction= " + direction, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.4,(255,150,0), 2)

            prev_x = center_x
            prev_y = center_y
 
    cv2.imshow('Original', frame) 
    cv2.imshow('hehe', output) 
 
vid.release()
cv2.destroyAllWindows()