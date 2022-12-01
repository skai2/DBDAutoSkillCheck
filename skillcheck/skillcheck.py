import argparse
import logging as log
from math import floor
from time import time, sleep

from control import Controller
from cvision import get_skillcheck_img, get_greatzone_pos, get_indicator_pos
from game import get_time_to_hit, get_line_speed
from screen import Screen


def auto_skillcheck(params):
    log.basicConfig(level=log.INFO, format='[%(asctime)s][%(levelname)s] %(funcName)s() %(message)s',
                    datefmt='%H:%M:%S')
    screen = Screen(params.monitor)
    controller = Controller()

    # Continuously check for active skill check
    while True:
        first_check, first_time = get_skillcheck_img(screen)
        first_zone_pos = get_greatzone_pos(first_check)
        first_line_pos = get_indicator_pos(first_check)
        # log.info(f"{first_time}: zone:{first_zone_pos}° - line:{first_line_pos}°")

        # If active skillcheck, prepare to hit
        if first_zone_pos and first_line_pos:
            log.info("Active skillcheck")
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
                new_zone_pos = get_greatzone_pos(new_check)
                new_line_pos = get_indicator_pos(new_check)
                # Update parameters
                if new_zone_pos and new_line_pos and (old_line_pos < new_line_pos):
                    fails = 0
                    samples += 1
                    # update speed
                    spd = get_line_speed(old_time, old_line_pos, new_time, new_line_pos)
                    speed = spd if speed is None else (speed + spd) / 2
                    # update delay
                    new_zone_pos = int(floor((old_zone_pos + new_zone_pos) / 2))
                    delay = get_time_to_hit(new_zone_pos, new_time, new_line_pos, speed)

                    if (delay <= cycle_time * 1.5):  # and (samples >= 10)
                        controller.skillcheck(delay=delay)
                        sleep(1)
                        break
                    else:
                        old_time = new_time
                        old_zone_pos = new_zone_pos
                        old_line_pos = new_line_pos
                else:
                    fails += 1
                    if fails >= 5:
                        log.info("Cancel")
                        break
                # update cycle time
                cycle_time = (cycle_time + (time() - cycle_start)) / 2
            log.info(f"Hit: {old_zone_pos}° - {samples} sams - {fails} fails - {cycle_time * 1000:0.2f} ms cycles")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automatically hit skillchecks in Dead by Daylight')
    parser.add_argument('--monitor', type=int, default=1, required=False,
                        help='Number/Index of monitor in which the game is being run')
    args = parser.parse_args()
    auto_skillcheck(args)
