import cv2
import numpy as np

from cvision import get_skillcheck_img
from screen import Screen


def callback(x):
    pass


def tuner():
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    screen = Screen(number=3)


    # create trackbars for color change

    ilowH, ihighH = 0, 179
    ilowS, ihighS = 0, 255
    ilowV, ihighV = 0, 255

    cv2.createTrackbar('lowH', 'image', ilowH, ihighH, callback)
    cv2.createTrackbar('highH', 'image', ihighH, ihighH, callback)

    cv2.createTrackbar('lowS', 'image', ilowS, ihighS, callback)
    cv2.createTrackbar('highS', 'image', ihighS, ihighS, callback)

    cv2.createTrackbar('lowV', 'image', ilowV, ihighV, callback)
    cv2.createTrackbar('highV', 'image', ihighV, ihighV, callback)

    # create trackbars for blur, threshold and erosion
    ilowB, ihighB = 1, 30
    ilowT, ihighT = 1, 255
    ilowE, ihighE = 1, 50

    cv2.createTrackbar('blur', 'image', ilowB, ihighB, callback)
    cv2.createTrackbar('thres', 'image', ilowT, ihighT, callback)
    cv2.createTrackbar('erode', 'image', ilowE, ihighE, callback)

    while (True):
        # static test source
        image = cv2.imread(r"..\..\assets\skillcheck3.png")
        image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

        # live test source
        live_hsv, _ = get_skillcheck_img(screen)

        # concatenate sources
        sources_hsv = np.concatenate((image_hsv, live_hsv), axis=1)
        tests_hsv = sources_hsv
        sources_rgb = cv2.cvtColor(sources_hsv, cv2.COLOR_HSV2RGB)
        sources_gray = cv2.cvtColor(sources_rgb, cv2.COLOR_RGB2GRAY)

        # get trackbar positions
        ilowH = cv2.getTrackbarPos('lowH', 'image')
        ihighH = cv2.getTrackbarPos('highH', 'image')
        ilowS = cv2.getTrackbarPos('lowS', 'image')
        ihighS = cv2.getTrackbarPos('highS', 'image')
        ilowV = cv2.getTrackbarPos('lowV', 'image')
        ihighV = cv2.getTrackbarPos('highV', 'image')

        ilowB = cv2.getTrackbarPos('blur', 'image')
        ilowT = cv2.getTrackbarPos('thres', 'image')
        ilowE = cv2.getTrackbarPos('erode', 'image')

        results_gray = tests_hsv
        # filter colour
        lower_hsv = np.array([ilowH, ilowS, ilowV])
        higher_hsv = np.array([ihighH, ihighS, ihighV])
        results_gray = cv2.inRange(results_gray, lower_hsv, higher_hsv)
        # blur
        results_gray = cv2.blur(results_gray, (ilowB, ilowB))
        # threshold
        thresh, results_gray = cv2.threshold(results_gray, ilowT, 255, cv2.THRESH_BINARY)
        # erode
        kernel = np.ones((ilowE, ilowE), np.uint8)
        results_gray = cv2.erode(results_gray, kernel)

        cv2.imshow("image", np.concatenate((sources_gray, results_gray), axis=0))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    tuner()
