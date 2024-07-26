import cv2

def detect_edges(img, threshold1, threshold2):
    return cv2.Canny(img, threshold1, threshold2)
