import cv2
import unittest
from src.facial_recognition import face_detection_haar, face_detection_dlib, facial_landmarks

class TestFacialRecognition(unittest.TestCase):

    def setUp(self):
        self.img = cv2.imread('data/input_images/sample.jpg')

    def test_face_detection_haar(self):
        result_img, faces = face_detection_haar.detect_faces_haar(
            self.img, 'data/haarcascades/haarcascade_frontalface_default.xml')
        self.assertTrue(len(faces) > 0)

    def test_face_detection_dlib(self):
        result_img, faces = face_detection_dlib.detect_faces_dlib(self.img)
        self.assertTrue(len(faces) > 0)

    def test_facial_landmarks(self):
        result_img, landmarks = facial_landmarks.detect_facial_landmarks(
            self.img, 'data/shape_predictors/shape_predictor_68_face_landmarks.dat')
        self.assertTrue(landmarks.num_parts == 68)

if __name__ == '__main__':
    unittest.main()
