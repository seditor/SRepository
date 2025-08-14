import math

def generate_points(r=250, center=(0, 0)):
    o_x, o_y = center
    points = []
    for angle in range(0, 361, 5):
        rad = math.radians(angle)
        x = o_x + r * math.sin(rad)
        y = o_y + r * math.cos(rad)
        points.append((round(x, 5), round(y, 5)))
    return points

def test_circle_closed():
    pts = generate_points()
    assert pts[0] == pts[-1]
