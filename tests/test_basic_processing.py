import cv2
import unittest
from src.basic_processing import load_display_save, grayscale_conversion, resize_crop, edge_detection

class TestBasicProcessing(unittest.TestCase):

    def setUp(self):
        self.img = cv2.imread('data/input_images/sample.jpg')

    def test_load_image(self):
        self.assertIsNotNone(self.img)

    def test_grayscale_conversion(self):
        gray_img = grayscale_conversion.convert_to_grayscale(self.img)
        self.assertEqual(len(gray_img.shape), 2)

    def test_resize_image(self):
        resized_img = resize_crop.resize_image(self.img, 100, 100)
        self.assertEqual(resized_img.shape[0], 100)
        self.assertEqual(resized_img.shape[1], 100)

    def test_crop_image(self):
        cropped_img = resize_crop.crop_image(self.img, 0, 0, 50, 50)
        self.assertEqual(cropped_img.shape[0], 50)
        self.assertEqual(cropped_img.shape[1], 50)

    def test_edge_detection(self):
        edges = edge_detection.detect_edges(self.img, 100, 200)
        self.assertEqual(len(edges.shape), 2)

if __name__ == '__main__':
    unittest.main()
