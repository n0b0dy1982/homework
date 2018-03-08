import math
a = 5
b = 16
c = 8
print ("При а = %.f, b = %.f, c = %.f" % (a, b, c))
print (a + b * (c / 2))
print ((a**2 + b**2) % 2)
print ((a + b) / 12 * c % 4 + b)
print ((a - b * c) / (a + b) % c)
print (abs(a - b) / (a + b)**3 - math.cos(c))
print ((math.log(1 + c) / - b)**4 + abs(a))