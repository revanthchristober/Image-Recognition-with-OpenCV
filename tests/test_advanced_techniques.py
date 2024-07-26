import cv2
import unittest
from src.advanced_techniques import histogram_equalization, template_matching

class TestAdvancedTechniques(unittest.TestCase):

    def setUp(self):
        self.img = cv2.imread('data/input_images/sample.jpg')

    def test_histogram_equalization(self):
        equalized_img = histogram_equalization.equalize_histogram(self.img)
        self.assertEqual(len(equalized_img.shape), 2)

    def test_template_matching(self):
        result_img, res = template_matching.match_template(self.img, 'data/templates/template.jpg')
        self.assertIsNotNone(res)

if __name__ == '__main__':
    unittest.main()
