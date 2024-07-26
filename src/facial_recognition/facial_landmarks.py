import dlib
import cv2

def detect_facial_landmarks(img, predictor_path):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    faces = detector(gray_img)
    for face in faces:
        landmarks = predictor(gray_img, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
    return img, landmarks
