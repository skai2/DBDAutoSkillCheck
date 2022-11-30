from time import time


def get_estimated_delay(zone_pos, line_time, line_pos, line_speed):
    """Calculate aproximate time to wait in order to hit great skillcheck"""
    time_to_zone = (zone_pos - line_pos) / line_speed
    return max([0, time_to_zone - (time() - line_time)])
