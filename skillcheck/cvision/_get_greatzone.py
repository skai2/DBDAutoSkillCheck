import logging as log

import cv2
import numpy as np

from cvision import get_angle


def get_greatzone_img(img):
    """Filter skillcheck success zone from skillcheck image"""
    new = img
    low_hsv = [0, 0, 255]
    high_hsv = [0, 0, 255]
    blur = 8
    thres = 10
    erode = 3

    new = cv2.inRange(new, np.array(low_hsv), np.array(high_hsv))
    new = cv2.blur(new, (blur, blur))
    thresh, new = cv2.threshold(new, thres, 255, cv2.THRESH_BINARY)
    kernel = np.ones((erode, erode), np.uint8)
    new = cv2.erode(new, kernel)

    return new


def get_greatzone_pos(img):
    great = get_greatzone_img(img)
    pos = get_angle(great, min_radius=63, max_radius=67)
    return pos


if __name__ == '__main__':
    log.basicConfig(level=log.INFO, format='[%(asctime)s][%(levelname)s] %(funcName)s() %(message)s',
                    datefmt='%H:%M:%S')
    image = cv2.imread(r"..\..\assets\skillcheck3.png")
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    pos = get_greatzone_pos(image_hsv)
    filtered = get_greatzone_img(image_hsv)
    pos = get_greatzone_pos(image_hsv)
    log.info(f"Obtained position: {pos}")
    cv2.imshow("great zone", image)
    cv2.imshow("indicator filtered", filtered)
    cv2.waitKey(0)
