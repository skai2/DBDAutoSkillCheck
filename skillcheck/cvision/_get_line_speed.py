def get_line_speed(old_time, old_line_pos, new_time, new_line_pos):
    """Calculate skillcheck line indicator speed in angular velocity"""
    line_speed = (new_line_pos - old_line_pos) / (new_time - old_time)
    return line_speed
