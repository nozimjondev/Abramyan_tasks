x1 = float(input('Enter a number for x1: '))
y1 = float(input('Enter a number for y1: '))
x2 = float(input('Enter a number for x2: '))
y2 = float(input('Enter a number for y2: '))
x3 = float(input('Enter a number for x3: '))
y3 = float(input('Enter a number for y3: '))
import math
a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2 )
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2 )
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 )
P = a + b + c
p = (a + b +c) / 2 
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'P = {P}, p = {p} and S = {S}')
