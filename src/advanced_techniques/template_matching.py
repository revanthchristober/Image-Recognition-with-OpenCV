import cv2

def match_template(img, template_path):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, 0)
    res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    return img, res
