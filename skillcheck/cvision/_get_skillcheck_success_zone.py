import cv2
import numpy as np


def get_skillcheck_success_zone(img):
    """Filter skillcheck success zone from skillcheck image"""
    low_val = 230
    low_white = np.array([low_val, low_val, low_val])
    high_white = np.array([255, 255, 255])

    img = cv2.blur(img, (5, 5))
    img = cv2.inRange(img, low_white, high_white)
    img = cv2.blur(img, (5, 5))
    thresh, img = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.erode(img, kernel)
    return img
