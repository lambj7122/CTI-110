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

print()
print('The diameter of the circle is', f'{d:.1f}')
print()
print('The circumference of the circle is', f'{c:.2f}')
print()
print('The area of the circle is', f'{a:.3f}')
