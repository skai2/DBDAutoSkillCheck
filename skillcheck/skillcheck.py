import argparse
from math import floor
from time import time

from control import Controller
from cvision import get_skillcheck_img, get_indicator_img, get_greatzone_img, get_angle_position
from game import get_time_to_hit, get_line_speed
from screen import Screen


def auto_skillcheck(args):
    screen = Screen(args.monitor)
    controller = Controller()

    # Continuously check for active skill check
    while True:
        first_check, first_time = get_skillcheck_img(screen)

        first_zone_img = get_greatzone_img(first_check)
        first_zone_pos = get_angle_position(first_zone_img)

        first_line_img = get_indicator_img(first_check)
        first_line_pos = get_angle_position(first_line_img)

        # If active skillcheck, prepare to hit
        if first_zone_pos and first_line_pos:
            old_time = first_time
            old_zone_pos = first_zone_pos
            old_line_pos = first_line_pos
            cycle_time = 0.020
            speed = None
            samples = 0
            fails = 0
            # Update skill check parameters until ready to hit
            while True:
                cycle_start = time()

                new_check, new_time = get_skillcheck_img(screen)

                new_zone_img = get_greatzone_img(new_check)
                new_zone_pos = get_angle_position(new_zone_img)

                new_line_img = get_indicator_img(new_check)
                new_line_pos = get_angle_position(new_line_img)

                # gray = cv2.cvtColor(new_check, cv2.COLOR_RGB2GRAY)
                # cv2.imshow("skillcheck", np.concatenate((gray, new_zone_img + new_line_img), axis=1))
                # cv2.waitKey(0)

                if new_zone_pos and new_line_pos and (old_line_pos < new_line_pos):
                    samples += 1
                    # update speed
                    spd = get_line_speed(old_time, old_line_pos, new_time, new_line_pos)
                    speed = spd if speed is None else (speed + spd) / 2
                    # update delay
                    new_zone_pos = int(floor((old_zone_pos + new_zone_pos) / 2))
                    delay = get_time_to_hit(new_zone_pos, new_time, new_line_pos, speed)

                    if (delay <= cycle_time * 1.5):  # and (samples >= 10)
                        controller.skillcheck(delay=delay)
                        print(f"skillcheck: {new_zone_pos}° - {samples} samples - {cycle_time * 1000:0.2f} ms cycles")
                        break
                    else:
                        old_time = new_time
                        old_zone_pos = new_zone_pos
                        old_line_pos = new_line_pos
                else:
                    fails += 1
                    if fails >= 10:
                        break

                cycle_end = time()
                # update average cycle time
                cycle_time = (cycle_time + (cycle_end - cycle_start)) / 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automatically hit skillchecks in Dead by Daylight')
    parser.add_argument('--monitor', type=int, default=1, required=False,
                        help='Number/Index of monitor in which the game is being run')
    args = parser.parse_args()
    auto_skillcheck(args)
