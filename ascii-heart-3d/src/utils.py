def generate_heart_points(size):
    points = []
    for i in range(size):
        for j in range(size * 2):
            x = j / size - 1
            y = i / size - 1
            if (x**2 + (y - (x**2)**0.5)**2) <= 1:
                points.append((j, i))
    return points

def rotate_point(point, angle):
    import math
    x, y = point
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    return (x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle)

def project_point(point, distance):
    x, y = point
    z = distance
    return (x / (z + 5), y / (z + 5))

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')