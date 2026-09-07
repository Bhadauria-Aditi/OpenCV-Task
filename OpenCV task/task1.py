import cv2
import matplotlib.pyplot as plt

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

vid=cv2.VideoCapture(0)
while True: 
    success, frame=vid.read()
    if not success or cv2.waitKey(1) & 0xFF==ord('q'):
        break
    corners, ids, rejected = detector.detectMarkers(frame)
    
    print("Detected Marker= ", ids)

    if ids is not None:
        
        for i in range(len(ids)):    
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)    
            marker_id = ids[i][0]
            (top_left, top_right, bottom_right, bottom_left) = corners[i][0]

            x = int((top_left[0] + top_right[0] + bottom_right[0] + bottom_left[0]) / 4)
            y = int((top_left[1] + top_right[1] + bottom_right[1] + bottom_left[1]) / 4)
        
            print("ID= ", marker_id, "Center= ", (x, y))
        
            cv2.putText(frame, "ID= " + str(marker_id), (x, y), cv2.FONT_HERSHEY_DUPLEX,0.5, (180, 105, 255), 2)        
            cv2.putText(frame, str(x) +"," + str(y) , (x, y + 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255,150,0), 2)

    cv2.imshow('Video',frame)

vid.release()
cv2.destroyAllWindows()