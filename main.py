import cv2
import numpy as np
from face_detector import faceDetector

def videoCap():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        frame = frame[0:650, 15:840]
        img = faceDetector(frame)
        cv2.imshow('frame', img)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
videoCap()