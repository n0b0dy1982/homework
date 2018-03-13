import math
def degrees2radians(degrees):
    return float(math.radians(degrees))
corner_1 = degrees2radians(math.cos(60))
corner_2 = degrees2radians(math.cos(45))
corner_3 = degrees2radians(math.cos(40))
print(corner_1, corner_2, corner_3)
