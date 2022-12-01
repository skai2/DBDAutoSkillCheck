import cv2
import numpy as np

from cvision import get_skillcheck_img, get_greatzone_img, get_indicator_img
from screen import Screen


def callback(x):
    pass


def debug():
    screen = Screen(number=3)

    while (True):
        # static test source
        image = cv2.imread(r"..\..\assets\skillcheck3.png")
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # live test source
        live_hsv, _ = get_skillcheck_img(screen)
        live_gray = cv2.cvtColor(live_hsv, cv2.COLOR_RGB2GRAY)
        # concatenate original
        original = np.concatenate((image_hsv, live_hsv), axis=1)
        original_gray = cv2.cvtColor(original, cv2.COLOR_HSV2RGB)
        original_gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

        great_image = get_greatzone_img(image_hsv)
        line_image = get_indicator_img(image_hsv)
        skill_image = great_image + line_image

        great_live = get_greatzone_img(live_hsv)
        line_live = get_indicator_img(live_hsv)
        skill_live = great_live + line_live

        test = np.concatenate((skill_image, skill_live), axis=1)

        cv2.imshow("debug", np.concatenate((original_gray, test), axis=0))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    debug()
