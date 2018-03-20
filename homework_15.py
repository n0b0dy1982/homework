import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if d < r1 + r2 or d == r1 + r2:
        return True
    else:
        return False
print(circles_intersect(1, 8, 100, 14, 28, 1))
