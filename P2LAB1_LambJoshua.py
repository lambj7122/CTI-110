##Joshua Lamb
##2-26-2025
##P2LAB1
##Code that performs mathematical calculations and displays information to users.

import math
pi = math.pi

r = float(input('What is the radius of the cirle? '))

d = 2 * r
c = 2 * pi * r
a = pi * r**2

print(f'\nThe diameter of the circle is {d:.1f}')

print(f'\nThe circumference of the circle is {c:.2f}')

print(f'\nThe area of the circle is {a:.3f}')
