import cv2

def equalize_histogram(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray_img)
