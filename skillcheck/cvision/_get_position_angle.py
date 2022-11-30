from math import sin, cos, radians, floor


def get_position_angle(img, radius=65):
    """Get element position expressed as angular distance from the top of the skillcheck circle"""
    img_height, img_width = img.shape[:2]
    center_x = int(floor(img_width / 2))
    center_y = int(floor(img_height / 2))
    max_radius = min([center_x, center_y]) - 1
    radius = min([radius, max_radius])
    for angle in range(0, 360):
        x = int(radius * cos(radians(angle - 90)) + center_x)
        y = int(radius * sin(radians(angle - 90)) + center_y)
        (value) = img[y, x]
        if value > 0:
            return angle
