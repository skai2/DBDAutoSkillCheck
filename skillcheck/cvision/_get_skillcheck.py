from time import time

import cv2
import numpy as np

from screen import Screen


def get_skillcheck_img(screen: Screen):
    """Grab skillcheck image from screen"""
    if screen.type == "WIDE":
        left = 880
    elif screen.type == "ULTRA":
        left = 890 + 320
    else:
        left = None
    area = {
        "top": 460,
        "left": left,
        "width": 160,
        "height": 160
    }
    img = np.array(screen.shot(**area))
    pos_time = time()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img, pos_time


if __name__ == '__main__':
    screen = Screen(number=3)
    while True:
        grab, _ = get_skillcheck_img(screen)
        grab = cv2.cvtColor(grab, cv2.COLOR_HSV2RGB)
        cv2.imshow('skillcheck', grab)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
