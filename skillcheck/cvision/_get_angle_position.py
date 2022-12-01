from math import sin, cos, radians, floor


def get_angle_position(img, min_radius=45, max_radius=75):
    """Get element position expressed as angular distance from the top of the skillcheck circle"""
    img_height, img_width = img.shape[:2]
    center_x = int(floor(img_width / 2))
    center_y = int(floor(img_height / 2))
    min_radius = max([min_radius, 1])
    max_radius = min([max_radius, min([center_x, center_y])])
    for angle in range(0, 360):
        for radius in range(min_radius, max_radius):
            x = int(radius * cos(radians(angle - 90)) + center_x)
            y = int(radius * sin(radians(angle - 90)) + center_y)
            (value) = img[y, x]
            if value > 0:
                return angle