import math

x = 2.
y = 3.

z1 = 3 * x**3 * y**2 - 5 * x * y**2
z2 = 3 * math.pow(x,3) * math.pow(y,2) - 5 * x * math.pow(y,2)

print('Z1 =', z1, "e Z2 =", z2)