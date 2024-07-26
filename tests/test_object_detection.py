import cv2
import unittest
from src.object_detection import haar_cascade_detection, contour_detection

class TestObjectDetection(unittest.TestCase):

    def setUp(self):
        self.img = cv2.imread('data/input_images/sample.jpg')

    def test_haar_cascade_detection(self):
        result_img, objects = haar_cascade_detection.detect_objects_with_haar(
            self.img, 'data/haarcascades/haarcascade_frontalface_default.xml')
        self.assertTrue(len(objects) > 0)

    def test_contour_detection(self):
        result_img, contours = contour_detection.detect_contours(self.img)
        self.assertTrue(len(contours) > 0)

if __name__ == '__main__':
    unittest.main()
