import cv2
import numpy as np


def get_greatzone_img(img):
    """Filter skillcheck success zone from skillcheck image"""
    new = img

    new = cv2.cvtColor(new, cv2.COLOR_RGB2HSV)
    new = cv2.inRange(new, np.array([0, 0, 255]), np.array([0, 0, 255]))
    new = cv2.blur(new, (5, 5))
    thresh, new = cv2.threshold(new, 15, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    new = cv2.erode(new, kernel)

    return new
