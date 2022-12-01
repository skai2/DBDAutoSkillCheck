from time import time

import cv2
import numpy as np

from screen import Screen


def get_skillcheck_img(screen: Screen):
    """Grab skillcheck image from screen"""
    if screen.type == "WIDE":
        left = 890
    elif screen.type == "ULTRA":
        left = 890 + 320
    area = {
        "top": 470,
        "left": left,
        "width": 140,
        "height": 140
    }
    pos_time = time()
    img = np.array(screen.shot(**area))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img, pos_time
