import argparse
from math import floor
from time import time

from control import Controller
from cvision import get_skillcheck, get_skillcheck_indicator, get_skillcheck_success_zone, get_estimated_delay, \
    get_line_speed, get_position_angle
from screen import Screen


def auto_skillcheck(args):
    screen = Screen(args.monitor)
    controller = Controller()

    # Continuously check for active skill check
    while True:
        first_check, first_time = get_skillcheck(screen)

        first_zone_img = get_skillcheck_success_zone(first_check)
        first_zone_pos = get_position_angle(first_zone_img)

        first_line_img = get_skillcheck_indicator(first_check)
        first_line_pos = get_position_angle(first_line_img)

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

                new_check, new_time = get_skillcheck(screen)

                new_zone_img = get_skillcheck_success_zone(new_check)
                new_zone_pos = get_position_angle(new_zone_img)

                new_line_img = get_skillcheck_indicator(new_check)
                new_line_pos = get_position_angle(new_line_img)

                if new_line_pos and (old_line_pos < new_line_pos):
                    samples += 1
                    # update speed
                    spd = get_line_speed(old_time, old_line_pos, new_time, new_line_pos)
                    speed = spd if speed is None else (speed + spd) / 2
                    # update delay
                    new_zone_pos = int(floor((old_zone_pos + new_zone_pos) / 2))
                    delay = get_estimated_delay(new_zone_pos, new_time, new_line_pos, speed)

                    if (delay <= cycle_time * 5):  # and (samples >= 10)
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
    parser.add_argument('--monitor', type=int, default=1, required=False, help='Number/Index of monitor in which the game is being run')
    args = parser.parse_args()
    auto_skillcheck(args)
