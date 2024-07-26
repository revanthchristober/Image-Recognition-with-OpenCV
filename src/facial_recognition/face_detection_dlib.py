import dlib
import cv2

def detect_faces_dlib(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray_img)
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img, faces
