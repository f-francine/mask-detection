import cv2

def faceDetector(img): #image from video capture
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface.xml') #load the choosen classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #draw a rectangle on the face found
    return img