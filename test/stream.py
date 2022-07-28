import cv2
import numpy as np

cap = cv2.VideoCapture("http://172.24.79.106:8080/?action=stream")
while True:
    ret, img = cap.read()
    cv2.imshow("display", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()