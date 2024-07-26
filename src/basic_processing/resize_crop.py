import cv2

def resize_image(img, width, height):
    return cv2.resize(img, (width, height))

def crop_image(img, x, y, w, h):
    return img[y:y+h, x:x+w]
