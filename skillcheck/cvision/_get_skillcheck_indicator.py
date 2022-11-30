import cv2
import numpy as np


def get_skillcheck_indicator(img):
    """Filter skillcheck red indicator line from skillcheck image"""
    low_red = np.array([160, 0, 0])
    high_red = np.array([255, 30, 30])

    img = cv2.inRange(img, low_red, high_red)
    img = cv2.blur(img, (5, 5))
    thresh, img = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.erode(img, kernel)
    return img
