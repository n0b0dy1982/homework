import math
def triangle_square_and_perimeter(a, b):
    square = a * b / 2
    c = math.sqrt(a ** 2 + b ** 2)
    perimeter = a + b + c
    return square, perimeter
print(triangle_square_and_perimeter(15, 6))




