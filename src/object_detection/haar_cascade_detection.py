import cv2

def detect_objects_with_haar(img, cascade_path, scaleFactor=1.1, minNeighbors=5):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    objects = cascade.detectMultiScale(gray_img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img, objects
