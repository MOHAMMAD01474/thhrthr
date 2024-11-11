import math
a = 12
b = 54
c = 6
discriminat = b * b - 4.0 * a * c
if discriminat < 0 :
    print("no real roots")
else:
    D = math.sqrt(discriminat)
    print(((-b + D) / 2.0))
    print(((-b - D) / 2.0))