import logging as log

import cv2
import numpy as np

from cvision import get_angle


def get_indicator_img(img):
    """Filter skillcheck red indicator line from skillcheck image"""
    new = img
    low_hsv = [0, 180, 130]
    high_hsv = [0, 255, 200]
    blur = 3
    thres = 100
    erode = 10

    new = cv2.inRange(new, np.array(low_hsv), np.array(high_hsv))
    new = cv2.blur(new, (blur, blur))
    thresh, new = cv2.threshold(new, thres, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((erode, erode), np.uint8)
    # new = cv2.erode(new, kernel)

    return new


def get_indicator_pos(img):
    indi = get_indicator_img(img)
    pos = get_angle(indi, min_radius=70, max_radius=72)
    return pos


if __name__ == '__main__':
    log.basicConfig(level=log.INFO, format='[%(asctime)s][%(levelname)s] %(funcName)s() %(message)s',
                    datefmt='%H:%M:%S')
    image = cv2.imread(r"..\..\assets\skillcheck3.png")
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    filtered = get_indicator_img(image_hsv)
    pos = get_indicator_pos(image_hsv)
    log.info(f"Obtained position: {pos}")
    cv2.imshow("indicator original", image)
    cv2.imshow("indicator filtered", filtered)
    cv2.waitKey(0)
