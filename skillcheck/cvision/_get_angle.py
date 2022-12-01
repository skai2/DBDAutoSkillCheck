from math import sin, cos, radians, floor


def get_angle(img, min_radius=50, max_radius=80):
    """Get element position expressed as angular distance from the top of the skillcheck circle"""
    img_height, img_width = img.shape[:2]
    center_x = int(floor(img_width / 2))
    center_y = int(floor(img_height / 2))
    shortest = min([center_x, center_y]) - 1
    min_radius = min_radius if 1 < min_radius < shortest else 60
    max_radius = max_radius if 1 < max_radius < shortest else 65
    for angle in range(0, 360):
        for radius in range(min_radius, max_radius+1):
            x = int(radius * cos(radians(angle - 90)) + center_x)
            y = int(radius * sin(radians(angle - 90)) + center_y)
            (value) = img[y, x]
            if value > 0:
                return angle