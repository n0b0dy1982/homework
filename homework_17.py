import math
def solve_quadratic_equation(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = - b + math.sqrt(D) / (2 * a)
        x2 = - b - math.sqrt(D) / (2 * a)
        return x1, x2
    if D == 0:
        x = - b / (2 * a)
        return x
    else:
        print('None')
print(solve_quadratic_equation(1, 2, 1))







